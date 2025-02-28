from sqlalchemy import CheckConstraint, Column, Integer, String, ForeignKey
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Настройка базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseVSU.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Product(db.Model):
    __tablename__  = 'product'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    brand_id= db.Column(db.Integer, db.ForeignKey('brand.brand_id'),nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'),nullable=False)
    name = db.Column(db.String(255), nullable=False)
   
    
class Brand(db.Model):
    __tablename__ = 'brand'

    brand_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    group_id = db.Column(db.Integer,  db.ForeignKey('group.group_id'),nullable=False)
    manufacturer_id = db.Column(db.Integer,  db.ForeignKey('manufacturer.manufacturer_id'),nullable=False)
    brand_name = db.Column(db.String(60), nullable=False)

    product = db.relationship('Product', backref = 'brand',lazy=True)

class Manufacturer(db.Model):
    __tablename__ = 'manufacturer'
    manufacturer_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String, nullable=False)

    brand = db.relationship('Brand', backref='manufacturer', lazy = True)


class Group(db.Model):
    __tablename__ = 'group'
    group_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    group_name = db.Column(db.String, nullable=False)

    product = db.relationship('Product', backref='group',lazy = True)
