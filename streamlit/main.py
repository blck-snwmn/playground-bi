"""
SuperStore Sales Dashboard - Streamlit版

Evidence と同じデータを使った売上分析ダッシュボード。
比較のために同様の機能を Streamlit で実装。
"""

import streamlit as st
import duckdb
import pandas as pd
from pathlib import Path

# ページ設定
st.set_page_config(
    page_title="SuperStore Dashboard",
    page_icon="📊",
    layout="wide"
)

# データパス（プロジェクトルートから相対パス）
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "SuperStore.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    """CSVデータをDuckDB経由で読み込み"""
    conn = duckdb.connect()
    df = conn.execute(f"""
        SELECT
            "Order Date" as order_date,
            "Ship Mode" as ship_mode,
            "Customer Name" as customer_name,
            "Segment" as segment,
            "City" as city,
            "State" as state,
            "Category" as category,
            "Sub-Category" as sub_category,
            "Product Name" as product_name,
            "Sales" as sales,
            "Quantity" as quantity,
            "Discount" as discount,
            "Profit" as profit
        FROM read_csv('{DATA_PATH}', header=true)
    """).fetchdf()
    conn.close()
    return df


def main():
    st.title("📊 SuperStore 売上分析ダッシュボード")
    st.caption("Streamlit + DuckDB で構築 | 👈 サイドバーから他のページへ")

    # データ読み込み
    df = load_data()

    # --- サマリーKPI ---
    st.header("概要")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("総注文数", f"{len(df):,}")
    with col2:
        st.metric("総売上", f"${df['sales'].sum():,.0f}")
    with col3:
        st.metric("総利益", f"${df['profit'].sum():,.0f}")
    with col4:
        profit_margin = df['profit'].sum() / df['sales'].sum() * 100
        st.metric("利益率", f"{profit_margin:.1f}%")

    st.divider()

    # --- フィルター ---
    st.sidebar.header("フィルター")

    # カテゴリフィルター
    categories = ["全カテゴリ"] + sorted(df["category"].unique().tolist())
    selected_category = st.sidebar.selectbox("カテゴリ", categories)

    # セグメントフィルター（複数選択）
    segments = df["segment"].unique().tolist()
    selected_segments = st.sidebar.multiselect(
        "セグメント",
        segments,
        default=segments
    )

    # データフィルタリング
    filtered_df = df.copy()
    if selected_category != "全カテゴリ":
        filtered_df = filtered_df[filtered_df["category"] == selected_category]
    if selected_segments:
        filtered_df = filtered_df[filtered_df["segment"].isin(selected_segments)]

    # --- カテゴリ別売上 ---
    st.header("カテゴリ別売上")

    category_sales = (
        filtered_df.groupby("category")
        .agg({"sales": "sum", "profit": "sum"})
        .reset_index()
        .sort_values("sales", ascending=False)
    )

    st.bar_chart(category_sales, x="category", y="sales")

    # --- 地域別売上 Top 10 ---
    st.header("州別売上 Top 10")

    state_sales = (
        filtered_df.groupby("state")
        .agg({"sales": "sum", "profit": "sum"})
        .reset_index()
        .sort_values("sales", ascending=False)
        .head(10)
    )

    st.bar_chart(state_sales, x="state", y="sales", horizontal=True)

    # --- セグメント別分析 ---
    st.header("セグメント別分析")

    segment_analysis = (
        filtered_df.groupby("segment")
        .agg({
            "sales": ["count", "sum"],
            "profit": "sum"
        })
        .reset_index()
    )
    segment_analysis.columns = ["segment", "注文数", "売上", "利益"]
    segment_analysis["利益率"] = (
        segment_analysis["利益"] / segment_analysis["売上"] * 100
    ).round(1)
    segment_analysis["売上"] = segment_analysis["売上"].apply(lambda x: f"${x:,.0f}")
    segment_analysis["利益"] = segment_analysis["利益"].apply(lambda x: f"${x:,.0f}")
    segment_analysis["利益率"] = segment_analysis["利益率"].apply(lambda x: f"{x}%")
    segment_analysis = segment_analysis.rename(columns={"segment": "セグメント"})

    st.dataframe(segment_analysis, use_container_width=True, hide_index=True)

    st.divider()

    # --- 指標選択（ButtonGroup相当） ---
    st.header("指標切り替え")

    metric = st.radio(
        "表示する指標",
        ["売上", "利益", "数量"],
        horizontal=True
    )

    metric_map = {"売上": "sales", "利益": "profit", "数量": "quantity"}
    selected_metric = metric_map[metric]

    category_metric = (
        filtered_df.groupby("category")
        .agg({selected_metric: "sum"})
        .reset_index()
    )

    st.bar_chart(category_metric, x="category", y=selected_metric)

    # --- 月別トレンド ---
    st.header("月別売上トレンド")

    chart_type = st.radio(
        "チャートタイプ",
        ["棒グラフ", "折れ線グラフ", "エリアグラフ"],
        horizontal=True
    )

    monthly_df = filtered_df.copy()
    monthly_df["month"] = pd.to_datetime(monthly_df["order_date"]).dt.to_period("M").astype(str)
    monthly_sales = (
        monthly_df.groupby("month")
        .agg({"sales": "sum"})
        .reset_index()
        .sort_values("month")
    )

    if chart_type == "棒グラフ":
        st.bar_chart(monthly_sales, x="month", y="sales")
    elif chart_type == "折れ線グラフ":
        st.line_chart(monthly_sales, x="month", y="sales")
    else:
        st.area_chart(monthly_sales, x="month", y="sales")


if __name__ == "__main__":
    main()
