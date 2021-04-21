Spanning Tree With Maximum Degree (Using Kruskal’s Algorithm)



Given an undirected unweighted connected graph consisting of **n** vertices
and **m** edges. The task is to find any spanning tree of this graph such that
the maximum degree over all vertices is maximum possible. The order in which
you print the output edges does not matter and an edge can be printed in
reverse also i.e. (u, v) can also be printed as (v, u).

 **Examples:**

    
    
    **Input:**
            1
           / \
          2   5
           \ /
            3
            |
            4
    **Output:**
    3 2
    3 5
    3 4
    1 2
    The maximum degree over all vertices 
    is of vertex 3 which is 3 and is 
    maximum possible.
    
    **Input:**
            1
           /
          2 
         / \ 
        5   3
            |
            4
    **Output:**
    2 1
    2 5
    2 3
    3 4

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Prerequisite:** Kruskal Algorithm to find Minimum Spanning Tree

 **Approach:** The given problem can be solved using Kruskal’s algorithm to
find the Minimum Spanning tree.  
We find the vertex which has maximum degree in the graph. At first we will
perform the union of all the edges which are incident to this vertex and than
carry out normal Kruskal’s algorithm. This gives us optimal spanning tree.

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java implementation of the approach

import java.util.*;

public class GFG {

 // par and rank will store the parent

 // and rank of particular node

 // in the Union Find Algorithm

 static int par[], rank[];

 // Find function of Union Find Algorithm

 static int find(int x)

 {

 if (par[x] != x)

 par[x] = find(par[x]);

 return par[x];

 }

 // Union function of Union Find Algorithm

 static void union(int u, int v)

 {

 int x = find(u);

 int y = find(v);

 if (x == y)

 return;

 if (rank[x] > rank[y])

 par[y] = x;

 else if (rank[x] < rank[y])

 par[x] = y;

 else {

 par[x] = y;

 rank[y]++;

 }

 }

 // Function to find the required spanning tree

 static void findSpanningTree(int deg[], int n,

 int m, ArrayList<Integer> g[])

 {

 par = new int[n + 1];

 rank = new int[n + 1];

 // Initialising parent of a node

 // by itself

 for (int i = 1; i <= n; i++)

 par[i] = i;

 // Variable to store the node

 // with maximum degree

 int max = 1;

 // Finding the node with maximum degree

 for (int i = 2; i <= n; i++)

 if (deg[i] > deg[max])

 max = i;

 // Union of all edges incident

 // on vertex with maximum degree

 for (int v : g[max]) {

 System.out.println(max + " " + v);

 union(max, v);

 }

 // Carrying out normal Kruskal Algorithm

 for (int u = 1; u <= n; u++) {

 for (int v : g[u]) {

 int x = find(u);

 int y = find(v);

 if (x == y)

 continue;

 union(x, y);

 System.out.println(u + " " + v);

 }

 }

 }

 // Driver code

 public static void main(String args[])

 {

 // Number of nodes

 int n = 5;

 // Number of edges

 int m = 5;

 // ArrayList to store the graph

 ArrayList<Integer> g[] = new ArrayList[n + 1];

 for (int i = 1; i <= n; i++)

 g[i] = new ArrayList<>();

 // Array to store the degree

 // of each node in the graph

 int deg[] = new int[n + 1];

 // Add edges and update degrees

 g[1].add(2);

 g[2].add(1);

 deg[1]++;

 deg[2]++;

 g[1].add(5);

 g[5].add(1);

 deg[1]++;

 deg[5]++;

 g[2].add(3);

 g[3].add(2);

 deg[2]++;

 deg[3]++;

 g[5].add(3);

 g[3].add(5);

 deg[3]++;

 deg[5]++;

 g[3].add(4);

 g[4].add(3);

 deg[3]++;

 deg[4]++;

 findSpanningTree(deg, n, m, g);

 }

}  
  
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

# Python3 implementation of the approach

from typing import List

# par and rank will store the parent

# and rank of particular node

# in the Union Find Algorithm

par = []

rnk = []

# Find function of Union Find Algorithm

def find(x: int) -> int:

 

 global par

 

 if (par[x] != x):

 par[x] = find(par[x])

 

 return par[x]

# Union function of Union Find Algorithm

def Union(u: int, v: int) -> None:

 

 global par, rnk

 x = find(u)

 y = find(v)

 

 if (x == y):

 return

 if (rnk[x] > rnk[y]):

 par[y] = x

 elif (rnk[x] < rnk[y]):

 par[x] = y

 else:

 par[x] = y

 rnk[y] += 1

