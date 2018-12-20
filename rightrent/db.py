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
            calls query_username to get user info
         
    get_user_info(db, username) - 
        returns non-confidential user information 
            (everything except passwordhash)

    get_expenses(db, user_id, renter_id=None, expense_id=None, pending=True) - 
        Make a sql query to the database
        extracting the expenses
            that are associated with userid
        returns non-confidential information in dict form
        If pending=True, then return only unpaid expenses
        If pending=False, then return all expenses 
   
    get_renters(db, user_id,building_id=None,apartment_id=None,renter_id=None) - 
        Make sql query to the database
        to extract renters that are associated with user_id
        return non-confidential information in dict form

    check_other_renters(db, user_id, building_id, apartment_id, renter_data) -
        Makes sql query to see to check if
            another renter in database is associated with
                building_id, apartment_id 
                    and has an unfinished lease term

    add_renter(db, user_id, building_id, apartment_id, renter_data) -
        Make a sql query to the database to add
            a renter associated with building_id, apartmant_id 

    edit_renter(db, user_id, building_id, apartment_id, renter_id, renter_data) - 
        Make a sql query to the database to edit 
            a renter with renter_id with renter_data

    check_renter_expenses(db, user_id, renter_id) - 
        Makes a sql query to check whether
            any expenses exist in the database
            that are associated with renter_id
    
    delete_renter(db, user_id, building_id, apartment_id, renter_id) - 
        Makes a sql query to delete the renter
            associated with renter_id from the database
    
    get_payments(db, user_id, renter_id=None, expense_id=None, payment_id=None) - 
        Make a sql query to the database
            to extract payment information
        return non-confidential information in dict form

    get_apartments(db, user_id, building_id=None, apartment_id=None,
        vacant=None) - 
        Make a sql query to the database 
            to extract apartment information
        return non-confidential information in dict form

    add_apartment(db, user_id, building_id, apartment_data) -
        Makes a sql query to the database
            to add an apartment associated
                with user_id and building_id

    check_apartment_duplicate(db, user_id, building_id, apartment_data) - 
        Make a sql query to the database
            to check that apartment number is
                taken other apartments in the database
                    with same user and building ids.

    check_apartment_renters(db, user_id, building_id, apartment_id) -
        Make a sql query to the database
            to check if renters live in 
                building id, apartment id 

    edit_apartment(db, user_id, building_id, apartment_id, apartment_data) - 
        Make a sql query to edit information
            corresponding to apartment_id with new apartment data 

    delete_apartment(db, user_id, building_id, apartment_id) - 
        Makes sql query to delete building

    get_buildings(db, user_id, building_id=None) - 
        Make a sql query to the database
            to extract building information
        return non-confidential information in dict form

    add_building(db, user_id, building_data) - 
        Makes a sql query to the database
            to add a building to the user_id

    check_building_duplicate(db, user_id, building_data) - 
        Checks to see if building name
            is already taken by another building in database
                associated with user_id

    edit_building(db, user_id, building_id, building_data) - 
        Makes a sql query to edit
            the building information
            of the entry corresponding to building_id    

    check_building_renters(db, user_id, building_id) - 
         Checks to see if any renters associated with 
            the user_id lives in building with building_id

    checks_building_apartments(db, user_id, building_id) - 
        Checks to see if any apartments associated
            with the user_id lives in building with building_id

    delete_building(db, user_id, building_id) -
        Makes sql query to delete building
""" 
