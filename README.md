E-Commerce Sales Data Warehouse — AWS ETL Pipeline (S3 → Glue → Redshift)
=====================================================================

Project scaffold for a beginner-friendly data engineering portfolio:

- Goal: Build an ETL pipeline from raw CSVs to a star-schema in Redshift using AWS Glue for ETL. Include local scripts for development and Streamlit for a simple dashboard.
- Datasets (already present): `datasets/` contains Olist CSVs.

Getting started
--------------
1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the CSV analysis script to generate column/type/missing summaries:

```bash
python3 scripts/analyze_csvs.py
```

Project structure
-----------------
- `datasets/` — raw CSVs provided by the user (do not commit large raw files).
- `scripts/` — local helper scripts (CSV analysis, local ETL helpers).
- `src/` — Python package for ETL logic and Glue-compatible job code.
- `glue_scripts/` — starter Glue job templates (PySpark Glue jobs).
- `infra/` — infra notes / CloudFormation or Terraform placeholders.
- `notebooks/` — exploratory notebooks.
- `docs/` — architecture, design decisions, README fragments.

Next steps
----------
1. Run `scripts/analyze_csvs.py` to compute missing-value counts and uniques. (I will run this next if you want.)
2. After analysis, I will implement the Glue PySpark job and Redshift DDL statements.

