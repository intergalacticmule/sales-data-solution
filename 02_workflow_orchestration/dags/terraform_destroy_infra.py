from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    'terraform_destroy_infra',
    description = 'Destroy GCP infrastructure with Terraform',
    schedule_interval = None,
    start_date = datetime(2025, 3, 14),
    catchup=False
) as dag:

    terraform_destroy = BashOperator(
        task_id = 'terraform_destroy',
        bash_command = '/home/airflow/scripts/terraform/destroy.sh ',
    )

terraform_destroy