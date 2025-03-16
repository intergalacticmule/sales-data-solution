from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG(
    '01_terraform_init',
    description = 'Initiallize Terraform working directory',
    schedule_interval = None,
    start_date = datetime(2025, 3, 14),
    catchup=False
)

terraform_init = BashOperator(
    task_id = 'terraform_init',
    bash_command =' /home/airflow/scripts/terraform/terraform_init.sh ',
    dag = dag
)

terraform_init