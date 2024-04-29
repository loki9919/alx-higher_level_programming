#!/usr/bin/python3
"""
 prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from sqlalchemy import create_engine, asc
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).filter(State.id == City.state_id).order_by(asc(City.id)).all()

    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()