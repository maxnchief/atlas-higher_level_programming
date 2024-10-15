#!/usr/bin/python3

"""the previous task had an empty thing"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query in a safe way to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows in a list of lists
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()