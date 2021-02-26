# 4.5 Write a python program which will throw an exception if the value entered by user is
# less than zero.

class CSV(ValueError):
    def __init__(self, args):
        self.strerror = args

def check(num):
    try:
        num = int(num)
        if num < 0:
            raise CSV("The Number entered should in postive range")
        elif num != int:
            raise CSV("Enter an Integer!! ")
    except CSV as cv:
        print("User defnied exception!!\n", cv.strerror)


n = input("Enter the Number: ")
check(n)
