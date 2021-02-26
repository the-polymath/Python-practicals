# 3.8 Write a python program to know the current working directory and to print all contents of the
# current directory. What changes we need to make in the program if we wish to display the
# contents of only 'mysub' directory available in current directory?

import os

print("The directory is : ")
print(os.getcwd(), "\n\n")

lst = os.listdir(os.getcwd())
print("The contents of directory are :")
for i in lst:
    print(i)
print("\n\n")
print("The contents of 'mysub' folder is ", os.listdir('mysub'))
