#!/usr/bin/python3
"""
Task 9
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, database), pool_pre_ping=True)

    session = Session(engine)

    for row in session.query(State).filter(State.name.like('%a%')).\
            order_by(State.id):
        print("{}: {}".format(row.id, row.name))

    session.close()
