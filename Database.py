import sqlite3 as sl
import csv

with sl.connect("databaseVSU.db") as database:
    cursor = database.cursor()

    cursor.execute("""DROP TABLE IF EXISTS students""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS students (
                    ID_student INTEGER PRIMARY KEY AUTOINCREMENT,
                    ID_kur INTEGER,
                    ID_group INTEGER,
                    name VARCHAR(60),
                    surname VARCHAR(60),
                    age INTEGER,  
                    email TEXT,
                    passport VARCHAR(6),
                    FOREIGN KEY(ID_kur) REFERENCES kurators(ID_kur),
                    FOREIGN KEY(ID_group) REFERENCES groups(ID_group));""")
                        
    cursor.execute("""DROP TABLE IF EXISTS teachers""")                                        
    cursor.execute("""CREATE TABLE IF NOT EXISTS teachers (
                        ID_teacher INTEGER PRIMARY KEY AUTOINCREMENT,
                        ID_subject INTEGER,
                        name VARCHAR(60) NOT NULL,
                        surname VARCHAR(60) NOT NULL,
                        email TEXT,
                        specialization TEXT,
                        FOREIGN KEY(ID_subject) REFERENCES subjects(ID_subject));""")      
                        
                                    
    cursor.execute("""DROP TABLE IF EXISTS subjects""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS subjects (
                        ID_subject INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL);""")
                        
    cursor.execute("""DROP TABLE IF EXISTS kurators""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS kurators (
                        ID_kur INTEGER PRIMARY KEY AUTOINCREMENT,
                        ID_kurs INTEGER,    
                        name VARCHAR(60) NOT NULL,
                        surname VARCHAR(60) NOT NULL,
                        email TEXT,
                        FOREIGN KEY(ID_kurs) REFERENCES kurses(ID_kurs));""")   
    
    cursor.execute("""DROP TABLE IF EXISTS kurses""")                               
    cursor.execute("""CREATE TABLE IF NOT EXISTS kurses (
                        ID_kurs INTEGER PRIMARY KEY AUTOINCREMENT,
                        ID_subject INTEGER,
                        ID_teacher INTEGER,
                        title TEXT NOT NULL,
                        time INTEGER(120),
                        cost INTEGER,
                        dateStart TEXT,
                        FOREIGN KEY(ID_subject) REFERENCES subjects(ID_subject),
                        FOREIGN KEY(ID_teacher) REFERENCES teachers(ID_teacher));""")        
          
    cursor.execute("""DROP TABLE IF EXISTS groups""")                    
    cursor.execute("""CREATE TABLE IF NOT EXISTS groups(
                        ID_group INTEGER PRIMARY KEY AUTOINCREMENT, 
                        titleGroup VARCHAR(100) NOT NULL UNIQUE,
                        ID_teacher INTEGER,
                        FOREIGN KEY(ID_teacher) REFERENCES teachers(ID_teacher));""")
    
    with open("table_data.csv", newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        insert_values = [(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in reader]
    insert_query = "INSERT INTO students (ID_student,ID_kur,ID_group,name,surname,age,email,passport) VALUES (?,?,?,?,?,?,?,?)"  
    cursor.executemany(insert_query, insert_values)

database.commit()

cursor.close()
database.close()