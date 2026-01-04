"""
カテゴリ別分析ページ

Evidence の /categories と /categories/[category] に相当
"""

import streamlit as st
import duckdb
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Categories - SuperStore",
    page_icon="📁",
    layout="wide"
)

# データパス
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "SuperStore.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    conn = duckdb.connect()
    df = conn.execute(f"""
        SELECT
            "Order Date" as order_date,
            "Category" as category,
            "Sub-Category" as sub_category,
            "Product Name" as product_name,
            "State" as state,
            "Sales" as sales,
            "Quantity" as quantity,
            "Profit" as profit
        FROM read_csv('{DATA_PATH}', header=true)
    """).fetchdf()
    conn.close()
    return df


def main():
    df = load_data()
    categories = sorted(df["category"].unique().tolist())

    # Query params から選択カテゴリを取得
    selected = st.query_params.get("category", None)

    # パンくずリスト
    if selected:
        st.markdown(f"[Home](/) > [Categories](/Categories) > **{selected}**")
    else:
        st.markdown("[Home](/) > **Categories**")

    st.title("📁 カテゴリ分析")

    # カテゴリ選択
    col1, col2 = st.columns([1, 3])
    with col1:
        st.subheader("カテゴリ一覧")
        for cat in categories:
            if st.button(cat, key=f"btn_{cat}", use_container_width=True):
                st.query_params["category"] = cat
                st.rerun()

    with col2:
        if selected and selected in categories:
            show_category_detail(df, selected)
        else:
            show_category_overview(df)


def show_category_overview(df: pd.DataFrame):
    """カテゴリ一覧表示"""
    st.subheader("カテゴリ概要")

    category_summary = (
        df.groupby("category")
        .agg({
            "sales": ["count", "sum"],
            "profit": "sum"
        })
        .reset_index()
    )
    category_summary.columns = ["カテゴリ", "注文数", "売上", "利益"]
    category_summary["売上"] = category_summary["売上"].apply(lambda x: f"${x:,.0f}")
    category_summary["利益"] = category_summary["利益"].apply(lambda x: f"${x:,.0f}")

    st.dataframe(category_summary, use_container_width=True, hide_index=True)

    st.info("👈 左のカテゴリをクリックすると詳細が見れます")


def show_category_detail(df: pd.DataFrame, category: str):
    """カテゴリ詳細表示"""
    st.subheader(f"{category} の詳細分析")

    filtered = df[df["category"] == category]

    # KPI
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("注文数", f"{len(filtered):,}")
    with col2:
        st.metric("売上", f"${filtered['sales'].sum():,.0f}")
    with col3:
        st.metric("利益", f"${filtered['profit'].sum():,.0f}")
    with col4:
        margin = filtered['profit'].sum() / filtered['sales'].sum() * 100
        st.metric("利益率", f"{margin:.1f}%")

    st.divider()

    # サブカテゴリ別
    st.subheader("サブカテゴリ別売上")
    sub_sales = (
        filtered.groupby("sub_category")
        .agg({"sales": "sum"})
        .reset_index()
        .sort_values("sales", ascending=False)
    )
    st.bar_chart(sub_sales, x="sub_category", y="sales")

    # 州別
    st.subheader("州別売上 Top 10")
    state_sales = (
        filtered.groupby("state")
        .agg({"sales": "sum"})
        .reset_index()
        .sort_values("sales", ascending=False)
        .head(10)
    )
    st.bar_chart(state_sales, x="state", y="sales", horizontal=True)

    # トップ商品
    st.subheader("売上トップ10商品")
    top_products = (
        filtered.groupby("product_name")
        .agg({"sales": "sum", "quantity": "sum", "profit": "sum"})
        .reset_index()
        .sort_values("sales", ascending=False)
        .head(10)
    )
    top_products["sales"] = top_products["sales"].apply(lambda x: f"${x:,.0f}")
    top_products["profit"] = top_products["profit"].apply(lambda x: f"${x:,.0f}")
    top_products.columns = ["商品名", "売上", "数量", "利益"]
    st.dataframe(top_products, use_container_width=True, hide_index=True)

    # 戻るボタン
    if st.button("← カテゴリ一覧に戻る"):
        del st.query_params["category"]
        st.rerun()


if __name__ == "__main__":
    main()
