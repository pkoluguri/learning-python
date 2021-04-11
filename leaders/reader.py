import json
import pymongo

client = pymongo.MongoClient(host="localhost",port=27017)
db = client.leaders_db
leaders_db_file = db.leaders_file

def process_input(input:str):
    doc = list(leaders_db_file.find({"country":input}))
    if len(doc) != 0:
        country_information = doc[0]
        print("Country:{}\nHeadOfState:{}\nHeadOfGovernement:{}".format(country_information["country"],country_information["headofstate"],country_information["headofgovernement"]))
    doc = list(leaders_db_file.find({"headofstate":input}))
    if len(doc) != 0:
        country_information = doc[0]
        print("Country:{}\nHeadOfState:{}\nHeadOfGovernement:{}".format(country_information["country"],country_information["headofstate"],country_information["headofgovernement"]))
    doc = list(leaders_db_file.find({"headofgovernement":input}))
    if len(doc) != 0:
        country_information = doc[0]
        print("Country:{}\nHeadOfState:{}\nHeadOfGovernement:{}".format(country_information["country"],country_information["headofstate"],country_information["headofgovernement"]))

if __name__ == "__main__":
 while True:
    name =input("enter the name of the country or headofgovernement(president) or headofstate(prime minister) you want to find: ")
    if name.lower() == "exit":
        break
    else:
     process_input(name)