#!/usr/bin/python3
"""
cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities JOIN states ON cities.state_id = states.id;")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
