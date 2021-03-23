# Write a python program to retrieve strings starting with m and having 5 characters.
import re

x = input("Enter the String : ")

y = re.findall('m....', x)
print(y)
