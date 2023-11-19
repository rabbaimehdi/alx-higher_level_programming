#!/usr/bin/python3
"""Write a script that deletes all State objects with
a name containing the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def main():
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:\
                           {argv[2]}@localhost/{argv[3]}')
    # Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).filter(State.name.contains("a"))
    if states is not None:
        for state in states:
            session.delete(state)
    session.commit()


if __name__ == "__main__":
    main()
