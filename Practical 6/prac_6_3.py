''' 6.3 Write a Python program to match a string that contains only upper
 and lowercase letters, numbers, and underscores using Regular Expression '''
import re

text = input("Enter the sentence : ")

if re.search('^[a-zA-Z0-9_]*$',  text):
    print("It is a proper sentence ")
else:
    print('''string should contains only upper
 and lowercase letters, numbers, and underscores ''')
