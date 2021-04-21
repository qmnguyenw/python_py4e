K means Clustering – Introduction



We are given a data set of items, with certain features, and values for these
features (like a vector). The task is to categorize those items into groups.
To achieve this, we will use the kMeans algorithm; an unsupervised learning
algorithm.

 **Overview**

(It will help if you think of items as points in an n-dimensional space). The
algorithm will categorize the items into k groups of similarity. To calculate
that similarity, we will use the euclidean distance as measurement.

The algorithm works as follows:

  1. First we initialize k points, called means, randomly.
  2. We categorize each item to its closest mean and we update the mean’s coordinates, which are the averages of the items categorized in that mean so far.
  3. We repeat the process for a given number of iterations and at the end, we have our clusters.

The “points” mentioned above are called means, because they hold the mean
values of the items categorized in it. To initialize these means, we have a
lot of options. An intuitive method is to initialize the means at random items
in the data set. Another method is to initialize the means at random values
between the boundaries of the data set (if for a feature _x_ the items have
values in [0,3], we will initialize the means with values for _x_ at [0,3]).

  

  

The above algorithm in pseudocode:

    
    
    Initialize k means with random values
    
    For a given number of iterations:
        Iterate through items:
            Find the mean closest to the item
            Assign item to mean
            Update mean
    

**Read Data**

We receive input as a text file (‘data.txt’). Each line represents an item,
and it contains numerical values (one for each feature) split by commas. You
can find a sample data set here.

We will read the data from the file, saving it into a list. Each element of
the list is another list containing the item values for the features. We do
this with the following function:

 __

 __  
 __

 __

 __  
 __  
 __

def ReadData(fileName): 

 

 # Read the file, splitting by lines 

 f = open(fileName, 'r'); 

 lines = f.read().splitlines(); 

 f.close(); 

 

 items = []; 

 

 for i in range(1, len(lines)): 

 line = lines[i].split(','); 

 itemFeatures = []; 

 

 for j in range(len(line)-1): 

 

 # Convert feature value to float

 v = float(line[j]); 

 

 # Add feature value to dict 

 itemFeatures.append(v); 

 

 items.append(itemFeatures); 

 

 shuffle(items); 

 

 return items;   
  
---  
  
__

__

**Initialize Means**

We want to initialize each mean’s values in the range of the feature values of
the items. For that, we need to find the min and max for each feature. We
accomplish that with the following function:

 __

 __  
 __

 __

 __  
 __  
 __

def FindColMinMax(items):

 n = len(items[0]);

 minima = [sys.maxint for i in range(n)];

 maxima = [-sys.maxint -1 for i in range(n)];

 

 for item in items:

 for f in range(len(item)):

 if (item[f] < minima[f]):

 minima[f] = item[f];

 

 if (item[f] > maxima[f]):

 maxima[f] = item[f];

 

return minima,maxima;  
  
---  
  
 __

 __

The variables _minima, maxima_ are lists containing the min and max values of
the items respectively. We initialize each mean’s feature values randomly
between the corresponding minimum and maximum in those above two lists:

 __

 __  
 __

 __

 __  
 __  
 __

def InitializeMeans(items, k, cMin, cMax):

 

 # Initialize means to random numbers between

 # the min and max of each column/feature 

 f = len(items[0]); # number of features

 means = [[0 for i in range(f)] for j in
range(k)];

 

 for mean in means:

 for i in range(len(mean)):

 

 # Set value to a random float

 # (adding +-1 to avoid a wide placement of a mean)

 mean[i] = uniform(cMin[i]+1, cMax[i]-1);

 

 return means;  
  
---  
  
 __

 __

 **Euclidean Distance**

  

  

We will be using the euclidean distance as a metric of similarity for our data
set (note: depending on your items, you can use another similarity metric).

 __

 __  
 __

 __

 __  
 __  
 __

def EuclideanDistance(x, y): 

 S = 0; # The sum of the squared differences of the elements 

 for i in range(len(x)): 

 S += math.pow(x[i]-y[i], 2)

 

 #The square root of the sum

 return math.sqrt(S)  
  
---  
  
 __

 __

 **Update Means**

To update a mean, we need to find the average value for its feature, for all
the items in the mean/cluster. We can do this by adding all the values and
then dividing by the number of items, or we can use a more elegant solution.
We will calculate the new average without having to re-add all the values, by
doing the following:

    
    
    m = (m*(n-1)+x)/n

