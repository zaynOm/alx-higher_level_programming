#!/usr/bin/python3
"print the first State object from db"

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    conn = engine.connect()
    query = select(State).order_by(State.id)
    state = conn.execute(query).first()
    if state:
        print(f'{state.id}: {state.name}')
    else:
        print('Nothing')

    engine.dispose()
