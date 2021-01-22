number = 0
def generate_odd_number(number):
  if number == 0:
      number += 1
      yield number
  else:
      number += 2
      yield number
while True:
    number = next(generate_odd_number(number))
    print(number)
    print("press enter for next number...")
    input()