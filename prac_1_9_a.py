# Part A
myStr = "GTU is the best University"
print(myStr[15 : : 1])
print(myStr[-10 : -1 : 2])

# Part B
t = (1, 2, 3, (4, ), [5, 6])
print(t[3])
t[4][0] = 7
print(t)


# Part C
I = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(I)

# Part D
str1 = "This is Pyhton"
print("Slice of String : ", str1[1 : 4 : 1])
print("Slice of String : ", str1[0 : -1 : 2])
