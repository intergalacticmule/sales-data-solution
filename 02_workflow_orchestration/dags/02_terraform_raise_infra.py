from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG(
    '02_terraform_raise_infra',
    description = 'Raise GCP infrastructure with Terraform',
    schedule_interval = None,
    start_date = datetime(2025, 3, 14),
    catchup=False
)
terraform_apply = BashOperator(
    task_id = 'terraform_apply',
    bash_command =' /home/airflow/scripts/terraform_apply.sh ',
    dag = dag
)
terraform_apply