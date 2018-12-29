# Imports
import os
from flask import Flask

"""
This file contains the application factory function
"""

def _create_app():
    """
    Returns a Flask instance that is set up to search instance/ folder
    """
    return Flask(__name__, instance_relative_config=True)

def _set_config(rightrent, test_config):
    """
    Sets the default config, the file config and the test config for rightrent app 
    """
    # Configure default settings
    rightrent.config.from_mapping(
        # Security key for cookie and session objects
        SECRET_KEY="dev_dummy_key",
        # Database path
        DATABASE=os.path.join(app.instance_path, "rightrent.sqlite"),
    )

    if test_config is None:
        # Loads config file if test_config is not set
        rightrent.config.from_pyfile("config.py", silent=True)
        # If config.py does not exist, rightrent will use default settings
    else:
        # Otherwise, load test_config
        rightrent.config.from_mapping(test_config)

def _register_components(rightrent):
    """
    Registers the blueprints and database for rightrent app
    """
    # Register the database
    from . import db
        db.init_app(rightrent)
    # Register the authentication blueprint
    from . import auth
        rightrent.register_blueprint(auth.blueprint)
    # Register the user blueprint  
    from . import user
        rightrent.register_blueprint(user.blueprint)
    # Register the building blueprint
    from . import building
        rightrent.register_blueprint(building.blueprint)
    # Register the apartment blueprint
    from . import apartment
        rightrent.register_blueprint(apartment.blueprint)
    # Register the renter blueprint
    from . import renter
        rightrent.register_blueprint(renter.blueprint)
    # Register the expenses blueprint
    from . import expense    
        rightrent.register_blueprint(expense.blueprint)
    # Register the payment blueprint
    from . import payment
        rightrent.payment_blueprint(payment.blueprint)
    
def _instance_folder_check():
    """
    Check to see if database instance folder exists
    """
    try:
       os.makedirs(app.instance_path)
    except OSError:
        pass

def _set_index_route():
    """
    Set route of endpoint url / - Redirect to auth.login endpoint 
    """
    @rightrent.route('/')
    def index():
        # TODO: Fill This in

def create_app(test_config=None):
    """
    The application factory function makes a flask app instance for our web application
    """
    rightrent = _create_app()
    _set_config(rightrent, test_config)
    _instance_folder_check()
    _register_components()
    _set_index_route()
    return rightrent
