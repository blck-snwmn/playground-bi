---
title: 条件分岐デモ
---

# 条件分岐と繰り返し

Evidence は Svelte ベースなので、`{#if}`, `{#each}` などの制御構文が使える！

---

## 利益率データ

```sql profit_check
SELECT
    SUM(profit) as total_profit,
    SUM(profit) / SUM(sales) * 100 as profit_margin
FROM superstore.orders
```

<BigValue data={profit_check} value=profit_margin title="利益率" fmt='0.0"%"' />

---

## カテゴリ別データ

```sql top_categories
SELECT
    category,
    SUM(sales) as sales,
    SUM(profit) as profit
FROM superstore.orders
GROUP BY category
ORDER BY sales DESC
```

<DataTable data={top_categories}>
    <Column id=category title="カテゴリ" />
    <Column id=sales title="売上" fmt='$#,##0' />
    <Column id=profit title="利益" fmt='$#,##0' />
</DataTable>

---

## 動的なチャートタイプ切替

<ButtonGroup name=chart_type>
    <ButtonGroupItem value="bar" valueLabel="棒グラフ" default />
    <ButtonGroupItem value="line" valueLabel="折れ線" />
    <ButtonGroupItem value="area" valueLabel="エリア" />
</ButtonGroup>

```sql monthly_sales
SELECT
    STRFTIME('%Y-%m', order_date) as month,
    SUM(sales) as sales
FROM superstore.orders
GROUP BY month
ORDER BY month
```

{#if inputs.chart_type.value === 'bar'}
<BarChart data={monthly_sales} x=month y=sales title="月別売上（棒グラフ）" />
{:else if inputs.chart_type.value === 'line'}
<LineChart data={monthly_sales} x=month y=sales title="月別売上（折れ線）" />
{:else}
<AreaChart data={monthly_sales} x=month y=sales title="月別売上（エリア）" />
{/if}
