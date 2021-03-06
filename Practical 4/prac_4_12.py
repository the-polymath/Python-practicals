''' 4.11 Write a Python program to create class GTU with attributes like class variable cnt,
instance variables x and y, instance methods get_value and print_value.'''

cnt = 0
class GTU:
    cnt = 0

    def get_value(self, x, y):
        self.x = x
        self.y = y
        global cnt
        cnt += 1

    def print_value(self):
        print("\nCount : ", cnt)
        print("X : ", self.x)
        print("Y : ", self.y)


gtu1 = GTU()
x = int(input("Enter X : "))
y = int(input("Enter y : "))
gtu1.get_value(x, y)
gtu1.print_value()
gtu2 = GTU()
x = int(input("Enter X : "))
y = int(input("Enter y : "))
gtu2.get_value(x, y)
gtu2.print_value()
