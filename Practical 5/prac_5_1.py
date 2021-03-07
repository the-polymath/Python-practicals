''' 5.1 Write a Python program to search a specific value from a given list of values using binary
search method. '''

def bubble(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

    return lst

def binary(lst, high, low, no):
    if high > low:
        mid = (high + low) // 2
        if lst[mid] == no:
            return mid

        elif lst[mid] > no:
            return binary(lst, mid-1, low, no)
        else:
            return binary(lst, high, mid+1, no)

    else:
        return -1


temp = input("Enter 10 elements separated by space : \n")
lst = temp.split(" ")
lst = [int(i) for i in lst]
new_lst = bubble(lst)
x = int(input("Enter the number to be searched : "))
print("Sorted list = ", new_lst)
index = binary(new_lst, len(new_lst)-1, 0, x)
if index == -1:
    print("Value not found !!")
else:
    print("Value found at ", index)
