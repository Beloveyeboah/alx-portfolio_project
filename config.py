import os
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

class Config:
    SECRET_KEY = os.environ.get('yeboah') or 'belove'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///big_stores'
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:beauty12@localhost/big_stores'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
