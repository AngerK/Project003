#! python3
# Project003_SQL.py

"""
This script runs a SQL query.
"""

import sqlite3, pandas

conn = sqlite3.connect('Project003_DB.db')

"""
cur = conn.cursor()
cur.execute("select * from Adjustments")
results = cur.fetchall()
print(results)
"""

results = pandas.read_sql_query("select * from Adjustments;", conn)
print(results)
