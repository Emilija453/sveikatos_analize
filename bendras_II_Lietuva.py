import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('health-index-1.csv')

label_encoder = LabelEncoder()
df['country_ENCOD'] = label_encoder.fit_transform(df['country'])
salis_vizual = 99
df_salis = df[df['country_ENCOD'] == salis_vizual]
df_filtered_sorted = df_salis.sort_values('year')

X = df_filtered_sorted[['year', 'country_ENCOD']]
y = df_filtered_sorted[['value']]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)



plt.scatter(df_filtered_sorted['year'], df_filtered_sorted['value'], color='blue', label='Mokymo duomenys', s=10)
plt.plot(X_test['year'], y_pred, linestyle='--', marker='o', color='red', label='Prognoze')
plt.xlabel('Metai')
plt.ylabel('Value')
plt.title('Sveikatos indekso prognoze pagal metus - Lietuva')
plt.legend()
plt.grid(True)
plt.show()