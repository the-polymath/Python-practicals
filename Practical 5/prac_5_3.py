# 5.3 To write a Python Program to perform Selection sort.

def selection(lst):
    for i in range(len(lst)):
        min = lst[i]
        p = i
        for j in range(i+1, len(lst)):
            if lst[j] < min:
                p = j
                min = lst[j]
        lst[p] = lst[i]
        lst[i] = min

temp = input("Enter 10 elements separated by space : \n")
lst = temp.split(" ")
lst = [int(i) for i in lst]
selection(lst)
print("\n Sorted list : ", lst)
