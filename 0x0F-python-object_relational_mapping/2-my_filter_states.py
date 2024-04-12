#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa
where name matches the argument."""
import sys
import MySQLdb


if __name__ == '__main__':
    # make a connection to the database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    # Executing queries: name matches the argument.
    cur.execute(f"SELECT * FROM states WHERE name = '{sys.argv[4]}'")
    # fetch and print the result
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
    #  close all open cursors, and close all open database connections
    cur.close()
    db.close()
