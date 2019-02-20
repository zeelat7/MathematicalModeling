import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

cost = np.array([9,2,3,4,2,5,9,10])
                
num_widg = np.array([85,52,55,68,67,86,83,73])

plt.xlabel('Cost')
plt.ylabel('Number of Widgets')
plt.title ('Midterm #1')

plt.scatter(cost,num_widg)

slope, intercept, r_value, p_value, std_err = stats.linregress(cost,num_widg)

print('The slope of the least squares line is')
print(slope) 

print('The y-intercept of the least squares line is')
print(intercept)

y = slope*cost +intercept

plt.plot(cost,y)
plt.show()