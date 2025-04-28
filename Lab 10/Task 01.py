import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Sample customer data
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'age': [22, 25, 27, 24, 22, 30, 31, 23, 28, 26],
    'income': [50000, 60000, 80000, 40000, 55000, 95000, 110000, 45000, 70000, 75000],
    'spending_score': [30, 40, 60, 20, 50, 70, 80, 25, 55, 65]
}

df = pd.DataFrame(data)


X = df.drop(columns=['customer_id'])


kmeans_no_scaling = KMeans(n_clusters=3, random_state=42)
df['cluster_no_scaling'] = kmeans_no_scaling.fit_predict(X)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans_scaled = KMeans(n_clusters=3, random_state=42)
df['cluster_scaled'] = kmeans_scaled.fit_predict(X_scaled)


print(df)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.scatter(df['age'], df['income'], c=df['cluster_no_scaling'], cmap='viridis')
ax1.set_title('Clustering without Scaling')
ax1.set_xlabel('Age')
ax1.set_ylabel('Income')

ax2.scatter(df['age'], df['income'], c=df['cluster_scaled'], cmap='viridis')
ax2.set_title('Clustering with Scaling')
ax2.set_xlabel('Age')
ax2.set_ylabel('Income')

plt.show()
