{{
  config(
    materialized = 'table'
    )
}}

with sales_channels as (
  select 
    distinct(split(Region_and_Sales_Rep, '-')[offset(1)] || ' ' || split(Region_and_Sales_Rep, '-')[offset(0)]) as sales_rep_name
  from {{ ref('st_sales_data') }}
)

select
  row_number() over ()as sales_rep_id,
  sales_rep_name
from sales_channels
order by 1