# Imports

# Create an apartment object with url prefix apt/

"""
Endpoint for apt/<user-id>/add
Add the login required decorator
    If request method is POST
        - Gets building_id, apartment number, store information and extra information
            from the submitted form data
        - Checks that apartment number is not null
        - Calls check_apartment_duplicate 
            to check that apartments in database do not have duplicate number
        - If no errors, call add_apartment 
                and flash a message saying 
                    that apartment creation is successful. 
        - If errors, flash an error message
    If request method is GET
        - Call get_buildings to get list of buildings
        - render the template passing in the list of buildings
"""

"""
Endpoint for apt/<user-id>/<building-id>/<apartment-id>/info
Add the login required decorator
    Calls get_apartments(apartment_id) to get 
        apartment information in dict form
    Loads dict into render template and serves the page 
"""

"""
Endpoint for apt/<user-id>/<building-id>/<apartment-id>/edit
Add the login required decorator
    If request method is POST
        Collect form data into dict
        Check if new apartment name is not null
        Check if new apartment name is not taken
            by calling check_apartment_duplicate
        Call edit_apartment(user_id, building_id, apartment_id)
        flash success or error message
    If request method is GET
        Calls get_apartments(apartment_id)
            to get apartment information in dict form
        Calls check_apartment_renters to 
            see if delete button should be displayed
        Loads dict into render_template and serve this page 
"""

"""
Endpoint for apt/<user-id>/<building-id>/<apartment-id>/delete
Add the login required decorator
    Only accepts POST requests
    Calls delete_apartment to delete
        apartment in database. 
    Flashes success message and redirects to apartmentlist
"""
