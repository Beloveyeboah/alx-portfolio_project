from flask import render_template, url_for, flash, redirect, session, request
from app import db, photos
from app.products import product_bp
from app.products.forms import DesignerForm, ProductForm, CategoryForm
from app.products.models import Designer, Category
from flask_login import login_required
from app.models import User
from app.products.models  import Product
from werkzeug.utils import secure_filename



@product_bp.route('/add-category', methods=['GET', 'POST'])
@login_required
def add_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        flash('Category created successfully!', 'success')
        return redirect(url_for('product_bp.add_category'))
    return render_template('products/add_category.html', title='Add Category', form=form)

@product_bp.route('/add-designer', methods=['GET', 'POST'])
@login_required
def add_designer():
    form = DesignerForm()
    if form.validate_on_submit():
        designer = Designer(name=form.name.data, bio=form.bio.data)
        db.session.add(designer)
        db.session.commit()
        flash('Designer added successfully!', 'success')
        return redirect(url_for('product_bp.add_designer'))
    return render_template('products/add_designer.html', title='Add Designer', form=form)

@product_bp.route('/add-product', methods=['GET', 'POST'])
@login_required
def add_product():
    form = ProductForm()
    form.designer.choices = [(d.id, d.name) for d in Designer.query.all()]
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]
    if form.validate_on_submit():
        if form.image_file.data:
            filename = photos.save(form.image_file.data)
            image_file = filename
        else:
            image_file = 'default.jpg'
        product = Product(
                name=form.name.data,
                description=form.description.data,
                price=form.price.data,
                image_file=image_file,
                designer_id=form.designer.data,
                category_id=form.category.data,
                size=form.size.data,
                location=form.location.data,
                discount=form.discount.data
                )
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('product_bp.add_product'))
    return render_template('products/add_product.html', title='Add Products', form=form)

@product_bp.route('/designer/<int:designer_id>', methods=['GET', 'POST'])
def edit_designer(designer_id):
    if 'email' not in session:
        flash('Please login first')
    designers = Designer.query.get_or_404(designer_id)
    form = DesignerForm()
    if form.validate_on_submit():
        designers.name = form.name.data
        designers.bio = form.bio.data
        db.session.commit()
        flash('Designer has been updated!', 'success')
        return redirect(url_for('product_bp.add_designer'))
    elif request.method == 'GET':
        form.name.data = designers.name
        form.bio.data = designers.bio
    return render_template('product/edit_designer.html', form=form, title='Edit Designer',designers=designers)

@product_bp.route('/edit-product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm()
    form.designer.choices = [(d.id, d.name) for d in Designer.query.all()]
    form.category.choices = [(c.id, c.name) for c in Category.query.all()]
    
    if form.validate_on_submit():
        if form.image_file.data:
            filename = photos.save(form.image_file.data)
            product.image_file = filename
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        product.designer_id = form.designer.data
        product.category_id = form.category.data
        product.size = form.size.data
        product.location = form.location.data
        product.discount = form.discount.data
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('product_bp.edit_product', product_id=product.id))
    elif request.method == 'GET':
        form.name.data = product.name
        form.description.data = product.description
        form.price.data = product.price
        form.designer.data = product.designer_id
        form.category.data = product.category_id
        form.size.data = product.size
        form.location.data = product.location
        form.discount.data = product.discount
    return render_template('products/edit_product.html', title='Edit Product', form=form, product=product)
