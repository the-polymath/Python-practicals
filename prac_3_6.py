# Write a python program that reads a text file containing full-name of the
# employees of a company and then from these names it extracts Last-name of employee
# and stores them in sorted order in new file. Input Text file contains names in format: First-name Middle-name Last-name


def file_write(lst):
    with open("Employee_names.txt","w") as fp:
        for names in lst:
            surname = names + "\n"
            fp.write(surname)
            print(names)




file = open("employees.txt")
lst =[]
for lines in file:
    lines.rstrip()
    names = lines.split()
    lst.append(names[2])

file.close()

file_write(lst)
