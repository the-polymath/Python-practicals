# 4.4 Write a python program which will throw user defined Exception if the number is not in the range 1 to 10.
class CSV(ValueError):
    def __init__(self, args):
        self.strerror = args

def check(num):
    try:
        num = int(num)
        if num not in range(1, 11):
            raise CSV("The Number entered should be in range 1 to 10")
        elif num != int:
            raise CSV("Enter an Integer!! ")
    except CSV as cv:
        print("User defnied exception!!\n", cv.strerror)


n = input("Enter the Number: ")
check(n)
