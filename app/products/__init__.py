from flask import Blueprint

product_bp = Blueprint('product_bp', __name__)

from app.products import routes
