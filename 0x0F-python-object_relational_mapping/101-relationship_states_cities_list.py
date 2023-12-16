#!/usr/bin/python3
"lists all state and thier citys using relationship"

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    with Session(engine) as session:
        data = session.query(State).outerjoin(City).all()
        if data:
            for state in data:
                print(f'{state.id}: {state.name}')
                for city in state.cities:
                    print(f'\t{city.id}: {city.name}')
