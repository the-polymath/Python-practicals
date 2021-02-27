# 4.8 Write a Python program to overload + operator.
class add:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a


obj1 = add(int(input("Enter a number : ")))
obj2 = add(int(input("Enter a number : ")))
obj3 = obj1 + obj2
print("Adding numbers using operator overloading", obj3)
print()
o1 = add(input("Enter a string : "))
o2 = add(input("Enter a string : "))
o3 = o1 + o2
print("Adding Strings using operator overloading", o3)
