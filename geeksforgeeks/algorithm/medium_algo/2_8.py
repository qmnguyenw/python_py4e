Find if there is a path between two vertices in an undirected graph



Given an **undirected graph** with **N** vertices and **E** edges and two
vertices **(U, V)** from the graph, the task is to detect if a path exists
between these two vertices. Print _“Yes”_ if a path exists and _“No”_
otherwise.

 **Examples:**

> ![](https://media.geeksforgeeks.org/wp-
> content/uploads/20200522164343/GFGmain2-200x145.png)
>
> U = 1, V = 2  
> **Output:** No  
> **Explanation:**  
> There is no edge between the two points and hence its not possible to reach
> 2 from 1.
>
>  **Input:**  
>
>
>  
>
>
>  
>
>
> ![](https://media.geeksforgeeks.org/wp-
> content/uploads/20200522164250/GFGmain1-200x158.png)
>
> U = 1, V = 3  
> **Output:** Yes  
> **Explanation:** Vertex 3 from vertex 1 via vertices 2 or 4.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:**  
The idea is to use Floyd Warshall Algorithm. To solve the problem, we cneed to
try out all intermediate vertices ranging **[1, N]** and check:

  1. If there is a direct edge already which exists between the two nodes.
  2. Or we have a path from node **i** to intermediate node **k** and from node **k** to node **j**.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to detect if a path

// exists between any two vertices

// for the given undirected graph

#include <bits/stdc++.h>

using namespace std;

// Class representing a undirected

// graph using matrix

// representation

class Graph {

 int V;

 int** g;

public:

 Graph(int V);

 // Function to add an edge to graph

 void addEdge(int v, int w);

 // Function to check if

 // there exists a path or not

 bool isReachable(int s, int d);

 // function to compute paths

 // in the matrix using

 // Floyd Warshall Algorithm

 void computePaths();

};

Graph::Graph(int V)

{

 this->V = V;

 g = new int*[V + 1];

 for (int i = 1; i < V + 1; i++) {

 // Rows may not be contiguous

 g[i] = new int[V + 1];

 // Initialize all entries

 // as false to indicate

 // that there are

 // no edges initially

 memset(g[i], 0, (V + 1) * sizeof(int));

 }

 // Initializing node to itself

 // as it is always reachable

 for (int i = 1; i <= V; i++)

 g[i][i] = 1;

}

// Function to add edge between nodes

void Graph::addEdge(int v, int w)

{

 g[v][w] = 1;

 g[w][v] = 1;

}

// Function to compute the path

void Graph::computePaths()

{

 // Use Floyd Warshall algorithm

 // to detect if a path exists

 for (int k = 1; k <= V; k++) {

 // Try every vertex as an

 // intermediate vertex

 // to check if a path exists

 for (int i = 1; i <= V; i++) {

 for (int j = 1; j <= V; j++)

 g[i][j] = g[i][j]

 | (g[i][k]

 && g[k][j]);

 }

 }

}

// Function to check if nodes are reachable

bool Graph::isReachable(int s, int d)

{

 if (g[s][d] == 1)

 return true;

 else

 return false;

}

// Driver code

int main()

