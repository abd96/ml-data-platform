from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess

def materialize():
    result = subprocess.run(
        "cd /opt/airflow/feast_repo && feast materialize-incremental " + datetime.now().strftime("%Y-%m-%d"),
        shell=True,
        capture_output=True,
        text=True
    )
    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)
    result.check_returncode()  # This will raise CalledProcessError if exit code != 0



with DAG(
    dag_id="feast_materialize_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:
    task = PythonOperator(
        task_id="materialize_user_features",
        python_callable=materialize
    )
