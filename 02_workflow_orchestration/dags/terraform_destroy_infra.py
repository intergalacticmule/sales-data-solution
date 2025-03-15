from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG(
    'terraform_destroy_infra',
    description = 'Destroy GCP infrastructure with Terraform',
    schedule_interval = None,
    start_date = datetime(2025, 3, 14),
    catchup=False
)

terraform_destroy = BashOperator(
    task_id = 'terraform_destroy',
    bash_command = '/home/airflow/scripts/terraform/terraform_destroy.sh ',
    dag=dag
)

terraform_destroy