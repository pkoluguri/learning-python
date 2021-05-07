binary_search_list = [1,2,3,4,5,6,7]
binary_search_list.sort()

def perform_binary_search(start:int,stop:int,number:int):
  mid = start+(stop-start)//2
  if stop >= start:
   if binary_search_list[mid] == number:
     return mid
   elif number > binary_search_list[mid]:
     return perform_binary_search(mid+1,stop,number)
   elif number < binary_search_list[mid]:
     return perform_binary_search(1,mid-1,number)
  else:
      return None

if __name__ == "__main__":
    result= perform_binary_search(0,len(binary_search_list)-1,10)
    print(f"number at index {result}")
    