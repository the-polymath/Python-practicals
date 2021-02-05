# 3.2 Write a Python program to read a text file and do following:
# 1. Print no. of words 2. Print no. statements

file = open("file.txt")
word_count = 0
statement_coun = 0
for lines in file:
    lines.rstrip()
    words = lines.split()
    word_count += len(words)
    statement_coun += 1

print(word_count)
print(statement_coun)
