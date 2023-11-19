#!/usr/bin/python3
"""Write a script that prints the State object with the
name passed as argument from the database hbtn_0e_6_usa
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
    state_update = session.query(State).filter_by(
        id=2).update({"name": "New Mexico"})
    session.commit()


if __name__ == "__main__":
    main()
