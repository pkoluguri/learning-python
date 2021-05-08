binary_search_list = [1,2,3,4,5,6]
binary_search_list.sort()

def perform_binary_search(begin:int, end:int , search:int):
  mid = begin+(end-begin)//2
  if end >= begin:
   if binary_search_list[mid] == search:

     return mid

   elif search > binary_search_list[mid]:

     return perform_binary_search(mid+1,end,search)

   elif search < binary_search_list[mid]:

     return perform_binary_search(0,mid-1,search)

  else:
      return None

if __name__ == "__main__":
    result= perform_binary_search(0,len(binary_search_list)-1,5)
    print(f"number at index {result}")