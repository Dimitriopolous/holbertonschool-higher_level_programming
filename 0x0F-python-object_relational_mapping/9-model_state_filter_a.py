#!/usr/bin/python3
"""
A script that lists all states containing the
letter 'a' in the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).\
            filter(State.name.contains('%a%')).\
            order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
