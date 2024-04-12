#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("select cities.id, cities.name, states.name from cities\
            inner join states on cities.state_id = states.id\
            order by cities.id ASC")

    # fetch and print the result
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))

    #  close all open cursors, and close all open database connections
    cur.close()
    db.close()
