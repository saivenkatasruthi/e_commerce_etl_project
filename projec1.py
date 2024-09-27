import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sruthi104#",  # Replace with your actual password
    database="e_commerce"
)

cursor = conn.cursor()

# ETL Process: Extract from raw_sales, Transform, and Load into fact_sales
etl_query = """
    INSERT INTO fact_sales (product_id, customer_id, quantity_sold, total_amount, sales_date)
    SELECT dp.product_id, dc.customer_id, rs.quantity_sold, rs.total_amount, rs.sales_date
    FROM raw_sales rs
    JOIN dim_product dp ON rs.product_name = dp.product_name
    JOIN dim_customer dc ON rs.customer_name = dc.customer_name;
"""
cursor.execute(etl_query)
conn.commit()

print("ETL process completed successfully.")

cursor.close()
conn.close()
