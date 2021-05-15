def reverse_list(List:list):
   length = len(List)//2
   for i in range(0,length):
       neg_idx = i+1
       n = List[i]
       List[i] = List[-neg_idx]
       List[-neg_idx] = n

if __name__ == "__main__":
    List = [6,5,4,3,2,1]
    reverse_list(List)
    print(List)