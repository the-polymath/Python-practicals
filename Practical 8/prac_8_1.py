''' Write a Python program to plot following Equation using PyPlot
Y= 5*x + 1 '''

import matplotlib.pyplot as plt

fig = plt.figure(figsize = (10, 5))

x = []
y = []
for i in range(-50, 50):
    x.append(i)
    y.append((5*i) + 1)


plt.plot(x, y)
plt.show()
