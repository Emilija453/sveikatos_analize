import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 500)

df = pd.read_csv('health-index-1.csv')

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

bendras_saliu_pokytis = df.groupby('year')['value'].mean().round(2).pct_change()
baltijos_saliu_pokytis = baltijos_saliu_indeksai.groupby('year')['value'].mean().round(2).pct_change()
skandinavijos_saliu_pokytis = (skandinavijos_saliu_indeksai.groupby('year')['value'].mean().round(2).pct_change()) * 100

plt.figure(figsize=(14,8))
plt.plot(bendras_saliu_pokytis, label='Visų šalių')
plt.plot(baltijos_saliu_pokytis, label='Baltijos šalių')
plt.plot(skandinavijos_saliu_pokytis, label='Skandinavijos šalių')

plt.title('Sveikatos indekso pokytis pagal metus')
plt.xlabel('Metai')
plt.ylabel('Pokytis proc.')
plt.legend()
plt.show()
