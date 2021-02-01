import json
import sys

class filereader():
 def __init__(self,filename,fields):
   self.filename = filename
   self.fields = fields.split(",") 

 def get_json_and_process(self):
   if(self.filename == "no file given"):
     self.process_json_from_stdin()
   else:
     self.process_json_from_file()

 def process_json_from_file(self):  
  try:
    with open(self.filename) as file:
     for line in file:
       self.process(line)
  except FileNotFoundError:
    print(f"{self.filename} has not been found")
 
 def process_json_from_fileinput(self):   
  import fileinput 
  for line in fileinput.input():
    self.process(line)

 def process(self, line):
  try:    
    data = json.loads(line)
  except json.decoder.JSONDecodeError:
    data = line
  self.print_required_fields(data)

 def print_required_fields(self,data):
         if type(data) == dict:
            for idx,field in enumerate(self.fields,start=1):
                  if idx < len(self.fields):
                   try:
                     print(f"{field}:{data[field]}",end=" ")
                   except KeyError:
                     print(None,end=" ")
                  elif idx >= len(self.fields):
                    try:
                     print(f"{field}:{data[field]}")
                    except KeyError:
                     print(None)
         elif type(data) == str:
             print(data)
if __name__ == "__main__":
    import argparse
    import re
    parser = argparse.ArgumentParser(description="JSON log to Human readable")
    parser.add_argument("-f","--file",default="no file given",dest="filename")
    parser.add_argument("-fi","--fields",default="ts,m",help="enter the arguments with ,",dest="fields")
    args = parser.parse_args()
    print(args.filename)
    print(args.fields)
    fr = filereader(args.filename, args.fields)
    fr.get_json_and_process()
