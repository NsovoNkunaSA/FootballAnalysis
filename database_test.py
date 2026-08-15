import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="football_analysis"
)

print("Connected to MySQL successfully!")


connection.close()
