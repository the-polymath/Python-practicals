# 4.3 Write a python program which will throw an exception for valueError.

def check(n):

    try:
        sq = n ** 0.5
        print(sq)
    except:
        print(" Squareroot cannot be calculate of", n)

n = int(input())
check(n)
