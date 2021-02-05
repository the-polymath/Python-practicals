# 4.2 Write a python program which will throw an exception if any I/O related errors using files.
try:
    handle = input()
    file = open(handle)
    for line in file:
        print(line)

except:
    print("File related error!")


'''
except Exception as e:
    print(e)
    '''
