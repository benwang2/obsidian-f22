import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Setup
temps = pd.read_csv("./data/EuCitiesTemperatures.csv")

# Preprocessing
## Part 1
temps[['latitude','longitude']] = temps[['latitude','longitude']].fillna(temps.groupby('country')[['latitude','longitude']].transform('mean'))

## Part 2
lon_gte15 = temps[temps['longitude'] >= 15]
lon_lte30 = temps[temps['longitude'] <= 30]
lat_gte40 = temps[temps['latitude'] >= 40]
lat_lte60 = temps[temps['latitude'] <= 60]

lon_in_range = pd.merge(lon_gte15, lon_lte30, how='inner')
lat_in_range = pd.merge(lat_gte40, lat_lte60, how='inner')
subset = pd.merge(lon_in_range, lat_in_range, how='inner')

city_count = subset.value_counts(['country'])
maximal_cities = city_count[city_count == city_count.max()]

## Part 3
temps['temperature'] = temps['temperature'].fillna(temps.groupby(['EU','coastline'])['temperature'].transform('mean'))

# Visualization
## Part 1
grouped_types = temps.groupby(['EU','coastline'])
regiontype_groups = [f"EU={g[0]},CL={g[1]}" for g in grouped_types.groups]
regiontype_values = [len(grouped_types.get_group(g)) for g in grouped_types.groups]

# plt.bar(regiontype_groups, regiontype_values)
# plt.show()

## Part 2
# plt.scatter(
#     temps['latitude'],
#     temps['longitude'],
#     6,
#     [hash(country) for country in temps['country']]
# )
# plt.show()

## Part 3
population_count = temps['population'].unique()
country_to_population = [temps['country'][temps['population'] == pop].head(1).values[0] for pop in population_count]
print(country_to_population)