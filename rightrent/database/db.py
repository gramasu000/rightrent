# Imports
import sqlite3
from flask import current_app, g
"""
This file provides functions to start and stop a database connection 
"""

def get_db():
    """
    Creates a connection to database instance in instance folder
        and attaches it to g object
    """
    # Create a new db connection if one does not already exist
    if "db" not in g:
        g.db = sqlite3.connect(
            # The database path
            current_app.config['DATABASE'],
            # Data type in SQL table will match data type in python
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        # Rows in SQL table will be dicts in python
        g.db.row_factory = sqlite3.Row
    # Do nothing but return if g.db already exists
    return g.db
        
def close_db(e=None):
    """
    close_db(e=None) - Check if g.db exists, 
        if it does, then we pop it and close it
    """
    # If g.db exists, it will pop from g.db to db
    db = g.pop("db", None)
    # If it does not, db = None
    if db is not None:
        # Close the connection
        db.close()
