{{
    config(
        materialized = 'table'
    )
}}

with sales_channels as (
    select 
        distinct(Sales_Channel) as sales_channel_name
    from {{ ref('st_sales_data') }}
)

select
    row_number() over ()as sales_channel_id,
    sales_channel_name
from sales_channels
order by 1