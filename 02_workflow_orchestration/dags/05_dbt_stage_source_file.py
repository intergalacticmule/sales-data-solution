from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    "05_dbt_stage_source_file",
    description = "Create BigQuery external table from source file",
    schedule_interval = None,
    start_date = datetime(2025, 3, 14),
    catchup=False
) as dag:

    stage_source_file = BashOperator(
        task_id = "stage_source_file",
        bash_command =" /home/airflow/scripts/dbt/stage_external_sources.sh "
    )

stage_source_file