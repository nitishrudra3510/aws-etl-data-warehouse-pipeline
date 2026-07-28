-- Redshift DDL for star schema (adapt for your cluster)

-- Dimension: date -- 
CREATE TABLE IF NOT EXISTS dim_date (
    date_id INT PRIMARY KEY,
    date DATE,
    year INT,
    quarter INT,
    month INT,
    day INT,
    weekday INT,
    is_weekend BOOLEAN
);

-- Dimension: customer
CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id VARCHAR(64) PRIMARY KEY,
    customer_unique_id VARCHAR(64),
    zip_code_prefix VARCHAR(16),
    city VARCHAR(128),
    state CHAR(2)
);

-- Dimension: product
CREATE TABLE IF NOT EXISTS dim_product (
    product_id VARCHAR(64) PRIMARY KEY,
    product_category_name VARCHAR(256),
    product_category_name_english VARCHAR(256),
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g FLOAT,
    product_length_cm FLOAT,
    product_height_cm FLOAT,
    product_width_cm FLOAT
);

-- Dimension: seller
CREATE TABLE IF NOT EXISTS dim_seller (
    seller_id VARCHAR(64) PRIMARY KEY,
    seller_zip_code_prefix VARCHAR(16),
    seller_city VARCHAR(128),
    seller_state CHAR(2)
);

-- Fact: sales (grain = order line)
CREATE TABLE IF NOT EXISTS fact_sales (
    sale_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    order_id VARCHAR(64),
    order_item_id INT,
    customer_id VARCHAR(64),
    product_id VARCHAR(64),
    seller_id VARCHAR(64),
    date_id INT,
    order_status VARCHAR(64),
    order_purchase_timestamp TIMESTAMP,
    shipping_limit_date TIMESTAMP,
    price FLOAT,
    freight_value FLOAT,
    line_total FLOAT,
    payment_value FLOAT,
    payment_type VARCHAR(64)
);

-- Notes:
-- 1) Load parquet files from S3 using COPY or CREATE EXTERNAL TABLE + INSERT.
-- 2) Consider DISTKEY/SORTKEY choices for Redshift based on query patterns.
