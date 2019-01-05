"""
This file several utility functions to 
    handle database connections, requests and responses
    for expenses blueprint
"""

def get_expenses(db, user_id, renter_id=None, expense_id=None, pending=None):
    """
    Makes a sql query to the database to
        extract either pending or all expenses associated with renter_id, expense_id  
    """
    if expense_id is not None:
        return db.execute("SELECT * FROM expenses WHERE expenseid = ?", (expense_id,)).fetchone()
    elif renter_id is None and pending is None:
        return db.execute("SELECT * FROM expenses").fetchall()
    elif renter_id is None and pending is not None:
        return db.execute("SELECT * FROM expenses WHERE pending = ?", (pending, )).fetchall()
    elif renter_id is not None and pending is None:
        return db.execute("SELECT * FROM expenses WHERE renterid = ?", (renter_id, )).fetchall()
    else:
        return db.execute("SELECT * FROM expenses WHERE renterid = ?, pending = ?", (renter_id, pending)).fetchall()
    
def add_expenses(db, user_id, renter_list, expense_data):
    """
    Make a sql query to the database
        to add expense for each renter in renter list
        with expense_data
    """
    expense_list = []  
    for renter_id in renter_list:
        expense_list.append((renter_id, user_id, expense_data["name"], expense_data["amount"], expense_data["issue_date"], expense_data["extra_info"]))
    db.executemany("INSERT INTO expenses (renterid, userid, name, amount, issuedate, extrainfo) VALUES (?,?,?,?,?,?)", expense_list)
    db.commit()

def delete_expense(db, user_id, renter_id, expense_id):
    """    
    Make a sql query to the database
        to delete expense entry associated with expense_id
        from the database
    """
    db.execute("DELETE FROM expenses WHERE userid = ?, renterid = ?, expenseid = ?", (user_id, renter_id, expense_id))
    db.commit() 


