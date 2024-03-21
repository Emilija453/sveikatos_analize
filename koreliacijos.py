# - ryšys tarp bendro indekso (vidurkio) ir metu
# - ryšys tarp Baltijos šalių indekso (vidurkio) ir metu
# - ryšys tarp Skandinavijos šalių indekso (vidurkio) ir metu

import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 500)

df = pd.read_csv('health-index-1.csv')

bendrakoreliacija = df['year'].corr(df['value']).round(2)
print('Visų šalių sveikatos indekso priklausomybė nuo metų: ', bendrakoreliacija)

baltijos_saliu_indeksai = df.loc[(df['country'] == 'Lithuania') | (df['country'] == 'Latvia') | (df['country'] == 'Estonia')]
baltijos_saliu_koreliacija = baltijos_saliu_indeksai['year'].corr(baltijos_saliu_indeksai['value']).round(2)
print('Baltijos šalių sveikatos indekso priklausomybė nuo metų: ', baltijos_saliu_koreliacija)

skandinavijos_saliu_indeksai = df.loc[(df['country'] == 'Sweden') | (df['country'] == 'Norway') | (df['country'] == 'Finland')]
skandinavijos_saliu_koreliacija = skandinavijos_saliu_indeksai['year'].corr(skandinavijos_saliu_indeksai['value']).round(2)
print('Skandinavijos šalių sveikatos indekso priklausomybė nuo metų: ', skandinavijos_saliu_koreliacija)
