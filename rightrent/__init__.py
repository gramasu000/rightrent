# Imports


"""
In this file, the application factory function
    accomplishes the following tasks
----------------------------------------------------------
    - Make a Flask instance that is set up to search instance folder
            for database, and has a default configuration, 
            a file configuration and testing configuration
            (Copy from blog project)
    - Check to see if instance folder exists
    - Register the database
    - Register the authentication blueprint
    - Register the building blueprint
    - Register the apartments blueprint
    - Register the renter blueprint
    - Register the payments blueprint
    - Register the user blueprint
    - Set app.route / to redirect to auth.index 
"""

