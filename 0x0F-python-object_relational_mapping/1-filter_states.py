#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb
    # make a connection to the database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    # execute the query: name starting with N
    cur.execute("SELECT * FROM states WHERE name REGEXP '^N[.]*'")
    # fetch and print the result
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
