from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseVSU.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Определение моделей
class Student(db.Model):
    __tablename__ = 'students'
    ID_student = db.Column(db.Integer, primary_key=True)
    ID_kur = db.Column(db.Integer, db.ForeignKey('kurators.ID_kur'))
    ID_group = db.Column(db.Integer, db.ForeignKey('groups.ID_group'))
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60))
    age = db.Column(db.Integer)
    email = db.Column(db.String, nullable=False)
    passport = db.Column(db.String(6))

class Teacher(db.Model):
    __tablename__ = 'teachers'
    ID_teacher = db.Column(db.Integer, primary_key=True)
    ID_subject = db.Column(db.Integer, db.ForeignKey('subjects.ID_subject'))
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String)

class Subject(db.Model):
    __tablename__ = 'subjects'
    ID_subject = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

class Kurator(db.Model):
    __tablename__ = 'kurators'
    ID_kur = db.Column(db.Integer, primary_key=True)
    ID_kurs = db.Column(db.Integer, db.ForeignKey('kurses.ID_kurs'))
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String)

class Kurses(db.Model):
    __tablename__ = 'kurses'
    ID_kurs = db.Column(db.Integer, primary_key=True)
    ID_subject = db.Column(db.Integer, db.ForeignKey('subjects.ID_subject'))
    ID_teacher = db.Column(db.Integer, db.ForeignKey('teachers.ID_teacher'))
    title = db.Column(db.String, nullable=False)
    time = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    dateStart = db.Column(db.String)

class Group(db.Model):
    __tablename__ = 'groups'
    ID_group = db.Column(db.Integer, primary_key=True)
    titleGroup = db.Column(db.String(100), nullable=False, unique=True)
    ID_teacher = db.Column(db.Integer, db.ForeignKey('teachers.ID_teacher'))

@app.route('/')
def index():
    tables = db.engine.table_names()
    print("Tables in the database:", tables)  # Добавлено для отладки
    return render_template('index.html', tables=tables)

@app.route('/table/<table_name>')
def view_table(table_name):
    if table_name == 'students':
        rows = Student.query.all()
    elif table_name == 'teachers':
        rows = Teacher.query.all()
    elif table_name == 'subjects':
        rows = Subject.query.all()
    elif table_name == 'kurators':
        rows = Kurator.query.all()
    elif table_name == 'kurses':
        rows = Kurses.query.all()
    elif table_name == 'groups':
        rows = Group.query.all()
    else:
        return "Таблица не найдена", 404
    
    return render_template('table.html', table_name=table_name, rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
