Count of unique lengths of connected components for an undirected graph using
STL



Given an undirected graph, the task is to find the size of each connected
component and print the number of unique sizes of connected components  

![](https://media.geeksforgeeks.org/wp-content/uploads/20200421194558/Count-
of-Connected-Components.png)

As depicted above, the count(size of the connected component) associated with
the connected components is 2, 3, and 2. Now, the **unique** count of the
components is 2 and 3. Hence, the expected result is **Count = 2**  
 **Examples:**

    
    
    **Input:** N = 7
    

![](https://media.geeksforgeeks.org/wp-content/uploads/20200421200010/Graph-
Connected-Example-300x157.png)

    
    
    **Output:** 1 2 Count = 2
            3 4 5 Count = 3
            6 7 Count = 2
            Unique Counts of connected components: 2
    
    **Input:** N = 10
    

![](https://media.geeksforgeeks.org/wp-content/uploads/20200421201526/Graph-
Connected-Example-1-300x98.png)

  

  

    
    
    **Output:** 1 Count = 1
            2 3 4 5 Count = 4
            6 7 8 Count = 3
            9 10 Count = 2
            Unique Counts of connected components: 4
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Prerequisites:** Depth First Search  
 **Approach:**  
The basic idea is to utilize the Depth First Search traversal method to keep a
track of the connected components in the undirected graph. An STL container
Set is used to store the unique counts of all such components since it is
known that a set has the property of storing unique elements in a sorted
manner. Finally, extracting the size of the Set gives us the necessary result.
The step-wise implementation is as follows:

  1. Initialize a hash container (Set), to store the unique counts of connected components.
  2. Recursively call Depth First Search traversal.
  3. For every vertex visited, store the count in the set container.
  4. The final size of the Set is the required result.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find unique count of

// connected components

#include <bits/stdc++.h>

using namespace std;

// Function to add edge in the garph

void add_edge(int u, int v, vector<int> graph[])

{

 graph[u].push_back(v);

 graph[v].push_back(u);

}

// Function to traverse the undirected graph

// using DFS algorithm and keep a track of

// individual lengths of connected chains

void depthFirst(int v, vector<int> graph[],

 vector<bool>& visited, int& ans)

{

 // Marking the visited vertex as true

 visited[v] = true;

 cout << v << " ";

 // Incrementing the count of

 // connected chain length

 ans++;

 for (auto i : graph[v]) {

 if (visited[i] == false) {

 // Recursive call to the DFS algorithm

 depthFirst(i, graph, visited, ans);

 }

 }

}

// Function to initialize the graph

// and display the result

void UniqueConnectedComponent(int n,

 vector<int> graph[])

{

 // Initializing boolean visited array

 // to mark visited vertices

 vector<bool> visited(n + 1, false);

 // Initializing a Set container

 unordered_set<int> result;

 // Following loop invokes DFS algorithm

 for (int i = 1; i <= n; i++) {

 if (visited[i] == false) {

 // ans variable stores the

 // individual counts

 int ans = 0;

 // DFS algorithm

 depthFirst(i, graph, visited, ans);

 // Inserting the counts of connected

 // components in set

 result.insert(ans);

 cout << "Count = " << ans << "\n";

 }

 }

 cout << "Unique Counts of "

 << "connected components: ";

 // The size of the Set container

 // gives the desired result

 cout << result.size() << "\n";

}

// Driver code

int main()

