#!/usr/bin/python3
"""
displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '%{0}%'".format(argv[4]))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
    