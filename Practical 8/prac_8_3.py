#
import numpy as np
import matplotlib.pyplot as plt


def bar(grade, students):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(grade, students)
    plt.show()

def pie(grade, students):
    fig, ax = plt.subplots()
    ax.pie(students, labels=grade)
    ax.axis('equal')
    ax.set_title(' Grades ')
    plt.show()


grade = ["AA", "BB", "CC", "DD"]
students = []
for i in grade:
    print("Enter the no. of students of", i, " grade : ")
    temp = int(input())
    students.append(temp)

bar(grade, students)
pie(grade, students)
