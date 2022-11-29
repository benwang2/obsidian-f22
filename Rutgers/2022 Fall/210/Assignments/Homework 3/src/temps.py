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
regiontype_names = [f"EU={g[0]}\nCoastline={g[1]}" for g in grouped_types.groups]
regiontype_values = [len(grouped_types.get_group(g)) for g in grouped_types.groups]

# plt.xlabel("Region type")
# plt.ylabel("Number of cities")
# plt.bar(regiontype_names, regiontype_values)
# plt.show()

## Part 2
# plt.scatter(
#     temps['latitude'],
#     temps['longitude'],
#     6,
#     [hash(country) for country in temps['country']]
# )
# plt.xlabel("Latitude")
# plt.ylabel("Longitude")
# plt.show()

## Part 3
# plt.hist(temps['population'].unique(), bins=5)
# plt.xlabel("Population of country")
# plt.ylabel("Frequency")
# plt.show()

## Part 4

def get_color(t):
    if t < 6:
        return "blue"
    elif t > 10:
        return "red"
    else:
        return "orange"

fig, axs = plt.subplots(2, 2, constrained_layout=True)
for i, index in enumerate(grouped_types.groups):
    ax = axs.flat[i]
    row = grouped_types.get_group(index)
    # fig.add_subplot(2,2,i+1)
    # axs[i].title(
    #     ("EU" if index[0] == "yes" else "Non-EU") + " " +
    #     ("Coastline" if index[1] == "yes" else "Other")
    # ) 
    ax.scatter(
        row["city"],
        row["latitude"],
        4,
        [get_color(t) for t in row["temperature"]]
    )
    ax.set_xticks([i for i in range(len(row) - 1)])
    
fig.supxlabel("Latitude")
fig.supylabel("Longitude")
plt.show()