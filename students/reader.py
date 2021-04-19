from pymongo import MongoClient

client = MongoClient(host="localhost",port=27017)
db = client.students_db
students_folder = db.students_db
subjects_a = {"Biology":0,"physics":0,"chemistry":0,"Geography":0,"Computer":0,"History & Civics":0}

def get_key(given_dict,val):
    keys = []
    for key,value in zip(given_dict.keys(),given_dict.values()):
        if value == val:
            keys.append(key)
    return keys

def get_mostAs_subject():
   resultsA = list(students_folder.find({"subjects":{"$elemMatch":{"grade":"A"}}}))
   for ra in resultsA:
        subjects = ra["subjects"]
        for subject in subjects:
            if subject["grade"] == "A":
                no_of_a = subjects_a[subject["subject"]]
                subjects_a[subject["subject"]] =  no_of_a + 1
   subjects = get_key(subjects_a,max(subjects_a.values()))
   print("the subject(s) with most A's:")
   for subject in subjects:
        print(subject)

def get_failed_students():
    results = students_folder.find({"subjects":{"$elemMatch":{"grade":{"$in":["D","E","F"]}}}})
    for result in list(results):
        print("Students who failed:")
        name = result["Name"]
        print(name)

def get_all_As():
    #can't figure it out
    pass