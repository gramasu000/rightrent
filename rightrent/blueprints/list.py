# Import

# Create a blueprint object for list - we will have url prefix list/

"""
Endpoint for list/pendingexpenseslist/ -> pendingexpenseslist
Add the login required decorator
    Call get_db to get a database connection,
        and call get_expenses(pending=True)
            to get pending expenses from database 
    The information will be arranged in dict form,
        and then passed to the template renderer
            which will render the listview template
""" 

"""
Endpoint for list/expenseslist -> expenseslist
Add the login required decorator
    Call get_db to get a database connection,
        and call get_expenses(pending=False)
            to get pending expenses from database 
    The information will be arranged in dict form,
        and then passed to the template renderer
        which will render the listview template
"""

"""
Endpoint for list/renterslist -> renterlist
Add the login required decorator
    Call get_db to get a database connection,
        and call get_renters to get 
        renters/lease information from the database.
    The information will be arranged in dict form,
        and then passed to the template renderer
        which will render the listview template 
"""

"""
Endpoint for list/paymentslist -> paymentslist
Add the login required decorator
    Call get_db to get a database connection,
        and call get_payments 
            to get payment information from database.
    This information will be arranged in dict form,
        and then passed to the template renderer,
        which will render the listview template
"""

"""
Endpoint for list/apartmentslist -> apartmentslist
Add the login required decorator
    Call get_db to get a database connection,
        and call get_apartments 
            to get apartment information from database.
    This information will be arranged in dict form,
        and then passed to the template renderer
        which will render the listview template
"""

"""
Endpoint for list/buildinglist -> buildinglist
Add the login required decorator
    Call get_db to get a database connection,
        and call get_buildings
            to get building information from database.
    This information will be arranged in dict form,
        and then passed to the template renderer
        which will render the listview template.
    If deletebuildingmessage is not null,
        then flash the message.
"""

