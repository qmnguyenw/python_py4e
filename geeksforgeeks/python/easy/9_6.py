ML | Random Intialization Trap in K-Means



Random initialization trap is a problem that occurs in the K-means algorithm.
In random initialization trap when the centroids of the clusters to be
generated are explicitly defined by the User then inconsistency may be created
and this may sometimes lead to generating wrong clusters in the dataset. So
random initialization trap may sometimes prevent us from developing the
correct clusters.

 **Example :**  
Suppose you have a dataset with the following points shown in the picture and
you want to generate three clusters in this dataset according to their
attributes by performing K-means clustering. From the figure, we can get the
intuition what are the clusters that are required to be generated. K-means
will perform clustering on the basis of the centroids fed into the algorithm
and generate the required clusters according to these centroids.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200206014327/rand1.png)  
 **First Trial**  
Suppose we choose 3 sets of centroids according to the figure shown below. The
clusters that are generated corresponding to these centroids are shown in the
figure below.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200206014758/rand2.png)

 **Final Model**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200206015629/rand3.png)

  

  

 **Second Trial**  
Consider another case in which we choose another set of centroids for the
dataset as shown. Now the set of clusters generated will be different from the
clusters generated in the previous practice.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200206020039/rand4.png)

 **Final model**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200206020912/rand5.png)

Similarly we may get different model outputs on the same dataset. This
condition where a different set of clusters is generated when a different set
of centroids are provided to the K-means algorithm making it inconsistent and
unreliable is called the Random initialization trap.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

