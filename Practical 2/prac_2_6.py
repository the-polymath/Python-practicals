# 2.6 Write a program to count the numbers of characters in the string and store them in a dictionary data structure.

def coun(string):
    dic ={}
    for i in string:
        dic[i] = dic.get(i, 0) + 1

    return dic

strin = input()
print("Total number of characters in string is :", len(strin))
print(coun(strin))
