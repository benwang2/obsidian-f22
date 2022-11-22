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

# lat_city = [temps[['latitude','longitude']][temps.city == c].values[0] for c in temps['city']]
# lon_city = [temps['longitude'][temps.city == c].values[0] for c in temps['city']]

# def get_cmap(n, name='hsv'):
#     '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
#     RGB color; the keyword argument name must be a standard mpl colormap name.'''
#     return plt.cm.get_cmap(name, n)

countries = [c for c in temps['country']]
lat_city = []
lon_city = []
clr_city = []
for (lat, lon, country) in temps[['latitude','longitude','country']].iloc(0):
    # print(lat, lon, country)
    lat_city.append(lat)
    lon_city.append(lon)
    clr_city.append(plt.cm.get_cmap('hsv', hash(country)))

plt.scatter(lat_city, lon_city, 6, clr_city)
plt.show()