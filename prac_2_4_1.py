# 2.4 Write a Python program
# 1) To generate a list except for the first 5 elements, where the values are square of
# numbers between 1 and 30(both included)

def printlist():
    lst = []
    for i in range(1, 31):
        lst.append(i**2)

    return lst[5:]

slst = printlist()
print(slst)
