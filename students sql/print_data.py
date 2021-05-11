import sqlite3

conn = sqlite3.connect("students.sqlite")

cur = conn.cursor()

cur.execute("SELECT * FROM Students")
for row in cur:
    print(row)

cur.execute("SELECT * FROM Subjects")
for row in cur:
    print(row)