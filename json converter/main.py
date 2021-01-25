import json
class filereader():
 def __init__(self,fields):
     self.fields = fields.split(" ")
 def get_json_and_convert(self):
    self.data_list = []
    with open("mcube.log") as file:
     for content in file.readlines():
      try:
        c = json.loads(content)
        self.data_list.append(c)
      except json.decoder.JSONDecodeError:
        self.data_list.append(content)
 def print_required_fields(self):
     for data in self.data_list:
         if type(data) == dict:
          try:
             print(str([data[feild] for feild in self.fields]).strip("[").strip("]").replace("'","").replace(",",""))
          except KeyError:
              print(None)
         elif type(data) == str:
             print(data)
if __name__ == "__main__":
    fields = input("enter the field(s):")
    fr = filereader(fields)
    fr.get_json_and_convert()
    fr.print_required_fields()