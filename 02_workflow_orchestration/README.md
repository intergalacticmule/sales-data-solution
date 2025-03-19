# <div align="center">Workflow Orchestration</div>

## Overview

In this section we will examine how we will automate the data pipeline - from raising the necessary cloud infrastructure, through retrieving the data from source, to landing it safely in our data storage.

We have chosen Apache Airflow for our workflow orchestration, containerized via Docker. Alongisde it we have Terraform, which is an IaC tool that will help us deploy the cloud infrastructure we need. Additionally, we will be installing dbt, which will help us build our warehouse model.

## Setup

In order to get everything up and running, we must first clone the repo, start our Dockerized Airflow, create a new project in Google Console, and raise the necessary infrastructure on the cloud via our Terraform DAGs, and finally transfer the data from source to the cloud:

### Get dockerized Airflow services up and running

1. Clone the repository:

```bash
$ git clone https://github.com/intergalacticmule/sales-data-solution.git
```

2. Navigate to folder 02_workflow_orchestration:

```bash
$ cd 02_workflow_orchestration
```

3. Set up our Dockerized Airflow:

- Create the necessary directories:

```bash
$ mkdir -p ./logs ./plugins ./config
$ echo -e "AIRFLOW_UID=$(id -u)" > .env
```

- Build the images from [docker-compose.yaml](./docker-compose.yaml). Note the use of [Dockerfile](./Dockerfile) to install Terraform and dbt on our Airflow image:

```bash
$ docker compose build
```

- Run Airflow database migrations and create user:

```bash
$ docker compose up airflow-init
```

- Start all services. You can also add `-d` at the end of this command to run in detached mode, however this is not recommended for the first run as you will surely miss out on any errors from the startup logs:

```bash
$ docker compose up 
```

This leaves us with the following folder structure:

```bash
02_workflow_orchestration/
├── config #Airflow config folder
├── dags #DAGs folder
│   ├── 01_terraform_init.py #DAG that performs terraform init
│   ├── 02_terraform_raise_infra.py #DAG that performs terraform apply
│   ├── 03_upload_data_to_gcp.py #DAG that retrieves source file and uploads it to GCP
│   └── terraform_destroy_infra.py #DAG that performs terraform destroy
├── dbt #dbt-core folder
│   ├── .user.yml #dbt cookie
│   ├── my-creds.json #dbt service account
│   └── profiles.yml #dbt-core config
├── docker-compose.yaml #docker compose file containing all our configured service images
├── Dockerfile #Dockerfile installing Terraform to Airflow image
├── logs #Airflow logs folder 
├── plugins #Airflow plugins folder
├── README.md #git README file
├── scripts #scripts folder
│   ├── terraform_apply.sh #bash script used by DAG to run terraform apply command
│   ├── terraform_destroy.sh #bash script used by DAG to run terraform apply command
│   └── terraform_init.sh #bash script used by DAG to run terraform apply command
└── terraform #Terraform folder
    ├── keys #keys folder
    │   └── my-creds.json #Airflow service account key file
    ├── main.tf #main Terraform file
    └── variables.tf #Terraform variables file
```

A couple of minutes after executing the `docker compose up` command, the webserver should be up and running. To check this, execute:

```bash
docker ps
```

The `CREATED` column of the command output should indicate all the containers are healthy, i.e. `Up X seconds (healthy)`, and none should indicate `Up X seconds (health: starting)`. If the latter is the case, wait a little bit more for the processes to start.

 Navitgate to http://localhost:8080/home in your browser. You should be greeted by a sign-in form like so:

![Airflow sign-in form](/images/airflow_sign_in.png)

The correct login credentials are:

```
Username: airflow
Password: airflow
```

Hit sign in, and you should find yourself in the main Airflow UI:

![Airflow UI](/images/airflow_ui.png)

### Create project in Google Console

1. Navigate to [Google Cloud Console](http://console.cloud.google.com/)

2. Create a new project:

![Creating GCP Project](/images/gcp_project.gif)

### Create service accounts 

Create a service account for Airflow with _BigQuery Admin_ and _Storage Admin_ roles, so that Airflow is able to raise the necessary infrastructure via Terraform:

![Creating GCP Service Account](/images/gcp_service_account.gif)

Repeating the steps above, create another service account for dbt, and add _BigQuery Admin_ and _Storage Object Viewer_ roles to it. These are necessary so that dbt can create tables and read files from our bucket respectively.

### Export service account keys

![Exporting GCP Service Account Key](/images/gcp_export_key.gif)

Save this key inside the project folder in `.../sales-data-solution/02_workflow_orchestration/terraform/keys/` named `my-creds.json`.

Repeat the same step for the dbt account, saving the key inside `.../sales-data-solution/02_workflow_orchestration/dbt/` named `my-creds.json`

### Update project ID in variables.tf

Open file [variables.tf](./terraform/variables.tf) and update it with your project's ID here:

```yml
variable "project" {
  description = "Project"
  default     = "sales-data-analysis-453808" #Your project ID here
}
```

### Update project ID in profiles.yml 

Open file [project.yml](./dbt/profiles.yml) and update it with your project's ID here:

```yml
project: sales-data-analysis-453808 #Your project ID here
```


### Execute 01_terraform_init DAG

Navigate back to [Airflow's web UI](http://localhost:8080/home), and execute DAG 01_terraform_init:

![Execute Terraform Init](/images/terraform_init.gif)

This DAG can be inspected [here](./dags/01_terraform_init.py). It consists of a BashOperator task that calls [this bash script](./scripts/terraform/init.sh), which basically navigates to the Terraform directory on the container and performs `terraform init`.

We have now initialized the Terraform working directory

### Execute 02_terraform_apply DAG

Execute DAG 02_terraform_apply from the Airflow homepage.

This DAG can be inspected [here](./dags/02_terraform_apply_infra.py). It consists of a BashOperator task that calls [this bash script](./scripts/terraform/apply.sh), which basically navigates to the Terraform directory on the container and performs `terraform apply`.

We have now created a GCS bucket, and two BigQuery datasets for our needs.

### Execute 03_upload_data_to_gcp DAG

Execute DAG 03_upload_data_to_gcp from the Airflow homepage.

This DAG can be inspected [here](./dags/03_upload_data_to_gcp.py). It consists of predefined functions that create our local working directory, download our data file, unzip it, upload it to GCP and verify that it was successful, and then clean up locally. These functions are executed via PythonOperator tasks one after the other, automating the entire process of data retrieval and storage.

We now have our source file securely stored on the cloud. Our goals for this section are thus complete.