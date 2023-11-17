#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def list_cities_states(username, password, database):
    """
    List all City objects with their associated State from the database hbtn_0e_101_usa
    """

    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured 'Session' class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all City objects with their associated State
    cities_states = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities_states:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()

if __name__ == "__main__":
    """
    Run the script with provided command line arguments
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    list_cities_states(sys.argv[1], sys.argv[2], sys.argv[3])

