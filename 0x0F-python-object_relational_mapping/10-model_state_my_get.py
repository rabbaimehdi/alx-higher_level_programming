#!/usr/bin/python3
"""Write a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
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
    state = session.query(State).order_by(
        State.id).filter(
        State.name == f"{argv[4]}").first()
    value_printed = state.id if state is not None else "Not found"
    print(value_printed)


if __name__ == "__main__":
    main()
