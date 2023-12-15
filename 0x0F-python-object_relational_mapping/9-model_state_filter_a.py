#!/usr/bin/python3
"lists all the States that contain `a` in there name"

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    conn = engine.connect()
    query = select(State).where(State.name.contains('a')).order_by(State.id)
    states = conn.execute(query)

    for id, name in states:
        print(f'{id}: {name}')

    engine.dispose()
