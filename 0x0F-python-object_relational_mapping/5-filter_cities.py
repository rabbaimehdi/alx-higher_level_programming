#!/usr/bin/python3
"""script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def main():
    conn = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states \
                 on cities.state_id = states.id WHERE states.name LIKE BINARY \
                 %(name)s ORDER BY cities.id ASC", {'name': sys.argv[4]})
    query_row = cur.fetchall()
    for row in query_row:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
