#!/usr/bin/python3
import MySQLdb
import sys

conn = MySQLdb.connect(host='localhost', port=3306,
                       user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_row = cur.fetchall()
for row in query_row:
    print(row)
cur.close()
conn.close()
