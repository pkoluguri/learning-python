import numpy
from os import system

sudoko_string = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"

sudoko_list = list(sudoko_string)

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

def solve(sudoko_list):

    find = find_empty(sudoko_list)
    
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(sudoko_list, i, (row, col)):
            sudoko_list[row][col] = i
            
            system("clear")
 
            print(numpy.matrix(sudoko_list))

            if solve(sudoko_list):
                return True
            
            sudoko_list[row][col] = 0

    return False

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


def find_empty(sudoko_list):
    for i in range(len(sudoko_list)):
        for j in range(len(sudoko_list[0])):
            if sudoko_list[i][j] == 0:
                return (i, j)  # row, col

    return None

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

    solve(sudoko_list)
   
   