where _m_ is the mean value for a feature, _n_ is the number of items in the
cluster and _x_ is the feature value for the added item. We do the above for
each feature to get the new mean.

 __

 __  
 __

 __

 __  
 __  
 __

def UpdateMean(n,mean,item):

 for i in range(len(mean)):

 m = mean[i];

 m = (m*(n-1)+item[i])/float(n);

 mean[i] = round(m, 3);

 

 return mean;  
  
---  
  
 __

 __

 **Classify Items**

Now we need to write a function to classify an item to a group/cluster. For
the given item, we will find its similarity to each mean, and we will classify
the item to the closest one.

 __

 __  
 __

 __

 __  
 __  
 __

def Classify(means,item):

 

 # Classify item to the mean with minimum distance 

 minimum = sys.maxint;

 index = -1;

 

 for i in range(len(means)):

 

 # Find distance from item to mean

 dis = EuclideanDistance(item, means[i]);

 

 if (dis < minimum):

 minimum = dis;

 index = i;

 

 return index;  
  
---  
  
 __

 __

 **Find Means**

To actually find the means, we will loop through all the items, classify them
to their nearest cluster and update the cluster’s mean. We will repeat the
process for some fixed number of iterations. If between two iterations no item
changes classification, we stop the process as the algorithm has found the
optimal solution.

The below function takes as input _k_ (the number of desired clusters), the
items and the number of maximum iterations, and returns the means and the
clusters. The classification of an item is stored in the array _belongsTo_ and
the number of items in a cluster is stored in _clusterSizes_.

 __

 __  
 __

 __

 __  
 __  
 __

def CalculateMeans(k,items,maxIterations=100000):

 

 # Find the minima and maxima for columns

 cMin, cMax = FindColMinMax(items);

 

 # Initialize means at random points

 means = InitializeMeans(items,k,cMin,cMax);

 

 # Initialize clusters, the array to hold

 # the number of items in a class

 clusterSizes= [0 for i in range(len(means))];

 

 # An array to hold the cluster an item is in

 belongsTo = [0 for i in range(len(items))];

 

 # Calculate means

 for e in range(maxIterations):

 

 # If no change of cluster occurs, halt

 noChange = True;

 for i in range(len(items)):

 

 item = items[i];

 

 # Classify item into a cluster and update the

 # corresponding means. 

 index = Classify(means,item);

 

 clusterSizes[index] += 1;

 cSize = clusterSizes[index];

 means[index] = UpdateMean(cSize,means[index],item);

 

 # Item changed cluster

 if(index != belongsTo[i]):

 noChange = False;

 

 belongsTo[i] = index;

 

 # Nothing changed, return

 if (noChange):

 break;

 

 return means;  
  
---  
  
 __

 __

 **Find Clusters**

Finally we want to find the clusters, given the means. We will iterate through
all the items and we will classify each item to its closest cluster.

 __

 __  
 __

 __

 __  
 __  
 __

def FindClusters(means,items):

 clusters = [[] for i in range(len(means))]; # Init
clusters

 

 for item in items:

 

 # Classify item into a cluster

 index = Classify(means,item);

 

 # Add item to cluster

 clusters[index].append(item);

 

 return clusters;  
  
---  
  
 __

 __

The other popularly used similarity measures are:-

1\. **Cosine distance:** It determines the cosine of the angle between the
point vectors of the two points in the n dimensional space

![d = \\frac{X.Y}{||X||*||Y||}\\ ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-3fd139cbbf734c3a069c4c1416528409_l3.png)

2\. **Manhattan distance:** It computes the sum of the absolute differences
between the co-ordinates of the two data points.

![d = \\sum_{n} X{_{i}}-Y{_{i}} ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-ac9b0b227cd80bf647d1df50d5ac3512_l3.png)

3\. **Minkowski distance:** It is also known as the generalised distance
metric. It can be used for both ordinal and quantitative variables

![d = \(\\sum _{n}|X_{i}-Y_{i}|^{\\frac{1}{p}}\)^{p}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-b9b33ef0586a88a621a0932327048647_l3.png)

You can find the entire code on my GitHub, along with a sample data set and a
plotting function. Thanks for reading.

This article is contributed by **Antonis Maronikolakis**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

