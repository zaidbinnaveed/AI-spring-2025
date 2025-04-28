from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report

customers = pd.read_csv('customers.csv')
customers = customers.dropna()
X = customers[['total_spent', 'age', 'num_visits', 'purchase_frequency']]
y = customers['value_label']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = SVC(kernel='linear')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)

import numpy as np
coef = model.coef_[0]
intercept = model.intercept_[0]
hyperplane_equation = f"{coef[0]:.2f}*x1 + {coef[1]:.2f}*x2 + {coef[2]:.2f}*x3 + {coef[3]:.2f}*x4 + {intercept:.2f} = 0"
