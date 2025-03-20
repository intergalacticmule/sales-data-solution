{{
    config(
        materialized = 'table',
        partition_by = {
            "field": "Sale_Date",
            "data_type": "date",
            "granularity": "day"
        },
        cluster_by =[
            "sales_rep_id",
            "region_id",
            "product_category_id",
            "customer_type_id"
        ]
    )
}}

select
    Sale_Date as sale_date,
    sales_reps.sales_rep_id,
    regions.region_id,
    Sales_Amount as sales_amount,
    Quantity_Sold as quantity_sold,
    product_categories.product_category_id,
    Unit_Cost as unit_cost,
    Unit_Price as unit_price,
    customer_types.customer_type_id,
    Discount as discount,
    payment_methods.payment_method_id,
    sales_channels.sales_channel_id
from {{ source('staging', 'st_sales_data') }} st
join {{ ref('dim_sales_reps') }} as sales_reps
    on st.Region_and_Sales_Rep = split(sales_reps.sales_rep_name, ' ')[offset(1)] || '-' || split(sales_reps.sales_rep_name, ' ')[offset(0)]
join {{ ref('dim_regions') }} as regions
    on st.Region = regions.region_name
join {{ ref('dim_product_categories') }} as product_categories
    on st.Product_Category = product_categories.product_category_name
join {{ ref('dim_customer_types') }} as customer_types
    on st.Customer_Type = customer_types.customer_type_name
join {{ ref('dim_payment_methods') }} as payment_methods
    on st.Payment_Method = payment_methods.payment_method_name
join {{ ref('dim_sales_channels') }} as sales_channels
    on st.Sales_Channel =  sales_channels.sales_channel_name
