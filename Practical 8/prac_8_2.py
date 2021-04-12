''' 8.2 Write a Python Program to plot sin and cosine wave in the
same figure using subplot() '''

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,6*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

plt.title('Plot of sin and cos')
plt.ylabel('sin(x) and cos(x)')
plt.plot(x,y,x,z)
plt.show()
