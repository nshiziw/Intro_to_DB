import mysql.connector

try:
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    my_cursor = my_db.cursor()

    my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("✅ Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"⚠️ Error: {err}")
    print("The database 'alx_book_store' may already exist.")
