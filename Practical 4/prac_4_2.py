# 4.2 Write a python program which will throw an exception if any I/O related errors using files.
try:
    handle = input()
    with open(handle) as file:
        print("\nThis is the content of file : \n")
        for line in file:
            print(line)

except OSError as e:
    print(e, "File related error!")
