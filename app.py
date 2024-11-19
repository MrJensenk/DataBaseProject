# from filecmp import cmpfiles
# from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# from Database import create_database

# app = Flask(__name__)

# # Настройка базы данных
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseVSU.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# # Определение моделей
# class students(db.Model):
#     ID_student = db.Column(db.Integer, primary_key=True)
#     ID_kur = db.Column(db.Integer, nullable=False)
#     ID_group = db.Column(db.Integer, nullable=False)
#     name = db.Column(db.String, nullable=False)
#     surname = db.Column(db.String, nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     email = db.Column(db.String, nullable=False)
#     passport = db.Column(db.String, nullable=False)

# class teachers(db.Model):
#     ID_teacher = db.Column(db.Integer, primary_key=True)
#     ID_subject = db.Column(db.String, nullable=False)
#     name = db.Column(db.String, nullable=False)
#     surname = db.Column(db.String, nullable=False)
#     email = db.Column(db.String, nullable=False)

# class subjects(db.Model):
#     ID_subject = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, nullable=False)

# class groups(db.Model):
#     ID_group = db.Column(db.Integer, primary_key=True)
#     titleGroup = db.Column(db.String, nullable=False)
#     ID_teacher = db.Column(db.Integer, nullable=False)

# class kurses(db.Model):
#     ID_kurs = db.Column(db.Integer, primary_key=True)
#     ID_subject = db.Column(db.Integer, primary_key=True)
#     ID_teacher = db.Column(db.Integer, nullable=False)
#     title = db.Column(db.String, nullable=False)
#     time = db.Column(db.Integer, nullable=False)
#     cost = db.Column(db.Integer, nullable=False)
#     dateStart = db.Column(db.String, nullable=False) 

# class kurators(db.Model):
#     ID_kur = db.Column(db.Integer, primary_key=True)
#     ID_kurs = db.Column(db.Integer, nullable=False)
#     name = db.Column(db.String, nullable=False)
#     surname = db.Column(db.String, nullable=False)
#     email = db.Column(db.String, nullable=False)

# # Создаем базу данных и загружаем данные из CSV
# with app.app_context():
#     db.create_all()


# @app.route('/')
# def index():
#     return render_template('index.html')

# # Студенты
# @app.route('/students')
# def view_students():
#     Students = students.query.all()
#     return render_template('students.html', Students=Students)

# @app.route('/students/add', methods=['GET', 'POST'])
# def add_student():
#     if request.method == 'POST':

#         name = request.form['name']
#         surname = request.form['surname']
#         age = request.form['age']
#         email = request.form['email']
#         passport = request.form['passport']
#         ID_kur = request.form['ID_kur']
#         ID_group = request.form['ID_group']
        
#         new_student = students(ID_kur=ID_kur, ID_group=ID_group, name=name, surname=surname, age=age, email=email, passport=passport)
#         db.session.add(new_student)
#         db.session.commit()
        
#         return redirect(url_for('view_students'))
    
#     return render_template('add_student.html')

# @app.route('/students/edit/<int:ID_student>', methods=['GET', 'POST'])
# def edit_student(ID_student):
#     student = students.query.get_or_404(ID_student)
    
#     if request.method == 'POST':
#         student.name = request.form['name']
#         student.surname = request.form['surname']
#         student.age = request.form['age']
#         student.email = request.form['email']
#         student.passport = request.form['passport']
#         student.ID_kur = request.form['ID_kur']
#         student.ID_group = request.form['ID_group']

#         db.session.commit()
#         return redirect(url_for('view_students'))
    
#     return render_template('upgrade_student.html', student=student)

# @app.route('/students/delete/<int:ID_student>', methods=['POST'])
# def delete_student(ID_student):
#     student = students.query.get_or_404(ID_student)
#     db.session.delete(student)
#     db.session.commit()
    
#     return redirect(url_for('view_students'))

# # Преподаватели
# @app.route('/teachers')
# def view_teachers():
#     Teachers = teachers.query.all()
#     return render_template('teachers.html', Teachers=Teachers)

# @app.route('/teachers/add', methods=['GET', 'POST'])
# def add_teacher():
#     if request.method == 'POST':
#         name = request.form['name']
#         surname = request.form['surname']
#         ID_subject = request.form['ID_subject']
#         email = request.form['email']
        
#         new_teacher = teachers(name=name, surname=surname, ID_subject=ID_subject, email=email)
#         db.session.add(new_teacher)
#         db.session.commit()
        
#         return redirect(url_for('view_teachers'))
    
#     return render_template('add_teacher.html')

# @app.route('/teachers/edit/<int:ID_teacher>', methods=['GET', 'POST'])
# def edit_teacher(ID_teacher):
#     teacher = teachers.query.get_or_404(ID_teacher)
    
