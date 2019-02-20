import matplotlib.pyplot as plt

team = ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 
        'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 
        'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WHN']

win_perc = [0.420, 0.388, 0.547, 0.558, 0.645, 0.482, 0.420, 0.577, 0.478, 0.540, 
            0.536, 0.522, 0.446, 0.565, 0.489, 0.424, 0.367, 0.529, 0.526, 0.429, 
            0.449, 0.493, 0.413, 0.507, 0.536, 0.533, 0.424, 0.597, 0.558, 0.587]

home_runs = [152, 99, 218, 175, 170, 143, 144, 168, 177, 182, 173, 125, 141, 167, 
            113, 158, 172, 189, 152, 143, 137, 129, 156, 188, 112, 201, 182, 187, 
            198, 181]


plt.scatter(home_runs, win_perc)


xlab = "Number of Home Runs"
ylab = "Winning Percentage"
title = "Home Runs and Winning Percentage Correlation"


plt.xlabel(xlab)
plt.ylabel(ylab)

plt.title(title)

plt.show()