import sqlite3
import pandas as pd

# df = pd.read_csv("class13\datasets\sample.csv")
# df = pd.read_json('class13\datasets\sample.json',encoding="UTF-8")
# df = pd.read_excel("class13\datasets\sample.xlsx")

connection = sqlite3.connect("class13\datasets\sample.db")
df = pd.read_sql_query("SELECT * FROM students",connection)

print(df)