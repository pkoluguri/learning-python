"""
fibonaci series:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
the series starts with 0 
if you add 1 to 0 you get 1
the series adds the previous number(0) to the result(1) and get's another result(1)
it continues the series by doing this several times
ex-
 0+1 = 1
 1+0 = 1
 1+1 = 2
 2+1 = 3
 3+2 = 5
 5+3 = 8
 ect..
"""
previous_number = 1
number = 0
while True: 
   print(number)
   print("press enter for next number..")
   input()
   result = previous_number + number
   previous_number = number
   number = result