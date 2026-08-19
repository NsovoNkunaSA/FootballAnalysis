import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PASSWORD_HERE",
    database="football_analysis"
)

print("Connected to MySQL successfully!")


connection.close()
