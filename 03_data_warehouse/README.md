# <div align="center">Data Warehouse</div>

## Overview

In this section we will examine how to build our data warehouse on top of the file we uploaded to GCS. We have chosen dbt and Google BigQuery for this purpose.

In the previous section we did a little bit of set-up for dbt, but now we will start using it to apply our data transformations to the source file and create our data warehouse model.

## Setup

### Initiallize dbt

1. Navigate to [Airflow UI](http://localhost:8080/home)

2. Execute DAG `04_dbt_init` from the Airflow homepage

This DAG can be inspected [here](../02_workflow_orchestration/dags/04_dbt_init.py). It consists of two BashOperator tasks - `dbt_debug` and `dbt_deps`:

- `dbt_debug` - this task calls [this bash script](../02_workflow_orchestration/scripts/dbt/debug.sh), which navigates to the dbt project directory on the container and performs `dbt debug`. What this command does is it tests the database connection to make sure everything is working fine.

- `dbt_deps` - this task calls [this bash script](../02_workflow_orchestration/scripts/dbt/deps.sh), which navigates to the dbt project directory on the container and performs `dbt deps`. What this command does is it installs the dependencies listed in [packages.yml](./sales_data_warehouse/packages.yml). In our case we have used the `dbt_external_tables` package, which helps us stage our source file in an external table.

### Stage source file in an external table

Execute DAG `05_dbt_stage_source_file` from the Airflow homepage.

This DAG can be inspected [here](../02_workflow_orchestration/dags/05_dbt_stage_source_file.py). It consists of a single BashOperator task that calls [this bash script](../02_workflow_orchestration/scripts/dbt/stage_external_sources.sh), which navigates to the dbt project directory on the container and perform `dbt run-operation stage_external_sources`. This is from the package we previously mentioned which stages our source file in an external table.

### Build Data Warehouse model