#     if request.method == 'POST':
#         teacher.name = request.form['name']
#         teacher.surname = request.form['surname']
#         teacher.ID_subject = request.form['ID_subject']
#         teacher.email = request.form['email']

#         db.session.commit()
#         return redirect(url_for('view_teachers'))
    
#     return render_template('upgrade_teacher.html', teacher=teacher)

# @app.route('/teachers/delete/<int:ID_teacher>', methods=['POST'])
# def delete_teacher(ID_teacher):
#     teacher = teachers.query.get_or_404(ID_teacher)
#     db.session.delete(teacher)
#     db.session.commit()
    
#     return redirect(url_for('view_teachers'))

# # Предметы
# @app.route('/subjects')
# def view_subjects():
#     Subjects = subjects.query.all()
#     return render_template('subjects.html', Subjects=Subjects)

# @app.route('/subjects/add', methods=['GET', 'POST'])
# def add_subject():
#     if request.method == 'POST':
#         title = request.form['title']
        
#         new_subject = subjects(title=title)
#         db.session.add(new_subject)
#         db.session.commit()
        
#         return redirect(url_for('view_subjects'))
    
#     return render_template('add_subject.html')

# @app.route('/subjects/edit/<int:ID_subject>', methods=['GET', 'POST'])
# def edit_subject(ID_subject):
#     subject = subjects.query.get_or_404(ID_subject)
    
#     if request.method == 'POST':
#         subject.title = request.form['title']

#         db.session.commit()
#         return redirect(url_for('view_subjects'))
    
#     return render_template('upgrade_subject.html', subject=subject)

# @app.route('/subjects/delete/<int:ID_subject>', methods=['POST'])
# def delete_subject(ID_subject):
#     subject = subjects.query.get_or_404(ID_subject)
#     db.session.delete(subject)
#     db.session.commit()
    
#     return redirect(url_for('view_subjects'))

# # Группы
# @app.route('/groups')
# def view_groups():
#     Groups = groups.query.all()
#     return render_template('groups.html', Groups=Groups)

# @app.route('/groups/add', methods=['GET', 'POST'])
# def add_group():
#     if request.method == 'POST':
#         title = request.form['title']
#         ID_teacher = request.form['ID_teacher']

        
#         new_group = groups(title=title, ID_teacher = ID_teacher)
#         db.session.add(new_group)
#         db.session.commit()
        
#         return redirect(url_for('view_groups'))
    
#     return render_template('add_group.html')

# @app.route('/groups/edit/<int:ID_group>', methods=['GET', 'POST'])
# def edit_group(ID_group):
#     group = groups.query.get_or_404(ID_group)
    
#     if request.method == 'POST':
#         group.title = request.form['title']
#         group.ID_teacher = request.form['ID_teacher']

#         db.session.commit()
#         return redirect(url_for('view_groups'))
    
#     return render_template('upgrade_group.html', group=group)

# @app.route('/groups/delete/<int:ID_group>', methods=['POST'])
# def delete_group(ID_group):
#     group = groups.query.get_or_404(ID_group)
#     db.session.delete(group)
#     db.session.commit()
    
#     return redirect(url_for('view_groups'))

# # Курсы
# @app.route('/kurses')
# def view_kurses():
#     Kurses = kurses.query.all()
#     return render_template('kurses.html', Kurses=Kurses)

# @app.route('/kurses/add', methods=['GET', 'POST'])
# def add_kur():
#     if request.method == 'POST':
#         ID_subject = request.form['ID_subject']
#         ID_teacher = request.form['ID_teacher']
#         title = request.form['title']
#         time = request.form['time']
#         cost = request.form['cost']
#         dateStart = request.form['dateStart'] 

        
#         new_kur = kurses(ID_subject=ID_subject, ID_teacher=ID_teacher, title=title, time=time, cost=cost, dateStart=dateStart)
#         db.session.add(new_kur)
#         db.session.commit()
        
#         return redirect(url_for('view_kurses'))
    
#     return render_template('add_kur.html')

# @app.route('/kurses/edit/<int:ID_kurs>', methods=['GET', 'POST'])
# def edit_kur(ID_kurs):
#     kur = kurses.query.get_or_404(ID_kurs)
    
#     if request.method == 'POST':
#         kur.ID_subject = request.form['ID_subject']
#         kur.ID_teacher = request.form['ID_teacher']
#         kur.title = request.form['title']
#         kur.time = request.form['time']
#         kur.cost = request.form['cost']
#         kur.dateStart = request.form['dateStart'] 

#         db.session.commit()
#         return redirect(url_for('view_kurses'))
    
