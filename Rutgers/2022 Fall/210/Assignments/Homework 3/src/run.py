import pandas as pd

f = pd.read_csv("./data/EuCitiesTemperatures.csv")
f[['latitude','longitude']] = f[['latitude','longitude']].fillna(f.groupby('country')[['latitude','longitude']].transform('mean'))

combined = pd.concat(f[f['longitude'] >= 15], f[f['longitude'] <= 30])
print(combined)

# print( type((15 <= f['longitude']) & (f['longitude'] < 30)) )
# f['longitude'].between(15, 30, inclusive=True)
