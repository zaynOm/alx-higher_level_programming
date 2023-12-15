#!/usr/bin/python3
"list all state objects"

from model_state import Base, State
from sqlalchemy import create_engine, select
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    conn = engine.connect()
    query = select(State).order_by(State.id)
    states = conn.execute(query)
    for s in states:
        print(f'{s.id}: {s.name}')

    engine.dispose()
