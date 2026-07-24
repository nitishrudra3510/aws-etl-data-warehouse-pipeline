"""Local transformation script: read raw CSVs, apply basic cleans, and write parquet to `processed/`.

This is intended for local testing and will be adapted to Glue PySpark later.
"""
import os
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT, 'datasets')
OUT_DIR = os.path.join(ROOT, 'processed')
os.makedirs(OUT_DIR, exist_ok=True)

def load_csv(name):
    path = os.path.join(DATA_DIR, name)
    return pd.read_csv(path)

def transform_products(df):
    df['product_category_name'] = df['product_category_name'].fillna('unknown')
    # ensure integer-like fields
    for c in ['product_name_lenght','product_description_lenght','product_photos_qty']:
        if c in df:
            df[c] = df[c].fillna(0).astype('Int64')
    return df

def transform_orders(df):
    # parse datetimes (include columns containing 'timestamp' or 'date' or ending with '_at')
    ts_cols = [c for c in df.columns if ('timestamp' in c) or ('date' in c) or c.endswith('_at')]
    for c in ts_cols:
        df[c] = pd.to_datetime(df[c], errors='coerce')
    df['order_date'] = df['order_purchase_timestamp'].dt.date
    df['order_year'] = df['order_purchase_timestamp'].dt.year
    df['order_month'] = df['order_purchase_timestamp'].dt.month
    return df

def transform_order_items(df):
    df['price'] = df['price'].astype(float)
    df['freight_value'] = df['freight_value'].astype(float)
    df['line_total'] = df['price'] + df['freight_value']
    return df

def main():
    print('Loading and transforming CSVs...')
    products = load_csv('olist_products_dataset.csv')
    products = transform_products(products)
    products.to_parquet(os.path.join(OUT_DIR, 'products.parquet'), index=False)

    customers = load_csv('olist_customers_dataset.csv')
    customers.to_parquet(os.path.join(OUT_DIR, 'customers.parquet'), index=False)

    orders = load_csv('olist_orders_dataset.csv')
    orders = transform_orders(orders)
    orders.to_parquet(os.path.join(OUT_DIR, 'orders.parquet'), index=False)

    items = load_csv('olist_order_items_dataset.csv')
    items = transform_order_items(items)
    items.to_parquet(os.path.join(OUT_DIR, 'order_items.parquet'), index=False)

    payments = load_csv('olist_order_payments_dataset.csv')
    payments.to_parquet(os.path.join(OUT_DIR, 'payments.parquet'), index=False)

    sellers = load_csv('olist_sellers_dataset.csv')
    sellers.to_parquet(os.path.join(OUT_DIR, 'sellers.parquet'), index=False)

    print('Wrote parquet files to', OUT_DIR)

if __name__ == '__main__':
    main()
