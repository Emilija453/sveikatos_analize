# bendras (visų šalių) indekso vidurkis periodais 
# (1980-1985, 1990-1995, 2000-2005, 2010-2013) - 4 periodų duomenys

import pandas as pd

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