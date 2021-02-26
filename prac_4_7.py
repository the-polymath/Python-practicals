# 4.7 Create a class Employee with data members: name, department and salary. Create
# suitable methods for reading and printing employee information.

class Employee:
    def reading(self):
        name = input("Enter employee's name : ")
        department = input("Enter employee's Department : ")
        salary = int(input("Enter employee's salary : "))
        self.name = name
        self.department = department
        self.salary = salary

    def printing(self):
        print("Name : ", self.name)
        print("Department : ", self.department)
        print("Salary : ", self.salary)

print("------Employee-1------", end="\n")
e1 = Employee()
e1.reading()
print("\n------Employee-2------", end="\n")
e2 = Employee()
e2.reading()

print("\n------Employee-1------", end="\n")
print(e1.printing())
print("\n")
print("\n------Employee-2------", end="\n")
print(e2.printing())
