import pandas as pd
import sqlite3

df = pd.read_csv("../database/merged.csv")

connection = sqlite3.connect("../database/merged.db")

df.to_sql(
    "people",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("SQLite database created successfully.")