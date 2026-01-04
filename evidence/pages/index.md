---
title: SuperStore Sales Dashboard
---

# SuperStore 売上分析ダッシュボード

```sql summary
SELECT
    COUNT(*) as total_orders,
    SUM(sales) as total_sales,
    SUM(profit) as total_profit,
    AVG(discount) as avg_discount
FROM superstore.orders
```

<BigValue
    data={summary}
    value=total_orders
    title="総注文数"
/>

<BigValue
    data={summary}
    value=total_sales
    title="総売上"
    fmt='$#,##0'
/>

<BigValue
    data={summary}
    value=total_profit
    title="総利益"
    fmt='$#,##0'
/>

---

## カテゴリ別売上

```sql categories
SELECT DISTINCT category FROM superstore.orders
```

<Dropdown data={categories} name=category value=category>
    <DropdownOption value="%" valueLabel="全カテゴリ"/>
</Dropdown>

```sql sales_by_category
SELECT
    category,
    SUM(sales) as sales,
    SUM(profit) as profit
FROM superstore.orders
WHERE category LIKE '${inputs.category.value}'
GROUP BY category
ORDER BY sales DESC
```

<BarChart
    data={sales_by_category}
    x=category
    y=sales
    title="カテゴリ別売上"
/>

---

## 地域別売上 Top 10

```sql sales_by_state
SELECT
    state,
    SUM(sales) as sales,
    SUM(profit) as profit
FROM superstore.orders
GROUP BY state
ORDER BY sales DESC
LIMIT 10
```

<BarChart
    data={sales_by_state}
    x=state
    y=sales
    title="州別売上 Top 10"
    swapXY=true
/>

---

## セグメント別分析

```sql segment_analysis
SELECT
    segment,
    COUNT(*) as orders,
    SUM(sales) as sales,
    SUM(profit) as profit,
    SUM(profit) / SUM(sales) * 100 as profit_margin
FROM superstore.orders
GROUP BY segment
ORDER BY sales DESC
```

<DataTable data={segment_analysis} search=true>
    <Column id=segment title="セグメント"/>
    <Column id=orders title="注文数" fmt='#,##0'/>
    <Column id=sales title="売上" fmt='$#,##0'/>
    <Column id=profit title="利益" fmt='$#,##0'/>
    <Column id=profit_margin title="利益率" fmt='0.0"%"'/>
</DataTable>

---

## Evidence 機能デモ

Evidence の様々な機能を試せるデモページ：

- [DataTable デモ](/datatable-demo) - 条件付きフォーマット、リンク、バッジなど
- [入力コンポーネント](/inputs-demo) - Dropdown, ButtonGroup, TextInput など
- [条件分岐デモ](/conditional-demo) - `{#if}`, `{#each}` の使い方
- [カスタムコンポーネント](/custom-components) - Svelte でコンポーネント作成
- カテゴリ詳細（テンプレートページ）- 動的ルートのデモ
  - [Technology](/categories/Technology)
  - [Furniture](/categories/Furniture)
  - [Office Supplies](/categories/Office-Supplies)
