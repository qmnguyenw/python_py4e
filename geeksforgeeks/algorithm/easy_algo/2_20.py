Shortest Path Faster Algorithm



 **Prerequisites:**Bellman-Ford Algorithm

Given a **directed weighted graph** with **V** vertices, **E** edges and a
source vertex **S**. The task is to find the shortest path from the source
vertex to all other vertices in the given graph.

 **Example:**

>  **Input:** V = 5, S = 1, arr = {{1, 2, 1}, {2, 3, 7}, {2, 4, -2}, {1, 3,
> 8}, {1, 4, 9}, {3, 4, 3}, {2, 5, 3}, {4, 5, -3}}  
>  **Output:**  
>  1, 0  
> 2, 1  
> 3, 8  
> 4, -1  
> 5, -4  
>  **Explanation:** For the given input, the shortest path from 1 to 1 is 0, 1
> to 2 is 1 and so on.
>
>  **Input:** V = 5, S = 1, arr = {{1, 2, -1}, {1, 3, 4}, {2, 3, 3}, {2, 4,
> 2}, {2, 5, 2}, {4, 3, 5}, {4, 2, 1}, {5, 4, 3}}  
>  **Output:**  
>  1, 0  
> 2, -1  
> 3, 2  
> 4, 1  
> 5, 1
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The shortest path faster algorithm is based on Bellman-Ford
algorithm where every vertex is used to relax its adjacent vertices but in SPF
algorithm, a queue of vertices is maintained and a vertex is added to the
queue only if that vertex is relaxed. This process repeats until no more
vertex can be relaxed.  
The following steps can be performed to compute the result:

  1. Create an array **d[]** to store the shortest distance of all vertex from the source vertex. Initialize this array by infinity except for d[S] = 0 where **S** is source vertex.
  2. Create a queue **Q** and push starting source vertex in it.
    * while Queue is not empty, do the following for each edge(u, v) in the graph
      * If d[v] > d[u] + weight of edge(u, v)
      * d[v] = d[u] + weight of edge(u, v)
      * If vertex v is not present in Queue, then push the vertex v into the Queue.

 **Note:** The term **relaxation** means updating the cost of all vertices
connected to a vertex **v** if those costs would be improved by including the
path via vertex **v**. This can be understood better from an analogy between
the estimate of the shortest path and the length of a helical tension spring,
which is not designed for compression. Initially, the cost of the shortest
path is an overestimate, likened to a stretched-out spring. As shorter paths
are found, the estimated cost is lowered, and the spring is relaxed.
Eventually, the shortest path, if one exists, is found and the spring has been
relaxed to its resting length.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of SPFA

 

#include <bits/stdc++.h>

using namespace std;

 

// Graph is stored as vector of vector of pairs

// first element of pair store vertex

// second element of pair store weight

vector<pair<int, int> > graph[100000];

 

// Function to add edges in the graph

// connecting a pair of vertex(frm) and weight

// to another vertex(to) in graph

void addEdge(int frm, int to, int weight)

{

 

 graph[frm].push_back({ to, weight });

}

 

// Function to print shortest distance from source

void print_distance(int d[], int V)

{

 cout << "Vertex \t\t Distance"

 << " from source" << endl;

 

 for (int i = 1; i <= V; i++) {

 printf("%d \t\t %d\n", i, d[i]);

 }

}

 

// Function to compute the SPF algorithm

void shortestPathFaster(int S, int V)

{

 // Create array d to store shortest distance

 int d[V + 1];

 

 // Boolean array to check if vertex

 // is present in queue or not

 bool inQueue[V + 1] = { false };

 

 // Initialize the distance from source to

 // other vertex as INT_MAX(infinite)

 for (int i = 0; i <= V; i++) {

 d[i] = INT_MAX;

 }

 d[S] = 0;

 

 queue<int> q;

 q.push(S);

 inQueue[S] = true;

 

 while (!q.empty()) {

 

 // Take the front vertex from Queue

 int u = q.front();

 q.pop();

 inQueue[u] = false;

 

 // Relaxing all the adjacent edges of

 // vertex taken from the Queue

 for (int i = 0; i < graph[u].size(); i++) {

 

 int v = graph[u][i].first;

 int weight = graph[u][i].second;

 

 if (d[v] > d[u] + weight) {

 d[v] = d[u] + weight;

 

 // Check if vertex v is in Queue or not

 // if not then push it into the Queue

 if (!inQueue[v]) {

 q.push(v);

 inQueue[v] = true;

 }

 }

 }

 }

 

 // Print the result

 print_distance(d, V);

}

 

// Driver code

