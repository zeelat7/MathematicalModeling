import matplotlib.pyplot as plt

team = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 
        'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 
        'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WHN']

win_perc = [0.421, 0.405, 0.536, 0.582, 0.641, 0.474, 0.414, 0.586, 0.477, 0.539, 
            0.529, 0.503, 0.438, 0.569, 0.497, 0.451, 0.359, 0.529, 0.520, 0.434, 
            0.451, 0.500, 0.418, 0.529, 0.526, 0.523, 0.428, 0.588, 0.546, 0.586]

run_diff = [-147, -142, 15, 188, 244, -40, -146, 108, 14, 17, 45, -32, -37, 87, 
            -17, -56, -160, 21, -13, -93, -149, 0, -82, 60, 44, 55, -28, 
            9, 83, 152]


plt.scatter(run_diff, win_perc)


xlab = "Run Differential"
ylab = "Winning Percentage"
title = "Run Differential vs Winning Percentage Correlation"


plt.xlabel(xlab)
plt.ylabel(ylab)

plt.title(title)

plt.show()