from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run(debug=True)
