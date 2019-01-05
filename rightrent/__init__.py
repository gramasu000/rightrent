# Imports
import os
import click
from flask import Flask
from flask.cli import with_appcontext
from database.db import get_db, close_db

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

def _register_db(rightrent):
    """
    Create a custom command to initialize the database,
        set close_db as a callback whenever app_context tears down 
    """
    # These decorators link this function to "flask init-db" cmd-line command.
    @click.command("init-db")
    @with_appcontext
    def init_db_command():
        """
        Make a connection and initialize the database (i.e. create tables, etc)
        """
        # Get database connection
        db = get_db()
        # Run initialization SQL script 
        with current_app.open_resource("schema.sql") as f:
            db.executescript(f.read().decode("utf-8"))
        # Print message
        click.echo("Initialized Database")
    # Attach close_db as a callback when the application context tears down
    rightrent.teardown_appcontext(close_db) 
    # we register init_db_command as a command line command
    rightrent.cli.add_command(init_db_command)
    

def _register_blueprints(rightrent):
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
