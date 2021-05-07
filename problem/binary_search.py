binary_search_list = [6,2,3,4,4,3,1,2]

def perform_binary_search(number:int)->list:
 binary_search_list.sort()
 for idx,num in enumerate(binary_search_list):
     if num >= number:
        return idx

if __name__ == "__main__":
    result= perform_binary_search(4)
    print(result)