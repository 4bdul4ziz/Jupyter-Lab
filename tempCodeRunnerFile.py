 figsize=(6, 6), dpi=200, title="K-Means Clustering"):
    clusters = k_means_clustering(data, k)
    plt.figure(figsize=figsize, dpi=dpi)
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(data[:][0], data[:][1], c='b', marker='o')
    plt.scatter(clusters[:][0], clusters[:][1], c='r', marker='x')
    plt.show()   