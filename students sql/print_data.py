import sqlite3

conn = sqlite3.connect("student.sqlite")

cur = conn.cursor()

cur.execute("SELECT * FROM Students")
print("students table:")
for row in cur:
    print(row)


print("subjects table:")
cur.execute("SELECT * FROM Subjects")
for row in cur:
    print(row)