from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    '04_dbt_test_connection',
    description = 'Test dbt connection to BigQuery',
    schedule_interval = None,
    start_date = datetime(2025, 3, 14),
    catchup=False
) as dag:

    dbt_debug = BashOperator(
        task_id = 'dbt_debug',
        bash_command =' /home/airflow/scripts/dbt/debug.sh '
    )

dbt_debug