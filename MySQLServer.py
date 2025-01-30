import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

my_cursor = my_db.cursor()

my_cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")
# display message if database exists

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    if db[0] == "my_database":
        print(f"Database 'my_database' already exists.")
        break

print("Database 'alx_book_store' created successfully!")