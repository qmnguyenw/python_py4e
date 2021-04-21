Find K Closest Points to the Origin



Given a list of points on the 2-D plane and an integer K. The task is to find
K closest points to the origin and print them.  
 **Note** : The distance between two points on a plane is the Euclidean
distance.

 **Examples:**

    
    
    **Input :** point = [[3, 3], [5, -1], [-2, 4]], K = 2
    **Output :** [[3, 3], [-2, 4]]
    Square of Distance of origin from this point is 
    (3, 3) = 18
    (5, -1) = 26
    (-2, 4) = 20
    So rhe closest two points are [3, 3], [-2, 4].
    
    **Input :** point = [[1, 3], [-2, 2]], K  = 1
    **Output :** [[-2, 2]]
    Square of Distance of origin from this point is
    (1, 3) = 10
    (-2, 2) = 8 
    So the closest point to origin is (-2, 2)
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to calculate the Euclidean distance from the origin
for every given point and sort the array according to the Euclidean distance
found. Print the first k closest points from the list.

 **Algorithm :**  
Consider two points with coordinates as (x1, y1) and (x2, y2) respectively.
The **Euclidean distance** between these two points will be:

    
    
    √{(x2-x1)2 + (y2-y1)2}
    

  1. Sort the points by distance using the Euclidean distance formula.
  2. Select first K points form the list
  3. Print the points obtained in any order.

Below is the implementation of the above approach:

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for implementation of

// above approach

#include<bits/stdc++.h>

using namespace std;

// Function to print required answer

void pClosest(vector<vector<int>> pts, int k)

{

 

 // In multimap values gets

 // automatically sorted based on

 // their keys which is distance here

 multimap<int, int> mp;

 for(int i = 0; i < pts.size(); i++)

 {

 int x = pts[i][0], y = pts[i][1];

 mp.insert({(x * x) + (y * y) , i});

 }

 

 for(auto it = mp.begin();

 it != mp.end() && k > 0;

 it++, k--)

 cout << "[" << pts[it->second][0] << ", "

 << pts[it->second][1] << "]" << "\n";

}

// Driver code

int main()

{

 vector<vector<int>> points = { { 3, 3 },

 { 5, -1 },

 { -2, 4 } };

 

 int K = 2;

 

 pClosest(points, K);

 return 0;

}

// This code is contributed by sarthak_eddy.  
  
---  
  
 __

 __

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java program for implementation of

// above approach

import java.util.*;

class GFG{

 

// Function to print required answer

static void pClosest(int [][]pts, int k)

{

 int n = pts.length;

 int[] distance = new int[n];

 for(int i = 0; i < n; i++)

 {

 int x = pts[i][0], y = pts[i][1];

 distance[i] = (x * x) + (y * y);

 }

 Arrays.sort(distance);

 

 // Find the k-th distance

 int distk = distance[k - 1];

 // Print all distances which are

 // smaller than k-th distance

 for(int i = 0; i < n; i++)

 {

 int x = pts[i][0], y = pts[i][1];

 int dist = (x * x) + (y * y);

 

 if (dist <= distk)

 System.out.println("[" + x + ", " + y + "]");

 }

}

// Driver code

public static void main (String[] args)

{

 int points[][] = { { 3, 3 },

 { 5, -1 },

 { -2, 4 } };

 int K = 2;

 

 pClosest(points, K);

}

}

// This code is contributed by sarthak_eddy.  
  
---  
  
 __

 __

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for implementation of

# above approach

# Function to return required answer

def pClosest(points, K):

 points.sort(key = lambda K: K[0]**2 +
K[1]**2)

 return points[:K]

# Driver program

points = [[3, 3], [5, -1], [-2, 4]]

K = 2

print(pClosest(points, K))  
  
---  
  
 __

 __

## C#

 __

 __  
 __

 __

 __  
 __  
 __

// C# program for implementation

// of above approach

using System;

class GFG{

 

// Function to print

// required answer

static void pClosest(int [,]pts,

 int k)

{

 int n = pts.GetLength(0);

 int[] distance = new int[n];

 

 for(int i = 0; i < n; i++)

 {

 int x = pts[i, 0],

 y = pts[i, 1];

 distance[i] = (x * x) +

 (y * y);

 }

 Array.Sort(distance);

 // Find the k-th distance

 int distk = distance[k - 1];

 // Print all distances which are

 // smaller than k-th distance

 for(int i = 0; i < n; i++)

 {

 int x = pts[i, 0],

 y = pts[i, 1];

 int dist = (x * x) +

 (y * y);

 if (dist <= distk)

 Console.WriteLine("[" + x +

 ", " + y + "]");

 }

}

// Driver code

public static void Main (string[] args)

{

 int [,]points = {{3, 3},

 {5, -1},

 {-2, 4}};

 int K = 2;

 pClosest(points, K);

}

}

// This code is contributed by Chitranayal  
  
---  
  
 __

 __

 **Output:**

    
    
    [[3, 3], [-2, 4]]
    
    
    
    
    

**Complexity Analysis:**

  * **Time Complexity:** O(n log n).   
Time complexity to find the distance from the origin for every point is O(n)
and to sort the array is O(n log n)

  *  **Space Complexity:** O(1).   
As no extra space is required.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

