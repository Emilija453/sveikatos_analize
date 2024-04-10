import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import KFold, cross_val_score
from sklearn import metrics


df = pd.read_csv('health-index-1.csv')
# print(df)
#OneHotEncoder
label_encoder = LabelEncoder()
df['country_ENCOD'] = label_encoder.fit_transform(df['country'])
print(df['country'])
salis_vizual = 99
df_salis = df[df['country_ENCOD'] == salis_vizual]
df_filtered_sorted = df_salis.sort_values('year')

X = df[['year', 'country_ENCOD']]
y = df[['value']]



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('MSE: ', mse)
print('R2: ', r2)

x_Lithuania = df_filtered_sorted[['year', 'country_ENCOD']]
y_Lithuania_pred = model.predict(x_Lithuania)


# n_features_optimal = 10
# rfe = RFE(model, n_features_to_select=n_features_optimal)
# rfe = rfe.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# r2 = sklearn.metrics.r2_score(y_test, y_pred)
# print(r2)
#
#
# k_folds = KFold(n_splits= 5, shuffle=True, random_state=42)
# scores = cross_val_score(model, X, y, cv=k_folds)
#
# print("Cross Validation Scores: ", scores)
# print("Average CV Score: ", scores.mean())
# print("Number of CV Scores used in Average: ", len(scores))

plt.scatter(df_filtered_sorted['year'], df_filtered_sorted['value'], color='blue', label='Mokymo duomenys', s=10)
plt.plot(df_filtered_sorted['year'], y_Lithuania_pred,linestyle='--', marker='o', color='red', label='Prognoze')
plt.xlabel('Metai')
plt.ylabel('Value')
plt.title('Sveikatos indekso prognoze pagal metus Lithuania 20%')
plt.legend()
plt.grid(True)
plt.show()
#
# plt.figure(figsize=(8, 6))
# plt.scatter(y_test, y_pred, color='blue', label='Predicted vs. Real')
# plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
# plt.xlabel('Real Values')
# plt.ylabel('Predicted Values')
# plt.title('Predicted vs. Real Values')
# plt.legend()
# plt.show()


#
# plt.scatter(df['PRICEEACH'], df['SALES'], color='green', s=10)
# # This will fit the best line into the graph
# plt.plot(np.unique(df['PRICEEACH']), np.poly1d(np.polyfit(df['PRICEEACH'], df['SALES'], 1))
# (np.unique(df['PRICEEACH'])), color='red')
# plt.title("PRICEEACH' / 'SALES'- koreliacija")
# plt.xlabel("PRICEEACH")
# plt.ylabel("SALES")
# plt.show()

