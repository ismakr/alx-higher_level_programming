#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, insert
import sys
from model_state import Base, State
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