{

 // Number of nodes

 int n = 7;

 // Create graph

 vector<int> graph[n + 1];

 // Constructing the undirected graph

 add_edge(1, 2, graph);

 add_edge(3, 4, graph);

 add_edge(3, 5, graph);

 add_edge(6, 7, graph);

 // Function call

 UniqueConnectedComponent(n, graph);

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

// Java program to find

// unique count of

// connected components

import java.util.*;

class GFG{

// Function to add edge in the garph

static void add_edge(int u, int v,

 Vector<Integer> graph[])

{

 graph[u].add(v);

 graph[v].add(u);

}

// Function to traverse the undirected graph

// using DFS algorithm and keep a track of

// individual lengths of connected chains

static int depthFirst(int v,

 Vector<Integer> graph[],

 Vector<Boolean> visited,

 int ans)

{

 // Marking the visited vertex as true

 visited.add(v, true);

 System.out.print(v + " ");

 // Incrementing the count of

 // connected chain length

 ans++;

 for (int i : graph[v])

 {

 if (visited.get(i) == false)

 {

 // Recursive call to the DFS algorithm

 ans = depthFirst(i, graph, visited, ans);

 }

 }

 return ans;

}

// Function to initialize the graph

// and display the result

static void UniqueConnectedComponent(int n,

 Vector<Integer> graph[])

{

 // Initializing boolean visited array

 // to mark visited vertices

 Vector<Boolean> visited = new Vector<>();

 for(int i = 0; i < n + 1; i++)

 visited.add(false);

 

 // Initializing a Set container

 HashSet<Integer> result = new HashSet<>();

 // Following loop invokes DFS algorithm

 for (int i = 1; i <= n; i++)

 {

 if (visited.get(i) == false)

 {

 // ans variable stores the

 // individual counts

 int ans = 0;

 // DFS algorithm

 ans = depthFirst(i, graph, visited, ans);

 // Inserting the counts of connected

 // components in set

 result.add(ans);

 System.out.print("Count = " + 

 ans + "\n");

 }

 }

 System.out.print("Unique Counts of " +

 "connected components: ");

 // The size of the Set container

 // gives the desired result

 System.out.print(result.size() + "\n");

}

// Driver code

public static void main(String[] args)

{

 // Number of nodes

 int n = 7;

 // Create graph

 Vector<Integer> []graph = new Vector[n + 1];

 for (int i = 0; i < graph.length; i++)

 graph[i] = new Vector<Integer>();

 

 // Constructing the undirected graph

 add_edge(1, 2, graph);

 add_edge(3, 4, graph);

 add_edge(3, 5, graph);

 add_edge(6, 7, graph);

 // Function call

 UniqueConnectedComponent(n, graph);

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

# Python3 program to find unique count of

# connected components

graph = [[] for i in range(100 + 1)]

visited = [False] * (100 + 1)

ans = 0

# Function to add edge in the garph

def add_edge(u, v):

 

 graph[u].append(v)

 graph[v].append(u)

# Function to traverse the undirected graph

# using DFS algorithm and keep a track of

# individual lengths of connected chains

def depthFirst(v):

 

 global ans

 

 # Marking the visited vertex as true

 visited[v] = True

 print(v, end = " ")

 #print(ans,end="-")

 # Incrementing the count of

 # connected chain length

 ans += 1

 for i in graph[v]:

 if (visited[i] == False):

 

 # Recursive call to the

 # DFS algorithm

 depthFirst(i)

# Function to initialize the graph

# and display the result

def UniqueConnectedComponent(n):

 

 global ans

 # Initializing boolean visited array

 # to mark visited vertices

 # Initializing a Set container

 result = {}

 # Following loop invokes DFS algorithm

 for i in range(1, n + 1):

 if (visited[i] == False):

 

 # ans variable stores the

 # individual counts

 # ans = 0

 # DFS algorithm

 depthFirst(i)

 # Inserting the counts of connected

 # components in set

 result[ans] = 1

 print("Count = ", ans)

 ans = 0

 print("Unique Counts of connected "

 "components: ", end = "")

 # The size of the Set container

 # gives the desired result

 print(len(result))

# Driver code

if __name__ == '__main__':

 

 # Number of nodes

 n = 7

 # Create graph

 # Constructing the undirected graph

 add_edge(1, 2)

 add_edge(3, 4)

 add_edge(3, 5)

 add_edge(6, 7)

 # Function call

 UniqueConnectedComponent(n)

# This code is contributed by mohit kumar 29  
  
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

// C# program to find

// unique count of

// connected components

using System;

using System.Collections.Generic;

class GFG{

// Function to add edge in the garph

static void add_edge(int u, int v,

 List<int> []graph)

{

 graph[u].Add(v);

 graph[v].Add(u);

}

// Function to traverse the undirected graph

// using DFS algorithm and keep a track of

// individual lengths of connected chains

static int depthFirst(int v,

 List<int> []graph,

 List<Boolean> visited,

 int ans)

{

 // Marking the visited

 // vertex as true

 visited.Insert(v, true);

 Console.Write(v + " ");

 // Incrementing the count of

 // connected chain length

 ans++;

 foreach (int i in graph[v])

 {

 if (visited[i] == false)

 {

 // Recursive call to

 // the DFS algorithm

 ans = depthFirst(i, graph,

 visited, ans);

 }

 }

 return ans;

}

// Function to initialize the graph

// and display the result

static void UniqueConnectedComponent(int n,

 List<int> []graph)

{

 // Initializing bool visited array

 // to mark visited vertices

 List<Boolean> visited = new List<Boolean>();

 for(int i = 0; i < n + 1; i++)

 visited.Add(false);

 

 // Initializing a Set container

 HashSet<int> result = new HashSet<int>();

 // Following loop invokes DFS algorithm

 for (int i = 1; i <= n; i++)

 {

 if (visited[i] == false)

 {

 // ans variable stores the

 // individual counts

 int ans = 0;

 // DFS algorithm

 ans = depthFirst(i, graph, visited, ans);

 // Inserting the counts of connected

 // components in set

 result.Add(ans);

 Console.Write("Count = " + 

 ans + "\n");

 }

 }

 Console.Write("Unique Counts of " +

 "connected components: ");

 // The size of the Set container

 // gives the desired result

 Console.Write(result.Count + "\n");

}

// Driver code

public static void Main(String[] args)

{

 // Number of nodes

 int n = 7;

 // Create graph

 List<int> []graph = new List<int>[n + 1];

 for (int i = 0; i < graph.Length; i++)

 graph[i] = new List<int>();

 // Constructing the undirected graph

 add_edge(1, 2, graph);

 add_edge(3, 4, graph);

 add_edge(3, 5, graph);

 add_edge(6, 7, graph);

 // Function call

 UniqueConnectedComponent(n, graph);

}

}

// This code is contributed by shikhasingrajput  
  
---  
  
 __

 __

 **Output:**

    
    
    1 2 Count = 2
    3 4 5 Count = 3
    6 7 Count = 2
    Unique Counts of connected components: 2
    
    
    
    
    
    
    
    

**Time Complexity:**  
As evident from the above implementation, the graph is traversed using the
Depth First Search algorithm. The individual counts are stored using Set
container wherein the insertion operation takes O(1) time. The overall
complexity is solely based on the time taken by the DFS algorithm to run
recursively. Hence, the time complexity of the program is **O(E + V)** where E
is the number of edges and V is the number of vertices of the graph.  
**Auxiliary Space:** _O(N)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

