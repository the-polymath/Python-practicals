# 3.1 Create a Python program to read a text file and do following:
# I. Print no. of lines
# II. Print no. of unique words
# III. Store each word with its occurrence in dictionary

file = open("file.txt",'r')
count = 0
dic = {}
for lines in file:
    count += 1
    lines.rstrip()
    words = lines.split()
    for word in words:
        dic[word] = dic.get(word, 0) + 1

print("total Number of lines in file are:", count)
print("total Number of distinct words are:", len(dic))
print("distinct words are:\n")
for key, values in dic.items():
    print(key,":", values)
