# ML-Ready Data Platform Project

## Project Goal

Build an **end-to-end data engineering platform** that:
- Ingests or generates simulated interaction data (user-item events)
- Transforms raw data into ML-ready features
- Stores features in a **feature store (Feast)** for training & inference
- Orchestrates workflows with **Airflow**
- Serves features in real-time via **FastAPI**
- Runs fully containerized with **Docker Compose**
- Adds monitoring with **Grafana + Prometheus**

---

## Key Components

| Layer         | Tool/Tech Used                                | Purpose                                              |
|---------------|------------------------------------------------|------------------------------------------------------|
| Ingestion     | Python scripts (or Kafka later)                | Generate or simulate user-item interaction logs     |
| Storage       | Local filesystem (Parquet), optionally S3      | Store raw and transformed data                      |
| Transformation| Spark (or Pandas), dbt (optional)              | Generate meaningful user/item features              |
| Feature Store | **Feast**                                      | Store & serve features for both training & inference|
| Orchestration | **Airflow**                                    | Schedule feature generation + materialization       |
| Serving       | **FastAPI**                                    | API to return user features to downstream services  |
| Infrastructure| **Docker Compose**                             | Run all services locally in isolated containers     |
| Monitoring    | Redis (for online store), PostgreSQL (Feast DB)| Track freshness, fast lookups, metadata, etc.       |


---
## How to run ?

1. ```docker-compose down --volumes --remove-orphan``` (if rerunnig)

2. ``` docker-compose run --rm airflow airflow db migrate``` 

3. ``` docker-compose up``` 
