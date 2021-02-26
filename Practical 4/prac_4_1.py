# 4.1 Write a python program which will throw an exception for divisible by zero.
def check(a, b):
    try:
        div = a / b
        print("Divion", div)
    except ArithmeticError as e:
        print(e)


a = int(input("Enter a : "))
b = int(input("Enter b : "))
check(a, b)
