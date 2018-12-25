# Imports

# Create an apartment object with url prefix usr/

"""
Endpoint for usr/<user-id>/info
Add the login required decorator
    We call get userinfo to get user information in dict form
    Pass the dict to render_template     
"""

"""
Endpoint for usr/<user-id>/edit
Add the login required decorator
    If the request method is POST
        Check that new username is not empty
        Call check_duplicate_username to check if username is valid
        Call edit_username passing in new values to edit
            the user information in database
            and redirect to info page
        Call check_user_buildings to see if
            delete account button will be shown
    If the request method is GET
        Call get userinfo to get user information in dict form
        Render the template with filled in textboxes
"""

"""
Endpoint for usr/<user-id>/pwdedit
Add the login required decorator
    If the request method is POST
        Call check_password to check if old password
            is similar to new password
        If not, flash error
        If so, save_credentials to database table
            flash success message and redirect to user edit endpoint  
    If the request method is GET
        Render the template
"""

"""
Endpoint for usr/<user-id>/delete
Add the login required decorator
    Only accept POST requests
    Calls delete_user(user_id) to delete user id from the database
        and then redirects to logout
"""
