# MSPA 400 Session 8 Python Module #2

# Reading assignment:
# "Think Python" 2nd Edition Chapter 11 (11.1-11.8)
# "Think Python" 3rd Edition Chapter 11 (pages 121-132)

# Module #2 objectives:  1)  demonstrate how to handle negative areas with
# numerical integration, 2) plot results using Python fill_between, and 3)
# demonstrate the use of an inequality for plotting different colors.

import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import *

# Function from Lial Section 15.4 Example 6

def f(x):
    f = x*x-2.0*x     #Students can supply a function at this point.
    return f
    

def integrate(a,b,n):
    sum = 0.0
    delta = (b-a)/n
    i = 0
    while i < n:
        sum = sum + delta*(f(a+delta*(i+1))+f(a+delta*i))/2
        i = i+1
    return sum
        
#This defines the parameters for integration.

c = 2.0
b = 0.0
a = -1.0
n=100

# One area is negative and the other is positive.  We integrate them separately
# and combine their absolute values.

area1 = integrate(a,b,n)
area2 = integrate(b,c,n)
area =  abs(area1)+np.abs(area2)

print "Final Estimate of Area= %r" %area

# The next section of code shows how to plot different colors by
# dividing the interval based on which area is negative.

x = arange(-1.0,2.1,0.1)    # This defines the interval for the color red.
y = f(x)

plot(x,y,c='k') 
ymin=min(y)-0.5 
ymax=max(y)+0.5

fill_between(x,0.0,y,where= y < 0.0, facecolor = 'y',interpolate=True) 
fill_between(x,0.0,y,where= y > 0.0, facecolor = 'g', interpolate=True) 
xlim(-2.0,4.0)
ylim(ymin-0.5,ymax+2.5)
xlabel('x-axis')
ylabel('y-axis')
title('Plot Showing Color Coded Integration Areas')

x=arange(-1.5,3.6,.1) 
y=f(x)
z=0.0*x

u=0.0*y 
plot(x,y,c='k') 
plot(x,z,u,y,c='b') 
show()


# Assignment #1: Refer to Lial Section 15.4 Exercise 42.  Modify the code
# to reproduce the plot shown in the exercise.  Compare to the answer sheet.


