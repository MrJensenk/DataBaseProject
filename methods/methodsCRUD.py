# def insert_table(db, table, values):
#     query = "INSERT INTO {} VALUES ({})".format(table,values)
#     db.execute(query)
#     db.commit()

# def read_table(db, table, pk):
#     query = "SELECT * FROM {} WHERE ID = {}".format(table,pk)
#     rows = db.query(query)
#     if rows:
#         return rows[0]
#     else:
#         return None

# def delete_table(db, table, pk):
#     query = "DELETE FROM {} WHERE ID = {}".format(table,pk)
#     db.execute(query)
#     db.commit()