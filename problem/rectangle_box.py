example_list = ["Hello!","I","am","in","this","Box"]
length = [len(str(elem)) for elem in example_list]
length.sort()
greatest = length[-1]
for i in range(greatest+5):
   print("*",end="")
print("*")
for elem in example_list:
  g= greatest+2-len(elem)
  print("*"+" "*2+elem+" "*g+"*")
for i in range(greatest+5):
   print("*",end="")
print("*")