"""
積み上げグラフ デモページ

Altair を使った積み上げグラフの実装
"""

import streamlit as st
import duckdb
import pandas as pd
import altair as alt
from pathlib import Path

st.set_page_config(
    page_title="Stacked Charts - SuperStore",
    page_icon="📊",
    layout="wide"
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "SuperStore.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    conn = duckdb.connect()
    df = conn.execute(f"""
        SELECT
            "Order Date" as order_date,
            "Category" as category,
            "Segment" as segment,
            "Sales" as sales,
            "Profit" as profit
        FROM read_csv('{DATA_PATH}', header=true)
    """).fetchdf()
    conn.close()
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    return df


def main():
    st.markdown("[Home](/) > **Stacked Charts**")
    st.title("📊 積み上げグラフ デモ")

    df = load_data()

    # --- カテゴリ × セグメント ---
    st.header("カテゴリ × セグメント 積み上げ棒グラフ")

    category_segment = (
        df.groupby(["category", "segment"])
        .agg({"sales": "sum"})
        .reset_index()
    )

    chart1 = alt.Chart(category_segment).mark_bar().encode(
        x=alt.X("category:N", title="カテゴリ"),
        y=alt.Y("sales:Q", title="売上"),
        color=alt.Color("segment:N", title="セグメント"),
        order=alt.Order("segment:N")
    ).properties(
        title="カテゴリ別・セグメント別 売上（積み上げ）",
        height=400
    )
    st.altair_chart(chart1, use_container_width=True)

    st.divider()

    # --- 月別 × カテゴリ ---
    st.header("月別 × カテゴリ 積み上げ棒グラフ")

    monthly_category = (
        df.groupby(["month", "category"])
        .agg({"sales": "sum"})
        .reset_index()
    )

    chart2 = alt.Chart(monthly_category).mark_bar().encode(
        x=alt.X("month:N", title="月", sort=None),
        y=alt.Y("sales:Q", title="売上"),
        color=alt.Color("category:N", title="カテゴリ"),
        order=alt.Order("category:N")
    ).properties(
        title="月別・カテゴリ別 売上（積み上げ）",
        height=400
    )
    st.altair_chart(chart2, use_container_width=True)

    st.divider()

    # --- 積み上げエリアチャート ---
    st.header("積み上げエリアチャート")

    monthly_segment = (
        df.groupby(["month", "segment"])
        .agg({"sales": "sum"})
        .reset_index()
    )

    chart3 = alt.Chart(monthly_segment).mark_area().encode(
        x=alt.X("month:N", title="月", sort=None),
        y=alt.Y("sales:Q", title="売上", stack="zero"),
        color=alt.Color("segment:N", title="セグメント"),
        order=alt.Order("segment:N")
    ).properties(
        title="月別・セグメント別 売上（積み上げエリア）",
        height=400
    )
    st.altair_chart(chart3, use_container_width=True)

    st.divider()

    # --- 100% 積み上げ ---
    st.header("100% 積み上げ棒グラフ")

    chart4 = alt.Chart(category_segment).mark_bar().encode(
        x=alt.X("category:N", title="カテゴリ"),
        y=alt.Y("sales:Q", title="割合", stack="normalize"),
        color=alt.Color("segment:N", title="セグメント"),
        order=alt.Order("segment:N")
    ).properties(
        title="カテゴリ別・セグメント別 売上（100%積み上げ）",
        height=400
    )
    st.altair_chart(chart4, use_container_width=True)

    st.divider()

    # --- グループ化 ---
    st.header("グループ化棒グラフ（比較用）")

    chart5 = alt.Chart(category_segment).mark_bar().encode(
        x=alt.X("segment:N", title="セグメント"),
        y=alt.Y("sales:Q", title="売上"),
        color=alt.Color("segment:N", title="セグメント"),
        column=alt.Column("category:N", title="カテゴリ")
    ).properties(
        title="カテゴリ別・セグメント別 売上（グループ化）",
        height=300,
        width=200
    )
    st.altair_chart(chart5)


if __name__ == "__main__":
    main()
