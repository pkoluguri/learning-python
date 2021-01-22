previous_number = 1
number = 0
def addnumber(previous_number,number):
    yield previous_number + number
while True:
    print(number)
    print("press enter to continue...")
    input()
    result = addnumber(previous_number,number)
    previous_number = number
    number = next(result)


#improvements
# 1 - write it as class and membeer function
# 2 - call it from main function
# 3 use log statement instead of print.    