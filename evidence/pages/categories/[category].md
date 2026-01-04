---
title: カテゴリ詳細
---

[Home](/) > [Categories](/categories) > {params.category}

# {params.category} の分析

```sql category_summary
SELECT
    COUNT(*) as total_orders,
    SUM(sales) as total_sales,
    SUM(profit) as total_profit,
    SUM(profit) / SUM(sales) * 100 as profit_margin,
    COUNT(DISTINCT customer_name) as unique_customers
FROM superstore.orders
WHERE LOWER(REPLACE(category, ' ', '-')) = LOWER('${params.category}')
```

<BigValue data={category_summary} value=total_orders title="注文数" />
<BigValue data={category_summary} value=total_sales title="売上" fmt='$#,##0' />
<BigValue data={category_summary} value=total_profit title="利益" fmt='$#,##0' />
<BigValue data={category_summary} value=profit_margin title="利益率" fmt='0.0"%"' />
<BigValue data={category_summary} value=unique_customers title="顧客数" />

---

## サブカテゴリ別売上

```sql subcategory_sales
SELECT
    sub_category,
    SUM(sales) as sales,
    SUM(profit) as profit
FROM superstore.orders
WHERE LOWER(REPLACE(category, ' ', '-')) = LOWER('${params.category}')
GROUP BY sub_category
ORDER BY sales DESC
```

<BarChart
    data={subcategory_sales}
    x=sub_category
    y=sales
    title="サブカテゴリ別売上"
/>

---

## 売上トップ10商品

```sql top_products
SELECT
    product_name,
    SUM(sales) as sales,
    SUM(quantity) as quantity,
    SUM(profit) as profit
FROM superstore.orders
WHERE LOWER(REPLACE(category, ' ', '-')) = LOWER('${params.category}')
GROUP BY product_name
ORDER BY sales DESC
LIMIT 10
```

<DataTable data={top_products}>
    <Column id=product_name title="商品名" />
    <Column id=sales title="売上" fmt='$#,##0' />
    <Column id=quantity title="数量" />
    <Column id=profit title="利益" fmt='$#,##0' />
</DataTable>

---

## 州別売上

```sql state_sales
SELECT
    state,
    SUM(sales) as sales
FROM superstore.orders
WHERE LOWER(REPLACE(category, ' ', '-')) = LOWER('${params.category}')
GROUP BY state
ORDER BY sales DESC
LIMIT 10
```

<BarChart
    data={state_sales}
    x=state
    y=sales
    swapXY=true
    title="州別売上 Top 10"
/>

---

[← カテゴリ一覧に戻る](/categories) | [ホームに戻る](/)
