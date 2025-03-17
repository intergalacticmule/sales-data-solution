# <div align="center">Workflow Orchestration</div>

## Overview

In this section we will examine how we achieve automating the data pipeline - from raising the necessary cloud infrastructure, through retrieving the data from source, to landing it safely in our data storage.

We have chosen Apache Airflow for our workflow orchestration, containerized via Docker. Alongisde it we have Terraform, which is an IaC tool that will help us deploy the cloud infrastructure we need.

## Setup

1. Clone the repository:

```bash
$ git clone https://github.com/intergalacticmule/sales-data-solution.git
```

2. Navigate to folder 02_workflow_orchestration:

```bash
$ cd 02_workflow_orchestration
```

3. 