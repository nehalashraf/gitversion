print("Hello")
import pandas as pd 
import sqlite3
conn = sqlite3.connect("level3_activity1_foodtrucks.db")
x=pd.read_sql_query('select * from trucks', conn)
print(x)