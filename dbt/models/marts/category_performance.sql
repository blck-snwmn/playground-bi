{{ config(materialized='table') }}

-- カテゴリ別パフォーマンス
SELECT
    category,
    COUNT(*) as order_count,
    SUM(sales) as sales,
    SUM(profit) as profit,
    SUM(profit) / NULLIF(SUM(sales), 0) * 100 as profit_margin
FROM {{ ref('stg_superstore') }}
GROUP BY category
ORDER BY sales DESC
