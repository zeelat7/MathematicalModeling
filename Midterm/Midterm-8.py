import pulp
from pulp import *

# declare your variables
x1 = LpVariable("x1", 0, None) # x1>=0
x2 = LpVariable("x2", 0, None) # x2>=0
x3 = LpVariable("x3", 0, None) # x3>=0

 
# defines the problem
prob = LpProblem("problem", LpMaximize)
 
# defines the constraints
prob += 0.16*x1 + 0.5*x2 + 0.84*x3 <= 100
prob += 0.84*x1 + 0.5*x2 + 0.16*x3 <= 140

 
# defines the objective function to maximize
prob += 1.0*x1 + 2.0*x2 + 3.80*x3
 
# solve the problem
status = prob.solve()
LpStatus[status]
 
rev = 1.0*value(x1) + 2.0*value(x2) + 3.80*(value(x3))
 
# print the results
print('Liters of Drink 1 to make in order to maximize revenue is')
print(value(x1))

print('Liters of Drink 2 to make in order to maximize revenue is')
print(value(x2))

print('Liters of Drink 3 to make in order to maximize revenue is')
print(value(x3))


print("Actual Revenue is")
print(rev)