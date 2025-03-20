{{
  config(
    materialized = 'table'
    )
}}

with regions as (
  select 
    distinct(Region) as region_name
  from {{ ref('st_sales_data') }}
)

select
  row_number() over ()as region_id,
  region_name
from regions
order by 1