import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy as np
from numpy import poly1d, linspace

def d(x):
    return 4.0*np.log((x+5.0)/6.0)+2.5

def Dd(x):
    return 4.0/(x+5.0)

x=linspace(-30,30,10000)
y=d(x)
yg=Dd(x)  # These statements define points for plotting.

y0=0*x   # This statement defines the y axis for plotting.

plot (x,y,label ='y=d(x)')
plot (x,yg,label ='Derivative of d(x)')
legend(loc='best')

ylim(-20,20)

plot (x,y0)
xlabel('Dosage (mg)')
ylabel('Body Temperature (C)')
title ('Final Number 9')
show()

