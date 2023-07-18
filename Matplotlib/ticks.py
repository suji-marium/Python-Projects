from pylab import *

x=[5,10,15,20,25,30]
y=[2,12,4,10,8,6]
plot(x,y)

xticks(arange(0,31,5))
yticks(arange(0,14,2))
tick_params(axis="y",colors="red",rotation=45)
show()
