import pulp
from pulp import *

# declare your variables
x1 = LpVariable("x1", 0, None) # x1>=0
x2 = LpVariable("x2", 0, None) # x2>=0
x3 = LpVariable("x3", 0, None) # x3>=0
 
# defines the problem
prob = LpProblem("problem", LpMaximize)
 
# defines the constraints
prob += 1*x1 + 1*x2 + 0*x3 <= 11
prob += 0*x1 + 0*x2 + 1*x3 <= 6
prob += 1*x1 - 2*x3 >= 0
 
# defines the objective function to maximize
prob += 500*x1 + 900*x2 + 400*x3
 
# solve the problem
status = prob.solve()
LpStatus[status]

max_num = 500*(value(x1)) + 900*(value(x2)) + 400*(value(x3))

# print the results
print('The number of classical concerts to have')
print(value(x1))

print('The number of jazz concerts to have')
print(value(x2))

print('The number of rock concerts to have')
print(value(x3))

print('The maximum number of attendees is')
print(max_num)