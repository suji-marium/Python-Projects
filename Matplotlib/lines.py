from matplotlib import pyplot as plt 

x1=[2,4,7]
y1=[1,3,8]
plt.plot(x1,y1,label="line1")


x2=[1,4,9]
y2=[5,7,11]
plt.plot(x2,y2,'r-',label='line2')

x3=[2,5,9]
y3=[4,7,9]
plt.plot(x3,y3,'g-',label='line3')

plt.xlabel("X")
plt.ylabel('Y')
plt.title("Lines")

plt.legend(loc="upper right")
plt.show()
