#!/usr/bin/python3
"updates State with id=2 to `New Mixico`"

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, update

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    conn = engine.connect()
    trans = conn.begin()
    query = update(State).where(State.id == 2).values(name='New Mexico')
    state = conn.execute(query)
    trans.commit()

    engine.dispose()
