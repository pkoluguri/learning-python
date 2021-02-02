import json
class filereader():
 def __init__(self,filename,fields):
   self.filename = filename
   self.fields = fields.split(",")  
 def get_json_and_convert(self):
  if self.filename == "no file given":
     import sys
     line = sys.stdin.readline()
     self.process(line)
  else:
    try:
     with open(self.filename) as file:
      for line in file:
        self.process(line)
    except FileNotFoundError:
      print(f"{self.filename} has not been found")
 def process(self,line):
    try:    
        data = json.loads(line)
        self.print_required_fields(data)
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
         else:
             print(data)
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="testing")
    parser.add_argument("-f","--file",default="no file given",dest="filename")
    parser.add_argument("-fi","--fields",default="ts",help="enter the arguments with ,",dest="fields")
    args = parser.parse_args()
    fr = filereader(args.filename,args.fields)
    fr.get_json_and_convert()
