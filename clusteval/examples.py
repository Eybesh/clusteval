# EXAMPLE
import clusteval
from sklearn.datasets import make_blobs
print(clusteval.__version__)
print(dir(clusteval))

# %%
from clusteval import clusteval
[X, labels_true] = make_blobs(n_samples=750, centers=4, n_features=2, cluster_std=0.5)

ce1 = clusteval(method='silhouette')
out1 = ce1.fit(X)
ce1.plot(X)

ce2 = clusteval(method='dbindex')
out2 = ce2.fit(X)
ce2.plot(X)

ce3 = clusteval(method='derivative')
out3 = ce3.fit(X)
ce3.plot(X)

ce4 = clusteval(method='dbscan')
out4 = ce4.fit(X)
ce4.plot(X)

ce5 = clusteval(method='hdbscan')
out5 = ce5.fit(X)
ce5.plot(X)