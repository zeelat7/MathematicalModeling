import pulp
from pulp import *

# declare your variables
x1 = LpVariable("x1", 0, None) # x1>=0
x2 = LpVariable("x2", 0, None) # x2>=0
x3 = LpVariable("x3", 0, None) # x3>=0
 
# defines the problem
prob = LpProblem("problem", LpMinimize)
 
# defines the constraints
prob += 4*x1 + 1*x2 + 10*x3 >= 10
prob += 3*x1 + 2*x2 + 1*x3 >= 12
prob += 4*x2 + 5*x3 >= 20
 
# defines the objective function to minimize
prob += 40*x1 + 50*x2 + 10*x3
 
# solve the problem
status = prob.solve()
LpStatus[status]

min_cost = 40*(value(x1)) + 50*(value(x2)) + 10*(value(x3))

# print the results
print('The amount to order package 1 per week is')
print(value(x1))

print('The amount to order package 2 per week is')
print(value(x2))

print('The amount to order package 3 per week is')
print(value(x3))

print('The minimum cost in dollars is')
print(min_cost)