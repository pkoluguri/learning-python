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