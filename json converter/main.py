import json
class filereader():
 def __init__(self,filename,fields):
   self.filename = filename
   self.fields = fields.split(",")  
 def get_json_and_convert(self):
  try:
    with open(self.filename) as file:
     line = file.readline()
     while line != "":
      try:    
       data = json.loads(line)
      except json.decoder.JSONDecodeError:
       data = line
      self.print_required_fields(data)
      line = file.readline()
  except FileNotFoundError:
     print(f"{self.filename} has not been found")
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
    parser = argparse.ArgumentParser(description="testing")
    parser.add_argument("-f","--file",default="mcube.log")
    parser.add_argument("-fi","--fields",default="ts",help="enter the arguments with ,")
    args = parser.parse_args()
    filename = re.findall(r"file='(.+)',",str(args))[0]
    fields = re.findall(r"fields='(.+)'\)",str(args))[0]
    fr = filereader(filename,fields)
    fr.get_json_and_convert()