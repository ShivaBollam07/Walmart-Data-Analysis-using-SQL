# Walmart Data Analysis


This project involves analyzing sales data from Walmart in order to gain insights into various aspects of their business operations, including product performance, customer trends, and market demand.

## Dataset Details

The dataset used for this analysis can be found at [Walmart Recruiting - Store Sales Forecasting](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting).

## Steps to Set Up and Run the Project

0. **Clone Repository:**
   -   `git clone https://github.com/ShivaBollam07/Walmart-Data-Analysis-using-SQL.git`

1. **Create a MySQL Database:**

   - Open MySQL Workbench or any preferred MySQL client.
   - Execute the SQL command: `CREATE DATABASE IF NOT EXISTS walmart;`.
2. **Update Connection Details:**

   - Open `db_connection.py`.
   - Modify connection parameters with your MySQL server details.
3. **Create Database Structure:**

   - Run `send_data_to_mysql.py` to create the necessary table structure.
4. **Verify Database Connection:**

   - Run `access_data_from_mysql.py` to ensure the connection and data access are successful.
5. **Ensure CSV File:**

   - Make sure `WalmartSalesData.csv` is present in the specified location or update the file path accordingly.

## Running the Project

To run the project, follow these steps:

```bash
cd Walmart-Data-Analysis-using-SQL
Run all DataAnalysis.ipynb
```

## Dependencies

1. Pandas
2. Matplotlib
3. Numpy
4. mysql-connector

