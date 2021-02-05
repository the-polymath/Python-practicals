# 2.5 Write a python program to print numbers given in the list after removing even numbers from it.
def remove_even(lst):
    nlst = []
    for i in lst:
        if i % 2 != 0:
            nlst.append(i)
    return nlst

string = input().split()
lst =[]
for i in string:
    lst.append(int(i))

slst = remove_even(lst)
print(slst)
