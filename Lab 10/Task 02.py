import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}

df = pd.DataFrame(data)


X = df.drop(columns=['vehicle_serial_no', 'vehicle_type'])


kmeans_no_scaling = KMeans(n_clusters=3, random_state=42)
df['cluster_no_scaling'] = kmeans_no_scaling.fit_predict(X)


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans_scaled = KMeans(n_clusters=3, random_state=42)
df['cluster_scaled'] = kmeans_scaled.fit_predict(X_scaled)


print(df)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.scatter(df['mileage'], df['fuel_efficiency'], c=df['cluster_no_scaling'], cmap='viridis')
ax1.set_title('Clustering without Scaling')
ax1.set_xlabel('Mileage')
ax1.set_ylabel('Fuel Efficiency')

ax2.scatter(df['mileage'], df['fuel_efficiency'], c=df['cluster_scaled'], cmap='viridis')
ax2.set_title('Clustering with Scaling')
ax2.set_xlabel('Mileage')
ax2.set_ylabel('Fuel Efficiency')

plt.show()
