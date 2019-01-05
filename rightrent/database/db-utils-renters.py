"""
This file several utility functions to 
    handle database connections, requests and responses
    for the renters blueprint
"""

def get_renters(db, user_id, building_id=None, apartment_id=None, renter_id=None):
    """
    Make sql query to the database
    to extract renters that are associated with user_id
    return non-confidential information in dict form
    """ 
    if renter_id is not None:
        return db.execute("SELECT * FROM renters WHERE userid = ?, renterid = ?", (user_id, renter_id)).fetchone()    
    elif building_id is None and apartment_id is None:
        return db.execute("SELECT * FROM renters WHERE userid = ?", (user_id,)).fetchall()
    elif building_id is not None and apartment_id is None:
        return db.execute("SELECT * FROM renters WHERE userid = ?, buildingid = ?", (user_id, building_id)).fetchall()
    elif building_id is None and apartment_id is not None:
        return db.execute("SELECT * FROM renters WHERE userid = ?, apartmentid = ?", (user_id, apartment_id)).fetchall()
    else:
        return db.execute("SELECT * FROM renters WHERE userid = ?, buildingid = ?, apartmentid = ?", (user_id, building_id, apartment_id)).fetchall()
        
def check_other_renters(db, user_id, building_id, apartment_id):
    """
    Makes sql query to see to check if
        another renter in database is associated with
        building_id, apartment_id 
        and has an unfinished lease term
    """
    if db.execute(
        "SELECT renterid FROM renters WHERE user_id = ?, building_id = ?, apartment_id = ?, leaseended = TRUE",
        (user_id, building_id, apartment_id)
    ).fetchone() is not None:
        return True
    else:
        return False

def add_renter(db, user_id, building_id, apartment_id, renter_data):
    """
    Make a sql query to the database to add
        a renter associated with building_id, apartmant_id
    """
    db.execute(
        "INSERT INTO renters (apartmentid, buildingid, userid, name, phonenumber, phonenumber2, leasestart, leaseend, leaseterm, extrainfo)",
        (apartment_id, building_id, user_id, renter_data["name"], renter_data["phone1"], renter_data["phone2"], renter_data["lease_start"], 
            renter_data["lease_end"], renter_data["lease_term"], renter_data["extra_info"]) 
    )
    db.commit()
    db.execute("UPDATE apartments SET rented = TRUE WHERE building_id = ?, apartment_id = ?", (building_id, apartment_id))
    db.commit()

def edit_renter(db, user_id, building_id, apartment_id, renter_id, renter_data):
    """
    Make a sql query to the database to edit 
        a renter with renter_id with renter_data
    """
    db.execute(
        "UPDATE renters SET name = ?, phonenumber = ?, phonenumber2 = ?, leasestart = ?, leaseend = ?, leaseterm = ?, extrainfo = ? 
            WHERE userid = ?, building_id = ?, apartment_id = ?, renter_id = ?",
        (renter_data["name"], renter_data["phone1"], renter_data["phone2"], renter_data["lease_start"], renter_data["lease_end"],
            renter_data["lease_term"], renter_data["extra_info"], user_id, building_id, apartment_id, renter_id)
    )
    db.commit()

def check_renter_expenses(db, user_id, renter_id):
    """
    Makes a sql query to check whether
        any expenses exist in the database
        that are associated with renter_id
    """
    if db.execute("SELECT expenseid FROM expenses WHERE userid = ?, renterid = ?", (user_id, renter_id)).fetchone() is not None:
        return True
    else:
        return False
     
def delete_renter(db, user_id, building_id, apartment_id, renter_id):
    """
    Makes a sql query to delete the renter
        associated with renter_id from the database
    """
    db.execute("DELETE FROM renters WHERE userid = ?, buildingid = ?, apartmentid = ?, renterid = ?", (user_id, building_id, apartment_id, renter_id))
    db.commit()
    db.execute("UPDATE apartments SET rented = FALSE WHERE building_id = ?, apartment_id = ?", (building_id, apartment_id))
    db.commit()

