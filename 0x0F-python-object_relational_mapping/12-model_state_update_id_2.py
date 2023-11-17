#!/usr/bin/python3
"""
Script that changes the name of a State object in the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def update_state_name(username, password, database):
    """
    Update the name of a State where id = 2 to New Mexico
    """

    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a configured 'Session' class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name to 'New Mexico' if the state exists
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    """
    Run the script with provided command line arguments
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    update_state_name(sys.argv[1], sys.argv[2], sys.argv[3])

