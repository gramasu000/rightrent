# Imports


# Create a blueprint object with url prefix auth/

"""
Endpoint for auth/register/ -> register
    - if request method is GET
        - We serve the rendered template corresponding to the register page
    - if request method is POST
        - We get name, username, password, confirm password from form
        - Error checks
            - username is not empty - separate functions
            - password is not empty - separate function
            - password == confirm password
        - Call get_db to initiate db connection 
        - Call check_duplicate_username to check non-duplicity of username
        - Call save_credentials to enter username to database
"""

"""
Endpoint for auth/login -> login
    - if request method is GET
        - We serve the rendered template corresponding to the login page
    - if request method is POST
        - We get username and password
        - Call get_db to initiate a db connection
        - Call check_username_exists to check if username is valid,
                if not, we flash error and return
        - Call check_password to see if password is correct,
                if not, we flash error and return
        - Call get_user_info to get the user_id, name
        - Save the user_id and name to session object
        - We redirect to payments.balancelistview endpoint
"""

"""
Endpoint for logout -> logout
    We clear the session variable and we show the logout page
"""

"""
before_app_request callback function -> load_logged_in_user
    We transfer
        - user id
        - user name
        from session variable
        to g.user dictionary if they exist
    If they don't exist, we create then and set them equal to None
"""

"""
Decorator function -> login_required(view)
    We check the g object for user id and user name
        before we enter an endpoint.
    If they exist, we enter the endpoint
    Otherwise,
            we redirect to login page.
"""
