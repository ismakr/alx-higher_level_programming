#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb
import re
# should not be executed when imported
if __name__ == '__main__':

    # connect to the MySQL database located on localhost, using user,
    # connecting with password passwd, to database db
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    # Executing queries: name matches the argument.
    cur.execute("select cities.name from cities\
            inner join states on cities.state_id = states.id\
            WHERE states.name = '{}'".format(sys.argv[4]))

    # fetch and print the result
    rows = cur.fetchall()
    i = 0
    for row in rows:
        if i == 0:
            print("{}".format(re.sub("[()',]", "", str(row))), end="")
        else:
            print(", {}".format(re.sub("[()',]", "", str(row))), end="")
        i += 1
    print("")
    #  close all open cursors, and close all open database connections
    cur.close()
    db.close()
