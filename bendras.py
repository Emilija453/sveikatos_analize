# bendras (visų šalių) indekso vidurkis periodais
# (1980-1985, 1990-1995, 2000-2005, 2010-2013) - 4 periodų duomenys

import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

df = pd.read_csv('health-index-1.csv')

# 1980-1985
years_1980_1985 = df[(df['year'] >= 1980) & (df['year'] <= 1985)]

median_1980_1985 = years_1980_1985['value'].mean()
print(f'\nVidutinis HDI 1980-1985 metais: {median_1980_1985}')

median_by_country_1980_1985 = years_1980_1985.groupby('country')['value'].mean()

top_five_1980_1985 = median_by_country_1980_1985.nlargest(5)
worst_five_1980_1985 = median_by_country_1980_1985.nsmallest(5)

print(f'\nAukščiausi HDI 1980-1985 metais:\n{top_five_1980_1985}')
print(f'\nŽemiausi HDI 1980-1985 metais:\n{worst_five_1980_1985}')


# 1990-1995
years_1990_1995 = df[(df['year'] >= 1990) & (df['year'] <= 1995)]

median_1990_1995 = years_1990_1995['value'].mean()
print(f'\nVidutinis HDI 1990-1995 metais: {median_1990_1995}')

median_by_country_1990_1995 = years_1990_1995.groupby('country')['value'].mean()

top_five_1990_1995 = median_by_country_1990_1995.nlargest(5)
worst_five_1990_1995 = median_by_country_1990_1995.nsmallest(5)

print(f'\nAukščiausi HDI 1990-1995 metais:\n{top_five_1990_1995}')
print(f'\nŽemiausi HDI 1990-1995 metais:\n{worst_five_1990_1995}')


# 2000-2005
years_2000_2005 = df[(df['year'] >= 2000) & (df['year'] <= 2005)]

median_2000_2005 = years_2000_2005['value'].mean()
print(f'\nVidutinis HDI 2000-2005 metais: {median_2000_2005}')

median_by_country_2000_2005 = years_2000_2005.groupby('country')['value'].mean()

top_five_2000_2005 = median_by_country_2000_2005.nlargest(5)
worst_five_2000_2005 = median_by_country_2000_2005.nsmallest(5)

print(f'\nAukščiausi HDI 2000-2005 metais:\n{top_five_2000_2005}')
print(f'\nŽemiausi HDI 2000-2005 metais:\n{worst_five_2000_2005}')


# 2010-2013
years_2010_2013 = df[(df['year'] >= 2010) & (df['year'] <= 2013)]

median_2010_2013 = years_2010_2013['value'].mean()
print(f'\nVidutinis HDI 2010-2013 metais: {median_2010_2013}')

median_by_country_2010_2013 = years_2010_2013.groupby('country')['value'].mean()

top_five_2010_2013 = median_by_country_2010_2013.nlargest(5)
worst_five_2010_2013 = median_by_country_2010_2013.nsmallest(5)

print(f'\nAukščiausi HDI 2010-2013 metais:\n{top_five_2010_2013}')
print(f'\nŽemiausi HDI 2010-2013 metais:\n{worst_five_2010_2013}')

### Skandinavijos šalys

skandinavijos_salys = df.loc[(df['country'] == 'Denmark') | (df['country'] == 'Sweden') | (df['country'] == 'Norway')]
# print(skandinavijos_salys)

periodas_1980_1985 = skandinavijos_salys[(skandinavijos_salys['year'] >= 1980) & (skandinavijos_salys['year'] <= 1985)]
# print(periodas_1980_1985)

saliu_indekso_vidurkis_1980_1985 = periodas_1980_1985.groupby('country')['value'].mean()
print(f'Skandinavijos šalių indekso vidurkis 1980 - 1985 m.laikotarpiu :\n{saliu_indekso_vidurkis_1980_1985}')

periodas_1990_1995 = skandinavijos_salys[(skandinavijos_salys['year'] >= 1990) & (skandinavijos_salys['year'] <= 1995)]
# print(periodas_1990_1995)

saliu_indekso_vidurkis_1990_1995 = periodas_1990_1995.groupby('country')['value'].mean()
print(f'Skandinavijos šalių indekso vidurkis 1990 - 1995 m.laikotarpiu :\n{saliu_indekso_vidurkis_1990_1995}')

periodas_2000_2005 = skandinavijos_salys[(skandinavijos_salys['year'] >= 2000) & (skandinavijos_salys['year'] <= 2005)]
# print(periodas_2000_2005)

