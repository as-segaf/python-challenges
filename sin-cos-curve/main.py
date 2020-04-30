#!/usr/bin/python3.8

import numpy as np
import matplotlib.pyplot as plt


degree = np.arange(-360,361)
x = np.arange(-360,361)
y = np.sin(degree * np.pi/180)
z = np.cos(degree * np.pi/180)
plt.plot(x,y,x,z)
plt.xlabel("degree")
plt.ylabel("value")
plt.title("Sin Cos Curve")
plt.legend(['sin(x)', 'cos(x)'])
plt.show()