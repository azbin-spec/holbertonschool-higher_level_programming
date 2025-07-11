#!/usr/bin/python3
"""
Module containing function updating specific object from a database.
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


def main():
    """
    Updates a State object from a database.
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
    try:
        state = session.query(State).where(State.id == 2).limit(1).one()
    except NoResultFound:
        print("Not found")
    else:
        state.name = 'New Mexico'
        session.commit()
    session.close()


if __name__ == "__main__":
    main()
