from sqlalchemy import CheckConstraint, Column, Integer, String, ForeignKey
from sqlalchemy.sql import func
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import csv
import os
from models import *
    
# Функция для загрузки данных из CSV
def load_data_from_csv():
    csv_files = {
        'products': 'tables/products.csv',
        'brands': 'tables/brands.csv',
        'manufacturers': 'tables/manufacturer.csv',
        'groups' : 'tables/groups.csv'
    }

    for key, file_path in csv_files.items():
        if not os.path.exists(file_path):
            print(f"Файл не найден: {file_path}")
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if key == 'products':
                        existing_product = Product.query.filter_by(product_id=row['product_id']).count()
                        if existing_product == 0:
                            new_product = Product(
                                product_id = row['product_id'],
                                brand_id=row['brand_id'],
                                group_id=row['group_id'],
                                name=row['name']
                            )
                            db.session.add(new_product)

                    elif key == 'brands':
                        existing_brand = Brand.query.filter_by(brand_id=row['brand_id']).count()
                        if existing_brand == 0 :
                            new_brand = Brand(
                                brand_id = row['brand_id'],
                                group_id=row['group_id'],
                                brand_name=row['brand_name'],
                                manufacturer_id=row['manufacturer_id']
                                )
                            db.session.add(new_brand)
                    elif key == 'manufacturers':
                        existing_manufacturer = Manufacturer.query.filter_by(manufacturer_id=row['manufacturer_id']).count()   
                        if existing_manufacturer == 0:
                            new_manufacturer = Manufacturer(
                                manufacturer_id = row['manufacturer_id'],
                                name = row['name']
                                )
                            db.session.add(new_manufacturer)
                    elif key == 'groups':
                        existing_group = Group.query.filter_by(group_id=row['group_id']).count()
                        if existing_group == 0:
                            new_group = Group(
                                group_id = row['group_id'],
                                group_name = row['group_name']
                                )
                            db.session.add(new_group)
                db.session.commit()
                print(f"Данные из {key} успешно загружены.")
        except Exception as e:
            print(f"Ошибка при загрузке данных из {file_path}: {e}")

 
with app.app_context():
    db.create_all()  
    load_data_from_csv()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products', methods=['GET', 'POST'])
def view_products():
    product_id = request.args.get('product_id', '')
    brand_id = request.args.get('brand_id', '')
    name = request.args.get('name', '')
    page = request.args.get('page', 1, type=int)

    query = Product.query

    if name:
        query = query.filter(Product.name.ilike(f'%{name}%'))
    if product_id:
        query = query.filter(Product.product_id == product_id)
    if brand_id:
        query = query.filter(Product.brand_id == brand_id)

    products = query.paginate(page=page, per_page=25)
    total_products = query.count()

    return render_template('products.html', products=products, name=name, product_id=product_id, brand_id=brand_id,
                           total_products=total_products)

@app.route('/products/add', methods=['GET', 'POST'])
def add_product(): 
    if request.method == 'POST':
        name = request.form.get('name')
        brand_id = request.form.get('brand_id')
        group_id= request.form.get('group_id') 
        group = Group.query.get(group_id)
        if group is None:
            return "Группа не найдена", 404
    
        brand = Brand.query.get(brand_id)
        if brand is None: 
            return "Бренд не найден", 404
        
        new_product = Product(brand_id=int(brand_id), group_id=int(group_id), name=name)
        db.session.add(new_product)
        db.session.commit()
        
        
        return redirect(url_for('view_products'))
    
    return render_template('add_product.html')

@app.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.brand_id = request.form.get('brand_id')
        product.group_id = request.form.get('group_id')
        group = Group.query.get(product.group_id)
        if group is None:
            return "Группа не найдена", 404
    
        brand = Brand.query.get(product.brand_id)
        if brand is None: 
            return "Бренд не найден", 404
        db.session.commit()
        return redirect(url_for('view_products'))
    
    return render_template('upgrade_product.html', Product=product)

