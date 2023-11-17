#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_states_with_a(username, password, database):
    """
    Print all State objects that contain the letter a
    from the database hbtn_0e_6_usa
    """

    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a configured 'Session' class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query State objects containing the letter a, sorted by states.id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # Print the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()

if __name__ == "__main__":
    """
    Run the script with provided command line arguments
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    print_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])

