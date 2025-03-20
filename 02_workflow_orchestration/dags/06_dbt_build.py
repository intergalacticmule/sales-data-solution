from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    "06_dbt_build",
    description = "Build dbt models",
    schedule_interval = None,
    start_date = datetime(2025, 3, 14),
    catchup=False
) as dag:

    dbt_build = BashOperator(
        task_id = "dbt_build",
        bash_command =" /home/airflow/scripts/dbt/build.sh "
    )

dbt_build