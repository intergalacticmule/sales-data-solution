{{
  config(
    materialized = 'table'
    )
}}

with customer_types as (
  select 
    distinct(Customer_Type) as customer_type_name
  from {{ ref('st_sales_data') }}
)

select
  row_number() over ()as customer_type_id,
  customer_type_name
from customer_types
order by 1