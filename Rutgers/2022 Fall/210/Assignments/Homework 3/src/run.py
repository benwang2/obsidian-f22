import pandas as pd

f = pd.read_csv("./data/EuCitiesTemperatures.csv")
f[['latitude','longitude']] = f[['latitude','longitude']].fillna(f.groupby('country')[['latitude','longitude']].transform('mean'))

# combined = pd.concat(f[f['longitude'] >= 15], f[f['longitude'] <= 30])
lon_gte15 = f[f['longitude'] >= 15]
lon_lte30 = f[f['longitude'] <= 30]

lat_gte40 = f[f['latitude'] >= 40]
lat_lte60 = f[f['latitude'] <= 60]


lon_in_range = pd.merge(lon_gte15, lon_lte30, how='inner')
lat_in_range = pd.merge(lat_gte40, lat_lte60, how='inner')
subset = pd.merge(lon_in_range, lat_in_range, how='inner')
print(subset)

# print( type((15 <= f['longitude']) & (f['longitude'] < 30)) )
# f['longitude'].between(15, 30, inclusive=True)
