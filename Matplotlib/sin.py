from matplotlib import pyplot as plt
import numpy as np
import math

x=np.arange(0,math.pi*2,0.05)
y=np.sin(x)
plt.title("sin wave")
plt.xlabel("angle")
plt.ylabel("sine")
plt.plot(x,y)
plt.show()
