#!/usr/bin/python3
"lists all cities of a state"

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, select, join

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    conn = engine.connect()
    query = select(City.id, City.name, State.name).select_from(
                   join(City, State, City.state_id == State.id))

    data = conn.execute(query)

    for id, c, s in data:
        print(f'{s}: ({id}) {c}')

    engine.dispose()
