# Imports

# Create a blueprint object with url prefix bd/

"""
Endpoint for bd/<user-id>/add -> add
Add the login required decorator
    - If request method is POST
        - Gets the building name and building address
            from the submitted form data
        - Checks if building name is not empty or null
        - Calls check_building_duplicate 
            to check for buildings in database with duplicate name
        - If no errors,  
            flash a message 
            saying that building creation successful
        - If errors, flash an error message 
    - If request method is GET
        simply serve the page
"""

"""
Endpoint for bd/<user-id>/<building-id>/info
Add the login required decorator
    - Calls get_building(building_id) to 
        get building information in dict form
    - Load dict into render_template and serve the page 
"""  

"""
Endpoint for bd/<user-id>/<building-id>/edit
Add the login required decorator
    - If request method is POST
        - Collect form data into dict
        - Check if new building name is not null
        - Check if new building name is not taken
            by calling check_building_duplicate
        - Call edit_building(user_id, building_id)
        - flash message that edit building is successful 
    - If request method is GET
        - Calls get_building(building_id)
            to get building info in dict form
        - Calls check_building_renters and
            check_building_apartments to see if
                delete button should be displayed 
        - Loads dict into render_template and serve the page 
"""

"""
Endpoint for bd/<user-id>/<building-id>/delete
    Call delete_building to delete
        building in database, and then
            redirect to buildinglist
    Creates an deletebuildingmessage as
        a property of g 
"""
