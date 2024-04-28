#!/usr/bin/python3
"""
 takes in the name of a state as an argument and lists all cities of
 that state, using the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                   INNER JOIN states ON cities.state_id = states.id \
                   WHERE states.name = %s \
                   ORDER BY cities.id ASC",(argv[4],))
    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))
    cursor.close()
    db.close()
