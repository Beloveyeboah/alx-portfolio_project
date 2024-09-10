""" this create the roustes for
Big store
"""

from flask import Blueprint, render_template, url_for, flash, redirect, request
from app import db
from app.forms import RegistrationForm, LoginForm
from app.models import User
from app.products.models import Product, Designer, Category
from flask_login import login_user, current_user, logout_user


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
def index():
    products = Product.query.all()
    designers = Designer.query.all()
    return render_template('index.html', products=products, designers=designers)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@main.route('/designer/<int:designer_id>')
def get_designer(id):
    designers = Designer.query.filter_by(designer_id=id)
    return render_template('index.html', designers=designers)

@main.route('/category/<int:category_id>')
def get_category(id):
    categories = Category.query.filter_by(category_id=id)
    return render_template('index.html', categories=categories)


@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

 