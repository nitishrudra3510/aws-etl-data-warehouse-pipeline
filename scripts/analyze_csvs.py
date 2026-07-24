"""Analyze all CSVs in the `datasets/` folder and print concise summaries.

Run:
    python3 scripts/analyze_csvs.py
"""
import os
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'datasets')

def analyze_file(path):
    print('---')
    print(f'File: {path}')
    try:
        df = pd.read_csv(path)
    except Exception as e:
        print('Error reading file:', e)
        return
    print('Rows:', len(df))
    print('Columns:', list(df.columns))
    print('Dtypes:')
    print(df.dtypes)
    print('Missing values:')
    print(df.isna().sum())
    print('Unique counts (first 10 cols):')
    for c in df.columns[:10]:
        try:
            print(f'  {c}:', df[c].nunique())
        except Exception:
            print(f'  {c}: error')
    print('Sample rows:')
    print(df.head(3).to_string(index=False))

def main():
    files = [f for f in os.listdir(DATA_DIR) if f.lower().endswith('.csv')]
    if not files:
        print('No CSV files in datasets/.')
        return
    for f in files:
        analyze_file(os.path.join(DATA_DIR, f))

if __name__ == '__main__':
    main()
