from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sl
from Database import create_database

app = Flask(__name__)

# Создаем базу данных и загружаем данные из CSV

create_database()

def get_data_from_table(table_name):
    with sl.connect("databaseVSU.db") as database:
        cursor = database.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def view_students():
    students = get_data_from_table('students')
    return render_template('students.html', students=students)

@app.route('/teachers')
def view_teachers():
    teachers = get_data_from_table('teachers')
    return render_template('teachers.html', teachers=teachers)

@app.route('/subjects')
def view_subjects():
    subjects = get_data_from_table('subjects')
    return render_template('subjects.html', subjects=subjects)

@app.route('/groups')
def view_groups():
    groups = get_data_from_table('groups')
    return render_template('groups.html', groups=groups)

@app.route('/kurses')
def view_kurses():
    kurses = get_data_from_table('kurses')
    return render_template('kurses.html', kurses=kurses)

@app.route('/kurators')
def view_kurators():
    kurators = get_data_from_table('kurators')
    return render_template('kurators.html', kurators=kurators)

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
        
        with sl.connect("databaseVSU.db") as database:
            cursor = database.cursor()
            cursor.execute("INSERT INTO students (ID_kur, ID_group, name, surname, age, email, passport) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (ID_kur, ID_group, name, surname, age, email, passport))
            database.commit()
        
        return redirect(url_for('view_students'))
    
    return render_template('add_student.html')

@app.route('/students/edit/<int:ID_student>', methods=['GET', 'POST'])
def edit_student(ID_student):
    with sl.connect("databaseVSU.db") as database:
        cursor = database.cursor()
        if request.method == 'POST':    
            name = request.form['name']
            surname = request.form['surname']
            age = request.form['age']
            email = request.form['email']
            passport = request.form['passport']
            ID_kur = request.form['ID_kur']
            ID_group = request.form['ID_group']

            cursor.execute("UPDATE students SET ID_kur=?, ID_group=?, name=?, surname=?, age=?, email=?, passport=? WHERE ID_student=?",
                           (ID_kur, ID_group, name, surname, age, email, passport, ID_student))
            database.commit()
            return redirect(url_for('view_students'))
        
        cursor.execute("SELECT * FROM students WHERE ID_student=?", (ID_student,))
        student = cursor.fetchone()
    
    return render_template('upgrade_student.html', student=student)

@app.route('/students/delete/<int:ID_student>', methods=['POST'])
def delete_student(ID_student):
    with sl.connect("databaseVSU.db") as database:
        cursor = database.cursor()
        cursor.execute("DELETE FROM students WHERE ID_student=?", (ID_student,))
        database.commit()
    
    return redirect(url_for('view_students'))

# Остальные маршруты для teachers, subjects, groups, kurses...

if __name__ == '__main__':
    app.run(debug=True)
