#!/usr/bin/python3
"""
lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine, select
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id)
    for states in state:
        if "a" in states.name:
            print("{}: {}".format(states.id, states.name))
