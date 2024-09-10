from app import db
from werkzeug.utils import secure_filename
from datetime import datetime

class Designer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    #products = db.relationship('Product', backref='designer', lazy=True)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, default='shoe')
    #products = db.relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_file = db.Column(db.String(100), nullable=False, default='default.jpg')
    designer_id = db.Column(db.Integer, db.ForeignKey('designer.id', name='fk_product_designer'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', name='fk_product_category'), nullable=False)
    size = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    discount = db.Column(db.Float, nullable=False, default=0.0)
    date_post = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    designer = db.relationship('Designer', backref=db.backref('designer', lazy=True))
    category = db.relationship('Category', backref=db.backref('posts', lazy=True))

"""
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    designer_id = db.Column(db.Integer, db.ForeignKey('designer.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    size = db.Column(db.String(20), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    discount = db.Column(db.Float, nullable=True)
    date_post = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    designer = db.relationship('Designer', backref=db.backref('designer', lazy=True))
    category = db.relationship('Category', backref=db.backref('posts', lazy=True))
    """
