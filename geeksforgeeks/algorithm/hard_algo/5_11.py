Minimum distance to visit all the nodes of an undirected weighted tree



Given a weighted tree with **N** nodes starting from **1 to N**. The distance
between any two nodes is given by the edge weight. Node **1** is the source,
the task is to visit all the nodes of the tree with minimum distance traveled.

**Examples:**

> **Input:**  
> u[] = {1, 1, 2, 2, 1}  
> v[] = {2, 3, 5, 6, 4}  
> w[] = {1, 4, 2, 50, 5}  
> **Output:** 73
>
> **Input:**  
>  u[] = {1, 2}  
> v[] = {2, 3}  
> w[] = {3, 1}  
> **Output:** 4

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Let’s suppose there are **n** leaf **l 1**, **l 2**, **l 3**,
……, **l n** and the cost of the path from root to each leaf is **c 1**, **c
2**, **c 3**, ……, **c n**.  
To travel from **l 1** to **l 2** some of the edges will be visited twice (
till the LCA of **l 1** and **l 2** all the edges will be visited twice ), for
**l 2** to **l 3** and some of the edges will be visited ( till the LCA of **l
2** and **l 3** all the edges will be visited twice ) twice and similarly
every edge of the tree will be visited twice ( observation ).

  

  

To minimize the cost of travelling, the maximum cost path from the root to
some leaf should be avoided.  
Hence the cost = ( **c 1** \+ **c 2** \+ **c 3** \+ …… + **c n**) – **max** (
**c 1**, **c 2**, **c 3**, ……, **c n**)  
 **min cost** = **(2 * sum of edge weight)** – **max** ( **c 1**, **c 2**, **c
3**, ……, **c n**)  
DFS can be used with some modification to find the largest distance.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of above approach

#include <bits/stdc++.h>

using namespace std;

class Edge{

 

 public:

 

 // from - The source of an edge

 // to - destination of an edge

 // wt - distance between two nodes

 int from;

 int to;

 long wt;

 Edge(int a, int b, long w)

 {

 from = a;

 to = b;

 wt = w;

 }

};

// Method to add an edge between two nodes

void add_edge(vector<vector<Edge>> &adj;_lis,

 int to, int from, long wt)

{

 adj_lis[from].push_back(Edge(from, to, wt));

 adj_lis[to].push_back(Edge(to, from, wt));

}

// DFS method to find distance

// between node 1 to other nodes

void dfs(vector<vector<Edge>> &adj;_lis,

 long val[], int v, int par,

 long sum, bool visited[])

{

 val[v] = sum;

 visited[v] = true;

 

 for(Edge e : adj_lis[v])

 {

 if (!visited[e.to])

 dfs(adj_lis, val, e.to,

 v, sum + e.wt, visited);

 }

}

// Driver code

int main()

{

 

 // Number of nodes

 // V - Total number of

 // nodes in a tree

 int v = 6;

 

 // adj_lis - It is used to

 // make the adjacency list of a tree

 vector<vector<Edge>> adj_lis(v);

 

 // val - This array stores the

 // distance from node 1 to node 'n'

 long val[v];

 

 bool visited[v];

 

 int sum = 0;

 

 // Edge from a node to another

 // node with some weight

 int from[] = { 2, 3, 5, 6, 4 };

 int to[] = { 1, 1, 2, 2, 1 };

 int wt[] = { 1, 4, 2, 50, 5 };

 

 for(int i = 0; i < v - 1; i++)

 {

 sum += 2 * wt[i];

 add_edge(adj_lis, to[i] - 1,

 from[i] - 1, wt[i]);

 }

 

 dfs(adj_lis, val, 0, -1, 0, visited);

 long large = INT_MIN;

 

 // Loop to find largest

 // distance in a val.

 int size = sizeof(val) / sizeof(long);

 

 for(int i = 1; i < size; i++)

 if (val[i] > large)

 large = val[i];

 

 cout << (sum - large);

}

// This code is contributed by sanjeev2552  
  
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

// Java implementation of the approach

import java.util.LinkedList;

import java.util.Scanner;

class Graph {

 class Edge {

 // from - The source of an edge

 // to - destination of an edge

 // wt - distance between two nodes

 int from;

 int to;

 long wt;

 Edge(int a, int b, long w)

 {

 from = a;

 to = b;

 wt = w;

 }

 }

