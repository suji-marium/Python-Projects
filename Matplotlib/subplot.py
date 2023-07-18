from pylab import *
from numpy import *
from math import pi

x=arange(0,pi*2,0.05)
subplot(2,2,1)
plot(x,sin(x),("r-"),label="sin")
legend(loc="upper right")

subplot(2,2,2)
plot(x,cos(x),("g--"),label="cos")
legend(loc="upper right")

subplot(2,2,3)
plot(x,-sin(x),label="-sin")
legend(loc="upper right")

subplot(2,2,4)
plot(x,tan(x),("y-"),label="tan")
legend(loc="upper right")
show()
