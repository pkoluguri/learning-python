import random
import json
from pymongo import MongoClient

names = ["Rahul","Manas","Rohit","Akhil","Arjun","Thomas","Bella","Thomas","Ruby","Mary"]
Subjects = ["Biology","physics","chemistry","Geography","Computer","History & Civics"]
Grades = ["A","B","C","D","E","F"]
datas= []
client = MongoClient(host="localhost",port=27017)
db = client.students_db
students_folder = db.students_db

for name in names:
 data = {
   "Name": name,
   "subjects":[
       {
           "subject":Subjects[random.randint(0,1)],
           "grade":random.choice(Grades)
       },
       {
           "subject":Subjects[random.randint(2,3)],
           "grade":random.choice(Grades)
       },
       {
           "subject":Subjects[random.randint(4,5)],
           "grade":random.choice(Grades)
       }
   ]
 }
 
 students_folder.insert_one(data)