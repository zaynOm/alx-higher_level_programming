#!/usr/bin/python3
"add new State to the database"

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, insert

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    conn = engine.connect()
    trans = conn.begin()
    query = insert(State).values(name='Louisiana')
    state = conn.execute(query)
    trans.commit()

    print(state.inserted_primary_key[0])

    engine.dispose()
