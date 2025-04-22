import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# The data used for this clustering prediction was initially pulled from
# https://geodata.wisc.edu/catalog/367B52FB-6AEC-47F9-978D-29D1876AF057/metadata?utm_source=chatgpt.com
# and was modified to simulate the population distribution of wisconsin.
df = pd.read_csv("wis_pop_coord.csv")

X = df.iloc[:, 0:].to_numpy()

# Population scatterplot
plt.figure()
plt.scatter(X[:, 0], X[:, 1], s=1)
plt.show()

kmeans = KMeans(n_clusters=190)
kmeans.fit(X)

# Get the cluster labels and cluster centers
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Find the number of points in each cluster
cluster_sizes = [np.sum(labels == i) for i in range(kmeans.n_clusters)]

# Normalize the cluster sizes to use as a color map
normalized_sizes = np.array(cluster_sizes) / np.max(cluster_sizes)

# Scatterplot with predicted cities overtop
plt.figure()
plt.scatter(X[:, 0], X[:, 1], s=1)
for i, centroid in enumerate(centroids):
    plt.scatter(centroid[0], centroid[1], s=15, c=[plt.cm.hot(normalized_sizes[i])], marker='o')
plt.plot()

# This data was initially pulled from https://catalog.data.gov/dataset/2020-cartographic-boundary-file-shp-current-place-for-wisconsin-1-500000
# and modified to calculate the centroid of each incorporated
# wisconsin city boundary. This is used only for a visual representation
# of the accuracy of clustering the population as is.
df2 = pd.read_csv("cleaned_city_coords.csv")
X2 = df2.iloc[:, 0:].to_numpy()

# Actual city locations plotted for reference
plt.figure()
plt.scatter(X[:, 0], X[:, 1], s=1)
plt.scatter(X2[:, 0], X2[:, 1], s=15, c='red')
plt.show()
