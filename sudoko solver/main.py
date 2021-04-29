import numpy as np

sudoko_string = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"

sudoko_list = list(sudoko_string)
changed_values = []


#pre
def validate_sudoko():
 #check if any numbers are greater than 9 or smaller than 0
 for y in range(0,9):
   for x in range(0,9):
     if sudoko_list[y][x] > 9 or sudoko_list[y][x] < 0:
       print("number:",sudoko_list[y][x])
       print("number is greater than 9 or smaller than 0")
       return False
 #check if numbers are repeating in boxes
 for y in range(0,9,3):
  for x in range(0,9,3):
    box = []
    x0 = (x//3)*3
    y0=(y//3)*3
    for i in range(0,3):
      for j in range(0,3):
        if sudoko_list[y0+i][x0+j] not in box or sudoko_list[y0+i][x0+j] == 0:
          box.append(sudoko_list[y0+i][x0+j])
        else:
          print("box:",x)
          print("number:",sudoko_list[y0+i][x0+j])
          print("number in box repeated!")
          return False
 #check if any numbers are repeating in rows
 for y in range(0,9):
   row2 = []
   for x in range(0,9):
    if sudoko_list[y][x] not in row2 or sudoko_list[y][x] == 0:
      row2.append(sudoko_list[y][x])
    else:
      print("row:",y,"row index:",x)
      print("number:",sudoko_list[y][x])
      print("number in row repeated!")
      return False
 #check if any numbers are repeating in columns
 for x in range(0,9):
     column2 = []
     for y in range(0,9):
      if sudoko_list[y][x] not in column2 or sudoko_list[y][x] == 0:
        column2.append(sudoko_list[y][x])
      else:
        print("row:",y,"row index:",x)
        print("number:",sudoko_list[y][x])
        print("number in column repeated!")
        return False
 return True

#post
def post_valid_sudoko():
  #check if any numbers are greater than 9 or smaller than 1
 for y in range(0,9):
   for x in range(0,9):
     if sudoko_list[y][x] > 9 or sudoko_list[y][x] < 1:
       print("number:",sudoko_list[y][x])
       print("number is greater than 9 or smaller than 1")
       return False
 #check if numbers are repeating in boxes
 for y in range(0,9,3):
  for x in range(0,9,3):
    box = []
    x0 = (x//3)*3
    y0=(y//3)*3
    for i in range(0,3):
      for j in range(0,3):
        if sudoko_list[y0+i][x0+j] not in box:
          box.append(sudoko_list[y0+i][x0+j])
        else:
          print("number:",sudoko_list[y0+i][x0+j])
          print("number in box repeated!")
          return False
 #check if any numbers are repeating in rows
 for y in range(0,9):
   row2 = []
   for x in range(0,9):
    if sudoko_list[y][x] not in row2:
      row2.append(sudoko_list[y][x])
    else:
      print("row:",y,"row index:",x)
      print("number:",sudoko_list[y][x])
      print("number in row repeated!")
      return False
 #check if any numbers are repeating in columns
 for x in range(0,9):
     column2 = []
     for y in range(0,9):
      if sudoko_list[y][x] not in column2:
        column2.append(sudoko_list[y][x])
      else:
        print("row:",y,"row index:",x)
        print("number:",sudoko_list[y][x])
        print("number in column repeated!")
        return False
 return True

def seperate_rows():
   full_list = []
   list1 = []
   for number in sudoko_list:
       if len(list1) <= 8:
         list1.append(int(number))
       else:
           full_list.append(list1)
           list1 = []
           list1.append(int(number))
   full_list.append(list1)
   return full_list

def check_value(x,y,set_value):
  x0 = (x//3)*3
  y0=(y//3)*3
  for i in range(0,3):
    for j in range(0,3):
      if sudoko_list[y0+i][x0+j] == set_value:
        return False
  for y1 in range(0,9):
    if sudoko_list[y1][x] == set_value:
      return False
  for x1 in range(0,9):
    if sudoko_list[y][x1] == set_value:
      return False
  return True

def backtrack(index,y,x):
  index_2 = index - 1
  inf = changed_values[index_2]
  x2 = inf["x"]
  y2 = inf["y"]
  set_value=inf["value"]
  setvalue = check_value(x2,y2,set_value)
  while not setvalue:
        if set_value < 9:
         set_value += 1
        else:
         backtrack(index,y,x)
        setvalue = check_value(x2,y2,set_value)
  sudoko_list[y2][x2] = set_value
  
def solve():
  index = 0
  for y in range(0,9):
    for x in range(0,9):
     if sudoko_list[y][x] == 0:
      set_value = 1
      setvalue = check_value(x,y,set_value)
      while not setvalue:
        if set_value < 9:
         set_value += 1
        else:
          break
        setvalue = check_value(x,y,set_value)
      index += 1
      changed_values.append({"y":y,"x":x,"value":set_value})
      sudoko_list[y][x] = set_value
  
if __name__ == "__main__":
    sudoko_list=seperate_rows()
    solve()
    print(changed_values)
    post_valid_sudoko()
    print(np.matrix(sudoko_list))