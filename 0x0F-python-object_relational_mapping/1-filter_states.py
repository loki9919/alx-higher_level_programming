#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa 
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()