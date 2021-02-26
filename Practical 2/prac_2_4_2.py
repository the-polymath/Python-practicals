# 2) To generate a list of first and last 5 elements where the values are square of numbers btween 1 and 30.

def printlist():
    lst = []
    for i in range(1, 31):
        lst.append(i**2)

    return  lst[0:5], lst[-5:]


first_list, last_list = printlist()
print(first_list, last_list)
