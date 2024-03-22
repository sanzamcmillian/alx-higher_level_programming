#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
                FROM cities INNER JOIN states ON cities.state_id
                = states.id WHERE states.name = %s""", (sys.argv[4],))
    row = cur.fetchone()
    if row:
        print(row[0])
    cur.close()
    db.close()
