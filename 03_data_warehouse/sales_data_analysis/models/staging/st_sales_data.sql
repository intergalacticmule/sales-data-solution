{{
    config(
        materialized = 'table',
        partition_by = {
            "field": "Sale_Date",
            "data_type": "date",
            "granularity": "day"
        }
    )
}}

select
    *
from {{ source('staging', 'ext_sales_data') }}