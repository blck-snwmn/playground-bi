{{ config(materialized='table') }}

-- 月別トレンド
SELECT
    TO_CHAR(order_date::DATE, 'YYYY-MM') as month,
    category,
    segment,
    COUNT(*) as order_count,
    SUM(sales) as sales,
    SUM(profit) as profit
FROM {{ ref('stg_superstore') }}
GROUP BY 1, 2, 3
ORDER BY 1
