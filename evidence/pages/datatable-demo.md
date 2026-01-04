---
title: DataTable デモ
---

# DataTable の機能

## 基本のテーブル

```sql products
SELECT
    product_name,
    category,
    sub_category,
    sales,
    quantity,
    profit,
    profit / sales * 100 as profit_margin
FROM superstore.orders
ORDER BY sales DESC
LIMIT 100
```

<DataTable data={products} search=true rows=10>
    <Column id=product_name title="商品名" />
    <Column id=category title="カテゴリ" />
    <Column id=sub_category title="サブカテゴリ" />
    <Column id=sales title="売上" fmt='$#,##0' />
    <Column id=quantity title="数量" />
    <Column id=profit title="利益" fmt='$#,##0' />
    <Column id=profit_margin title="利益率" fmt='0.0"%"' />
</DataTable>

---

## 条件付きフォーマット（Conditional Formatting）

```sql profit_analysis
SELECT
    category,
    sub_category,
    SUM(sales) as sales,
    SUM(profit) as profit,
    SUM(profit) / SUM(sales) * 100 as profit_margin
FROM superstore.orders
GROUP BY category, sub_category
ORDER BY profit_margin DESC
```

<DataTable data={profit_analysis} search=true>
    <Column id=category title="カテゴリ" />
    <Column id=sub_category title="サブカテゴリ" />
    <Column id=sales title="売上" fmt='$#,##0' />
    <Column id=profit title="利益" fmt='$#,##0' contentType=colorscale />
    <Column id=profit_margin title="利益率" fmt='0.0"%"' contentType=colorscale />
</DataTable>

> 利益と利益率がカラースケールで表示される（赤=低い、緑=高い）

---

## カテゴリ別サマリー

```sql category_summary
SELECT
    category,
    COUNT(*) as order_count,
    SUM(sales) as total_sales
FROM superstore.orders
GROUP BY category
ORDER BY total_sales DESC
```

<DataTable data={category_summary}>
    <Column id=category title="カテゴリ" />
    <Column id=order_count title="注文数" fmt='#,##0' />
    <Column id=total_sales title="売上" fmt='$#,##0' />
</DataTable>

---

## 配送方法別統計

```sql ship_mode_stats
SELECT
    ship_mode,
    COUNT(*) as orders,
    SUM(sales) as total_sales
FROM superstore.orders
GROUP BY ship_mode
ORDER BY orders DESC
```

<DataTable data={ship_mode_stats}>
    <Column id=ship_mode title="配送方法" />
    <Column id=orders title="注文数" fmt='#,##0' />
    <Column id=total_sales title="売上" fmt='$#,##0' />
</DataTable>

---

## バー表示

```sql category_bars
SELECT
    category,
    SUM(sales) as sales
FROM superstore.orders
GROUP BY category
ORDER BY sales DESC
```

<DataTable data={category_bars}>
    <Column id=category title="カテゴリ" />
    <Column id=sales title="売上" contentType=bar />
</DataTable>