# Function to find the required spanning tree

def findSpanningTree(deg: List[int], n: int, m: int,

 g: List[List[int]]) -> None:

 

 global rnk, par

 # Initialising parent of a node

 # by itself

 par = [i for i in range(n + 1)]

 rnk = [0] * (n + 1)

 # Variable to store the node

 # with maximum degree

 max = 1

 # Finding the node with maximum degree

 for i in range(2, n + 1):

 if (deg[i] > deg[max]):

 max = i

 # Union of all edges incident

 # on vertex with maximum degree

 for v in g[max]:

 print("{} {}".format(max, v))

 Union(max, v)

 # Carrying out normal Kruskal Algorithm

 for u in range(1, n + 1):

 for v in g[u]:

 x = find(u)

 y = find(v)

 

 if (x == y):

 continue

 

 Union(x, y)

 print("{} {}".format(u, v))

# Driver code

if __name__ == "__main__":

 # Number of nodes

 n = 5

 # Number of edges

 m = 5

 # ArrayList to store the graph

 g = [[] for _ in range(n + 1)]

 # Array to store the degree

 # of each node in the graph

 deg = [0] * (n + 1)

 # Add edges and update degrees

 g[1].append(2)

 g[2].append(1)

 deg[1] += 1

 deg[2] += 1

 g[1].append(5)

 g[5].append(1)

 deg[1] += 1

 deg[5] += 1

 g[2].append(3)

 g[3].append(2)

 deg[2] += 1

 deg[3] += 1

 g[5].append(3)

 g[3].append(5)

 deg[3] += 1

 deg[5] += 1

 g[3].append(4)

 g[4].append(3)

 deg[3] += 1

 deg[4] += 1

 findSpanningTree(deg, n, m, g)

# This code is contributed by sanjeev2552  
  
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

// C# implementation of the approach

using System;

using System.Collections.Generic;

class GFG

{

 // par and rank will store the parent

 // and rank of particular node

 // in the Union Find Algorithm

 static int []par;

 static int []rank;

 // Find function of Union Find Algorithm

 static int find(int x)

 {

 if (par[x] != x)

 par[x] = find(par[x]);

 return par[x];

 }

 // Union function of Union Find Algorithm

 static void union(int u, int v)

 {

 int x = find(u);

 int y = find(v);

 if (x == y)

 return;

 if (rank[x] > rank[y])

 par[y] = x;

 else if (rank[x] < rank[y])

 par[x] = y;

 else {

 par[x] = y;

 rank[y]++;

 }

 }

 // Function to find the required spanning tree

 static void findSpanningTree(int []deg, int n,

 int m, List<int> []g)

 {

 par = new int[n + 1];

 rank = new int[n + 1];

 // Initialising parent of a node

 // by itself

 for (int i = 1; i <= n; i++)

 par[i] = i;

 // Variable to store the node

 // with maximum degree

 int max = 1;

 // Finding the node with maximum degree

 for (int i = 2; i <= n; i++)

 if (deg[i] > deg[max])

 max = i;

 // Union of all edges incident

 // on vertex with maximum degree

 foreach (int v in g[max])

 {

 Console.WriteLine(max + " " + v);

 union(max, v);

 }

 // Carrying out normal Kruskal Algorithm

 for (int u = 1; u <= n; u++)

 {

 foreach (int v in g[u])

 {

 int x = find(u);

 int y = find(v);

 if (x == y)

 continue;

 union(x, y);

 Console.WriteLine(u + " " + v);

 }

 }

 }

 // Driver code

 public static void Main(String []args)

 {

 

 // Number of nodes

 int n = 5;

 // Number of edges

 int m = 5;

 // ArrayList to store the graph

 List<int> []g = new List<int>[n + 1];

 for (int i = 1; i <= n; i++)

 g[i] = new List<int>();

 // Array to store the degree

 // of each node in the graph

 int []deg = new int[n + 1];

 // Add edges and update degrees

 g[1].Add(2);

 g[2].Add(1);

 deg[1]++;

 deg[2]++;

 g[1].Add(5);

 g[5].Add(1);

 deg[1]++;

 deg[5]++;

 g[2].Add(3);

 g[3].Add(2);

 deg[2]++;

 deg[3]++;

 g[5].Add(3);

 g[3].Add(5);

 deg[3]++;

 deg[5]++;

 g[3].Add(4);

 g[4].Add(3);

 deg[3]++;

 deg[4]++;

 findSpanningTree(deg, n, m, g);

 }

}

// This code has been contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    3 2
    3 5
    3 4
    1 2

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

