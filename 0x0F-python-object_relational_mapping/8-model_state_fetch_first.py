#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_first_state(username, password, database):
    """
    Print the first State object from the database hbtn_0e_6_usa
    """

    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a configured 'Session' class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the first State object ordered by states.id
    first_state = session.query(State).order_by(State.id).first()

    # Print the result or "Nothing" if the table is empty
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()

if __name__ == "__main__":
    """
    Run the script with provided command line arguments
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    print_first_state(sys.argv[1], sys.argv[2], sys.argv[3])

