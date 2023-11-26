#!/usr/bin/python3
"""
Task 4
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute(
        f"""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON states.id = cities.state_id
            ORDER BY cities.id ASC;
        """
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
