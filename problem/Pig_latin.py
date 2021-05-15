def Pig_latintoenglish(words):
    words = words.split(" ")
    for word in words:
       l =  word[0]
       word = word.lstrip(l)
       yield word+l+"ay"

def Pig_latintoenglishList(words):
    main_list = []
    words = words.split(" ")
    for word in words:
       l =  word[0]
       word = word.lstrip(l)
       main_list.append(word+l+"ay")
    return main_list

def Pig_latintoenglishStr(words):
    main_str = ""
    words = words.split(" ")
    for word in words:
       l =  word[0]
       word = word.lstrip(l)
       word = word+l+"ay"
       main_str = main_str+" "+word
    return main_str

print(Pig_latintoenglishStr("The quick brown fox"))