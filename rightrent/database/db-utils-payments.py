"""
This file several utility functions to 
    handle database connections, requests and responses
    for payments blueprint
"""

def get_payments(db, user_id, renter_id=None, expense_id=None, payment_id=None):
    """
    Make a sql query to the database
        to extract payment information
    return non-confidential information in dict form
    """
    if payment_id is not None:
        db.execute("SELECT * FROM payments where userid = ?, paymentid = ?", (user_id, payment_id)).fetchone()
    elif expense_id is not None:
        db.execute("SELECT * FROM payments where userid = ?, expenseid = ?", (user_id, expense_id)).fetchall()
    elif renter_id is not None:
        db.execute("SELECT * FROM payments where userid = ?, renterid = ?", (user_id, renter_id)).fetchall()
    else:
        db.execute("SELECT * FROM payments where userid = ?", (user_id,)).fetchall()

def add_payment(db, user_id, renter_id, expense_id, payment_data):
    """
    Make a sql query to the database
        to add payment associated with renter_id, expense_id
        with payment_data
    """
    db.execute(
        "INSERT INTO payments (expenseid, renterid, userid, name, amount, paymentmethod, paymentdate, extrainfo) VALUES (?,?,?,?,?,?,?,?)",
        (expense_id, renter_id, user_id, payment_data["name"], payment_data["amount"], payment_data["method"], payment_data["date"], payment_data["extrainfo"])
    )
    db.commit()
    # TODO: change expenses somehow

def delete_payment(db, user_id, renter_id, expense_id, payment_id):
    """
    Make a sql query to the database
        to delete payment entry associated with payment_id 
    """ 
    db.execute(
        "DELETE FROM payments WHERE userid = ?, renterid = ?, expenseid = ?, paymentid = ?", 
        (user_id, renter_id, expense_id, payment_id)
    )
    db.commit()
    # TODO: change expenses somehow
 
