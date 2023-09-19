import math
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

# Get 80% of the laps per race

race_subset = pd.DataFrame()

for race in set(lap_times['raceId']):
    race_subset = pd.concat([race_subset, lap_times.loc[(lap_times['raceId'] == race) & (lap_times['lap'] <=
                                                      math.floor(max(lap_times.loc[(lap_times['raceId'] ==
                                                                                    race)]['lap'])) * 0.8)]],
                          axis=0)

# Who held 1st the longest
p1 = race_subset.loc[(lap_times['position'] == 1)]

first = p1.groupby(['raceId', 'driverId'])['raceId'].count()
print(first)


# top five sustained fastest laps
top5 = race_subset.loc[(lap_times['position'] <= 5)]
first = p1.groupby(['raceId', 'driverId'])['raceId'].count()
print(first)


