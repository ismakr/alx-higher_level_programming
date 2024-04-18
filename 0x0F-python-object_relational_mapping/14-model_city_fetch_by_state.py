#!/usr/bin/python3
"""
prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import Base, City
import sys
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    city = session.query(City, State).order_by(City.id) \
                                     .filter(State.id == City.state_id)
    for cities, states in city:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
