import os
from flask import Flask, render_template
# from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage


from App.database import init_db
from App.config import load_config


from App.controllers import (
    add_auth_context
)

def create_app(overrides={}):
    app = Flask(__name__)
    load_config(app, overrides)
    CORS(app)
    add_auth_context(app)
    # photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    # configure_uploads(app, photos)
    init_db(app)
    # jwt = setup_jwt(app)
    # @jwt.invalid_token_loader
    # @jwt.unauthorized_loader
    # def custom_unauthorized_response(error):
    #     return render_template('401.html', error=error), 401
    app.app_context().push()
    return app