#!/usr/bin/python3
"Delete all States with a name containing `a`"

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, delete

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    conn = engine.connect()
    trans = conn.begin()
    query = delete(State).where(State.name.contains('a'))
    state = conn.execute(query)
    trans.commit()

    engine.dispose()
