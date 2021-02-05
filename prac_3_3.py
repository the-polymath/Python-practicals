# 3.4 Write a python program to append data to an existing file 'python.py'. Read data to be appended
# from the user. Then display the contents of entire file.

string = input("Enter data to be appended : ")

file = open("file.txt")
data = file.read()
data = data + "\n" + string
file.close()

with open("file.txt", "w") as file:
    file.write(data)

print(data)
