from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt


X, y = datasets.make_blobs()


clf = KMeans(n_clusters=3)
y_pred = clf.fit_predict(X)


plt.figure(figsize=(10, 8))
plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis')
plt.title("K-Means Clustering Results")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig('kmeans_plot.png') 
print("Plot has been saved as 'kmeans_plot.png'")