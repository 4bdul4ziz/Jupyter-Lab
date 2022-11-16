"""
Write a program to implement a k-means clustering algorithm by reading the coordinates of 12 input samples.
Read k value at runtime, k < n-1, where n is the number of input samples.
Print the members in the final ‘k’ clusters and the number of iterations is required to form the final ‘k’ clusters.
Also, print the members in each cluster in every iteration.
Use either Manhattan or Euclidean distance formula for cluster forming.
 
"""
import matplotlib.pyplot as plt
import numpy as np

def euclidean_distance(x, y, k):
    dist = 0
    for i in range(k):
        dist += (x[i] - y[i]) ** 2
    return dist ** 0.5

def k_means_clustering(k):
    clusters = [[] for i in range(k)]
    centroids = np.array(
        [
            [5, 1],
            [1, 1],
            [6, 0],
            [2, 1],
            [4, 0],
        ]
    )
    for i in range(len(centroids)):
        distances = []
        for j in range(k):
            distances.append(euclidean_distance(centroids[i], centroids[j], 2))
        clusters[distances.index(min(distances))].append(centroids[i])
    return clusters

def main():
    k = int(input("Enter the value of k: "))
    clusters = k_means_clustering(k)
    print("Final clusters: ", clusters)
    for i in range(k):
        print("Cluster ", i + 1, ": ", clusters[i])
main()