Architecture overview
=====================

Data flow (high-level):

1. Raw CSVs in `datasets/` (local) → upload to S3 `raw/` prefix
2. Glue Crawler builds table schema in Glue Data Catalog
3. Glue ETL job(s) transform raw → processed (parquet, partitioned by date)
4. Load transformed data to Redshift (COPY from S3) into star schema
5. Analytics via SQL queries and Streamlit dashboard

Star schema details and DDL will be added after CSV analysis.
