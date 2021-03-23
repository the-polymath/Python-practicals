# 5.4 To write a Python Program to perform Merge sort.
def merge(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

temp = input("Enter 10 elements separated by space : \n")
lst = temp.split(" ")
lst = [int(i) for i in lst]
merge(lst)
print("\n Sorted list : ", lst)
