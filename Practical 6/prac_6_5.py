# Write a Python program to Validate an Email Address Using Python
import re

text = input("Enter the e-mail : ")

if re.search('^[a-z0-9]+[@]+[a-zA-Z]+[.]+[a-zA-Z]+$',  text):
    print("proper email ")
else:
    print(" not proper email ")
