#!/usr/bin/python3
"""
Task 3
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    search = argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name = '{}' \
        ORDER BY id ASC".format(search))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
