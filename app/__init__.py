import os
from flask import Flask, url_for, redirect, render_template, request, send_from_directory

import flask_admin as admin
import flask_login as login

from app import views
from app import user

# Create Flask application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return user.User.get(user_id)

# Initialize flask-login
init_login()

from app import routes