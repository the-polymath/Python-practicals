''' 4.10 Create a class student with following member attributes: roll no, name, age and total marks.
Create suitable methods for reading and printing member variables. Write a python program to
overload ‘==’ operator to print the details of students having same marks. '''

class student:
    def __init__(self, roll, name, age, total):
        self.roll = roll
        self.name = name
        self.age = age
        self.total = total

    def __eq__(self, o):
        if self.total == o.total:
            print("These students have same marks : \n")
            self.printing()
            o.printing()

    def printing(self):
        print("\n------Student-------\n")
        print("Roll No. : ", self.roll)
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Total Marks : ", self.total, end="\n")


s1 = student(18, "Raj", 21, 50)
s2 = student(16, "deep", 22, 50)

s1 == s2
