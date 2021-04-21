Finding shortest path between any two nodes using Floyd Warshall Algorithm



Given a **graph** and two nodes **u** and **v** , the task is to print the
shortest path between u and v using the Floyd Warshall algorithm.  
 **Examples:**  

> **Input:** u = 1, v = 3  
>
>
> ![](https://media.geeksforgeeks.org/wp-
> content/uploads/20200607004217/graph33.png)
>
> **Output:** 1 -> 2 -> 3  
> **Explanation:**  
> Shortest path from 1 to 3 is through vertex 2 with total cost 3.  
> The first edge is 1 -> 2 with cost 2 and the second edge is 2 -> 3 with cost
> 1.  
>  **Input:** u = 0, v = 2  
>
>
> ![](https://media.geeksforgeeks.org/wp-
> content/uploads/20200607004217/graph33.png)
>
>  
>
>
>  
>
>
> **Output:** 0 -> 1 -> 2  
> **Explanation:**  
> Shortest path from 0 to 2 is through vertex 1 with total cost = 5  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  

  * The main idea here is to use a matrix(2D array) that will keep track of the next node to point if the shortest path changes for any pair of nodes. Initially, the shortest path between any two nodes u and v is v (that is the direct edge from u -> v).   

  * Initialising the **Next** array  

> If the path exists between two nodes then **Next[u][v] = v**  
>  else we set **Next[u][v] = -1**  
>

  *   * Modification in Floyd Warshall Algorithm  

> Inside the **if condition of Floyd Warshall Algorithm** we’ll add a
> statement Next[i][j] = Next[i][k]  
> (that means we found the shortest path between i, j through an intermediate
> node k).  
>

  * This is how our **if condition** would look like   

    
    
    if(dis[i][j] > dis[i][k] + dis[k][j])
    {
        dis[i][j] = dis[i][k] + dis[k][j];
        **Next[i][j] = Next[i][k];**   
    }

  *   * For constructing path using these nodes we’ll simply start looping through the node **u** while updating its value to next[u][v] until we reach node **v**.  

    
    
    path = [u]
    while u != v:
        u = Next[u][v]
        path.append(u)

  * 

Below is the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the shortest

// path between any two nodes using

// Floyd Warshall Algorithm.

#include <bits/stdc++.h>

using namespace std;

#define MAXN 100

// Infinite value for array

const int INF = 1e7;

int dis[MAXN][MAXN];

int Next[MAXN][MAXN];

// Initializing the distance and

// Next array

void initialise(int V,

 vector<vector<int> >& graph)

{

 for (int i = 0; i < V; i++) {

 for (int j = 0; j < V; j++) {

 dis[i][j] = graph[i][j];

 // No edge between node

 // i and j

 if (graph[i][j] == INF)

 Next[i][j] = -1;

 else

 Next[i][j] = j;

 }

 }

}

// Function construct the shotest

// path between u and v

vector<int> constructPath(int u,

 int v)

{

 // If there's no path between

 // node u and v, simply return

 // an empty array

 if (Next[u][v] == -1)

 return {};

 // Storing the path in a vector

 vector<int> path = { u };

 while (u != v) {

 u = Next[u][v];

 path.push_back(u);

 }

 return path;

}

// Standard Floyd Warshall Algorithm

// with little modification Now if we find

// that dis[i][j] > dis[i][k] + dis[k][j]

// then we modify next[i][j] = next[i][k]

void floydWarshall(int V)

{

 for (int k = 0; k < V; k++) {

 for (int i = 0; i < V; i++) {

 for (int j = 0; j < V; j++) {

 // We cannot travel through

 // edge that doesn't exist

 if (dis[i][k] == INF

 || dis[k][j] == INF)

 continue;

 if (dis[i][j] > dis[i][k]

 + dis[k][j]) {

 dis[i][j] = dis[i][k]

 + dis[k][j];

 Next[i][j] = Next[i][k];

 }

 }

 }

 }

}

// Print the shortest path

void printPath(vector<int>& path)

{

 int n = path.size();

 for (int i = 0; i < n - 1; i++)

 cout << path[i] << " -> ";

 cout << path[n - 1] << endl;

}

// Driver code

int main()

