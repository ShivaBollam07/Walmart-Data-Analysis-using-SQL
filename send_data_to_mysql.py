import csv
from datetime import datetime
from db_connection import get_connection

csv_file = './Dataset/WalmartSalesData.csv'
table_name = 'walmartTable'

conn = get_connection()
cursor = conn.cursor()

cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
table_exists = cursor.fetchone()

if not table_exists:
    create_table_query = """
    CREATE TABLE walmartTable (
        Invoice_ID VARCHAR(15),
        Branch CHAR(1),
        City VARCHAR(50),
        Customer_type VARCHAR(10),
        Gender VARCHAR(10),
        Product_line VARCHAR(50),
        Unit_price DECIMAL(10, 2),
        Quantity INT,
        Tax_5 DECIMAL(10, 4),
        Total DECIMAL(10, 4),
        Date DATE,
        Time TIME,
        Payment VARCHAR(20),
        cogs DECIMAL(10, 2),
        gross_margin_percentage DECIMAL(10, 4),
        gross_income DECIMAL(10, 4),
        Rating DECIMAL(3, 1)
    )
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("Table created successfully!")

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        row[10] = datetime.strptime(row[10], '%d-%m-%Y').strftime('%Y-%m-%d')
        cursor.execute(f"INSERT INTO {table_name} (Invoice_ID, Branch, City, Customer_type, Gender, Product_line, Unit_price, Quantity, Tax_5, Total, Date, Time, Payment, cogs, gross_margin_percentage, gross_income, Rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)

conn.commit()

cursor.close()
conn.close()

print("Data inserted successfully!")
