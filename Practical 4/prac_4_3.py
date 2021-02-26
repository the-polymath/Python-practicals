# 4.3 Write a python program which will throw an exception for valueError.

def check(n):

    try:
        n = int(n)
        sq = n ** 0.5
        print(sq)
    except ValueError:
        print(" Squareroot cannot be calculate of", n)

n = input("Enter no. : ")
check(n)
