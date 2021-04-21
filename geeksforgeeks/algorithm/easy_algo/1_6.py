Find if there is a path between two vertices in a directed graph | Set 2



Given a Directed Graph and two vertices in it, check whether there is a path
from the first given vertex to second.  
 **Example:**  

> **Consider the following Graph:**  
>
>
> ![](https://media.geeksforgeeks.org/wp-content/uploads/bfs-5.png)
>
> **Input :** (u, v) = (1, 3)  
> **Output:** Yes  
> **Explanation:**  
> There is a path from 1 to 3, 1 -> 2 -> 3
>
>  **Input :** (u, v) = (3, 6)  
> **Output:** No  
> **Explanation:**  
> There is no path from 3 to 6  
>
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

A BFS or DFS based solution of this problem is discuss here.  
 **Approach :** Here we will discuss a Dynamic Programming based solution
using Floyd Warshall Algorithm.

  * Create a boolean 2D matrix **mat** where **mat[i][j]** will be true if there is a path from vertex **i** to **j**.
  * For every starting vertex **i** and ending vertex **j** iterate over all intermediate vertex **k** and do check if there is a path for **i** to **j** through **k** then mark **mat[i][j]** as true.
  * Finally check if **mat[u][v]** is true then return true else return false.

Below is the implementation of the above approach :

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find if there is a

// path between two vertices in a

// directed graph using Dynamic Programming

#include <bits/stdc++.h>

using namespace std;

#define X 6

#define Z 2

// function to find if there is a

// path between two vertices in a

// directed graph

bool existPath(int V, int edges[X][Z],

 int u, int v)

{

 // dp matrix

 bool mat[V][V];

 memset(mat, false, sizeof(mat));

 // set dp[i][j]=true if there is

 // edge between i to j

 for (int i = 0; i < X; i++)

 mat[edges[i][0]][edges[i][1]] = true;

 // check for all intermediate vertex

 for (int k = 0; k < V; k++) {

 for (int i = 0; i < V; i++) {

 for (int j = 0; j < V; j++) {

 mat[i][j] = mat[i][j]

 || mat[i][k]

 && mat[k][j];

 }

 }

 }

 // if vertex is invalid

 if (u >= V || v >= V) {

 return false;

 }

 // if there is a path

 if (mat[u][v])

 return true;

 return false;

}

// Driver function

int main()

{

 int V = 4;

 int edges[X][Z]

 = { { 0, 2 }, { 0, 1 },

 { 1, 2 }, { 2, 3 },

 { 2, 0 }, { 3, 3 } };

 int u = 1, v = 3;

 if (existPath(V, edges, u, v))

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

// Java program to find if there is a path

// between two vertices in a directed graph

// using Dynamic Programming

import java.util.*;

class GFG{

 

static final int X = 6;

static final int Z = 2;

// Function to find if there is a

// path between two vertices in a

// directed graph

static boolean existPath(int V, int edges[][],

 int u, int v)

{

 

 // mat matrix

 boolean [][]mat = new boolean[V][V];

 // set mat[i][j]=true if there is

 // edge between i to j

 for (int i = 0; i < X; i++)

 mat[edges[i][0]][edges[i][1]] = true;

 // Check for all intermediate vertex

 for(int k = 0; k < V; k++)

 {

 for(int i = 0; i < V; i++)

 {

 for(int j = 0; j < V; j++)

 {

 mat[i][j] = mat[i][j] ||

 mat[i][k] &&

 mat[k][j];

 }

 }

 }

 // If vertex is invalid

 if (u >= V || v >= V)

 {

 return false;

 }

 // If there is a path

 if (mat[u][v])

 return true;

 return false;

}

// Driver code

public static void main(String[] args)

{

 int V = 4;

 int edges[][] = { { 0, 2 }, { 0, 1 },

 { 1, 2 }, { 2, 3 },

 { 2, 0 }, { 3, 3 } };

 int u = 1, v = 3;

 if (existPath(V, edges, u, v))

 System.out.print("Yes\n");

 else

 System.out.print("No\n");

}

}

// This code is contributed by Princi Singh  
  
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

# Python3 program to find if there

# is a path between two vertices in a

# directed graph using Dynamic Programming

X = 6

Z = 2

 

# Function to find if there is a

# path between two vertices in a

# directed graph

def existPath(V, edges, u, v):

 

 # dp matrix

 mat = [[False for i in range(V)]

 for j in range(V)]

 

 # Set dp[i][j]=true if there is

 # edge between i to j

 for i in range(X):

 mat[edges[i][0]][edges[i][1]] = True

 

 # Check for all intermediate vertex

 for k in range(V):

 for i in range(V):

 for j in range(V):

 mat[i][j] = (mat[i][j] or

 mat[i][k] and

 mat[k][j])

 

 # If vertex is invalid

 if (u >= V or v >= V):

 return False

 

 # If there is a path

 if (mat[u][v]):

 return True

 

 return False

# Driver code

V = 4

edges = [ [ 0, 2 ], [ 0, 1 ],

 [ 1, 2 ], [ 2, 3 ],

 [ 2, 0 ], [ 3, 3 ] ]

 

u, v = 1, 3

if (existPath(V, edges, u, v)):

 print("Yes")

else:

 print("No")

# This code is contributed by divyeshrabadiya07  
  
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

// C# program to find if there is a path

// between two vertices in a directed graph

// using Dynamic Programming

using System;

class GFG{

 

static readonly int X = 6;

static readonly int Z = 2;

// Function to find if there is a

// path between two vertices in a

// directed graph

static bool existPath(int V, int [,]edges,

 int u, int v)

{

 

 // mat matrix

 bool [,]mat = new bool[V, V];

 // set mat[i,j]=true if there is

 // edge between i to j

 for (int i = 0; i < X; i++)

 mat[edges[i, 0], edges[i, 1]] = true;

 // Check for all intermediate vertex

 for(int k = 0; k < V; k++)

 {

 for(int i = 0; i < V; i++)

 {

 for(int j = 0; j < V; j++)

 {

 mat[i, j] = mat[i, j] ||

 mat[i, k] &&

 mat[k, j];

 }

 }

 }

 // If vertex is invalid

 if (u >= V || v >= V)

 {

 return false;

 }

 // If there is a path

 if (mat[u, v])

 return true;

 return false;

}

// Driver code

public static void Main(String[] args)

{

 int V = 4;

 int [,]edges = { { 0, 2 }, { 0, 1 },

 { 1, 2 }, { 2, 3 },

 { 2, 0 }, { 3, 3 } };

 int u = 1, v = 3;

 if (existPath(V, edges, u, v))

 Console.Write("Yes\n");

 else

 Console.Write("No\n");

}

}

// This code is contributed by sapnasingh4991  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    
    
    
    

_**Time Complexity :** O ( V 3)_  
_**Auxiliary Space :** O ( V 2)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

