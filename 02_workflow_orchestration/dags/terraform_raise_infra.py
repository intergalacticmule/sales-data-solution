from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG(
    'terraform_raise_infra',
    description = 'Raise GCP infrastructure with Terraform',
    schedule_interval = None,
    start_date = datetime(2025, 3, 14),
    catchup=False
)

terraform_init = BashOperator(
    task_id = 'terraform_init',
    bash_command = '/home/airflow/scripts/terraform/terraform_init.sh ',
    dag=dag
)

terraform_apply = BashOperator(
    task_id = 'terraform_apply',
    bash_command =' /home/airflow/scripts/terraform/terraform_apply.sh ',
    dag = dag
)

terraform_init >> terraform_apply