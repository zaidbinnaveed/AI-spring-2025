import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


data = {
    'student_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'GPA': [3.5, 3.8, 2.9, 3.6, 3.3, 2.7, 3.9, 2.5, 3.2, 3.7],
    'study_hours': [15, 20, 10, 12, 16, 8, 22, 9, 14, 18],
    'attendance_rate': [90, 85, 80, 95, 88, 70, 92, 65, 85, 93]
}

df = pd.DataFrame(data)

X = df[['GPA', 'study_hours', 'attendance_rate']]

# Scaling the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


inertia = []
for k in range(2, 7):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)


plt.plot(range(2, 7), inertia, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()


kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

plt.scatter(df['study_hours'], df['GPA'], c=df['cluster'], cmap='viridis')
plt.title('Student Clustering based on GPA and Study Hours')
plt.xlabel('Study Hours')
plt.ylabel('GPA')
plt.show()


print(df[['student_id', 'cluster']])
