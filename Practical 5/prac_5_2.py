''' 5.2 Write a python program to arrange the characters of a given string 'welcome' in an alphabetical
order using insertion sort algorithm. '''

def insertion(lst):
    for i in range(1, len(lst)):

        min = lst[i]
        j = i-1
        while j >= 0 and lst[j] > min:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = min

    res = ""
    for val in lst:
        res = res + chr(val)
    return res

temp = input("Enter string : \n")

lst = [ord(i) for i in temp]
new_lst = insertion(lst)
print("\nSorted string : ", new_lst)
