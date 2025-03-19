from datetime import datetime
from urllib.request import urlretrieve
from zipfile import ZipFile
import os
from google.cloud import storage
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

url = "https://www.kaggle.com/api/v1/datasets/download/vinothkannaece/sales-dataset/"
destination_dir = "/home/airflow/files/GCP/sales_data/"
file_name_zipped = "sales_data.zip"
file_name_unzipped = file_name_zipped.replace("zip", "csv")
creds = "/home/airflow/terraform/keys/my-creds.json"
bucket_name = "sales_data_analysis_bucket"

def create_dir(dir):
    try:
        os.makedirs(dir)
        print(f"Directory {dir} created successfully.")
    except FileExistsError:
        print(f"Directory '{dir}' already exists. Moving on...")

def download_file(url, destination):
    urlretrieve(url, destination)
    print(f"File {destination} downloaded successfully from {url}.")

def unzip_file(zip_dir, zip_name, file_name):
    with ZipFile(zip_dir + zip_name, 'r') as zip_file:
        zip_file.extractall(zip_dir)
        print(f"File {zip_dir + file_name} extracted succesfully from {zip_dir + zip_name}.")

def delete_file(file):
    os.remove(file)
    print(f"File {file} deleted successfully.")

def upload_file(file, bucket_name, local_dir):
    print(f"Uploading file {file} to bucket {bucket_name}...")
    client = storage.Client.from_service_account_json(creds)
    bucket = client.get_bucket(bucket_name)
    file_name = file.replace(local_dir, "")
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file)
    if storage.Blob(bucket=bucket, name=file_name).exists(client):
        print(f"File {file} uploaded to bucket {bucket_name} successfully.")
    else:
        raise Exception(f"Failed to upload file {file} to bucket {bucket_name}.")

with DAG(
    "03_upload_data_to_gcp",
    description = "Fetch data file and upload it to GCP",
    schedule_interval = None,
    start_date = datetime(2025, 3, 14),
    catchup=False
) as dag:

    create_directory = PythonOperator(
        task_id = "create_directory",
        python_callable = create_dir,
        op_kwargs = {"dir": destination_dir}
    )

    download_data = PythonOperator(
        task_id = "download_data",
        python_callable = download_file,
        op_kwargs = {"url": url, "destination": destination_dir + file_name_zipped}
    )

    unzip_data = PythonOperator(
        task_id = "unzip_data",
        python_callable = unzip_file,
        op_kwargs = {"zip_dir": destination_dir, "zip_name": file_name_zipped, "file_name":file_name_unzipped}
    )

    delete_zip = PythonOperator (
        task_id = "delete_zip",
        python_callable = delete_file,
        op_kwargs = {"file": destination_dir + file_name_zipped}
    )

    upload_to_gcp = PythonOperator (
        task_id = "upload_to_gcp",
        python_callable = upload_file,
        op_kwargs = {"file": destination_dir + file_name_unzipped, "bucket_name": bucket_name, "local_dir": destination_dir}
    )

    delete_csv = PythonOperator (
        task_id = "delete_csv",
        python_callable = delete_file,
        op_kwargs = {"file": destination_dir + file_name_unzipped}
    )

create_directory >> download_data >> unzip_data >> delete_zip >> upload_to_gcp >> delete_csv