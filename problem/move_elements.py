list1 = [1,2,3,4,5,6]

def move(k:int)->None:
  if k >= len(list1):
      print("k is greater than the length of the list")
      return
  indexes = [i for i in range(k)]
  for i in range(len(list1)//k):
    for idd,idx in enumerate(indexes):
     if idx+k > len(list1)-1:
       return
     number = list1[idx+k]
     list1[idx+k] = list1[idx]
     list1[idx] = number
     indexes[idd]=idx+k
     print(list1)
     

if __name__ == "__main__":
 print(list1)
 move(5)