Implementation of BFS using adjacency matrix



Breadth First Search (BFS) has been discussed in this article which uses
adjacency list for the graph representation. In this article, adjacency matrix
will be used to represent the graph.

 **Adjacency matrix representation:** In adjacency matrix representation of a
graph, the matrix **mat[][]** of size n*n (where n is the number of vertices)
will represent the edges of the graph where **mat[i][j] = 1** represents that
there is an edge between the vertices **i** and **j** while **mat[i][j] = 0**
represents that there is no edge between the vertices **i** and **j**.  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190920114902/btreenew_img.jpg)

Below is the adjacency matrix representation of the graph shown in the above
image:

    
    
      0 1 2 3
    0 0 1 1 0 
    1 1 0 0 1 
    2 1 0 0 0 
    3 0 1 0 0

 **Examples:**

  

  

    
    
    **Input:** source = 0

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190920114902/btreenew_img.jpg)

    
    
     **Output:** 0 1 2 3
    
    **Input:** source = 1

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190920125614/graph2newcr_img.jpg)

    
    
     **Output:** 1 0 2 3 4

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  * Create a matrix of size n*n where every element is 0 representing there is no edge in the graph.
  * Now, for every edge of the graph between the vertices i and j set mat[i][j] = 1.
  * After the adjacency matrix has been created and filled, find the BFS traversal of the graph as described in this post.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <bits/stdc++.h>

using namespace std;

class Graph {

 // Number of vertex

 int v;

 // Number of edges

 int e;

 // Adjacency matrix

 int** adj;

public:

 // To create the initial adjacency matrix

 Graph(int v, int e);

 // Function to insert a new edge

 void addEdge(int start, int e);

 // Function to display the BFS traversal

 void BFS(int start);

};

// Function to fill the empty adjacency matrix

Graph::Graph(int v, int e)

{

 this->v = v;

 this->e = e;

 adj = new int*[v];

 for (int row = 0; row < v; row++) {

 adj[row] = new int[v];

 for (int column = 0; column < v; column++) {

 adj[row][column] = 0;

 }

 }

}

// Function to add an edge to the graph

void Graph::addEdge(int start, int e)

{

 // Considering a bidirectional edge

 adj[start][e] = 1;

 adj[e][start] = 1;

}

// Function to perform BFS on the graph

void Graph::BFS(int start)

{

 // Visited vector to so that

 // a vertex is not visited more than once

 // Initializing the vector to false as no

 // vertex is visited at the beginning

 vector<bool> visited(v, false);

 vector<int> q;

 q.push_back(start);

 // Set source as visited

 visited[start] = true;

 int vis;

 while (!q.empty()) {

 vis = q[0];

 // Print the current node

 cout << vis << " ";

 q.erase(q.begin());

 // For every adjacent vertex to the current vertex

 for (int i = 0; i < v; i++) {

 if (adj[vis][i] == 1 && (!visited[i])) {

 // Push the adjacent node to the queue

 q.push_back(i);

 // Set

 visited[i] = true;

 }

 }

 }

}

// Driver code

int main()

{

 int v = 5, e = 4;

 // Create the graph

 Graph G(v, e);

 G.addEdge(0, 1);

 G.addEdge(0, 2);

 G.addEdge(1, 3);

 G.BFS(0);

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

// Java implementation of the approach

import java.util.ArrayList;

import java.util.Arrays;

import java.util.List;

class GFG{

static class Graph

{

 

 // Number of vertex

 int v;

 // Number of edges

 int e;

 // Adjacency matrix

 int[][] adj;

 // Function to fill the empty

 // adjacency matrix

 Graph(int v, int e)

 {

 this.v = v;

 this.e = e;

 

 adj = new int[v][v];

 for(int row = 0; row < v; row++)

 Arrays.fill(adj[row], 0);

 }

 

 // Function to add an edge to the graph

 void addEdge(int start, int e)

 {

 

 // Considering a bidirectional edge

 adj[start][e] = 1;

 adj[e][start] = 1;

 }

 // Function to perform BFS on the graph

 void BFS(int start)

 {

 

 // Visited vector to so that

 // a vertex is not visited more than once

 // Initializing the vector to false as no

 // vertex is visited at the beginning

 boolean[] visited = new boolean[v];

 Arrays.fill(visited, false);

 List<Integer> q = new ArrayList<>();

 q.add(start);

 // Set source as visited

 visited[start] = true;

 int vis;

 while (!q.isEmpty())

 {

 vis = q.get(0);

 // Print the current node

 System.out.print(vis + " ");

 q.remove(q.get(0));

 // For every adjacent vertex to

 // the current vertex

 for(int i = 0; i < v; i++)

 {

 if (adj[vis][i] == 1 && (!visited[i]))

 {

 

 // Push the adjacent node to

 // the queue

 q.add(i);

 // Set

 visited[i] = true;

 }

 }

 }

 }

}

// Driver code

public static void main(String[] args)

{

 

 int v = 5, e = 4;

 // Create the graph

 Graph G = new Graph(v, e);

 G.addEdge(0, 1);

 G.addEdge(0, 2);

 G.addEdge(1, 3);

 G.BFS(0);

}

}

// This code is contributed by sanjeev2552  
  
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

class Graph:

 

 adj = []

 # Function to fill empty adjacency matrix

 def __init__(self, v, e):

 

 self.v = v

 self.e = e

 Graph.adj = [[0 for i in range(v)]

 for j in range(v)]

 # Function to add an edge to the graph

 def addEdge(self, start, e):

 

 # Considering a bidirectional edge

 Graph.adj[start][e] = 1

 Graph.adj[e][start] = 1

 # Function to perform DFS on the graph

 def BFS(self, start):

 

 # Visited vector to so that a

 # vertex is not visited more than

 # once Initializing the vector to

 # false as no vertex is visited at

 # the beginning

 visited = [False] * self.v

 q = [start]

 # Set source as visited

 visited[start] = True

 while q:

 vis = q[0]

 # Print current node

 print(vis, end = ' ')

 q.pop(0)

 

 # For every adjacent vertex to

 # the current vertex

 for i in range(self.v):

 if (Graph.adj[vis][i] == 1 and

 (not visited[i])):

 

 # Push the adjacent node

 # in the queue

 q.append(i)

 

 # set

 visited[i] = True

# Driver code

v, e = 5, 4

# Create the graph

G = Graph(v, e)

G.addEdge(0, 1)

G.addEdge(0, 2)

G.addEdge(1, 3)

# Perform BFS

G.BFS(0)

# This code is contributed by ng24_7  
  
---  
  
 __

 __

 **Output:**

    
    
    0 1 2 3

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

