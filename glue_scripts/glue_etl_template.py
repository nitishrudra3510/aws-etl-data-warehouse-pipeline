"""Glue PySpark ETL template (to adapt into AWS Glue job)

Responsibilities:
- Read raw CSVs from S3 (or Glue catalog)
- Clean and cast types
- Write Parquet to processed S3 prefix partitioned by order_date
"""
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col, to_date, concat_ws

def main():
    sc = SparkContext()
    glueContext = GlueContext(sc)
    spark = glueContext.spark_session

    # Example: replace with your S3 paths
    raw_prefix = 's3://your-bucket/raw/'
    processed_prefix = 's3://your-bucket/processed/'
    ##
    orders = spark.read.option('header', 'true').csv(raw_prefix + 'olist_orders_dataset.csv')
    items = spark.read.option('header', 'true').csv(raw_prefix + 'olist_order_items_dataset.csv')
    products = spark.read.option('header', 'true').csv(raw_prefix + 'olist_products_dataset.csv')

    # Basic casts
    items = items.withColumn('price', col('price').cast('double'))
    items = items.withColumn('freight_value', col('freight_value').cast('double'))
    items = items.withColumn('line_total', col('price') + col('freight_value'))

    orders = orders.withColumn('order_purchase_date', to_date(col('order_purchase_timestamp')))

    # Join example and write partitioned by order_purchase_date
    fact = items.join(orders, on='order_id', how='left')

    fact.write.mode('overwrite').partitionBy('order_purchase_date').parquet(processed_prefix + 'fact_sales/')

if __name__ == '__main__':
    main()
