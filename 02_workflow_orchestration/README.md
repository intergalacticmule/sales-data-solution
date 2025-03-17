# <div align="center">Workflow Orchestration</div>

## Overview

In this section we will examine how we achieve automating the data pipeline - from raising the necessary cloud infrastructure, through retrieving the data from source, to landing it safely in our data storage.

We have chosen Apache Airflow for our workflow orchestration, containerized via Docker. Alongisde it we have Terraform, which is an IaC tool that will help us deploy the cloud infrastructure we need.

## Setup

In order to get everything up and running, we must first clone the repo, start our Dockerized Airflow, create a new project in Google Console, and raise the necessary infrastructure on the cloud via our Terraform DAGs, and finally transfer the data from source to the cloud:

### Get dockerized Airflow services up and running

1. Clone the repository:

```bash
$ git clone https://github.com/intergalacticmule/sales-data-solution.git
```

2. Navigate to folder _02_workflow_orchestration_:

```bash
$ cd 02_workflow_orchestration
```

3. Set up our Dockerized Airflow:

- Create the necessary directories:

```bash
$ mkdir -p ./logs ./plugins ./config
$ echo -e "AIRFLOW_UID=$(id -u)" > .env
```

- Build the images from [docker-compose.yaml](./docker-compose.yaml). Note the use of [Dockerfile](./Dockerfile) to install Terraform on our Airflow image:

```bash
$ docker compose build
```

- Run Airflow database migrations and create user

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
    │   └── my-creds.json #service account key file
    ├── main.tf #main Terraform file
    └── variables.tf #Terraform variables file
```
Refering to lines 76-82 of [docker-compose.yaml](./docker-compose.yaml), we can see that all of our subdirectories are mapped to directories in the Airflow container. Most notably, folders _dags_, _terraform_, and _scripts_ are mapped to the home folder of our newly created Airflow user, and are directly tied to the logic we will be implementing shortly.

A couple of minutes after executing the _`docker compose up`_ command, the webserver should be up and running. Navitgate to http://localhost:8080/home in your browser. You should be greeted by a sign in form like so:

![Airflow sign-in form](/images/airflow_sign_in.png)

The correct login credentials are:

```
Username: airflow
Password: airflow
```

Hit sign in, and you should find yourself in the main Airflow UI:

![Airflow UI](/images/airflow_ui.png)

### Create project in Google Console