ML | Hierarchical clustering (Agglomerative and Divisive clustering)



In data mining and statistics, hierarchical clustering analysis is a method of
cluster analysis which seeks to build a hierarchy of clusters i.e. tree type
structure based on the hierarchy.

 **Basically, there are two types of hierarchical cluster analysis strategies
–**

  1.  **Agglomerative Clustering:** Also known as bottom-up approach or hierarchical agglomerative clustering (HAC). A structure that is more informative than the unstructured set of clusters returned by flat clustering. This clustering algorithm does not require us to prespecify the number of clusters. Bottom-up algorithms treat each data as a singleton cluster at the outset and then successively agglomerates pairs of clusters until all clusters have been merged into a single cluster that contains all data.

 **Algorithm :**

    
    
    given a dataset (d1, d2, d3, ....dN) of size N
    # compute the distance matrix
    for i=1 to N:
       # as the distance matrix is symmetric about 
       # the primary diagonal so we compute only lower 
       # part of the primary diagonal 
       for j=1 to i:
          dis_mat[i][j] = distance[di, dj] 
    each data point is a singleton cluster
    **repeat**
       merge the two cluster having minimum distance
       update the distance matrix
    **untill** only a single cluster remains
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190508025311/781ff66c-b380-4a78-af25-80507ed6ff26-300x300.png)  
  
Python implementation of the above algorithm using scikit-learn library:

 __

 __  
 __

 __

 __  
 __  
 __

from sklearn.cluster import AgglomerativeClustering

import numpy as np

 

# randomly chosen dataset

X = np.array([[1, 2], [1, 4], [1, 0],

 [4, 2], [4, 4], [4, 0]])

 

# here we need to mention the number of clusters 

# otherwise the result will be a single cluster

# containing all the data

clustering = AgglomerativeClustering(n_clusters = 2).fit(X)

 

# print the class labels

print(clustering.labels_)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    [1, 1, 1, 0, 0, 0]
    

  2. **Divisive clustering :** Also known as top-down approach. This algorithm also does not require to prespecify the number of clusters. Top-down clustering requires a method for splitting a cluster that contains the whole data and proceeds by splitting clusters recursively until individual data have been splitted into singleton cluster.

 **Algorithm :**

    
    
    given a dataset (d1, d2, d3, ....dN) of size N
    at the top we have all data in one cluster
    the cluster is split using a flat clustering method eg. K-Means etc
    **repeat**
    choose the best cluster among all the clusters to split
    split that cluster by the flat clustering algorithm
    **untill** each data is in its own singleton cluster
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190508025314/781ff66c-b380-4a78-af25-80507ed6ff261-300x300.png)

**Hierarchical Agglomerative _vs_ Divisive clustering –**

  * Divisive clustering is more _complex_ as compared to agglomerative clustering, as in case of divisive clustering we need a flat clustering method as “subroutine” to split each cluster until we have each data having its own singleton cluster.
  * Divisive clustering is more _efficient_ if we do not generate a complete hierarchy all the way down to individual data leaves. Time complexity of a naive agglomerative clustering is **O(n 3)** because we exhaustively scan the N x N matrix dist_mat for the lowest distance in each of N-1 iterations. Using priority queue data structure we can reduce this complexity to **O(n 2logn)**. By using some more optimizations it can be brought down to **O(n 2)**. Whereas for divisive clustering given a fixed number of top levels, using an efficient flat algorithm like K-Means, divisive algorithms are linear in the number of patterns and clusters.
  * Divisive algorithm is also more _accurate_. Agglomerative clustering makes decisions by considering the local patterns or neighbor points without initially taking into account the global distribution of data. These early decisions cannot be undone. whereas divisive clustering takes into consideration the global distribution of data when making top-level partitioning decisions.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