#     return render_template('upgrade_kur.html', kur=kur)

# @app.route('/kurses/delete/<int:ID_kurs>', methods=['POST'])
# def delete_kur(ID_kurs):
#     kur = kurses.query.get_or_404(ID_kurs)
#     db.session.delete(kur)
#     db.session.commit()
    
#     return redirect(url_for('view_kurses'))

# # Кураторы
# @app.route('/kurators')
# def view_kurators():
#     Kurators = kurators.query.all()
#     return render_template('kurators.html', Kurators=Kurators)

# @app.route('/kurators/add', methods=['GET', 'POST'])
# def add_kurator():
#     if request.method == 'POST':
#         ID_kur = request.form['ID_kur']
#         name = request.form['name']
#         surname = request.form['surname']
#         email = request.form['email']
        
#         new_kurator = kurators(ID_kur=ID_kur, name=name, surname=surname, email=email)
#         db.session.add(new_kurator)
#         db.session.commit()
        
#         return redirect(url_for('view_kurators'))
    
#     return render_template('add_kurator.html')

# @app.route('/kurators/edit/<int:ID_kur>', methods=['GET', 'POST'])
# def edit_kurator(ID_kur):
#     kurator = kurators.query.get_or_404(ID_kur)
    
#     if request.method == 'POST':
#         kurator.ID_kur = request.form['ID_kur']
#         kurator.name = request.form['name']
#         kurator.surname = request.form['surname']
#         kurator.email = request.form['email']

#         db.session.commit()
#         return redirect(url_for('view_kurators'))
    
#     return render_template('upgrade_kurator.html', kurator=kurator)

# @app.route('/kurators/delete/<int:ID_kur>', methods=['POST'])
# def delete_kurator(ID_kur):
#     kurator = kurators.query.get_or_404(ID_kur)
#     db.session.delete(kurator)
#     db.session.commit()
    
#     return redirect(url_for('view_kurators'))

# if __name__ == '__main__':
    
#     app.run(debug=True)
from sqlalchemy import CheckConstraint, Column, Integer, String, ForeignKey
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import csv
import os

app = Flask(__name__)

# Настройка базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseVSU.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Определение моделей
class Student(db.Model):
    __tablename__  = 'student'

    ID_student = db.Column(db.Integer, primary_key=True)
    ID_kur = db.Column(db.Integer,ForeignKey('kurator.ID_kur'),nullable=False)
    ID_group = db.Column(db.Integer, ForeignKey('group.ID_group'), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False)
    passport = db.Column(db.String(6), nullable=False)
    __table_args__ = (CheckConstraint('age >= 18', name='check_age'))
    
    group = db.relationship('Group', back_populates = 'student')
    kurator = db.relationship('Kurator', back_populates='student')
    
class Teacher(db.Model):
    __tablename__ = 'teacher'

    ID_teacher = db.Column(db.Integer, primary_key=True)
    ID_subject = db.Column(db.Integer,ForeignKey('subject.ID_subject'), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String, nullable=False)

    subject = db.relationship('Subject', back_populates='teacher')
    group = db.relationship('Group', back_populates = 'teacher')

class Subject(db.Model):
    __tablename__ = 'subject'
    ID_subject = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    teacher = db.relationship('Teacher', back_populates='subject')

class Group(db.Model):
    __tablename__ = 'group'
    ID_group = db.Column(db.Integer, primary_key=True)
    titleGroup = db.Column(db.String, nullable=False)
    ID_teacher = db.Column(db.Integer, ForeignKey('teacher.ID_teacher'), nullable=False)

    student = db.relationship('Student', back_populates='group')
    teacher = db.relationship('Teacher', back_populates='group')

class Kurses(db.Model):
    __tablename__ = 'kurses'
    ID_kurs = db.Column(db.Integer, primary_key=True)
    ID_subject = db.Column(db.Integer,  primary_key=True)
    ID_teacher = db.Column(db.Integer,  nullable=False)
    title = db.Column(db.String, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    dateStart = db.Column(db.String, nullable=False)
    __table_args__ = (CheckConstraint('time >= 1 and time <=24 ', name='check_time'),)
    __table_args__ = (CheckConstraint('cost <= 200000', name='check_cost'),)

class Kurator(db.Model):
    __tablename__ = 'kurator'
    ID_kur = db.Column(db.Integer, primary_key=True)
    ID_kurs = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String, nullable=False)

    student = db.relationship('Student', back_populates='kurator')

