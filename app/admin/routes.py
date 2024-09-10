from flask import render_template, url_for, flash, redirect, request, session
from app import db
from app.admin import admin
from app.products.models import Product, Designer, Category
from app.products.forms import DesignerForm, ProductForm, CategoryForm

@admin.route('/')
@admin.route('/dashboard')
def dashboard():
    products = Product.query.all()
    return render_template('admin/dashboard.html', products=products, title='Admin Panel')

@admin.route('/designers')
def designers():
    designers = Designer.query.all()
    return render_template('admin/designers.html', designers=designers)

@admin.route('/category')
def category():
    categories = Category.query.all()
    return render_template('admin/category.html', categories=categories)

@admin.route('/designer/new', methods=['GET', 'POST'])
def new_designer():
    form = DesignerForm()
    if form.validate_on_submit():
        designer = Designer(name=form.name.data, bio=form.bio.data)
        db.session.add(designer)
        db.session.commit()
        flash('Designer has been created!', 'success')
        return redirect(url_for('admin.designers'))
    return render_template('admin/create_designer.html', form=form)

@admin.route('/category/new', methods=['GET', 'POST'])
def new_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        flash('Category has been created!', 'success')
        return redirect(url_for('admin.category'))
    return render_template('admin/create_category.html', form=form)

@admin.route('/designer/<int:designer_id>/edit', methods=['GET', 'POST'])
def edit_designer(designer_id):
    designer = Designer.query.get_or_404(designer_id)
    form = DesignerForm()
    if form.validate_on_submit():
        designer.name = form.name.data
        designer.bio = form.bio.data
        db.session.commit()
        flash('Designer has been updated!', 'success')
        return redirect(url_for('admin.designers'))
    elif request.method == 'GET':
        form.name.data = designer.name
        form.bio.data = designer.bio
    return render_template('admin/edit_designer.html', form=form, designer=designer)

@admin.route('/designer/<int:designer_id>/delete', methods=['POST'])
def delete_designer(designer_id):
    designer = Designer.query.get_or_404(designer_id)
    db.session.delete(designer)
    db.session.commit()
    flash('Designer has been deleted!', 'success')
    return redirect(url_for('admin.designers'))

@admin.route('/category/<int:category_id>/delete', methods=['POST'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    flash('Category has been deleted!', 'success')
    return redirect(url_for('admin.category'))

@admin.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    form = CategoryForm()
    if form.validate_on_submit():
        category.name = form.name.data
        db.session.commit()
        flash('Category has been updated!', 'success')
        return redirect(url_for('admin.category'))
    elif request.method == 'GET':
        form.name.data = category.name
    return render_template('admin/edit_category.html', form=form)

@admin.route('/edit-product/<int:product_id>', methods=['GET', 'POST'])
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
        return redirect(url_for('admin.dashboard', product_id=product.id))
    elif request.method == 'GET':
        form.name.data = product.name
        form.description.data = product.description
        form.price.data = product.price
        form.designer.data = product.designer_id
        form.category.data = product.category_id
        form.size.data = product.size
        form.location.data = product.location
        form.discount.data = product.discount
    return render_template('admin/edit_product.html', title='Edit Product', form=form, product=product)

@admin.route('/delete-product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('admin.dashboard'))



@admin.route('/settings')
def settings():
    return render_template('admin/settings.html')