saliu_indekso_vidurkis_2000_2005 = periodas_2000_2005.groupby('country')['value'].mean()
print(f'Skandinavijos šalių indekso vidurkis 2000 - 2005 m.laikotarpiu :\n{saliu_indekso_vidurkis_2000_2005}')

periodas_2010_2013 = skandinavijos_salys[(skandinavijos_salys['year'] >= 2010) & (skandinavijos_salys['year'] <= 2013)]
# print(periodas_2010_2013)

saliu_indekso_vidurkis_2010_2013 = periodas_1990_1995.groupby('country')['value'].mean()
print(f'Skandinavijos šalių indekso vidurkis 2010 - 2013 m.laikotarpiu :\n{saliu_indekso_vidurkis_2010_2013}')

"KORELIACIJOS"
bendrakoreliacija = df['year'].corr(df['value']).round(2)
print('Visų šalių sveikatos indekso priklausomybė nuo metų: ', bendrakoreliacija)

baltijos_saliu_indeksai = df.loc[(df['country'] == 'Lithuania') | (df['country'] == 'Latvia')
                                 | (df['country'] == 'Estonia')]
baltijos_saliu_koreliacija = baltijos_saliu_indeksai['year'].corr(baltijos_saliu_indeksai['value']).round(2)
print('Baltijos šalių sveikatos indekso priklausomybė nuo metų: ', baltijos_saliu_koreliacija)

skandinavijos_saliu_indeksai = df.loc[(df['country'] == 'Sweden') | (df['country'] == 'Norway')
                                      | (df['country'] == 'Denmark')]
skandinavijos_saliu_koreliacija = (skandinavijos_saliu_indeksai['year'].corr(skandinavijos_saliu_indeksai['value']).
                                   round(2))
print('Skandinavijos šalių sveikatos indekso priklausomybė nuo metų: ', skandinavijos_saliu_koreliacija)


"SVEIKATOS INDEKSŲ POKYČIAI PROC. SU GRAFIKU"
bendras_saliu_pokytis = df.groupby('year')['value'].mean().round(2).pct_change()
baltijos_saliu_pokytis = baltijos_saliu_indeksai.groupby('year')['value'].mean().round(2).pct_change()
skandinavijos_saliu_pokytis = (skandinavijos_saliu_indeksai.groupby('year')['value'].mean().round(2).pct_change()) * 100

plt.figure(figsize=(14, 8))
plt.plot(bendras_saliu_pokytis, label='Visų šalių')
plt.plot(baltijos_saliu_pokytis, label='Baltijos šalių')
plt.plot(skandinavijos_saliu_pokytis, label='Skandinavijos šalių')
plt.title('Sveikatos indekso pokytis pagal metus')
plt.xlabel('Metai')
plt.ylabel('Pokytis proc.')
plt.legend()
plt.show()

baltijos_saliu_indeksai = df.loc[(df['country'] == 'Lithuania') | (df['country'] == 'Latvia') | (df['country'] == 'Estonia')]

#print(baltijos_saliu_indeksai)

baltijos_saliu_indeksu_vidurkiai = baltijos_saliu_indeksai.groupby('country')['value'].mean()

bal_ind_1980_1985 = baltijos_saliu_indeksai[(baltijos_saliu_indeksai['year'] >= 1980) & (baltijos_saliu_indeksai['year'] <= 1985)]
#print(bal_ind_1980_1985)
bal_ind_1990_1995 = baltijos_saliu_indeksai[(baltijos_saliu_indeksai['year'] >= 1990) & (baltijos_saliu_indeksai['year'] <= 1995)]
bal_ind_2000_2005 = baltijos_saliu_indeksai[(baltijos_saliu_indeksai['year'] >= 2000) & (baltijos_saliu_indeksai['year'] <= 2005)]
bal_ind_2010_2013 = baltijos_saliu_indeksai[(baltijos_saliu_indeksai['year'] >= 2100) & (baltijos_saliu_indeksai['year'] <= 2013)]



#print(df)

plt.figure(figsize=(14, 9))
#baltijos_saliu_indeksu_vidurkiai.plot(kind='bar', color='skyblue')
bal_ind_1980_1985.plot(kind='bar', color='red')
plt.title('Baltijos saliu vidurkiai')
plt.xlabel('ŠALYS')
plt.ylabel('Value')
plt.show()
