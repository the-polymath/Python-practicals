''' 4.9 Write a Python program that counts the number of occurrences of the character in the given
string. Provide two implementations: recursive and iterative '''

class check:
    def checkrecursive(self, string, ch):
        if not string:
            return 0
        elif string[0] == ch:
            return 1+self.checkrecursive(string[1:], ch)
        else:
            return self.checkrecursive(string[1:], ch)

    def checkiterative(self, string):
        dic = {}
        for i in string:
            count = 0
            for j in string:
                if i == j:
                    count += 1

            dic[i] = count

        return dic

string = input("Enter the string : ")
dic = {}
obj1 = check()
ite = obj1.checkiterative(string)
print("characters using iterative method : ", ite)
for i in string:
    dic[i] = obj1.checkrecursive(string, i)

print("characters using iterative method : ", dic)
