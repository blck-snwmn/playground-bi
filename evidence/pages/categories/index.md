---
title: カテゴリ一覧
---

[Home](/) > Categories

# カテゴリ一覧

```sql all_categories
SELECT
    category,
    COUNT(*) as order_count,
    SUM(sales) as total_sales,
    SUM(profit) as total_profit
FROM superstore.orders
GROUP BY category
ORDER BY total_sales DESC
```

<DataTable data={all_categories} link=category_link>
    <Column id=category title="カテゴリ" />
    <Column id=order_count title="注文数" fmt='#,##0' />
    <Column id=total_sales title="売上" fmt='$#,##0' />
    <Column id=total_profit title="利益" fmt='$#,##0' />
</DataTable>

---

## カテゴリページへのリンク

- [Technology](/categories/Technology)
- [Furniture](/categories/Furniture)
- [Office Supplies](/categories/Office-Supplies)
