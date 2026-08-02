import sqlite3
conn=sqlite3.connect("students.db")
cursor=conn.cursor()
cursor.execute("SELECT * FROM students")
data=cursor.fetchall()
for row in data:
    print(row)
    
conn.close()