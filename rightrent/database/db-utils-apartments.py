"""
This file several utility functions to 
    handle database connections, requests and responses
    for apartments blueprint
"""
   
def get_apartments(db, user_id, building_id=None, apartment_id=None, vacant=None):
    """
    Make a sql query to the database 
        to extract apartment information
    return non-confidential information in dict form
    """
    if apartment_id is not None:
        return db.execute("SELECT * FROM apartments WHERE userid = ?, apartmentid = ?", (user_id, apartment_id)).fetchone()
    elif building_id is not None and vacant is None:
        return db.execute("SELECT * FROM apartments WHERE userid = ?, buildingid = ?", (user_id, building_id)).fetchall()
    elif building_id is not None and vacant is not None:
        return db.execute("SELECT * FROM apartments WHERE userid = ?, buildingid = ?, vacant = ?", (user_id, building_id, vacant)).fetchall()
    elif building_id is None and vacant is not None:
        return db.execute("SELECT * FROM apartments WHERE userid = ?, vacant = ?", (user_id, vacant)).fetchall()
    else:
        return db.execute("SELECT * FROM apartments WHERE userid = ?", (user_id,)).fetchall()

def add_apartment(db, user_id, building_id, apartment_data):
    """
    Makes a sql query to the database
        to add an apartment associated
        with user_id and building_id
    """
    db.execute(
        "INSERT INTO apartments (buildingid, userid, apartmentnumber, store, extrainfo) VALUES (?,?,?,?)",
        (building_id, user_id, apartment_data["number"], apartment_data["store"], apartment_data["extra_info"])   
    )
    db.commit()


def check_apartment_duplicate(db, user_id, building_id, apartment_data):
    """
    Make a sql query to the database
        to check that apartment number is
        taken other apartments in the database
        with same user and building ids.
    """ 
    if db.execute(
        "SELECT apartmentid FROM apartments WHERE userid = ?, buildingid = ?, apartmentnumber = ?",
        (user_id, building_id, apartment_data["number"])
    ).fetchone() is not None:
        return True
    else:
        return False 

def check_apartment_renters(db, user_id, building_id, apartment_id):
    """
    Make a sql query to the database
        to check if renters live in building id, apartment id 
    """
    if db.execute(
        "SELECT renterid FROM renters WHERE userid = ?, buildingid = ?, apartmentid = ?",
        (user_id, building_id, apartment_id)
    ).fetchone() is not None:
        return True
    else:
        return False

def edit_apartment(db, user_id, building_id, apartment_id, apartment_data):
    """
    Make a sql query to edit information
    corresponding to apartment_id with new apartment data 
    """
    db.execute(
        "UPDATE apartments SET apartmentnumber = ?, store = ?, extrainfo = ? WHERE userid = ?, buildingid = ?, apartmentid = ?",
        (apartment_data["number"], apartment_data["store"], apartment_data["extra_info"], user_id, building_id, apartment_id)
    )
    db.commit()

def delete_apartment(db, user_id, building_id, apartment_id):
    """
    Makes sql query to delete building
    """
    db.execute(
        "DELETE FROM apartments WHERE userid = ?, buildingid = ?, apartmentid = ?",
        (user_id, building_id, apartment_id)    
    )
    db.commit()

