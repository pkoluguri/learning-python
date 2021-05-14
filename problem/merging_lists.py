
def merge(list1,list2):
    main_list = []
    smallest_length = min(len(list1),len(list2))
    for i in range(smallest_length):
        if list1[i] > list2[i]:
            main_list.append(list2[i])
            main_list.append(list1[i])
        elif list2[i] < list1[i]:
            main_list.append(list2[i])
            main_list.append(list1[i])
        else:
            main_list.append(list1[i])
            main_list.append(list2[i])
    for el in list1:
        if el not in main_list:
            print(el)
            main_list.append(el)
    for el in list2:
        if el not in main_list:
            main_list.append(el)
    return main_list

print(merge([1,4,6],[2,3,5]))