int main()

{

 int V = 5;

 int S = 1;

 

 // Connect vertex a to b with weight w

 // addEdge(a, b, w)

 

 addEdge(1, 2, 1);

 addEdge(2, 3, 7);

 addEdge(2, 4, -2);

 addEdge(1, 3, 8);

 addEdge(1, 4, 9);

 addEdge(3, 4, 3);

 addEdge(2, 5, 3);

 addEdge(4, 5, -3);

 

 // Calling shortestPathFaster function

 shortestPathFaster(S, V);

 

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

// Java implementation of SPFA

import java.util.*;

 

class GFG

{

 static class pair

 { 

 int first, second; 

 public pair(int first, int second) 

 { 

 this.first = first; 

 this.second = second; 

 } 

 }

 

// Graph is stored as vector of vector of pairs

// first element of pair store vertex

// second element of pair store weight

static Vector<pair > []graph = new Vector[100000];

 

// Function to add edges in the graph

// connecting a pair of vertex(frm) and weight

// to another vertex(to) in graph

static void addEdge(int frm, int to, int weight)

{

 

 graph[frm].add(new pair( to, weight ));

}

 

// Function to print shortest distance from source

static void print_distance(int d[], int V)

{

 System.out.print("Vertex \t\t Distance"

 + " from source" +"\n");

 

 for (int i = 1; i <= V; i++) 

 {

 System.out.printf("%d \t\t %d\n", i, d[i]);

 }

}

 

// Function to compute the SPF algorithm

static void shortestPathFaster(int S, int V)

{

 // Create array d to store shortest distance

 int []d = new int[V + 1];

 

 // Boolean array to check if vertex

 // is present in queue or not

 boolean []inQueue = new boolean[V + 1];

 

 // Initialize the distance from source to

 // other vertex as Integer.MAX_VALUE(infinite)

 for (int i = 0; i <= V; i++) 

 {

 d[i] = Integer.MAX_VALUE;

 }

 d[S] = 0;

 

 Queue<Integer> q = new LinkedList<>();

 q.add(S);

 inQueue[S] = true;

 

 while (!q.isEmpty())

 {

 

 // Take the front vertex from Queue

 int u = q.peek();

 q.remove();

 inQueue[u] = false;

 

 // Relaxing all the adjacent edges of

 // vertex taken from the Queue

 for (int i = 0; i < graph[u].size(); i++)

 {

 

 int v = graph[u].get(i).first;

 int weight = graph[u].get(i).second;

 

 if (d[v] > d[u] + weight) 

 {

 d[v] = d[u] + weight;

 

 // Check if vertex v is in Queue or not

 // if not then push it into the Queue

 if (!inQueue[v]) 

 {

 q.add(v);

 inQueue[v] = true;

 }

 }

 }

 }

 

 // Print the result

 print_distance(d, V);

}

 

// Driver code

public static void main(String[] args)

{

 int V = 5;

 int S = 1;

 for (int i = 0; i < graph.length; i++)

 {

 graph[i] = new Vector<pair>();

 }

 

 // Connect vertex a to b with weight w

 // addEdge(a, b, w)

 addEdge(1, 2, 1);

 addEdge(2, 3, 7);

 addEdge(2, 4, -2);

 addEdge(1, 3, 8);

 addEdge(1, 4, 9);

 addEdge(3, 4, 3);

 addEdge(2, 5, 3);

 addEdge(4, 5, -3);

 

 // Calling shortestPathFaster function

 shortestPathFaster(S, V);

}

}

 

// This code is contributed by 29AjayKumar  
  
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

// C# implementation of SPFA

using System;

using System.Collections.Generic;

 

class GFG

{

 class pair

 { 

 public int first, second; 

 public pair(int first, int second) 

 { 

 this.first = first; 

 this.second = second; 

 } 

 }

 

// Graph is stored as vector of vector of pairs

// first element of pair store vertex

// second element of pair store weight

static List<pair> []graph = new List<pair>[100000];

 

// Function to add edges in the graph

// connecting a pair of vertex(frm) and weight

// to another vertex(to) in graph

static void addEdge(int frm, int to, int weight)

{

 

 graph[frm].Add(new pair( to, weight ));

}

 

// Function to print shortest distance from source

static void print_distance(int []d, int V)

{

 Console.Write("Vertex \t\t Distance"

 + " from source" +"\n");

 

 for (int i = 1; i <= V; i++) 

 {

 Console.Write("{0} \t\t {1}\n", i, d[i]);

 }

}

 

// Function to compute the SPF algorithm

static void shortestPathFaster(int S, int V)

{

 // Create array d to store shortest distance

 int []d = new int[V + 1];

 

 // Boolean array to check if vertex

 // is present in queue or not

 bool []inQueue = new bool[V + 1];

 

 // Initialize the distance from source to

 // other vertex as int.MaxValue(infinite)

 for (int i = 0; i <= V; i++) 

 {

 d[i] = int.MaxValue;

 }

 d[S] = 0;

 

 Queue<int> q = new Queue<int>();

 q.Enqueue(S);

 inQueue[S] = true;

 

 while (q.Count!=0)

 {

 

 // Take the front vertex from Queue

 int u = q.Peek();

 q.Dequeue();

 inQueue[u] = false;

 

 // Relaxing all the adjacent edges of

 // vertex taken from the Queue

 for (int i = 0; i < graph[u].Count; i++)

 {

 

 int v = graph[u][i].first;

 int weight = graph[u][i].second;

 

 if (d[v] > d[u] + weight) 

 {

 d[v] = d[u] + weight;

 

 // Check if vertex v is in Queue or not

 // if not then push it into the Queue

 if (!inQueue[v]) 

 {

 q.Enqueue(v);

 inQueue[v] = true;

 }

 }

 }

 }

 

 // Print the result

 print_distance(d, V);

}

 

// Driver code

public static void Main(String[] args)

{

 int V = 5;

 int S = 1;

 for (int i = 0; i < graph.Length; i++)

 {

 graph[i] = new List<pair>();

 }

 

 // Connect vertex a to b with weight w

 // addEdge(a, b, w)

 addEdge(1, 2, 1);

 addEdge(2, 3, 7);

 addEdge(2, 4, -2);

 addEdge(1, 3, 8);

 addEdge(1, 4, 9);

 addEdge(3, 4, 3);

 addEdge(2, 5, 3);

 addEdge(4, 5, -3);

 

 // Calling shortestPathFaster function

 shortestPathFaster(S, V);

}

}

 

// This code is contributed by PrinciRaj1992  
  
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

# Python3 implementation of SPFA

from collections import deque

 

# Graph is stored as vector of vector of pairs

# first element of pair store vertex

# second element of pair store weight

graph = [[] for _ in range(100000)]

 

# Function to add edges in the graph

# connecting a pair of vertex(frm) and weight

# to another vertex(to) in graph

def addEdge(frm, to, weight):

 

 graph[frm].append([to, weight])

 

# Function to prshortest distance from source

def print_distance(d, V):

 print("Vertex","\t","Distance from source")

 

 for i in range(1, V + 1):

 print(i,"\t",d[i])

 

# Function to compute the SPF algorithm

def shortestPathFaster(S, V):

 

 # Create array d to store shortest distance

 d = [10**9]*(V + 1)

 

 # Boolean array to check if vertex

 # is present in queue or not

 inQueue = [False]*(V + 1)

 

 d[S] = 0

 

 q = deque()

 q.append(S)

 inQueue[S] = True

 

 while (len(q) > 0):

 

 # Take the front vertex from Queue

 u = q.popleft()

 inQueue[u] = False

 

 # Relaxing all the adjacent edges of

 # vertex taken from the Queue

 for i in range(len(graph[u])):

 

 v = graph[u][i][0]

 weight = graph[u][i][1]

 

 if (d[v] > d[u] + weight):

 d[v] = d[u] + weight

 

 # Check if vertex v is in Queue or not

 # if not then append it into the Queue

 if (inQueue[v] == False):

 q.append(v)

 inQueue[v] = True

 

 # Print the result

 print_distance(d, V)

 

# Driver code

if __name__ == '__main__':

 V = 5

 S = 1

 

 # Connect vertex a to b with weight w

 # addEdge(a, b, w)

 

 addEdge(1, 2, 1)

 addEdge(2, 3, 7)

 addEdge(2, 4, -2)

 addEdge(1, 3, 8)

 addEdge(1, 4, 9)

 addEdge(3, 4, 3)

 addEdge(2, 5, 3)

 addEdge(4, 5, -3)

 

 # Calling shortestPathFaster function

 shortestPathFaster(S, V)

 

# This code is contributed by mohit kumar 29  
  
---  
  
 __

 __

 **Output:**

    
    
    Vertex    Distance from source
    1          0
    2          1
    3          8
    4          -1
    5          -4
    

**Time Complexity:**  
 **Average Time Complexity:** O(|E|)  
 **Worstcase Time Complexity** : O(|V|.|E|)  
 **Note:** Bound on average runtime has not been proved yet.

 **References:** Shortest Path Faster Algorithm

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