 // adj_lis - It is used to

 // make the adjacency list of a tree

 // V - Total number of nodes in a tree

 // val - This array stores the

 // distance from node 1 to node 'n'

 static LinkedList<Edge>[] adj_lis;

 static int V;

 static long val[];

 Graph(int v)

 {

 this.V = v;

 adj_lis = new LinkedList[V];

 for (int i = 0; i < V; i++)

 adj_lis[i] = new LinkedList<>();

 }

 // Method to add an edge between two nodes

 void add_edge(int to, int from, long wt)

 {

 adj_lis[from].add(

 new Edge(from, to, wt));

 adj_lis[to].add(

 new Edge(to, from, wt));

 }

 // DFS method to find distance

 // between node 1 to other nodes

 void dfs(int v,

 int par,

 long sum,

 boolean[] visited)

 {

 val[v] = sum;

 visited[v] = true;

 for (Edge e : adj_lis[v]) {

 if (!visited[e.to])

 dfs(e.to,

 v,

 sum + e.wt,

 visited);

 }

 }

 // Driver code

 public static void main(String a[])

 {

 // Number of nodes

 int v = 6;

 Graph obj = new Graph(v);

 val = new long[v];

 boolean[] visited

 = new boolean[v];

 int sum = 0;

 // Edge from a node to another

 // node with some weight

 int from[] = { 2, 3, 5, 6, 4 };

 int to[] = { 1, 1, 2, 2, 1 };

 int wt[] = { 1, 4, 2, 50, 5 };

 for (int i = 0; i < v - 1; i++) {

 sum += 2 * wt[i];

 obj.add_edge(to[i] - 1,

 from[i] - 1,

 wt[i]);

 }

 obj.dfs(0, -1, 0, visited);

 long large = Integer.MIN_VALUE;

 // Loop to find largest

 // distance in a val.

 for (int i = 1; i < val.length;

 i++)

 if (val[i] > large)

 large = val[i];

 System.out.println(sum - large);

 }

}  
  
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

// C# implementation of above approach

using System;

using System.Collections.Generic;

class Graph

{

 public class Edge

 {

 // from - The source of an edge

 // to - destination of an edge

 // wt - distance between two nodes

 public int from;

 public int to;

 public long wt;

 public Edge(int a, int b, long w)

 {

 from = a;

 to = b;

 wt = w;

 }

 }

 // adj_lis - It is used to

 // make the adjacency list of a tree

 // V - Total number of nodes in a tree

 // val - This array stores the

 // distance from node 1 to node 'n'

 public static List<Edge>[] adj_lis;

 public static int V;

 public static long []val;

 public Graph(int v)

 {

 V = v;

 adj_lis = new List<Edge>[V];

 for (int i = 0; i < V; i++)

 adj_lis[i] = new List<Edge>();

 }

 // Method to add an edge between two nodes

 void add_edge(int to, int from, long wt)

 {

 adj_lis[from].Add(

 new Edge(from, to, wt));

 adj_lis[to].Add(

 new Edge(to, from, wt));

 }

 // DFS method to find distance

 // between node 1 to other nodes

 void dfs(int v,

 int par,

 long sum,

 bool[] visited)

 {

 val[v] = sum;

 visited[v] = true;

 foreach (Edge e in adj_lis[v])

 {

 if (!visited[e.to])

 dfs(e.to, v,

 sum + e.wt, visited);

 }

 }

 // Driver code

 public static void Main(String []a)

 {

 // Number of nodes

 int v = 6;

 Graph obj = new Graph(v);

 val = new long[v];

 bool []visited = new bool[v];

 int sum = 0;

 // Edge from a node to another

 // node with some weight

 int []from = { 2, 3, 5, 6, 4 };

 int []to = { 1, 1, 2, 2, 1 };

 int []wt = { 1, 4, 2, 50, 5 };

 for (int i = 0; i < v - 1; i++)

 {

 sum += 2 * wt[i];

 obj.add_edge(to[i] - 1,

 from[i] - 1, wt[i]);

 }

 obj.dfs(0, -1, 0, visited);

 long large = int.MinValue;

 // Loop to find largest

 // distance in a val.

 for (int i = 1; i < val.Length;

 i++)

 if (val[i] > large)

 large = val[i];

 Console.WriteLine(sum - large);

 }

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    73

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

