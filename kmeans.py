import matplotlib.pyplot as plt
import numpy as np
from sklearn import cluster

fig = plt.figure(figsize=(5,10))
ax = fig.add_subplot(2,1,1)

# Generate "random" data, should be approximately two clusters
group1 = -np.random.rand(100,2)
group2 = 2 * np.random.rand(100, 2)
group3 = np.concatenate((-2.5 * np.random.rand(100, 1), 1.25 * np.random.rand(100, 1)), axis=1)
data = np.concatenate([group1, group2, group3])
print data
x = data[:,0]
y = data[:,1]

ax.set_title("Before clustering")
ax.scatter(x,y)

ax = fig.add_subplot(2,1,2)

## K Means clustering

k = 3
kmeans = cluster.KMeans(n_clusters=k)
kmeans.fit(data)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

ax.set_title("Clustered")

for i in range(k):
    # select only data observations with cluster label == i
    ds = data[np.where(labels==i)]
    # plot the data observations
    ax.plot(ds[:,0],ds[:,1],'o')
    # plot the centroids
    lines = ax.plot(centroids[i,0],centroids[i,1],'kx')
    # make the centroid x's bigger
    plt.setp(lines,ms=15.0)
    plt.setp(lines,mew=2.0)

plt.show()
