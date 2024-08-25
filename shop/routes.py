from flask import Blueprint, render_template
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Welcome to the Shop!"


@main.route('/register')
def register():
    title = 'Register Designer'
    return render_template('admin/register.html', title=title)
