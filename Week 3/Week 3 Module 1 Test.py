import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import arange

# Exercise: Refer to Lial Section 3.1 page 118. Write the code to reproduce
# Figure 10.  Compare your code and the resulting plot to the answer sheet.

figure()

x = arange(-10,10.1,1)

y1= 12.0 - 2.0*x
y2= 6.0 - 0.5*x

xlim(-10, 10)
ylim(-10, 10)

xlim(0,10)
ylim(0,10)
xlabel('x-axis')
ylabel('y-axis')

plot(x,y1, c='r', label='y=12-2x')
plot(x,y2, c='b', label='y=6-0.5x') 
legend(['y=12-2*x','y=6-0.5x'],loc='best') 

fill_between(x,y2,where=(y2<=y1), color= 'b')
fill_between(x,y1,where=(y1<=y2), color= 'b') 

title ('Shaded Area Shows the Feasible Region') 
show()