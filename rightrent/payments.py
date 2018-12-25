# Imports

# Create a payments blueprint with url prefix pmt/

"""
Endpoint for pmt/<user_id>/add
Add the login required decorator
    If the request method is POST
        - Get payment information from form data
        - Make sure payment name is not null
        - Make sure paymentdate is not in the future
        - Make sure payment amount is number between 1-1000000 dollars
        - Call add_payment(user_id, expense_id, payment_data)
            to add payment to database
        - Flash success or error message
    If the request method is GET
        Call get_expenses(pending=True) to get a list of pending expenses
        Pass the list to render_template 
"""

"""
Endpoint for pmt/<user-id>/<expense-id>/<payment-id>/info
Add login-required decorator
    Call get_payments(payment_id=None) to get payment information in dict form
    Pass the dict to render_template 
"""


"""
Endpoint for pmt/<user-id>/<expense-id>/<payment-id>/delete
Add login-required decorator
    Only accepts POST requests
    Call delete_payments
    flash success or error message and redirect to paymentlist
"""
