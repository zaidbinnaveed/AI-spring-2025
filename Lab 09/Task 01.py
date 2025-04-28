import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('house_data.csv')
df = df.dropna()
le = LabelEncoder()
df['neighborhood'] = le.fit_transform(df['neighborhood'])
X = df[['square_footage', 'bedrooms', 'bathrooms', 'age', 'neighborhood']]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

new_house = pd.DataFrame({'square_footage': [2000], 'bedrooms': [3], 'bathrooms': [2], 'age': [5], 'neighborhood': [1]})
predicted_price = model.predict(new_house)
