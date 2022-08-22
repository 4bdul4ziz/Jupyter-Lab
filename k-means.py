"""
Write a program to implement a k-means clustering algorithm by reading the coordinates of 12 input samples.
Read k value at runtime, k < n-1, where n is the number of input samples.
Print the members in the final ‘k’ clusters and the number of iterations is required to form the final ‘k’ clusters.
Also, print the members in each cluster in every iteration.
Use either Manhattan or Euclidean distance formula for cluster forming.

"""
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def manhattan_distance(x, y, k):
    dist = 0
    for i in range(k):
        dist += abs(x[i] - y[i])
    return dist


def k_means_clustering(data, k):
    # Initialize k clusters
    clusters = []
    for i in range(k):
        clusters.append(data[i])
    iterations = 0
    while True:
        iterations += 1
        clusters_assigned = []
        for i in range(len(data)):
            min_dist = float("inf")
            min_cluster = None
            for j in range(len(clusters)):
                dist = manhattan_distance(data[i], clusters[j], len(data[i]))
                if dist < min_dist:
                    min_dist = dist
                    min_cluster = j
            clusters_assigned.append(min_cluster)
        for i in range(len(clusters)):
            cluster_data = []
            for j in range(len(data)):
                if clusters_assigned[j] == i:
                    cluster_data.append(data[j])
            if len(cluster_data) == 0:
                continue
            clusters[i] = np.mean(cluster_data, axis=0)
        if len(set(clusters_assigned)) == k:
            break
        print("Number of iterations:", iterations)
    return clusters


def plotClusters(data, k, figsize=(6, 6), dpi=200, title="K-Means Clustering"):
    clusters = k_means_clustering(data, k)
    plt.figure(figsize=figsize, dpi=dpi)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(data[:][0], data[:][1], c="b", marker="o")
    plt.scatter(clusters[:, 0], clusters[:1], c="r", marker="x")
    plt.show()


def visuallise_clustering(data, k):
    clusters = k_means_clustering(data, k)
    print("Clusters:")
    for i in range(k):
        print("Cluster", i, ":", clusters[i])


def main():
    data = np.array(
        [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
    )
    k = int(input("Enter k:"))
    visuallise_clustering(data, k)
    plotClusters(data, k)


main()
