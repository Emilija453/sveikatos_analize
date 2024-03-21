import pandas as pd

df = pd.read_csv('health-index-1.csv')
# print(df)

### Skandinavijos šalys

skandinavijos_salys = df.loc[(df['country'] == 'Denmark') | (df['country'] == 'Sweden') | (df['country'] == 'Norway')]
# print(skandinavijos_salys)



periodas_1980_1985 = skandinavijos_salys[(skandinavijos_salys['year'] >= 1980) & (skandinavijos_salys['year'] <= 1985)]
# print(periodas_1980_1985)

saliu_indekso_vidurkis_1980_1985 = periodas_1980_1985.groupby('country')['value'].mean()
# print(f'Skandinavijos šalių indekso vidurkis 1980 - 1985 m.laikotarpiu :\n{saliu_indekso_vidurkis_1980_1985}')



periodas_1990_1995 = skandinavijos_salys[(skandinavijos_salys['year'] >= 1990) & (skandinavijos_salys['year'] <= 1995)]
# print(periodas_1990_1995)

saliu_indekso_vidurkis_1990_1995 = periodas_1990_1995.groupby('country')['value'].mean()
# print(f'Skandinavijos šalių indekso vidurkis 1990 - 1995 m.laikotarpiu :\n{saliu_indekso_vidurkis_1990_1995}')



periodas_2000_2005 = skandinavijos_salys[(skandinavijos_salys['year'] >= 2000) & (skandinavijos_salys['year'] <= 2005)]
# print(periodas_2000_2005)

saliu_indekso_vidurkis_2000_2005 = periodas_2000_2005.groupby('country')['value'].mean()
# print(f'Skandinavijos šalių indekso vidurkis 2000 - 2005 m.laikotarpiu :\n{saliu_indekso_vidurkis_2000_2005}')



periodas_2010_2013 = skandinavijos_salys[(skandinavijos_salys['year'] >= 2010) & (skandinavijos_salys['year'] <= 2013)]
# print(periodas_2010_2013)

saliu_indekso_vidurkis_2010_2013 = periodas_1990_1995.groupby('country')['value'].mean()
# print(f'Skandinavijos šalių indekso vidurkis 2010 - 2013 m.laikotarpiu :\n{saliu_indekso_vidurkis_2010_2013}')