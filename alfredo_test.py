import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('health-index-1.csv')

baltijos_saliu_indeksai = df.loc[(df['country'] == 'Lithuania') | (df['country'] == 'Latvia') | (df['country'] == 'Estonia')]

#print(baltijos_saliu_indeksai)

baltijos_saliu_indeksu_vidurkiai = baltijos_saliu_indeksai.groupby('country')['value'].mean()

#print(baltijos_saliu_indeksu_vidurkiai)




#print(df)

plt.figure(figsize= (12, 8))
plt.baltijos_saliu_indeksu_vidurkiai
plt.title('Baltijos saliu vidurkiai')
plt.xlabel('xxx')
plt.ylabel('yyy')
plt.show()



