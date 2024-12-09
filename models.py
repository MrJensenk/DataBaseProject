from sqlalchemy import CheckConstraint, Column, Integer, String, ForeignKey
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Настройка базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseVSU.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Student(db.Model):
    __tablename__  = 'student'

    ID_student = db.Column(db.Integer, primary_key=True, autoincrement = True)
    ID_kur = db.Column(db.Integer, db.ForeignKey('kurator.ID_kur'),nullable=False)
    ID_group = db.Column(db.Integer, db.ForeignKey('group.ID_group'),nullable=False)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False)
    passport = db.Column(db.String(6), nullable=False)
    __table_args__ = (CheckConstraint('age >= 18', name='check_age'),)
    
    
class Teacher(db.Model):
    __tablename__ = 'teacher'

    ID_teacher = db.Column(db.Integer, primary_key=True, autoincrement = True)
    ID_subject = db.Column(db.Integer,  db.ForeignKey('subject.ID_subject'),nullable=False)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String, nullable=False)

    group = db.relationship('Group', backref = 'teacher',lazy=True)
    kurses = db.relationship('Kurses', backref='teacher', lazy=True)

class Subject(db.Model):
    __tablename__ = 'subject'
    ID_subject = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String, nullable=False)

    teacher = db.relationship('Teacher', backref='subject', lazy = True)
    kurses = db.relationship('Kurses', backref = 'subject',lazy = True)


class Group(db.Model):
    __tablename__ = 'group'
    ID_group = db.Column(db.Integer, primary_key=True, autoincrement = True)
    titleGroup = db.Column(db.String, nullable=False)
    ID_teacher = db.Column(db.Integer, db.ForeignKey('teacher.ID_teacher'), nullable=False)

    student = db.relationship('Student', backref='group',lazy = True)

class Kurses(db.Model):
    __tablename__ = 'kurses'
    ID_kurs = db.Column(db.Integer, primary_key=True, autoincrement = True)
    ID_subject = db.Column(db.Integer,  db.ForeignKey('subject.ID_subject'), nullable = False)
    ID_teacher = db.Column(db.Integer,  db.ForeignKey('teacher.ID_teacher'),nullable=False)
    title = db.Column(db.String, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    dateStart = db.Column(db.String, nullable=False)
    __table_args__ = (CheckConstraint('time >= 1 and time <=24 ', name='check_time'),)
    __table_args__ = (CheckConstraint('cost <= 200000', name='check_cost'),)

    kurators = db.relationship('Kurator', backref = 'kurses', lazy = True)
class Kurator(db.Model):
    __tablename__ = 'kurator'
    ID_kur = db.Column(db.Integer, primary_key=True, autoincrement = True)
    ID_kurs = db.Column(db.Integer,  db.ForeignKey('kurses.ID_kurs'),nullable=False)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String, nullable=False)

    student =db.relationship('Student', backref='kurator',lazy = True)