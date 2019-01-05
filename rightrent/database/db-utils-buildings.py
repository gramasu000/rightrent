"""
This file several utility functions to 
    handle database connections, requests and responses
        for buildings template
"""

def get_buildings(db, user_id, building_id=None):
    """
    Make a sql query to the database
        to extract building information
    return non-confidential information in dict form
    """
    if building_id is not None:
        return db.execute("SELECT * FROM buildings WHERE userid = ?, buildingid = ?", (user_id, building_id)).fetchone()
    else:
        return db.execute("SELECT * FROM buildings WHERE userid = ?", (user_id,)).fetchall()

def add_building(db, user_id, building_data):
    """
    Makes a sql query to the database
        to add a building to the user_id
    """
    db.execute(
        "INSERT INTO buildings (userid, buildingname, buildingaddress, extrainfo) VALUES (?,?,?,?)",
        (user_id, building_data["name"], building_data["address"], building_data["extrainfo"])   
    )
    db.commit()

def check_building_duplicate(db, user_id, building_data):
    """
    Checks to see if building name
        is already taken by another building in database
        associated with user_id
    """
    if db.execute(
        "SELECT buildingid FROM buildings WHERE userid = ?, buildingname = ?", 
        (user_id, buildingname)
    ).fetchone() is not None:
        return True
    else:
        return False

def edit_building(db, user_id, building_id, building_data):
    """
    Makes a sql query to edit
        the building information
        of the entry corresponding to building_id
    """
    db.execute(
        "UPDATE buildings SET buildingname = ?, buildingaddress = ?, extrainfo = ? WHERE userid = ?, buildingid = ?",
        (building_data["name"], building_data["address"], building_data["extrainfo"], user_id, building_id)
    )
    db.commit()

def check_building_renters(db, user_id, building_id):
    """
    Checks to see if any renters associated with 
        the user_id lives in building with building_id
    """
    if db.execute(
        "SELECT renterid FROM renters WHERE userid = ?, buildingid = ?",
        (user_id, building_id)
    ).fetchone() is not None:
        return True
    else:
        return False

def check_building_apartments(db, user_id, building_id):
    """
    Checks to see if any apartments associated
        with the user_id lives in building with building_id
    """
    if db.execute(
        "SELECT apartmentid FROM apartments WHERE userid = ?, buildingid = ?",
        (user_id, building_id)
    ).fetchone() is not None:
        return True
    else
        return False

def delete_building(db, user_id, building_id):
    """
    Makes sql query to delete building
    """
    db.execute("DELETE FROM buildings WHERE userid = ?, buildingid = ?", (userid, buildingid))
    db.commit()
 
