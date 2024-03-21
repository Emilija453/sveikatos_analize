import pandas as pd

df = pd.read_csv('health-index-1.csv')
# print(df)

### Skandinavijos šalys

skandinavijos_salys = df.loc[(df['country'] == 'Denmark') | (df['country'] == 'Sweden') | (df['country'] == 'Norway')]
# print(skandinavijos_salys)

periodas_1980_1985 = skandinavijos_salys[(skandinavijos_salys['year'] >= 1980) & (skandinavijos_salys['year'] <= 1985)]
# print(periodas_1980_1985)

saliu_indekso_vidurkis_1980_1985 = periodas_1980_1985.groupby('country')['value'].mean()
print(saliu_indekso_vidurkis_1980_1985)