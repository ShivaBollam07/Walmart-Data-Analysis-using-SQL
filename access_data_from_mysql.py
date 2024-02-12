import mysql.connector
from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM walmartTable")
rows = cursor.fetchall()

if rows == []:
    print("No data found")

for row in rows:
    print(row)

cursor.close()
conn.close()
