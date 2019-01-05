# Imports

# Create a renter blueprint with URL prefix rntr/

"""
Endpoint for rntr/<user-id>/add
Add the login required decorator
    If request method is POST
        - Gets building_id, apartment_id, renter name, renter phone numbers,
                renter lease information, and extra info 
            from submitted data form
        - Checks that renter name is not null
        - Checks that lease information is not null
        - Checks that leaseend is at least 1 month after leasestart
        - Calculate lease term by leasestart and leaseend
        - Calls check_other_renters to check 
            that no renter that has an unfinished lease for 
                the same apartment exists in the database
        - If no errors, call add_renter
                and flash a message saying 
                    that the renter creation was successful
        - If errors, flash an error message
    If request method is GET
        - Call get_apartments(vacant=True) to get a list
            of vacant apartments
        - Pass in the list to render_template 
"""

"""
Endpoint for rntr/<user-id>/<building-id>/<apartment-id>/<renter-id>/info
Add the login required decorator
    Calls get_renters(renter_id) to get renter information in dict form
    Pass in the dict to render_template
"""

"""
Endpoint for rntr/<user-id>/<building-id>/<apartment-id>/<renter-id>/edit
Add the login required decorator
    If request method is POST
        - Collect form data into dict
        - Checks that renter name is not null
        - Checks that lease information is not null
        - Checks that leaseend is at least 1 month after leasestart
        - Calculate lease term by leasestart and leaseend
        - Calls check_other_renters to check 
            that no renter that has an unfinished lease for 
                the same apartment exists in the database
        - Call edit_renter(renter_id)
        flash success or error message
    If the request method is GET
        Call get_renter(renter_id) to get renter information
            in dict form
        Call check_renter_expenses to see if the delete button
            should be displayed
        Loads dict into render_template
"""

"""
Endpoint for rntr/<user-id>/<building-id>/<apartment-id>/<renter-id>/delete
Add the login required decorator
    Only accepts POST requests
    Calls delete_renter to delete renter in database
    Flashes success message and redirects to renterlist
"""
