if __name__ == "__main__":
 list1 = [1,2,3,4,5,6,7]
 index_1 = 0
 index_2 = 1
 for i in range(2,len(list1)):
    if i % 2 == 0:
        number = list1[i]
        list1[i] = 2
        list1[index_2] = number 
        index_2 = i
        print(list1)
    else:
        number = list1[i]
        list1[i] = 1
        list1[index_1] = number 
        index_1 = i
        print(list1)
