{{ config(materialized='view') }}

SELECT
    "Order Date" as order_date,
    "Ship Mode" as ship_mode,
    "Customer Name" as customer_name,
    "Segment" as segment,
    "City" as city,
    "State" as state,
    "Category" as category,
    "Sub-Category" as sub_category,
    "Product Name" as product_name,
    CAST("Sales" AS NUMERIC) as sales,
    CAST("Quantity" AS INTEGER) as quantity,
    CAST("Discount" AS NUMERIC) as discount,
    CAST("Profit" AS NUMERIC) as profit
FROM {{ ref('superstore') }}
