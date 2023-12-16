#!/usr/bin/python3
"create a state and a city using relationship"

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
        california = State(name='California')
        san_fran = City(name='San Francisco', state=california)
        session.add_all([california, san_fran])
        session.commit()
