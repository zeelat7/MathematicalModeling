import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy
from numpy import *
import pulp
from pulp import *


# declare your variables
x1 = LpVariable("x1", 0, None) # x1>=0
x2 = LpVariable("x2", 0, None) # x2>=0

 
# defines the problem
prob = LpProblem("problem", LpMinimize)
 
# defines the constraints
prob += 1*x1 + 1*x2 <= 6
prob += 1*x1 + 1*x2 >= 3
prob += 1*x1 - 1*x2 <= -3
 
# defines the objective function to minimize
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