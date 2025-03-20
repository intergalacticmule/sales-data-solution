from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    "04_dbt_init",
    description = "dbt test connection and install deps",
    schedule_interval = None,
    start_date = datetime(2025, 3, 14),
    catchup=False
) as dag:

    dbt_debug = BashOperator(
        task_id = "dbt_debug",
        bash_command =" /home/airflow/scripts/dbt/debug.sh "
    )

    dbt_deps = BashOperator(
        task_id = "dbt_deps",
        bash_command =" /home/airflow/scripts/dbt/deps.sh "
    )

dbt_debug >> dbt_deps