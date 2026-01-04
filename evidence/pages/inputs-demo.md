---
title: 入力コンポーネント デモ
---

# 入力コンポーネント

Evidence では様々な入力を使ってインタラクティブなダッシュボードが作れるにぇ！

---

## Dropdown（ドロップダウン）

```sql categories
SELECT DISTINCT category FROM superstore.orders
```

```sql states
SELECT DISTINCT state FROM superstore.orders ORDER BY state
```

<Dropdown data={categories} name=selected_category value=category>
    <DropdownOption value="%" valueLabel="全カテゴリ"/>
</Dropdown>

<Dropdown data={states} name=selected_state value=state>
    <DropdownOption value="%" valueLabel="全州"/>
</Dropdown>

```sql filtered_data
SELECT
    category,
    state,
    SUM(sales) as sales,
    SUM(profit) as profit
FROM superstore.orders
WHERE category LIKE '${inputs.selected_category.value}'
  AND state LIKE '${inputs.selected_state.value}'
GROUP BY category, state
ORDER BY sales DESC
LIMIT 10
```

<BarChart
    data={filtered_data}
    x=state
    y=sales
    series=category
    title="州別・カテゴリ別売上"
/>

---

## ButtonGroup（ボタングループ）

<ButtonGroup name=metric_select title="指標選択">
    <ButtonGroupItem valueLabel="売上" value="sales" default />
    <ButtonGroupItem valueLabel="利益" value="profit" />
    <ButtonGroupItem valueLabel="数量" value="quantity" />
</ButtonGroup>

```sql metric_by_category
SELECT
    category,
    SUM(sales) as sales,
    SUM(profit) as profit,
    SUM(quantity) as quantity
FROM superstore.orders
GROUP BY category
```

{#if inputs.metric_select.value === 'sales'}
<BarChart data={metric_by_category} x=category y=sales title="カテゴリ別 売上" />
{:else if inputs.metric_select.value === 'profit'}
<BarChart data={metric_by_category} x=category y=profit title="カテゴリ別 利益" />
{:else}
<BarChart data={metric_by_category} x=category y=quantity title="カテゴリ別 数量" />
{/if}

---

## 複数選択（MultiSelect）

```sql segments
SELECT DISTINCT segment FROM superstore.orders
```

<Dropdown
    data={segments}
    name=multi_segment
    value=segment
    multiple=true
    selectAllByDefault=true
    title="セグメント選択"
/>

```sql segment_sales
SELECT
    segment,
    SUM(sales) as sales,
    SUM(profit) as profit
FROM superstore.orders
WHERE segment IN ${inputs.multi_segment.value}
GROUP BY segment
ORDER BY sales DESC
```

<BarChart data={segment_sales} x=segment y=sales title="セグメント別売上" />

<DataTable data={segment_sales}>
    <Column id=segment title="セグメント" />
    <Column id=sales title="売上" fmt='$#,##0' />
    <Column id=profit title="利益" fmt='$#,##0' />
</DataTable>
