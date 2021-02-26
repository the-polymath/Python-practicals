# 4.6 Write a Python program to implement the concept of inheritance.

class A:
    def xyz(self):
        print("This is class A ")

    def value(self, num):
        self.num = num
        return self.num


class B(A):
    def xyz(self):
        print("This is Class B")

    def notvalue(self, no):
        self.no = no + 2
        return self.no


class C(B):
    def xyz(self):
        print("This is class C")


a = A()
b = B()
c = C()
a.xyz()
b.xyz()
c.xyz()

print("\nValue() Called using A's object : ", a.value(5))
print("Value() using B's object : ", b.value(10))
print("Value() using C's object : ", c.value(15))
print("notvalue() called using C's object : ", c.notvalue(4))
