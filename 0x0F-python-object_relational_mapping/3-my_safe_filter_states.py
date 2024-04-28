#!/usr/bin/python3
"""
 takes in arguments and displays all values in the states table of
 hbtn_0e_0_usa where name matches the argument.
 But this time, write one that is safe from MySQL injections
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s", (argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