# Функция для загрузки данных из CSV
def load_data_from_csv():
    csv_files = {
        'students': 'tables/table_data.csv',
        'teachers': 'tables/teachers_data.csv',
        'subjects': 'tables/subjects_data.csv',
        'groups' : 'tables/groups_data.csv'
    }

    for key, file_path in csv_files.items():
        if not os.path.exists(file_path):
            print(f"Файл не найден: {file_path}")
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if key == 'students':
                        existing_student = Student.query.filter_by(ID_student=row['ID_student']).count()
                        if existing_student == 0:
                            new_student = Student(
                                ID_kur=row['ID_kur'],
                                ID_group=row['ID_group'],
                                name=row['name'],
                                surname=row['surname'],
                                age=row['age'],
                                email=row['email'],
                                passport=row['passport']
                            )
                            db.session.add(new_student)

                    elif key == 'teachers':
                        existing_teacher = Teacher.query.filter_by(ID_teacher=row['ID_teacher']).count()
                        if existing_teacher == 0 :
                            new_teacher = Teacher(
                                ID_subject=row['ID_subject'],
                                name=row['name'],
                                surname=row['surname'],
                                email=row['email']
                                )
                            db.session.add(new_teacher)
                    elif key == 'subjects':
                        existing_subject = Subject.query.filter_by(ID_subject=row['ID_subject']).count()   
                        if existing_subject == 0:
                            new_subject = Subject(
                                title = row['title']
                            )
                            db.session.add(new_subject)
                    elif key == 'groups':
                        existing_group = Group.query.filter_by(ID_group=row['ID_group']).count()
                        if existing_group == 0:
                            new_group = Group(
                                titleGroup = row['titleGroup'],
                                ID_teacher = row['ID_teacher']
                            )
                            db.session.add(new_group)
                db.session.commit()
                print(f"Данные из {key} успешно загружены.")
        except Exception as e:
            print(f"Ошибка при загрузке данных из {file_path}: {e}")

# Создаем базу данных и загружаем данные из CSV  
with app.app_context():
    db.create_all()  
    load_data_from_csv()

def get_data_from_table(model):
    return model.query.all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def view_students():
    students = get_data_from_table(Student)
    return render_template('students.html', Student=students)



@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        email = request.form['email']
        passport = request.form['passport']
        ID_kur = request.form['ID_kur']
        ID_group = request.form['ID_group']
        
        new_student = Student(ID_kur=ID_kur, ID_group=ID_group, name=name, surname=surname, age=age, email=email, passport=passport)
        db.session.add(new_student)
        db.session.commit()
        
        return redirect(url_for('view_students'))
    
    return render_template('add_student.html')

@app.route('/students/edit/<int:ID_student>', methods=['GET', 'POST'])
def edit_student(ID_student):
    student = Student.query.get_or_404(ID_student)
    
    if request.method == 'POST':
        student.name = request.form['name']
        student.surname = request.form['surname']
        student.age = request.form['age']
        student.email = request.form['email']
        student.passport = request.form['passport']
        student.ID_kur = request.form['ID_kur']
        student.ID_group = request.form['ID_group']

        db.session.commit()
        return redirect(url_for('view_students'))
    
    return render_template('upgrade_student.html', Student=student)

@app.route('/students/delete/<int:ID_student>', methods=['POST'])
def delete_student(ID_student):
    student = Student.query.get_or_404(ID_student)
    db.session.delete(student)
    db.session.commit()
    
    return redirect(url_for('view_students'))

@app.route('/teachers')
def view_teachers():
    teachers = get_data_from_table(Teacher)
    return render_template('teachers.html', Teacher=teachers)

@app.route('/teachers/add', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        ID_subject = request.form['ID_subject']
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        
        new_teacher = Teacher(ID_subject=ID_subject,name=name, surname=surname,  email=email)
        db.session.add(new_teacher)
        db.session.commit()
        
        return redirect(url_for('view_teachers'))
    
    return render_template('add_teacher.html')

@app.route('/teachers/edit/<int:ID_teacher>', methods=['GET', 'POST'])
def edit_teacher(ID_teacher):
    teacher = Teacher.query.get_or_404(ID_teacher)
    
    if request.method == 'POST':
        teacher.ID_subject = request.form['ID_subject']
        teacher.name = request.form['name']
        teacher.surname = request.form['surname']
        teacher.email = request.form['email']

        db.session.commit()
        return redirect(url_for('view_teachers'))
    
    return render_template('upgrade_teacher.html', Teacher=teacher)

@app.route('/teachers/delete/<int:ID_teacher>', methods=['POST'])
def delete_teacher(ID_teacher):
    teacher = Teacher.query.get_or_404(ID_teacher)
    db.session.delete(teacher)
    db.session.commit()
    
    return redirect(url_for('view_teachers'))

if __name__ == '__main__':
    app.run(debug=True)
