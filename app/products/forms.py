from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired
from app.products.models import Designer, Category, Product
from flask_wtf.file import FileField, FileRequired, FileAllowed

class DesignerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    bio = TextAreaField('Bio')
    submit = SubmitField('Add Designer')

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    discount = FloatField('Discount', default=0) 
    image_file = FileField('Image File', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    designer = SelectField('Designer', coerce=int, validators=[DataRequired()])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    size = StringField('Size', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Add Product')

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired()])
    submit = SubmitField('Add Category')
