---
title: 積み上げグラフ デモ
---

# 積み上げグラフ

Evidence での積み上げグラフ（Stacked Chart）のデモ。

---

## カテゴリ × セグメント 積み上げ棒グラフ

```sql category_segment_sales
SELECT
    category,
    segment,
    SUM(sales) as sales,
    SUM(profit) as profit
FROM superstore.orders
GROUP BY category, segment
ORDER BY category, segment
```

<BarChart
    data={category_segment_sales}
    x=category
    y=sales
    series=segment
    title="カテゴリ別・セグメント別 売上（積み上げ）"
/>

---

## 月別 × カテゴリ 積み上げ棒グラフ

```sql monthly_category_sales
SELECT
    STRFTIME('%Y-%m', order_date) as month,
    category,
    SUM(sales) as sales
FROM superstore.orders
GROUP BY month, category
ORDER BY month, category
```

<BarChart
    data={monthly_category_sales}
    x=month
    y=sales
    series=category
    sort=false
    title="月別・カテゴリ別 売上（積み上げ）"
/>

---

## 積み上げエリアチャート

```sql monthly_segment_sales
SELECT
    STRFTIME('%Y-%m', order_date) as month,
    segment,
    SUM(sales) as sales
FROM superstore.orders
GROUP BY month, segment
ORDER BY month, segment
```

<AreaChart
    data={monthly_segment_sales}
    x=month
    y=sales
    series=segment
    sort=false
    title="月別・セグメント別 売上（積み上げエリア）"
/>

---

## 100% 積み上げ棒グラフ

<BarChart
    data={category_segment_sales}
    x=category
    y=sales
    series=segment
    type=stacked100
    title="カテゴリ別・セグメント別 売上（100%積み上げ）"
/>

---

## グループ化棒グラフ（比較用）

<BarChart
    data={category_segment_sales}
    x=category
    y=sales
    series=segment
    type=grouped
    title="カテゴリ別・セグメント別 売上（グループ化）"
/>
