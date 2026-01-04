-- SuperStore データを DuckDB にロード
-- Usage: duckdb < shared/init_duckdb.sql

-- CSVファイルからテーブルを作成
CREATE TABLE IF NOT EXISTS superstore AS
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
    CAST("Sales" AS DOUBLE) as sales,
    CAST("Quantity" AS INTEGER) as quantity,
    CAST("Discount" AS DOUBLE) as discount,
    CAST("Profit" AS DOUBLE) as profit
FROM read_csv('data/SuperStore.csv', header=true);

-- 確認
SELECT COUNT(*) as total_rows FROM superstore;
SELECT * FROM superstore LIMIT 5;
