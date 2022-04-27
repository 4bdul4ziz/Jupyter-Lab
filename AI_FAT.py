'''
write the algorithm and program to form the clusters using k-means algorithm for a given set of locations of N samples,
 execute the program with different k and N values. Use Manhattan distance formula.

 Print the following details: 
    1. 'k' and 'N' value
    2. Initial medoids, mean values and members of each cluster
    3. Level number
    4. Distance value
    5. Reformed clusters with members and next medoid or mean
    6. Number of levels to complete the cluster formation
    7. Final cluster with members
    8. For the same 'N' samples, increase the 'k' value from 2 to 4 and observe the similarity score.
    9. Compare the result with manual calculation
'''



def manhattan_distance(x, y):
    '''
    Calculate the Manhattan distance between two points
    '''
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def get_closest_medoid(point, medoids):
    '''
    Get the closest medoid to the point
    '''
    min_dist = float('inf')
    closest_medoid = None
    for medoid in medoids:
        dist = manhattan_distance(point, medoid)
        if dist < min_dist:
            min_dist = dist
            closest_medoid = medoid
    return closest_medoid

#function to take k and N inputs
def get_inputs():
    '''
    Get the inputs from user
    '''
    k = int(input("Enter the value of k: "))
    N = int(input("Enter the value of N: "))
    return k, N

#function to calculate the initial medoids, mean values and members of each cluster
def get_initial_medoids(points, k):
    '''
    Get the initial medoids, mean values and members of each cluster
    '''
    medoids = []
    for i in range(k):
        medoids.append(points[i])
    return medoids

#function to find the level number of the cluster formation
def get_level_number(points, medoids):
    '''
    Get the level number of the cluster formation
    '''
    level_number = 0
    for point in points:
        closest_medoid = get_closest_medoid(point, medoids)
        if closest_medoid != point:
            level_number += 1
    return level_number


#function to find the distance value
def get_distance_value(points, medoids):
    '''
    Get the distance value
    '''
    distance_value = 0
    for point in points:
        closest_medoid = get_closest_medoid(point, medoids)
        distance_value += manhattan_distance(point, closest_medoid)
    return distance_value

#function to find the reformed clusters with members and next medoid or mean
def get_reformed_clusters(points, medoids):
    '''
    Get the reformed clusters with members and next medoid or mean
    '''
    reformed_clusters = []
    for point in points:
        closest_medoid = get_closest_medoid(point, medoids)
        if closest_medoid != point:
            reformed_clusters.append((point, closest_medoid))
    return reformed_clusters

#function to find the number of levels required to complete the cluster formation
def get_number_of_levels(points, medoids):
    '''
    Get the number of levels required to complete the cluster formation
    '''
    number_of_levels = 0
    for point in points:
        closest_medoid = get_closest_medoid(point, medoids)
        if closest_medoid != point:
            number_of_levels += 1
    return number_of_levels


#function to find the final cluster with members
def get_final_cluster(points, medoids):
    '''
    Get the final cluster with members
    '''
    final_cluster = []
    for point in points:
        closest_medoid = get_closest_medoid(point, medoids)
        if closest_medoid == point:
            final_cluster.append(point)
    return final_cluster

#function to observe the similarity score between two different k values
def get_similarity_score(points, k):
    '''
    Get the similarity score between two different k values
    '''
    similarity_score = 0
    for i in range(k):
        for j in range(i + 1, k):
            similarity_score += manhattan_distance(points[i], points[j])
    return similarity_score
    

def main():
    '''
    Main function
    '''
    points = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    k, N = get_inputs()
    medoids = get_initial_medoids(points, k)
    print("Initial medoids: ", medoids)
    print("Mean values: ", [sum(x) / len(x) for x in zip(*points)])
    print("Members of each cluster: ", [points.count(x) for x in medoids])
    level_number = get_level_number(points, medoids)
    print("Level number: ", level_number)
    distance_value = get_distance_value(points, medoids)
    print("Distance value: ", distance_value)
    reformed_clusters = get_reformed_clusters(points, medoids)
    print("Reformed clusters with members and next medoid or mean: ", reformed_clusters)
    number_of_levels = get_number_of_levels(points, medoids)
    print("Number of levels to complete the cluster formation: ", number_of_levels)
    final_cluster = get_final_cluster(points, medoids)
    print("Final cluster with members: ", final_cluster)
    print("Similarity score between two different k values: ", get_similarity_score(points, k))

main()

'''
Output:

abdul@Abduls-MacBook-Air Jupyter Lab % python -u "/Users/abdul/Desktop/Programming/Jupyt
er Lab/AI_FAT.py"
Enter the value of k: 2
Enter the value of N: 8
Initial medoids:  [(1, 1), (1, 2)]
Mean values:  [2.0, 2.0]
Members of each cluster:  [1, 1]
Level number:  7
Distance value:  12
Reformed clusters with members and next medoid or mean:  [((1, 3), (1, 2)), ((2, 1), (1, 1)), ((2, 2), (1, 2)), ((2, 3), (1, 2)), ((3, 1), (1, 1)), ((3, 2), (1, 2)), ((3, 3), (1, 2))]
Number of levels to complete the cluster formation:  7
Final cluster with members:  [(1, 1), (1, 2)]
Similarity score between two different k values:  1


'''