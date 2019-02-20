import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy
from numpy import *
import pulp
from pulp import *

x=arange(0,100.1,0.1)
y=arange(0,100.1,0.1)

y1= -1*x + 10.0
y2= -1*x + 3.0
y3= 1*x - 3.0
y4 = (-2.0/3.0)*x + (47.0/6.0)

xlim(0,15)
ylim(0,15)

xlabel('x-axis')
ylabel('y-axis')
title('Final Number 1')

plot(x,y1,'r')
plot(x,y2,'b')
plot(x,y3,'g')
plot(x,y4,'--')

legend(['x+y <= 10','x+y >= 3', 'y-x <= -3 ','y = -2/3x + 47/6'])

x= [3, 6.5, 10]
y= [0, 3.5, 0]
fill(x,y, color='grey', alpha=0.2)
show()

# declare your variables
x1 = LpVariable("x1", 0, None) # x1>=0
x2 = LpVariable("x2", 0, None) # x2>=0

 
# defines the problem
prob = LpProblem("problem", LpMaximize)
 
# defines the constraints
prob += 1*x1 + 1*x2 <= 10
prob += 1*x1 + 1*x2 >= 3
prob += 1*x1 - 1*x2 <= -3
 
# defines the objective function to maximize
prob += 4*x1 + 6*x2 
 
# solve the problem
status = prob.solve()
LpStatus[status]

max_amt = 4*(value(x1)) + 6*(value(x2)) 

# print the results
print('x1 is')
print(value(x1))

print('x2 is')
print(value(x2))

print('The max amount is')
print(max_amt)