{

 int V = 4;

 vector<vector<int> > graph

 = { { 0, 3, INF, 7 },

 { 8, 0, 2, INF },

 { 5, INF, 0, 1 },

 { 2, INF, INF, 0 } };

 // Function to initialise the

 // distance and Next array

 initialise(V, graph);

 // Calling Floyd Warshall Algorithm,

 // this will update the shortest

 // distance as well as Next array

 floydWarshall(V);

 vector<int> path;

 // Path from node 1 to 3

 cout << "Shortest path from 1 to 3: ";

 path = constructPath(1, 3);

 printPath(path);

 // Path from node 0 to 2

 cout << "Shortest path from 0 to 2: ";

 path = constructPath(0, 2);

 printPath(path);

 // path from node 3 to 2

 cout << "Shortest path from 3 to 2: ";

 path = constructPath(3, 2);

 printPath(path);

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

// Java program to find the shortest

// path between any two nodes using

// Floyd Warshall Algorithm.

import java.util.*;

class GFG{

static final int MAXN = 100;

// Infinite value for array

static int INF = (int) 1e7;

static int [][]dis = new int[MAXN][MAXN];

static int [][]Next = new int[MAXN][MAXN];

// Initializing the distance and

// Next array

static void initialise(int V,

 int [][] graph)

{

 for(int i = 0; i < V; i++)

 {

 for(int j = 0; j < V; j++)

 {

 dis[i][j] = graph[i][j];

 

 // No edge between node

 // i and j

 if (graph[i][j] == INF)

 Next[i][j] = -1;

 else

 Next[i][j] = j;

 }

 }

}

// Function conthe shotest

// path between u and v

static Vector<Integer> constructPath(int u,

 int v)

{

 // If there's no path between

 // node u and v, simply return

 // an empty array

 if (Next[u][v] == -1)

 return null;

 // Storing the path in a vector

 Vector<Integer> path = new Vector<Integer>();

 path.add(u);

 

 while (u != v)

 {

 u = Next[u][v];

 path.add(u);

 }

 return path;

}

// Standard Floyd Warshall Algorithm

// with little modification Now if we find

// that dis[i][j] > dis[i][k] + dis[k][j]

// then we modify next[i][j] = next[i][k]

static void floydWarshall(int V)

{

 for(int k = 0; k < V; k++)

 {

 for(int i = 0; i < V; i++)

 {

 for(int j = 0; j < V; j++)

 {

 

 // We cannot travel through

 // edge that doesn't exist

 if (dis[i][k] == INF ||

 dis[k][j] == INF)

 continue;

 

 if (dis[i][j] > dis[i][k] +

 dis[k][j])

 {

 dis[i][j] = dis[i][k] +

 dis[k][j];

 Next[i][j] = Next[i][k];

 }

 }

 }

 }

}

// Print the shortest path

static void printPath(Vector<Integer> path)

{

 int n = path.size();

 for(int i = 0; i < n - 1; i++)

 System.out.print(path.get(i) + " -> ");

 System.out.print(path.get(n - 1) + "\n");

}

// Driver code

public static void main(String[] args)

{

 int V = 4;

 int [][] graph = { { 0, 3, INF, 7 },

 { 8, 0, 2, INF },

 { 5, INF, 0, 1 },

 { 2, INF, INF, 0 } };

 // Function to initialise the

 // distance and Next array

 initialise(V, graph);

 // Calling Floyd Warshall Algorithm,

 // this will update the shortest

 // distance as well as Next array

 floydWarshall(V);

 Vector<Integer> path;

 // Path from node 1 to 3

 System.out.print("Shortest path from 1 to 3: ");

 path = constructPath(1, 3);

 printPath(path);

 // Path from node 0 to 2

 System.out.print("Shortest path from 0 to 2: ");

 path = constructPath(0, 2);

 printPath(path);

 // Path from node 3 to 2

 System.out.print("Shortest path from 3 to 2: ");

 path = constructPath(3, 2);

 printPath(path);

}

}

// This code is contributed by Amit Katiyar  
  
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

// C# program to find the shortest

// path between any two nodes using

// Floyd Warshall Algorithm.

using System;

using System.Collections.Generic;

class GFG{

static readonly int MAXN = 100;

// Infinite value for array

static int INF = (int)1e7;

static int [,]dis = new int[MAXN, MAXN];

static int [,]Next = new int[MAXN, MAXN];

// Initializing the distance and

// Next array

static void initialise(int V,

 int [,] graph)

{

 for(int i = 0; i < V; i++)

 {

 for(int j = 0; j < V; j++)

 {

 dis[i, j] = graph[i, j];

 

 // No edge between node

 // i and j

 if (graph[i, j] == INF)

 Next[i, j] = -1;

 else

 Next[i, j] = j;

 }

 }

}

// Function conthe shotest

// path between u and v

static List<int> constructPath(int u, int v)

{

 

 // If there's no path between

 // node u and v, simply return

 // an empty array

 if (Next[u, v] == -1)

 return null;

 // Storing the path in a vector

 List<int> path = new List<int>();

 path.Add(u);

 

 while (u != v)

 {

 u = Next[u, v];

 path.Add(u);

 }

 return path;

}

// Standard Floyd Warshall Algorithm

// with little modification Now if we find

// that dis[i,j] > dis[i,k] + dis[k,j]

// then we modify next[i,j] = next[i,k]

static void floydWarshall(int V)

{

 for(int k = 0; k < V; k++)

 {

 for(int i = 0; i < V; i++)

 {

 for(int j = 0; j < V; j++)

 {

 

 // We cannot travel through

 // edge that doesn't exist

 if (dis[i, k] == INF || 

 dis[k, j] == INF)

 continue;

 

 if (dis[i, j] > dis[i, k] +

 dis[k, j])

 {

 dis[i, j] = dis[i, k] + 

 dis[k, j];

 Next[i, j] = Next[i, k];

 }

 }

 }

 }

}

// Print the shortest path

static void printPath(List<int> path)

{

 int n = path.Count;

 

 for(int i = 0; i < n - 1; i++)

 Console.Write(path[i] + " -> ");

 

 Console.Write(path[n - 1] + "\n");

}

// Driver code

public static void Main(String[] args)

{

 int V = 4;

 int [,] graph = { { 0, 3, INF, 7 },

 { 8, 0, 2, INF },

 { 5, INF, 0, 1 },

 { 2, INF, INF, 0 } };

 // Function to initialise the

 // distance and Next array

 initialise(V, graph);

 // Calling Floyd Warshall Algorithm,

 // this will update the shortest

 // distance as well as Next array

 floydWarshall(V);

 List<int> path;

 // Path from node 1 to 3

 Console.Write("Shortest path from 1 to 3: ");

 path = constructPath(1, 3);

 printPath(path);

 // Path from node 0 to 2

 Console.Write("Shortest path from 0 to 2: ");

 path = constructPath(0, 2);

 printPath(path);

 // Path from node 3 to 2

 Console.Write("Shortest path from 3 to 2: ");

 path = constructPath(3, 2);

 printPath(path);

}

}

// This code is contributed by Amit Katiyar  
  
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

# Python3 program to find the shortest

# path between any two nodes using

# Floyd Warshall Algorithm.

# Initializing the distance and

# Next array

def initialise(V):

 global dis, Next

 for i in range(V):

 for j in range(V):

 dis[i][j] = graph[i][j]

 # No edge between node

 # i and j

 if (graph[i][j] == INF):

 Next[i][j] = -1

 else:

 Next[i][j] = j

# Function construct the shotest

# path between u and v

def constructPath(u, v):

 global graph, Next

 

 # If there's no path between

 # node u and v, simply return

 # an empty array

 if (Next[u][v] == -1):

 return {}

 # Storing the path in a vector

 path = [u]

 while (u != v):

 u = Next[u][v]

 path.append(u)

 return path

# Standard Floyd Warshall Algorithm

# with little modification Now if we find

# that dis[i][j] > dis[i][k] + dis[k][j]

# then we modify next[i][j] = next[i][k]

def floydWarshall(V):

 global dist, Next

 for k in range(V):

 for i in range(V):

 for j in range(V):

 

 # We cannot travel through

 # edge that doesn't exist

 if (dis[i][k] == INF or dis[k][j] == INF):

 continue

 if (dis[i][j] > dis[i][k] + dis[k][j]):

 dis[i][j] = dis[i][k] + dis[k][j]

 Next[i][j] = Next[i][k]

# Prthe shortest path

def printPath(path):

 n = len(path)

 for i in range(n - 1):

 print(path[i], end=" -> ")

 print (path[n - 1])

# Driver code

if __name__ == '__main__':

 MAXM,INF = 100,10**7

 dis = [[-1 for i in range(MAXM)] for i in
range(MAXM)]

 Next = [[-1 for i in range(MAXM)] for i in
range(MAXM)]

 V = 4

 graph = [ [ 0, 3, INF, 7 ],

 [ 8, 0, 2, INF ],

 [ 5, INF, 0, 1 ],

 [ 2, INF, INF, 0 ] ]

 # Function to initialise the

 # distance and Next array

 initialise(V)

 # Calling Floyd Warshall Algorithm,

 # this will update the shortest

 # distance as well as Next array

 floydWarshall(V)

 path = []

 # Path from node 1 to 3

 print("Shortest path from 1 to 3: ", end = "")

 path = constructPath(1, 3)

 printPath(path)

 # Path from node 0 to 2

 print("Shortest path from 0 to 2: ", end = "")

 path = constructPath(0, 2)

 printPath(path)

 # Path from node 3 to 2

 print("Shortest path from 3 to 2: ", end = "")

 path = constructPath(3, 2)

 printPath(path)

 # This code is contributed by mohit kumar 29  
  
---  
  
 __

 __

 **Output:**

    
    
    Shortest path from 1 to 3: 1 -> 2 -> 3
    Shortest path from 0 to 2: 0 -> 1 -> 2
    Shortest path from 3 to 2: 3 -> 0 -> 1 -> 2

**Complexity Analysis:**  

  * The time complexity for Floyd Warshall Algorithm is **O(V 3)**   

  * For finding shortest path time complexity is **O(V)** per query.   

**Note:** It would be efficient to use the Floyd Warshall Algorithm when your
graph contains a couple of hundred vertices and you need to answer multiple
queries related to the shortest path.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

