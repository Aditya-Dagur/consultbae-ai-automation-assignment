import sqlite3

connection = sqlite3.connect("../database/merged.db")

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM people")

print(cursor.fetchone())

connection.close()