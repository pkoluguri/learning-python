import sqlite3
import random

#normalized way

names = ["Rahul","Manas","Rohit","Akhil","Arjun","Thomas","Bella","Sneha","Ruby","Mary"]
Subjects = ["Biology","physics","chemistry","Geography","Computer","History & Civics"]
Grades = ["A","B","C","D","E","F"]


conn = sqlite3.connect("student.sqlite")

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Students")
cur.execute("DROP TABLE IF EXISTS Subjects")

cur.execute("CREATE TABLE Students (id INTIGER , name TEXT)")
cur.execute("CREATE TABLE Subjects (id INTIGER , subject TEXT , grade TEXT)")

for i in range(0,len(names)):
    cur.execute("INSERT INTO Students (id , name) VALUES (? , ?)",(i,names[i]))
    
    cur.execute("INSERT INTO Subjects (id , subject , grade) VALUES (?,?,?)",(i,Subjects[random.randint(0,1)],random.choice(Grades)))
    cur.execute("INSERT INTO Subjects (id , subject , grade) VALUES (?,?,?)",(i,Subjects[random.randint(2,3)],random.choice(Grades)))
    cur.execute("INSERT INTO Subjects (id , subject , grade) VALUES (?,?,?)",(i,Subjects[random.randint(4,5)],random.choice(Grades)))

conn.commit()

conn.close()