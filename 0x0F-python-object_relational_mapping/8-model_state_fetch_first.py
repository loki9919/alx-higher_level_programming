#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id).first()

    print("Nothing" if not query else "{}: {}".format(query.id, query.name))
    session.close()
