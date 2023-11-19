#!/usr/bin/python3
"""Write a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
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
    new_state = State("Louisiana")
    session.add(new_state)
    session.commit()
    new_state_id = session.query(State).filter(
        State.name == "Louisiana").first()
    print(f"{new_state_id.id}")


if __name__ == "__main__":
    main()
