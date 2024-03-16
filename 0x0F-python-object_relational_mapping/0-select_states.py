#!/usr/bin/python3
""" lists all states from theh databasee hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=33066)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fecthall()
    for row in rows:
        print(row)
    cur.close()
    dn.close()
