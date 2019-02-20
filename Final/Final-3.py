import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy
from numpy import *

#Plot to show the two separate lines
x1=arange(0,28.0,0.001)
x2=arange(28.0,100.1,0.001)
y=arange(0,100.1,0.001)

y1= 50 + 2.85*x1 + 0.6519*x1**2 + 0.00804*x1**3
y2= -1097 + 68.9*x2

xlim(0,60)
ylim(0,1000)

xlabel('Days')
ylabel('Weight in Grams')
title('Final Number 3')

plot(x1,y1,'r')
plot(x2,y2,'b')

legend(['50 + 2.85x + 0.6519x^2 + 0.00804x^3','-1097 + 68.9x'])
show()

#Plot to show the two lines together
figure()
def W(x):

	if x <= 28:
		return 50 + 2.85*x + 0.6519*x**2 + 0.00804*x**3
	else:
		return -1097 + 68.9*x

x=arange(0,100.1,0.1)
y=arange(0,100.1,0.1)

vW = np.vectorize(W)

xlim(0,60)
ylim(0,1000)

y = vW(x)

xlabel('Days')
ylabel('Weight in Grams')
title('Final Number 3')

plot(x,y)
show()