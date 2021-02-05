# 4.1 Write a python program which will throw an exception for divisible by zero.
def check(a, b):
    try:
        div = a / b
        print(div)
    except Exception as e:
        print(e)


a = int(input())
b = int(input())
check(a, b)
