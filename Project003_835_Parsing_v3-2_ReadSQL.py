#! python3
# Project003_835_Parsing_v3-2_ReadSQL.py

"""
This script runs a SQL query.
"""

import sqlite3, pandas

conn = sqlite3.connect('Project003_DB.db')

#This commented section is why pandas is nice
"""
cur = conn.cursor()
cur.execute("select * from Adjustments")
results = cur.fetchall()
print(results)
"""

results = pandas.read_sql_query("select * from Adjustments;", conn)

print(results)
