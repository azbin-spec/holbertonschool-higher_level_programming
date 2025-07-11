#!/usr/bin/python3
"""
Module containing function listing objects from a database.
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


def main():
    """
    Lists City objects from a database.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username,
            password,
            database
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(City, State).join(
        State, City.state_id == State.id
    ).order_by(City.id).all()

    for row in results:
        print("{}: ({}) {}".format(
            row.State.name,
            row.City.id,
            row.City.name
        ))

    session.close()


if __name__ == "__main__":
    main()
