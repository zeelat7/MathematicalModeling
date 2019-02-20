import numpy as np
from matplotlib.pyplot import *
import numpy
from numpy import *

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

