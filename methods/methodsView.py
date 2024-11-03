def view_students():
    with sl.connect("databaseVSU.db") as db:
        cursor = db.cursor()
        query = """SELECT * FROM students"""
        cursor.execute(query)
        rows = cursor.fetchall()
    
    print("\nСписок студентов:")
    for row in rows:
        print(f"{row[0]} | {row[3]} {row[4]}, группа: {row[2]}, возраст: {row[5]}, e-mail: {row[6]}")

def view_teachers():
    with sl.connect("databaseVSU.db") as db:
        cursor = db.cursor()
        query = """SELECT * FROM teachers"""
        cursor.execute(query)
        rows = cursor.fetchall()
    
    print("\nСписок преподавателей:")
    for row in rows:
        print(f"{row[0]} | {row[2]} {row[3]}, предмет: {row[1]}, e-mail: {row[4]}")

def view_kurators():
    with sl.connect("databaseVSU.db") as db:
        cursor = db.cursor()
        query = """SELECT * FROM kurators"""
        cursor.execute(query)
        rows = cursor.fetchall()
    
    print("\nСписок кураторов:")
    for row in rows:
        print(f"{row[0]} | {row[2]} {row[3]}, курс: {row[1]}, e-mail: {row[4]}")
