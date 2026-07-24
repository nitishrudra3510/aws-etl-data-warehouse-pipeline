Infrastructure notes
====================

This folder will contain CloudFormation/Terraform or CDK artifacts to provision:

- S3 buckets: `raw/`, `processed/`, `curated/`
- AWS Glue: crawlers + jobs
- IAM roles for Glue
- Amazon Redshift cluster (or serverless) and schemas

For a beginner-friendly free-tier approach, consider using Redshift Serverless or a small dev cluster and keep data volumes small.
