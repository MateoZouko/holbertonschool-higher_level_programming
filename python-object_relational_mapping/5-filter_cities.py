#!/usr/bin/python3
"""
Task 5
"""
from shlex import join
from sys import argv
import MySQLdb


if __name__ == "__main__":

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name)

    cur = db.cursor()
    cur.execute("SELECT cities.name\
                FROM cities JOIN states ON cities.state_id = states.id\
                WHERE states.name LIKE %s\
                ORDER BY cities.id ASC", (state_name_searched,))
    print(", ".join(["{:s}".format(row[0]) for row in cur]))
    cur.close()
    db.close()
