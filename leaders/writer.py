import requests
import re
from bs4 import BeautifulSoup
import json
from pymongo import MongoClient


client = MongoClient(host="localhost",port=27017)
db = client.leaders_db
leaders_db_file = db.leaders_file
infom_pattern = re.compile(r'href="/wiki/.+"')
country_pattern = re.compile(r'title="(.+)"')
president_pattern = re.compile(r'title="(.*?)"')
leaders_information = []

if __name__ == "__main__":
    resp = requests.get("https://en.wikipedia.org/wiki/List_of_current_heads_of_state_and_government")
    bsobj = BeautifulSoup(resp.content,"html.parser")
    infom = bsobj.find_all("tr")
    info = []
    presidents = []
    for info1 in infom:
        if "Prime Minister of" in str(info1) and "President of" in str(info1):
            info.append(info1)
            information = infom_pattern.findall(str(info1))
            if len(information) == 3:
                country = country_pattern.findall(str(information[0]))[0]
                headofstate = president_pattern.findall(str(information[1]))[1]
                HeadOfGoverment = president_pattern.findall(str(information[2]))[1]
                information = {"country":country,
                            "headofstate":headofstate,
                            "headofgovernement":HeadOfGoverment}
                leaders_db_file.insert_one(information) 