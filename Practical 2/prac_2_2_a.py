# 2.2 Write a Python program which will return the sum of the numbers in the array, returning 0 for an
# empty array. Except the number 13 is very unlucky, so it does not count and number that come
# immediately after 13 also do not count. Example : [1, 2, 3, 4] = 10 [1, 2, 3, 4, 13] = 10 [13, 1, 2,
# 3, 13] = 5

def no_count(lst):
    sm = 0
    for i in range(0, len(lst)):
        if lst[i] == 13:
            continue
        elif lst[i-1] == 13 and i != 0:
            continue
        else:
            sm += lst[i]

    return sm

N = int(input())
lst = []
for _ in range(0, N):
    sh = int(input())
    lst.append(sh)
sum_list = no_count(lst)
print(sum_list)
