{{
    config(
        materialized='table',
        partition_by={
            "field": "Sale_Date",
            "data_type": "date",
            "granularity": "day"
        },
        persist_docs={"columns": true}
    )
}}

select
    *
from {{ source('staging', 'ext_sales_data') }}