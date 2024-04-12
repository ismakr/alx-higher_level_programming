#!/usr/bin/python3
"""
module that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
import sys
import MySQLdb

# should not be executed when imported
if __name__ == '__main__':

    # connect to the MySQL database located on localhost, using user,
    # connecting with password passwd, to database db
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    # Executing queries: name matches the argument.
    cur.execute("SELECT * FROM states WHERE name= %s\
            ORDER BY id ASC", (sys.argv[4],))

    # fetch and print the result
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))

    #  close all open cursors, and close all open database connections
    cur.close()
    db.close()
