# 2.3 Write a program to convert a list of characters into a string
def strjoin(lst):
    string = "".join(lst)
    return string

ch = []
while(True):
    sh = input()
    if len(sh) < 1:
        break
    else:
        ch.append(sh)

string = strjoin(ch)
print(string)
