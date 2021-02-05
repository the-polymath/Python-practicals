# 2.2 Write a Python program which takes a list and returns a list with the elements "shifted
# left by one position" so [1, 2, 3] yields [2, 3, 1]. Example: [1, 2, 3] → [2, 3, 1] [11, 12, 13]
# → [12, 13, 11]

def shift(lst):
    temp = lst[0]
    lst = lst[1:]
    lst.append(temp)
    return lst

N = int(input("Enter the length of list:"))
lst = []
for _ in range(0, N):
    sh = int(input())
    lst.append(sh)
print("list before : ", lst)
slst = shift(lst)
print("List after  : ",slst)
