# 2.8 Write a python program to sort a dictionary by value
def sorting(dic):
    for i in sorted(dic, key=dic.get):
        print(i, dic[i])


dictionary = {'a':5, 'b':1, 'c':3, 'd':2, 'e':4}
sorting(dictionary)
