#!/bin/bash

cd /home/airflow/sales_data_warehouse

dbt run-operation stage_external_sources