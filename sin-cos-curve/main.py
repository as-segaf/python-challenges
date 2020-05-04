#!/usr/bin/python3.8

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-360,360)
y = np.sin(x * np.pi/180)
z = np.cos(x * np.pi/180)
plt.plot(x,y,x,z)
plt.xlabel("degree")
plt.ylabel("value")
plt.title("Sin Cos Curve")
plt.legend(['sin(x)', 'cos(x)'])
plt.show()