{{ config(materialized='table') }}

-- 全体サマリー（Evidence/Streamlitのトップページと同等）
SELECT
    COUNT(*) as total_orders,
    SUM(sales) as total_sales,
    SUM(profit) as total_profit,
    AVG(discount) as avg_discount,
    SUM(profit) / NULLIF(SUM(sales), 0) * 100 as profit_margin
FROM {{ ref('stg_superstore') }}
