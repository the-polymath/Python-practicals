# 5.5 To write a Python Program to perform bubble sort.

def bubble(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp


temp = input("Enter 10 elements separated by space : \n")
lst = temp.split(" ")
lst = [int(i) for i in lst]
bubble(lst)
print("Sorted list using bubble sort = ", lst)
