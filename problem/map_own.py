def multiply_with_2(num):
  return num*2

def map(func,iterateable):
   returned_list = []
   for el in iterateable:
       returned_list.append(func(el))      
   return returned_list

List = [1,2,3,4,5,6]
print(map(multiply_with_2,List))