@app.route('/products/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    
    return redirect(url_for('view_products'))

@app.route('/brands',methods=['GET', 'POST'])
def view_brands():
    brand_name = request.args.get('brand_name', '')
    group_id = request.args.get('group_id', '')
    page = request.args.get('page', 1, type=int)

    query = Brand.query

    if brand_name:
        query = query.filter(Brand.brand_name.ilike(f'%{brand_name}%'))
    if group_id:
        query = query.filter(Brand.group_id == group_id)

    brands = query.paginate(page=page, per_page=10)

    return render_template('brands.html', brands=brands, brand_name=brand_name, group_id=group_id)

@app.route('/brands/add', methods=['GET', 'POST'])
def add_brand():
    if request.method == 'POST':
        brand_name = request.form.get('brand_name')
        group_id = request.form.get('group_id')
        manufacturer_id = request.form.get('manufacturer_id')
        group = Group.query.get(group_id)
        if group is None:
            return "Группа не найдена", 404
        
        manufacturer = Manufacturer.query.get(manufacturer_id)
        if manufacturer is None:
            return "Завод не найден", 404
        
        new_brand = Brand(brand_name=brand_name, group_id=int(group_id),  manufacturer_id=int(manufacturer_id))
        db.session.add(new_brand)
        db.session.commit()
        
        return redirect(url_for('view_brands'))
    
    return render_template('add_brand.html')

@app.route('/brands/edit/<int:brand_id>', methods=['GET', 'POST'])
def edit_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)
    
    if request.method == 'POST':
        brand.name = request.form.get('name')
        brand.group_id = request.form.get('group_id')
        brand.manufacturer_id = request.form.get('manufacturer_id')

        brand.group_id = request.form.get('group_id')
        group = Group.query.get(brand.group_id)
        if group is None:
            return "Группа не найдена", 404
        
        manufacturer = Manufacturer.query.get(brand.manufacturer_id)
        if manufacturer is None:
            return "Завод не найден", 404
        
        db.session.commit()
        return redirect(url_for('view_brands'))
    
    return render_template('upgrade_brand.html', Brand=brand)

@app.route('/brands/delete/<int:brand_id>', methods=['POST'])
def delete_brand(brand_id):
    brand = Brand.query.get_or_404(brand_id)
    db.session.delete(brand)
    db.session.commit()
    
    return redirect(url_for('view_brands'))

@app.route('/manufacturers', methods=['GET', 'POST'])
def view_manufacturers():
    manufacturer_id = request.args.get('manufacturer_id', '')
    name = request.args.get('name', '')
    page = request.args.get('page', 1, type=int)

    query = Manufacturer.query

    if manufacturer_id:
        query = query.filter(Manufacturer.manufacturer_id == manufacturer_id)
    if name:
        query = query.filter(Manufacturer.name.ilike(f'%{name}%'))

    manufacturers = query.paginate(page=page, per_page=10)

    return render_template('manufacturers.html', manufacturers=manufacturers, manufacturer_id=manufacturer_id, name=name)

@app.route('/manufacturers/add', methods=['GET', 'POST'])
def add_manufacturer():
    if request.method == 'POST':
        name = request.form.get('name')
        
        new_manufacturer = Manufacturer(name=name)
        db.session.add(new_manufacturer)
        db.session.commit()
        
        return redirect(url_for('view_manufacturers'))
    
    return render_template('add_manufacturer.html')

@app.route('/manufacturers/edit/<int:manufacturer_id>', methods=['GET', 'POST'])
def edit_manufacturer(manufacturer_id):
    manufacturer = Manufacturer.query.get_or_404(manufacturer_id)
    
    if request.method == 'POST':
        manufacturer.name = request.form.get('name')

        db.session.commit()
        return redirect(url_for('view_manufacturers'))
    
    return render_template('upgrade_manufacturer.html', Manufacturer=manufacturer)

@app.route('/manufacturers/delete/<int:manufacturer_id>', methods=['POST'])
def delete_manufacturer(manufacturer_id):
    manufacturer = Manufacturer.query.get_or_404(manufacturer_id)
    db.session.delete(manufacturer)
    db.session.commit()
    
    return redirect(url_for('view_manufacturers'))

@app.route('/groups',methods=['GET', 'POST'])
def view_groups():
    group_name = request.args.get('group_name', '')
    page = request.args.get('page', 1, type=int)

    query = Group.query

    if group_name:
        query = query.filter(Group.group_name.ilike(f'%{group_name}%'))


    groups = query.paginate(page=page, per_page=25)

    return render_template('groups.html', groups=groups, group_name=group_name)

@app.route('/groups/add', methods=['GET', 'POST'])
def add_group():
    if request.method == 'POST':
        group_name = request.form.get('group_name')
        
        new_group = Group(group_name=group_name)
        db.session.add(new_group)
        db.session.commit()
        
        return redirect(url_for('view_groups'))
    
    return render_template('add_group.html')

@app.route('/groups/edit/<int:group_id>', methods=['GET', 'POST'])
def edit_group(group_id):
    group = Group.query.get_or_404(group_id)
    
    if request.method == 'POST':
        group.group_name = request.form.get('group_name')
        db.session.commit()
        return redirect(url_for('view_groups'))
    
    return render_template('upgrade_group.html', Group=group)

@app.route('/groups/delete/<int:group_id>', methods=['POST'])
def delete_group(group_id):
    group = Group.query.get_or_404(group_id)
    db.session.delete(group)
    db.session.commit()
    
    return redirect(url_for('view_groups'))


if __name__ == '__main__':
    app.run(debug=True)
