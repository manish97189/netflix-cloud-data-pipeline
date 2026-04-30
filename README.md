# 🎬 Netflix Global Content Strategy Pipeline

### Project Overview
This project is an end-to-end cloud data pipeline designed to ingest, process, and visualize Netflix's massive content catalog. 

### Architecture
* **Data Lake (Amazon S3):** Stored raw CSV drops and final processed Parquet files.
* **ETL Engine (AWS Glue):** Cleaned, normalized, and converted raw data into compressed Snappy Parquet format.
* **Schema Mapping (AWS Glue Crawler):** Dynamically updated the AWS Data Catalog.
* **Query Engine (Amazon Athena):** Executed serverless SQL queries to aggregate content metrics.
* **Frontend Dashboard (Streamlit):** An interactive, Python-based web app built with Pandas and Plotly to visualize genre distribution, global production reach, and historical release trends.
