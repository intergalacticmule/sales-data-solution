from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    '01_terraform_init',
    description = 'Initiallize Terraform working directory',
    schedule_interval = None,
    start_date = datetime(2025, 3, 14),
    catchup=False
) as dag:

    terraform_init = BashOperator(
        task_id = 'terraform_init',
        bash_command =' /home/airflow/scripts/terraform/init.sh ',
    )

terraform_init