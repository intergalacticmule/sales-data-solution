{{
    config(
        materialized = 'table'
    )
}}

with payment_methods as (
    select 
        distinct(Payment_Method) as payment_method_name
    from {{ ref('st_sales_data') }}
)

select
    row_number() over ()as payment_method_id,
    payment_method_name
from payment_methods
order by 1