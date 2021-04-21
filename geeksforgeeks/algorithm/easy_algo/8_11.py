K-Nearest Neighbours



K-Nearest Neighbors is one of the most basic yet essential classification
algorithms in Machine Learning. It belongs to the supervised learning domain
and finds intense application in pattern recognition, data mining and
intrusion detection.

It is widely disposable in real-life scenarios since it is non-parametric,
meaning, it does not make any underlying assumptions about the distribution of
data (as opposed to other algorithms such as GMM, which assume a Gaussian
distribution of the given data).

We are given some prior data (also called training data), which classifies
coordinates into groups identified by an attribute.

As an example, consider the following table of data points containing two
features:  
![k-nearest-neighbours1](https://media.geeksforgeeks.org/wp-
content/uploads/graph1-8.png)

Now, given another set of data points (also called testing data), allocate
these points a group by analyzing the training set. Note that the unclassified
points are marked as ‘White’.

  

  

![k-nearest-neighbours3](https://media.geeksforgeeks.org/wp-
content/uploads/graph2-2.png)

 **Intuition**  
If we plot these points on a graph, we may be able to locate some clusters or
groups. Now, given an unclassified point, we can assign it to a group by
observing what group its nearest neighbors belong to. This means a point close
to a cluster of points classified as ‘Red’ has a higher probability of getting
classified as ‘Red’.

Intuitively, we can see that the first point (2.5, 7) should be classified as
‘Green’ and the second point (5.5, 4.5) should be classified as ‘Red’.

 **Algorithm**  
Let m be the number of training data samples. Let p be an unknown point.

  1. Store the training samples in an array of data points arr[]. This means each element of this array represents a tuple (x, y).
  2.     for i=0 to m:
      Calculate Euclidean distance d(arr[i], p).

  3. Make set S of K smallest distances obtained. Each of these distances corresponds to an already classified data point.
  4. Return the majority label among S.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

K can be kept as an odd number so that we can calculate a clear majority in
the case where only two groups are possible (e.g. Red/Blue). With increasing
K, we get smoother, more defined boundaries across different classifications.
Also, the accuracy of the above classifier increases as we increase the number
of data points in the training set.

 **Example Program**  
Assume 0 and 1 as the two classifiers (groups).  

## C/C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find groups of unknown

// Points using K nearest neighbour algorithm.

#include <bits/stdc++.h>

using namespace std;

 

struct Point

{

 int val; // Group of point

 double x, y; // Co-ordinate of point

 double distance; // Distance from test point

};

 

// Used to sort an array of points by increasing

// order of distance

bool comparison(Point a, Point b)

{

 return (a.distance < b.distance);

}

 

// This function finds classification of point p using

// k nearest neighbour algorithm. It assumes only two

// groups and returns 0 if p belongs to group 0, else

// 1 (belongs to group 1).

int classifyAPoint(Point arr[], int n, int k, Point p)

{

 // Fill distances of all points from p

 for (int i = 0; i < n; i++)

 arr[i].distance =

 sqrt((arr[i].x - p.x) * (arr[i].x - p.x) +

 (arr[i].y - p.y) * (arr[i].y - p.y));

 

 // Sort the Points by distance from p

 sort(arr, arr+n, comparison);

 

 // Now consider the first k elements and only

 // two groups

 int freq1 = 0; // Frequency of group 0

 int freq2 = 0; // Frequency of group 1

 for (int i = 0; i < k; i++)

 {

 if (arr[i].val == 0)

 freq1++;

 else if (arr[i].val == 1)

 freq2++;

 }

 

 return (freq1 > freq2 ? 0 : 1);

}

 

// Driver code

int main()

