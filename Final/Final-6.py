import matplotlib.pyplot 
from matplotlib.pyplot import *
from scipy.misc import derivative
import numpy 
from numpy import poly1d, linspace

#show the derivative of the formula

p=poly1d([1.603, -23.258, 62.12, 6.992, 1010])
print ('Number 6 Degree Polynomial') 
print p 

print ('\nFirst Derivative')
h= p.deriv(m=1)  # First derivative with m=1.
print h

def f(x):
    return 1.603*x**4 - 23.258*x**3 + 62.12*x**2 + 6.992*x + 1010

#evaluate the derivative at within the interval [0:7]
for i in range(8):
    print(derivative(f,i, dx = 1e-6))

print('Rent is increasing most rapidly during year 1 or 1999, at')
print(derivative(f,1.0, dx = 1e-6))
