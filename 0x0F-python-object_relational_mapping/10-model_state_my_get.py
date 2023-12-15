#!/usr/bin/python3
"prints the State with the given name"

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    conn = engine.connect()
    query = select(State).where(State.name == argv[4])
    state = conn.execute(query).fetchone()

    print(state.id if state else 'Not found')

    engine.dispose()
