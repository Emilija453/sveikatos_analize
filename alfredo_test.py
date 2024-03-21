import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('health-index-1.csv')

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



