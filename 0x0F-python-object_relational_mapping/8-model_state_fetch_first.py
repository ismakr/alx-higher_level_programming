#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    qu = session.query(State).order_by(State.id).first()
    if qu is None:
        print("Nothing")
    else:
        print("{}: {}".format(qu.id, qu.name))
