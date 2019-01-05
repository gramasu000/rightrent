# Imports

# Create an expenses blueprint with url prefix exp/

"""
Endpoint for exp/<user-id>/add
Add the login required decorator
    If request method is POST
        - Get expense information from form data
        - Check that expense name is not null
        - Check that expense amount is number between 1-1000000 dollars
        - Check that expense issue date is not in the future
        - Call add_expenses(user_id, expense_data) to 
            add expense to database.
        - Flash success or error message.
    If request method is GET
        - Call getrenters to get a list of renters
        - Pass the list to render_template 
"""


"""
Endpoint for exp/<user-id>/<building-id>/<apartment-id>/<renter-id>/<expense-id>/info
Add the login required decorator
    Call getrenters(renter_id) to get renter information in dict form
    Pass the dict to render_template    
"""

"""
Endpoint for exp/<user-id>/<building-id>/<apartment-id>/<renter-id>/<expense-id>/delete
Add the login required decorator
    Only accepts POST requests
    Calls delete_expense
    Calls success or error message and redirect to expenseslist
""" 
