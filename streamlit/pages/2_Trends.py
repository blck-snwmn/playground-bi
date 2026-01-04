"""
トレンド分析ページ

時系列データの分析
"""

import streamlit as st
import duckdb
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Trends - SuperStore",
    page_icon="📈",
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
    return df


def main():
    st.markdown("[Home](/) > **Trends**")
    st.title("📈 トレンド分析")

    df = load_data()

    # フィルター
    st.sidebar.header("フィルター")

    categories = ["全て"] + sorted(df["category"].unique().tolist())
    selected_cat = st.sidebar.selectbox("カテゴリ", categories)

    segments = ["全て"] + sorted(df["segment"].unique().tolist())
    selected_seg = st.sidebar.selectbox("セグメント", segments)

    # フィルタリング
    filtered = df.copy()
    if selected_cat != "全て":
        filtered = filtered[filtered["category"] == selected_cat]
    if selected_seg != "全て":
        filtered = filtered[filtered["segment"] == selected_seg]

    # 期間選択
    col1, col2 = st.columns(2)
    with col1:
        granularity = st.radio(
            "集計単位",
            ["月別", "四半期別", "年別"],
            horizontal=True
        )
    with col2:
        metric = st.radio(
            "指標",
            ["売上", "利益"],
            horizontal=True
        )

    metric_col = "sales" if metric == "売上" else "profit"

    # 時系列集計
    filtered["period"] = filtered["order_date"].apply(
        lambda x: get_period(x, granularity)
    )

    trend_data = (
        filtered.groupby("period")
        .agg({metric_col: "sum"})
        .reset_index()
        .sort_values("period")
    )

    st.subheader(f"{granularity} {metric}推移")

    chart_type = st.radio(
        "チャートタイプ",
        ["折れ線", "棒グラフ", "エリア"],
        horizontal=True
    )

    if chart_type == "折れ線":
        st.line_chart(trend_data, x="period", y=metric_col)
    elif chart_type == "棒グラフ":
        st.bar_chart(trend_data, x="period", y=metric_col)
    else:
        st.area_chart(trend_data, x="period", y=metric_col)

    # 統計サマリー
    st.divider()
    st.subheader("統計サマリー")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("合計", f"${trend_data[metric_col].sum():,.0f}")
    with col2:
        st.metric("平均", f"${trend_data[metric_col].mean():,.0f}")
    with col3:
        st.metric("最大", f"${trend_data[metric_col].max():,.0f}")
    with col4:
        st.metric("最小", f"${trend_data[metric_col].min():,.0f}")

    # データテーブル
    with st.expander("データを見る"):
        display_data = trend_data.copy()
        display_data[metric_col] = display_data[metric_col].apply(
            lambda x: f"${x:,.0f}"
        )
        display_data.columns = ["期間", metric]
        st.dataframe(display_data, use_container_width=True, hide_index=True)


def get_period(date, granularity: str) -> str:
    if granularity == "月別":
        return date.strftime("%Y-%m")
    elif granularity == "四半期別":
        q = (date.month - 1) // 3 + 1
        return f"{date.year}-Q{q}"
    else:
        return str(date.year)


if __name__ == "__main__":
    main()
