# Write a Python program to find the substrings within a string using Regular Expression

import re

text = input("Enter the sentence : ")
substring = input("Enter the substring : ")
if re.search(substring,  text):
    print(" substring found  !! ")
else:
    print("Substring not found ")
