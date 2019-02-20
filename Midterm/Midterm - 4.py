import pulp
from pulp import *

# declare your variables
x1 = LpVariable("x1", 0, None) # x1>=0
x2 = LpVariable("x2", 0, None) # x2>=0

 
# defines the problem
prob = LpProblem("problem", LpMaximize)
 
# defines the constraints
prob += 0.5*x1 + 0.75*x2 <= 165
prob += 0.5*x1 + 0.25*x2 <= 93

 
# defines the objective function to maximize
prob += 8.25*x1 + 7.50*x2
 
# solve the problem
status = prob.solve()
LpStatus[status]
 
rev = 8.25*value(x1) +7.50*value(x2)
 
# print the results
print('kgs that are for 0.5 rye grass and 0.5 bluegrass mix')
print(value(x1))

print('kgs that are for 0.75 rye grass and 0.25 bluegrass mix')
print(value(x2))

print("Actual Revenue is")
print(rev)