{

 Graph _g(4);

 _g.addEdge(1, 2);

 _g.addEdge(2, 3);

 _g.addEdge(1, 4);

 _g.computePaths();

 int u = 4, v = 3;

 if (_g.isReachable(u, v))

 cout << "Yes\n";

 else

 cout << "No\n";

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

// Java program to detect if a path

// exists between any two vertices

// for the given undirected graph

import java.util.Arrays;

class GFG{

// Class representing a undirected

// graph using matrix representation

static class Graph

{

 int V;

 int[][] g;

 public Graph(int V)

 {

 this.V = V;

 

 // Rows may not be contiguous

 g = new int[V + 1][V + 1];

 for(int i = 0; i < V + 1; i++)

 {

 

 // Initialize all entries

 // as false to indicate

 // that there are

 // no edges initially

 Arrays.fill(g[i], 0);

 }

 // Initializing node to itself

 // as it is always reachable

 for(int i = 1; i <= V; i++)

 g[i][i] = 1;

 }

 

 // Function to add edge between nodes

 void addEdge(int v, int w)

 {

 g[v][w] = 1;

 g[w][v] = 1;

 }

 // Function to check if nodes are reachable

 boolean isReachable(int s, int d)

 {

 if (g[s][d] == 1)

 return true;

 else

 return false;

 }

 

 // Function to compute the path

 void computePaths()

 {

 

 // Use Floyd Warshall algorithm

 // to detect if a path exists

 for(int k = 1; k <= V; k++)

 {

 

 // Try every vertex as an

 // intermediate vertex

 // to check if a path exists

 for(int i = 1; i <= V; i++)

 {

 for(int j = 1; j <= V; j++)

 g[i][j] = g[i][j] | ((g[i][k] != 0 &&

 g[k][j] != 0) ? 1 : 0);

 }

 }

 }

};

// Driver code

public static void main(String[] args)

{

 Graph _g = new Graph(4);

 _g.addEdge(1, 2);

 _g.addEdge(2, 3);

 _g.addEdge(1, 4);

 _g.computePaths();

 int u = 4, v = 3;

 if (_g.isReachable(u, v))

 System.out.println("Yes");

 else

 System.out.println("No");

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

# Python3 program to detect if a path

# exists between any two vertices

# for the given undirected graph

# Class representing a undirected

# graph using matrix

# representation

class Graph:

 

 def __init__(self, V):

 

 self.V = V

 

 # Initialize all entries

 # as false to indicate

 # that there are

 # no edges initially

 self.g = [[0 for j in range(self.V + 1)]

 for i in range(self.V + 1)]

 

 # Initializing node to itself

 # as it is always reachable

 for i in range(self.V + 1):

 self.g[i][i] = 1

 # Function to add edge between nodes

 def addEdge(self, v, w):

 self.g[v][w] = 1

 self.g[w][v] = 1

 # Function to compute the path

 def computePaths(self):

 # Use Floyd Warshall algorithm

 # to detect if a path exists

 for k in range(1, self.V + 1):

 # Try every vertex as an

 # intermediate vertex

 # to check if a path exists

 for i in range(1, self.V + 1):

 for j in range(1, self.V + 1):

 self.g[i][j] = (self.g[i][j] |

 (self.g[i][k] and

 self.g[k][j]))

 

 # Function to check if nodes

 # are reachable

 def isReachable(self, s, d):

 if (self.g[s][d] == 1):

 return True

 else:

 return False

 

# Driver code

if __name__=='__main__':

 _g = Graph(4)

 _g.addEdge(1, 2)

 _g.addEdge(2, 3)

 _g.addEdge(1, 4)

 _g.computePaths()

 u = 4

 v = 3

 

 if (_g.isReachable(u, v)):

 print('Yes')

 else:

 print('No')

 

# This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

_**Time Complexity:** O(V3) _  
_**Auxiliary Space:** O(V2)_

 **Efficient Solution**  
We can either use BFS or DFS to find if there is a path from u to v. Below is
a BFS based solution

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to check if there is exist a path between

// two vertices of an undirected graph.

#include <iostream>

#include <list>

using namespace std;

// This class represents an undirected graph

// using adjacency list representation

class Graph {

 int V; // No. of vertices

 // Pointer to an array containing adjacency lists

 list<int>* adj;

public:

 Graph(int V); // Constructor

 // function to add an edge to graph

 void addEdge(int v, int w);

 bool isReachable(int s, int d);

};

Graph::Graph(int V)

{

 this->V = V;

 adj = new list<int>[V];

}

void Graph::addEdge(int v, int w)

{

 adj[v].push_back(w);

 adj[w].push_back(v);

}

// A BFS based function to check whether d is reachable from s.

bool Graph::isReachable(int s, int d)

{

 // Base case

 if (s == d)

 return true;

 // Mark all the vertices as not visited

 bool* visited = new bool[V];

 for (int i = 0; i < V; i++)

 visited[i] = false;

 // Create a queue for BFS

 list<int> queue;

 // Mark the current node as visited and enqueue it

 visited[s] = true;

 queue.push_back(s);

 // it will be used to get all adjacent vertices of a vertex

 list<int>::iterator i;

 while (!queue.empty()) {

 // Dequeue a vertex from queue and print it

 s = queue.front();

 queue.pop_front();

 // Get all adjacent vertices of the dequeued vertex s

 // If a adjacent has not been visited, then mark it

 // visited and enqueue it

 for (i = adj[s].begin(); i != adj[s].end(); ++i) {

 // If this adjacent node is the destination node,

 // then return true

 if (*i == d)

 return true;

 // Else, continue to do BFS

 if (!visited[*i]) {

 visited[*i] = true;

 queue.push_back(*i);

 }

 }

 }

 // If BFS is complete without visiting d

 return false;

}

// Driver program to test methods of graph class

int main()

{

 // Create a graph given in the above diagram

 Graph g(4);

 g.addEdge(0, 1);

 g.addEdge(0, 2);

 g.addEdge(1, 2);

 g.addEdge(2, 0);

 g.addEdge(2, 3);

 g.addEdge(3, 3);

 int u = 1, v = 3;

 if (g.isReachable(u, v))

 cout << "\n There is a path from " << u << " to " << v;

 else

 cout << "\n There is no path from " << u << " to " << v;

 return 0;

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

# Python3 program to check if there is exist a path between

# two vertices of an undirected graph.

from collections import deque

def addEdge(v, w):

 global adj

 adj[v].append(w)

 adj[w].append(v)

# A BFS based function to check whether d is reachable from s.

def isReachable(s, d):

 

 # Base case

 if (s == d):

 return True

 # Mark all the vertices as not visited

 visited = [False for i in range(V)]

 # Create a queue for BFS

 queue = deque()

 # Mark the current node as visited and enqueue it

 visited[s] = True

 queue.append(s)

 while (len(queue) > 0):

 

 # Dequeue a vertex from queue and prit

 s = queue.popleft()

 # queue.pop_front()

 # Get all adjacent vertices of the dequeued vertex s

 # If a adjacent has not been visited, then mark it

 # visited and enqueue it

 for i in adj[s]:

 # If this adjacent node is the destination node,

 # then return true

 if (i == d):

 return True

 # Else, continue to do BFS

 if (not visited[i]):

 visited[i] = True

 queue.append(i)

 # If BFS is complete without visiting d

 return False

# Driver program to test methods of graph class

if __name__ == '__main__':

 

 # Create a graph given in the above diagram

 V = 4

 adj = [[] for i in range(V+1)]

 addEdge(0, 1)

 addEdge(0, 2)

 addEdge(1, 2)

 addEdge(2, 0)

 addEdge(2, 3)

 addEdge(3, 3)

 u,v = 1, 3

 if (isReachable(u, v)):

 print("There is a path from",u,"to",v)

 else:

 print("There is no path from",u,"to",v)

 # This code is contributed by mohit kumar 29.  
  
---  
  
 __

 __

 **Output:**

    
    
    There is a path from 1 to 3

_**Time Complexity:** O(V + E) _  
_**Auxiliary Space:** O(V)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

