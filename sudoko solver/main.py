import numpy
from os import system

sudoko_string = "001008073005600001700001000090810000530000046000065030000100004800009300940500700"

sudoko_list = list(sudoko_string)

#the function to seperate the SMD format string to rows in a 2d list
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

#the function to solve the sudoko
def solve(sudoko_list):
    #finding the pos of the 0 in sudoko 2d list
    find = find_empty(sudoko_list)
    
    #if there is no pos that has 0 it's exiting
    if not find:
        return True
    else:
        #getting the riw and col
        row, col = find

   #checking values from 1 to 9 are valid in that pos
    for i in range(1,10):
        if valid(sudoko_list, i, (row, col)):
            #if it is valid then setting it to that number
            sudoko_list[row][col] = i
            
            #using recursion to check if the next value is valid
            if solve(sudoko_list):
                #if it is valid exiting
                return True
            
            #if it is not valid then setting it to 0
            sudoko_list[row][col] = 0
    #if there in no number that is valid from 1 to 9 then returning false
    return False

#checking if the number is valid at that pos
def valid(sudoko_list, num, pos):
    # Check row
    for i in range(len(sudoko_list[0])):
        if sudoko_list[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(sudoko_list)):
        if sudoko_list[i][pos[1]] == num and pos[0] != i:
            return False

    # Check sudoko_listx
    sudoko_listx_x = pos[1] // 3
    sudoko_listx_y = pos[0] // 3

    for i in range(sudoko_listx_y*3, sudoko_listx_y*3 + 3):
        for j in range(sudoko_listx_x * 3, sudoko_listx_x*3 + 3):
            if sudoko_list[i][j] == num and (i,j) != pos:
                return False

    return True


#function to return the pos of an empty value
def find_empty(sudoko_list):
    for i in range(len(sudoko_list)):
        for j in range(len(sudoko_list[0])):
            if sudoko_list[i][j] == 0:
                return (i, j)  # row, col

    return None

def valid_sudoko():
  #check if any numbers are greater than 9 or smaller than 0
 for y in range(0,9):
   for x in range(0,9):
     if sudoko_list[y][x] > 9 or sudoko_list[y][x] < 0:
       print("number:",sudoko_list[y][x])
       print("number is greater than 9 or smaller than 1")
       return False
 #check if numbers are repeating in sudoko_listxes
 for y in range(0,9,3):
  for x in range(0,9,3):
    sudoko_listx = []
    x0 = (x//3)*3
    y0=(y//3)*3
    for i in range(0,3):
      for j in range(0,3):
        if sudoko_list[y0+i][x0+j] not in sudoko_listx or sudoko_list[y0+i][x0+j] == 0:
          sudoko_listx.append(sudoko_list[y0+i][x0+j])
        else:
          print("number:",sudoko_list[y0+i][x0+j])
          print("number in sudoko_listx repeated!")
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

def post_valid_sudoko():
  #check if any numbers are greater than 9 or smaller than 1
 for y in range(0,9):
   for x in range(0,9):
     if sudoko_list[y][x] > 9 or sudoko_list[y][x] < 1:
       print("number:",sudoko_list[y][x])
       print("number is greater than 9 or smaller than 1")
       return False
 #check if numbers are repeating in sudoko_listxes
 for y in range(0,9,3):
  for x in range(0,9,3):
    sudoko_listx = []
    x0 = (x//3)*3
    y0=(y//3)*3
    for i in range(0,3):
      for j in range(0,3):
        if sudoko_list[y0+i][x0+j] not in sudoko_listx:
          sudoko_listx.append(sudoko_list[y0+i][x0+j])
        else:
          print("number:",sudoko_list[y0+i][x0+j])
          print("number in sudoko_listx repeated!")
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

if __name__ == "__main__":
    sudoko_list = seperate_rows()

    valid_1 = valid_sudoko()

    if not valid_1:
      print("the sudoko is not valid and cannot be solved!")
      exit(0)
    else:
      from time import sleep
      system("clear")
      for _ in range(2):
        print("starting.")
        sleep(0.5)
        system("clear")
        print("starting..")
        sleep(0.5)
        system("clear")
        print("starting...")
        sleep(0.5)
        system("clear")

    solve(sudoko_list)

    valid = post_valid_sudoko()

    if valid:
      print(numpy.matrix(sudoko_list))
      print("the sudoku is solved!")
