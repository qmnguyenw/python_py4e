Minimum Cost Graph



Given **N** nodes on a 2-D plane represented as **(x i, yi)**. The nodes are
said to be connected if the manhattan distance between them is **1**. You can
connect two nodes that are not connected at the cost of euclidean distance
between them. The task is to connect the graph such that every node has a path
from any node with minimum cost.

 **Examples:**

> **Input:** N = 3, edges[][] = {{1, 1}, {1, 1}, {2, 2}, {3, 2}}  
> **Output:** 1.41421  
> Since (2, 2) and (2, 3) are already connected.  
> So we try to connect either (1, 1) with (2, 2)  
> or (1, 1) with (2, 3) but (1, 1) with (2, 2)  
> yields the minimum cost.
>
>  **Input:** N = 3, edges[][] = {{1, 1}, {2, 2}, {3, 3}}  
> **Output:** 2.82843

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The brute force approach is to connect each node with every
other node and similarly for the other **N** nodes but in the worst case the
time complexity will be **N N**.  
The other way is to find the cost of every pair of vertices with the euclidean
distance and those pairs which are connected will have the cost as **0**.  
After knowing the cost of each pair we will apply the Kruskal Algorithm for
the minimum spanning tree and it will yield the minimum cost for connecting
the graph. Note that for Kruskal Algorithm, you have to have the knowledge of
Disjoint Set Union (DSU).

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implentation of the approach

#include <bits/stdc++.h>

using namespace std;

// Max number of nodes given

const int N = 500 + 10;

// arr is the parent array

// sz is the size of the

// subtree in DSU

int arr[N], sz[N];

// Function to initilize the parent

// and size array for DSU

void initialize()

{

 for (int i = 1; i < N; ++i) {

 arr[i] = i;

 sz[i] = 1;

 }

}

// Function to return the

// parent of the node

int root(int i)

{

 while (arr[i] != i)

 i = arr[i];

 return i;

}

// Function to perform the

// merge operation

void unin(int a, int b)

{

 a = root(a);

 b = root(b);

 if (a != b) {

 if (sz[a] < sz[b])

 swap(a, b);

 sz[a] += sz[b];

 arr[b] = a;

 }

}

// Function to return the minimum cost required

double minCost(vector<pair<int, int> >& p)

{

 // Number of points

 int n = (int)p.size();

 // To store the cost of every possible pair

 // as { cost, {to, from}}.

 vector<pair<double, pair<int, int> > > cost;

 // Calculating the cost of every possible pair

 for (int i = 0; i < n; ++i) {

 for (int j = 0; j < n; ++j) {

 if (i != j) {

 // Getting Manhattan distance

 int x = abs(p[i].first - p[j].first)

 + abs(p[i].second - p[j].second);

 // If the distance is 1 the cost is 0

 // or already connected

 if (x == 1) {

 cost.push_back({ 0, { i + 1, j + 1 } });

 cost.push_back({ 0, { j + 1, i + 1 } });

 }

 else {

 // Calculating the euclidean distance

 int a = p[i].first - p[j].first;

 int b = p[i].second - p[j].second;

 a *= a;

 b *= b;

 double d = sqrt(a + b);

 cost.push_back({ d, { i + 1, j + 1 } });

 cost.push_back({ d, { j + 1, i + 1 } });

 }

 }

 }

 }

 // Krushkal Algorithm for Minimum

 // spanning tree

 sort(cost.begin(), cost.end());

 // To initialize the size and

 // parent array

 initialize();

 double ans = 0.00;

 for (auto i : cost) {

 double c = i.first;

 int a = i.second.first;

 int b = i.second.second;

 // If the parents are different

 if (root(a) != root(b)) {

 unin(a, b);

 ans += c;

 }

 }

 return ans;

}

// Driver code

int main()

{

 // Vector pairs of points

 vector<pair<int, int> > points = {

 { 1, 1 },

 { 2, 2 },

 { 2, 3 }

 };

 // Function calling and printing

 // the answer

 cout << minCost(points);

 return 0;

}  
  
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

// Java implentation of the approach

import java.util.*;

import java.lang.*;

import java.io.*;

class GFG{

 

// Max number of nodes given

static int N = 500 + 10;

static class pair

{

 double c;

 int first, second;

 

 pair(double c, int first, int second)

 {

 this.c = c;

 this.first = first;

 this.second = second;

 }

}

// arr is the parent array

// sz is the size of the

// subtree in DSU

static int[] arr = new int[N],

 sz = new int[N];

 

// Function to initilize the parent

// and size array for DSU

static void initialize()

{

 for(int i = 1; i < N; ++i)

 {

 arr[i] = i;

 sz[i] = 1;

 }

}

 

// Function to return the

// parent of the node

static int root(int i)

{

 while (arr[i] != i)

 i = arr[i];

 

 return i;

}

 

// Function to perform the

// merge operation

static void unin(int a, int b)

{

 a = root(a);

 b = root(b);

 

 if (a != b)

 {

 if (sz[a] < sz[b])

 {

 int tmp = a;

 a = b;

 b = tmp;

 }

 

 sz[a] += sz[b];

 arr[b] = a;

 }

}

 

// Function to return the minimum

// cost required

static double minCost(int[][] p)

{

 

 // Number of points

 int n = (int)p.length;

 

 // To store the cost of every possible pair

 // as { cost, {to, from}}.

 ArrayList<pair> cost = new ArrayList<>();

 

 // Calculating the cost of every possible pair

 for(int i = 0; i < n; ++i)

 {

 for(int j = 0; j < n; ++j)

 {

 if (i != j)

 {

 

 // Getting Manhattan distance

 int x = Math.abs(p[i][0] - p[j][0]) +

 Math.abs(p[i][1] - p[j][1]);

 

 // If the distance is 1 the cost is 0

 // or already connected

 if (x == 1)

 {

 cost.add(new pair( 0, i + 1,

 j + 1 ));

 cost.add(new pair( 0, j + 1,

 i + 1 ));

 }

 else

 {

 

 // Calculating the euclidean

 // distance

 int a = p[i][0] - p[j][0];

 int b = p[i][1] - p[j][1];

 a *= a;

 b *= b;

 

 double d = Math.sqrt(a + b);

 cost.add(new pair(d, i + 1,

 j + 1 ));

 cost.add(new pair(d, j + 1,

 i + 1));

 }

 }

 }

 }

 

 // Krushkal Algorithm for Minimum

 // spanning tree

 Collections.sort(cost, new Comparator<>()

 {

 public int compare(pair a, pair b)

 {

 if(a.c <= b.c)

 return -1;

 else

 return 1;

 }

 });

 

 // To initialize the size and

 // parent array

 initialize();

 

 double ans = 0.00;

 for(pair i : cost)

 {

 double c = i.c;

 int a = i.first;

 int b = i.second;

 

 // If the parents are different

 if (root(a) != root(b))

 {

 unin(a, b);

 ans += c;

 }

 }

 return ans;

}

// Driver code

public static void main(String[] args)

{

 

 // Vector pairs of points

 int[][] points = { { 1, 1 },

 { 2, 2 },

 { 2, 3 }};

 

 // Function calling and printing

 // the answer

 System.out.format("%.5f", minCost(points));

}

}

// This code is contributed by offbeat  
  
---  
  
 __

 __

 **Output:**

    
    
    1.41421

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

