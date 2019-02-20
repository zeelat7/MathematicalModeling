import numpy as np
import matplotlib.pyplot as plt

time = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
                25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,
                46,47,48])
                
win_prob = np.array([49.4, 49.3, 49.2, 45.1, 42.3, 48.7, 43.1, 42.8, 42.5, 40.5, 40.3, 44.4,
                    63.7, 57.6, 66.5, 64.4, 71, 73.5, 72, 77, 81.8, 86, 77.5, 75.4,
                    79, 70.9, 82.1, 82.7, 89.5, 93.3, 88.7, 93.2, 95.9, 97.7, 99.1, 98.6,
                    99.6, 99.8, 99.7, 99.7, 100, 100, 100, 100, 100, 100, 100, 100])

plt.xlabel('Time in Minutes')
plt.ylabel('Probability of Winning')
plt.scatter(time,win_prob)
plt.plot(time, win_prob)

plt.title ('Game Winning Probability Bulls vs. Knicks')
plt.show()