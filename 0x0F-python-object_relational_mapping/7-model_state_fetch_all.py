#!/usr/bin/python3
"""script that lists all State objects from
the database hbtn_0e_6_usa
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
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
