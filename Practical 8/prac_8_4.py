import matplotlib.pylab as plt

fig = plt.figure(figsize = (10, 5))

x_temp = input("Enter the values of x (space separated) : ")
y_temp = input("Enter the values of y (space separated) : ")

x_temp = x_temp.split(" ")
y_temp = y_temp.split(" ")
x = [int(i) for i in x_temp]
y = [int(i) for i in y_temp]

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot(x, y)
plt.show()
