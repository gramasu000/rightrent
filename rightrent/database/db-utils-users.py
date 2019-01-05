# Imports
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file several utility functions to 
    handle database connections, requests and responses
    for user blueprint
"""

def get_users_unconfidential(db, user_id = None, username = None):
    """
    Queries the database for unconfidential information about
        the user corresponding either to username or user_id
    """
    if username is not None:
        return db.execute("SELECT (userid,username,name,joindate) FROM users WHERE username = ?", (username,)).fetchone()
    elif user_id is not None:
        return db.execute("SELECT (userid,username,name,joindate) FROM users WHERE userid = ?", (user_id,)).fetchone()
    else
        return db.execute("SELECT (userid,username,name,joindate) FROM users").fetchall() 

def check_username(db, username):
    """
    Check if username is already in the database.
    """
    if db.execute("SELECT userid FROM users WHERE username = ?", (username,)).fetchone() is not None:
        return True
    else:
        return False

def add_user(db, user_data):
    """
    Enters username and password to database table
    """
    db.execute(
        "INSERT INTO users (username, passwordhash, name) VALUES (?,?,?)",
        (user_data["username"], user_data["passwordhash"], user_data["name"])    
    )
    db.commit()

def edit_user_unconfidential(db, user_id, user_data):
    """
    Replaces user information associated with user_id
        with user_data
    """
    db.execute(
        "UPDATE users SET username = ?, name = ? WHERE id = ?",
        (user_data["username"], user_data["name"], user_id)
    )
    db.commit()

def check_password(db, username, user_id, password):
    """
    Check if password matches passwordhash 
        implemented by username/userid
    """
    password_hash = db.execute("SELECT passwordhash FROM users WHERE username = ?, userid = ?",
                (username, user_id)).fetchone() 
    
    return check_password_hash(password_hash, password)

def check_user_buildings(db, user_id):
    """
    Checks if any buildings are there in database
        that are associated to user_id
    
    """
    if db.execute("SELECT buildingid FROM buildings WHERE userid = ?", (user_id, )).fetchone() is not None:
        return True
    else
        return False

def delete_user(db, user_id):
    """
    Removes user associated with user_id from the database
    """
    db.execute("DELETE FROM users WHERE userid = ?", (user_id,))
    db.commit() 
