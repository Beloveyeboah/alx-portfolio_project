from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config
from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
from flask_migrate import Migrate


photos = UploadSet('photos', IMAGES)

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/products/uploads')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    # handles images upload
    configure_uploads(app, photos)

    from app.routes import main
    from app.products import product_bp
    from app.admin import admin

    app.register_blueprint(main)
    app.register_blueprint(product_bp, url_prefix='/product')
    app.register_blueprint(admin, url_prefix='/admin')
    #from .admin.routes import admin as admin_blueprint
    #app.register_blueprint(admin_blueprint)

    return app

