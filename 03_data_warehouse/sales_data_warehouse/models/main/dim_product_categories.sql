{{
    config(
        materialized = 'table'
    )
}}

with product_categories as (
    select 
        distinct(Product_Category) as product_category_name
    from {{ ref('st_sales_data') }}
)

select
    row_number() over ()as product_category_id,
    product_category_name
from product_categories
order by 1