{

 int n = 17; // Number of data points

 Point arr[n];

 

 arr[0].x = 1;

 arr[0].y = 12;

 arr[0].val = 0;

 

 arr[1].x = 2;

 arr[1].y = 5;

 arr[1].val = 0;

 

 arr[2].x = 5;

 arr[2].y = 3;

 arr[2].val = 1;

 

 arr[3].x = 3;

 arr[3].y = 2;

 arr[3].val = 1;

 

 arr[4].x = 3;

 arr[4].y = 6;

 arr[4].val = 0;

 

 arr[5].x = 1.5;

 arr[5].y = 9;

 arr[5].val = 1;

 

 arr[6].x = 7;

 arr[6].y = 2;

 arr[6].val = 1;

 

 arr[7].x = 6;

 arr[7].y = 1;

 arr[7].val = 1;

 

 arr[8].x = 3.8;

 arr[8].y = 3;

 arr[8].val = 1;

 

 arr[9].x = 3;

 arr[9].y = 10;

 arr[9].val = 0;

 

 arr[10].x = 5.6;

 arr[10].y = 4;

 arr[10].val = 1;

 

 arr[11].x = 4;

 arr[11].y = 2;

 arr[11].val = 1;

 

 arr[12].x = 3.5;

 arr[12].y = 8;

 arr[12].val = 0;

 

 arr[13].x = 2;

 arr[13].y = 11;

 arr[13].val = 0;

 

 arr[14].x = 2;

 arr[14].y = 5;

 arr[14].val = 1;

 

 arr[15].x = 2;

 arr[15].y = 9;

 arr[15].val = 0;

 

 arr[16].x = 1;

 arr[16].y = 7;

 arr[16].val = 0;

 

 /*Testing Point*/

 Point p;

 p.x = 2.5;

 p.y = 7;

 

 // Parameter to decide group of the testing point

 int k = 3;

 printf ("The value classified to unknown point"

 " is %d.\n", classifyAPoint(arr, n, k, p));

 return 0;

}  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find groups of unknown

# Points using K nearest neighbour algorithm.

 

import math

 

def classifyAPoint(points,p,k=3):

 '''

 This function finds the classification of p using

 k nearest neighbor algorithm. It assumes only two

 groups and returns 0 if p belongs to group 0, else

 1 (belongs to group 1).

 

 Parameters - 

 points: Dictionary of training points having two keys - 0 and 1

 Each key have a list of training data points belong to that 

 

 p : A tuple, test data point of the form (x,y)

 

 k : number of nearest neighbour to consider, default is 3 

 '''

 

 distance=[]

 for group in points:

 for feature in points[group]:

 

 #calculate the euclidean distance of p from training points 

 euclidean_distance = math.sqrt((feature[0]-p[0])**2
+(feature[1]-p[1])**2)

 

 # Add a tuple of form (distance,group) in the distance list

 distance.append((euclidean_distance,group))

 

 # sort the distance list in ascending order

 # and select first k distances

 distance = sorted(distance)[:k]

 

 freq1 = 0 #frequency of group 0

 freq2 = 0 #frequency og group 1

 

 for d in distance:

 if d[1] == 0:

 freq1 += 1

 elif d[1] == 1:

 freq2 += 1

 

 return 0 if freq1>freq2 else 1

 

# driver function

def main():

 

 # Dictionary of training points having two keys - 0 and 1

 # key 0 have points belong to class 0

 # key 1 have points belong to class 1

 

 points =
{0:[(1,12),(2,5),(3,6),(3,10),(3.5,8),(2,11),(2,9),(1,7)],


1:[(5,3),(3,2),(1.5,9),(7,2),(6,1),(3.8,1),(5.6,4),(4,2),(2,5)]}

 

 # testing point p(x,y)

 p = (2.5,7)

 

 # Number of neighbours 

 k = 3

 

 print("The value classified to unknown point is: {}".\

 format(classifyAPoint(points,p,k)))

 

if __name__ == '__main__':

 main()

 

# This code is contributed by Atul Kumar (www.fb.com/atul.kr.007)  
  
---  
  
 __

 __

  
Output:

    
    
    The value classified to unknown point is 0.
    

This article is contributed by **Anannya Uberoi**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
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

