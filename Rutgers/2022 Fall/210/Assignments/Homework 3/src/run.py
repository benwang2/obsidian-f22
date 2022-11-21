import pandas as pd

f = pd.read_csv("./data/EuCitiesTemperatures.csv")
f[['latitude','longitude']] = f[['latitude','longitude']].fillna(f.groupby('country')[['latitude','longitude']].transform('mean'))

print(f[60 >= f.longitude])