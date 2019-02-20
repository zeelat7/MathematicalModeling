import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy
from numpy import *


x=arange(0,100.1,0.1)
y=arange(0,100.1,0.1)

y1= -1*x +35.0
y2= -1*x +20.0
y3= (3.0/2.0)*x
y4 = 0.0*x +10

xlim(0,40)
ylim(0,40)

xlabel('Number of Strategists')
ylabel('Number of Assistants')
title('Midterm Number 5')

plot(x,y1,'b')
plot(x,y2,'r')
plot(x,y3,'y')
plot(x,y4,'g')

legend(['x+y <= 35','x+y >= 20', 'y = 3/2x','y >= 10'])

x= [8, 10, 25, 14]
y= [12, 10, 10, 21]
fill(x,y, color='grey', alpha=0.2)
show()


obj= matrix([2400.0,1100.0])
obj= transpose(obj)
corners= matrix([x,y])
corners= transpose(corners)
result= dot(corners,obj)
print ('Value of Objective Function at Each Corner Point:\n'), result
