import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Create an engine to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects and order by id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()