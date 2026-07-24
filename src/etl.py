"""Local ETL helpers and entrypoints.

This module contains starter functions that will be adapted to Glue PySpark later.
"""
import argparse
import pandas as pd

def summarize_csv(path, nrows=5):
    df = pd.read_csv(path)
    print(f"Summary for {path}")
    print(df.dtypes)
    print(df.isna().sum())
    print(df.head(nrows))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="CSV file to summarize")
    args = parser.parse_args()
    if args.file:
        summarize_csv(args.file)
    else:
        print("Provide --file to summarize a CSV")

if __name__ == '__main__':
    main()
