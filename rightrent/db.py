# Imports

"""
    In this file, I will define several utility functions to 
        handle database connections, requests and responses
"""

"""
    get_db() - Creates a connection to database instance in instance folder,
            sets it up so that table rows will be dictionaries,
                and attaches it to g object.
            Returns the database connection.
    close_db(e=None) - Check if g.db exists, if it does, then we pop it and close it
    
    init_db_command() - Attach this function to a click command, with_appcontext
            we call get_db, execute init.sql (which has initialization code), 
            and print out a message
     
    init_app(app) - We attach the close_db function as a callback whenever the
            application contexts tears down, and we register init_db_command 
            as a command line command.

    check_duplicate_username(db, username, error) - check if a username is
        already in the database, gives an error if user name is already there
    
    save_credentials(db, username, password) - enters username and password
        to database table

    query_username(db, username) - Queries the username 
        and returns the associated row if it exits

    check_username_exists(db, username, error) - 
        checks if username exists in database i.e.
            query_username does not output None

    check_password(db, username, password, error) -  
        checks if password matches the record in database 
         
    get_user_info(db, username) - 
        returns non-confidential user information 
            (everything except user_id and passwordhash)
"""
