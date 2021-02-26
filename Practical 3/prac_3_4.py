# 3.6 Write a python program to retrieve name and date of birth (mm-dd-yyyy) of students from a
# given file student.txt

file = open("students.txt")

for lines in file:
    ls = lines.split()
    print(ls[0].ljust(8, ' '), ls[1])
