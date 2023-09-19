"""
Formula one data analysis

Correlation of gird nad/or fastest lap time to position within top 5
Average lap time at each circuit over the years of top 5 (circuit ids: 14, 6, 13, 7, 22)
Performance of given constructor during time in Formula 1, i.e. number of wins etc.
Top performing driver on a 5-year rolling basis



"""


import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import cycle


cycol = cycle('bgrcmk')

race_results = pd.read_csv('./Data/results.csv', sep=',')
races = pd.read_csv('./Data/races.csv', sep=',')
circuits = pd.read_csv('./Data/circuits.csv', sep=',')
lap_times = pd.read_csv('./Data/lap_times.csv', sep=',')

race_results = race_results[race_results['position'] != '\\N']
race_results['position'] = race_results['position'].astype(int)
winners = race_results[race_results['position'] <= 20]

numerc_colmns = ['constructorId', 'position', 'grid', 'laps', 'fastestLap', 'fastestLapTime', 'fastestLapSpeed']
cols = ['position', 'grid']
corretn_matrx = winners.loc[:, cols].corr()

avgTimes = pd.DataFrame(lap_times.groupby('raceId').agg(avg_laptime=('milliseconds', np.mean)))
# races['averge_laptime'] = lap_times.groupby('raceId').agg(avg_laptime=('milliseconds', np.mean))['avg_laptime']
mergedRaces = pd.merge(races, avgTimes, on="raceId", how="inner")

top_5 = [14, 6, 13, 7, 22]
top_circuits = mergedRaces[mergedRaces['circuitId'].isin(top_5)]
tsLapTime = top_circuits[["year", "name", "avg_laptime"]]
tsLapTime.sort_values(by=['name', 'year'])


sorLapTimes = tsLapTime.sort_values(by=['name', 'year'])

fig, axs = plt.subplots(5)
fig.suptitle('Vertically stacked subplots')
count = 0


for f in set(sorLapTimes["name"]):
    curr = sorLapTimes[sorLapTimes["name"] == f]
    axs[count].set_title(f)
    axs[count].plot(curr['year'], curr['avg_laptime'], c=next(cycol))
    count += 1

#plt.show()



# Print the correlation matrix.
print(corretn_matrx)
# Pass the above correlation matrix and annot = True as the arguments to the heatmap() function
# to visualize the above correlation matrix
#sns.heatmap(corretn_matrx)
#plt.show()
#%%
