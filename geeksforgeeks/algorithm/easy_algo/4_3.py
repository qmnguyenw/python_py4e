Maximum number of nodes which can be reached from each node in a graph.



Given a graph with N nodes and K bidirectional edges between them find the
number of nodes which can be reachable from a particular. Two nodes X and Y
are said to be reachable if we can start at X and end at Y using any number of
edges.

**Note : A Node is reachable to itself.**

    
    
    **Input :** N = 7
           1            5
            \          / \
             2        6 __ 7
              \  
               3
                \
                 4
    
    **Output :** 4 4 4 4 3 3 3 
    From node 1 ,nodes {1,2,3,4} can be visited
    hence the answer is equal to 4
    From node 5,nodes {5,6,7} can be visited.
    hence the answer is equal to 3.
    Similarly, print the count for every node.
    
    **Input :** N = 8
          1              7
        /   \             \
       2     3              8   
        \   / \
          5    6
    **Output :** 6 6 6 6 6 6 2 2

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
To find the number of nodes reachable from a particular node, one thing to
observe is that we can reach from a node X to a node Y only when they are in
the same connected component.  
Since the graph is bidirectional, any node in a connected component to any
other node in the same connected components. Hence for a particular node X
number of nodes that will be reachable will be the number of nodes in that
particular component.Use depth-first search to find the answer.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

using namespace std;

const int maxx = 100005;

vector<int> graph[maxx];

// Function to perform the DFS calculating the

// count of the elements in a connected component

void dfs(int curr, int& cnt, int*

 visited, vector<int>& duringdfs)

{

 visited[curr] = 1;

 // Number of nodes in this component

 ++cnt;

 // Stores the nodes which belong

 // to current component

 duringdfs.push_back(curr);

 for (auto& child : graph[curr]) {

 // If the child is not visited

 if (visited[child] == 0) {

 dfs(child, cnt, visited, duringdfs);

 }

 }

}

// Function to return the desired

// count for every node in the graph

void MaximumVisit(int n, int k)

{

 // To keep track of nodes we visit

 int visited[maxx];

 // Mark every node unvisited

 memset(visited, 0, sizeof visited);

 int ans[maxx];

 // No of connected elements for each node

 memset(ans, 0, sizeof ans);

 vector<int> duringdfs;

 for (int i = 1; i <= n; ++i) {

 duringdfs.clear();

 int cnt = 0;

 // If a node is not visited, perform a DFS as

 // this node belongs to a different component

 // which is not yet visited

 if (visited[i] == 0) {

 cnt = 0;

 dfs(i, cnt, visited, duringdfs);

 }

 // Now store the count of all the visited

 // nodes for any particular component.

 for (auto& x : duringdfs) {

 ans[x] = cnt;

 }

 }

 

 // Print the result

 for (int i = 1; i <= n; ++i) {

 cout << ans[i] << " ";

 }

 cout << endl;

 return;

}

// Function to build the graph

void MakeGraph(){

 graph[1].push_back(2);

 graph[2].push_back(1);

 graph[2].push_back(3);

 graph[3].push_back(2);

 graph[3].push_back(4);

 graph[4].push_back(3);

 graph[5].push_back(6);

 graph[6].push_back(5);

 graph[6].push_back(7);

 graph[7].push_back(6);

 graph[5].push_back(7);

 graph[7].push_back(5);

}

// Driver code

int main()

{

 int N = 7, K = 6;

 

 // Build the graph

 MakeGraph();

 

 MaximumVisit(N, K);

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

// Java implementation of the above approach

import java.io.*;

import java.util.*;

class GFG

{

 static final int maxx = 100005;

 @SuppressWarnings("unchecked")

 static Vector<Integer>[] graph = new Vector[maxx];

 static Vector<Integer> duringdfs = new Vector<>();

 static int cnt = 0;

 // Function to perform the DFS calculating the

 // count of the elements in a connected component

 static void dfs(int curr, int[] visited)

 {

 visited[curr] = 1;

 // Number of nodes in this component

 ++cnt;

 // Stores the nodes which belong

 // to current component

 duringdfs.add(curr);

 for (int child : graph[curr])

 {

 // If the child is not visited

 if (visited[child] == 0)

 dfs(child, visited);

 }

 }

 // Function to return the desired

 // count for every node in the graph

 static void maximumVisit(int n, int k)

 {

 // To keep track of nodes we visit

 int[] visited = new int[maxx];

 // Mark every node unvisited

 Arrays.fill(visited, 0);

 int[] ans = new int[maxx];

 // No of connected elements for each node

 Arrays.fill(ans, 0);

 for (int i = 1; i <= n; i++)

 {

 duringdfs.clear();

 // If a node is not visited, perform a DFS as

 // this node belongs to a different component

 // which is not yet visited

 if (visited[i] == 0)

 {

 cnt = 0;

 dfs(i, visited);

 }

 // Now store the count of all the visited

 // nodes for any particular component.

 for (int x : duringdfs)

 ans[x] = cnt;

 }

 // Print the result

 for (int i = 1; i <= n; i++)

 System.out.print(ans[i] + " ");

 System.out.println();

 return;

 }

 // Function to build the graph

 static void makeGraph()

 {

 // Initializing graph

 for (int i = 0; i < maxx; i++)

 graph[i] = new Vector<>();

 graph[1].add(2);

 graph[2].add(1);

 graph[2].add(3);

 graph[3].add(2);

 graph[3].add(4);

 graph[4].add(3);

 graph[5].add(6);

 graph[6].add(5);

 graph[6].add(7);

 graph[7].add(6);

 graph[5].add(7);

 graph[7].add(5);

 }

 // Driver Code

 public static void main(String[] args)

 {

 int N = 7, K = 6;

 // Build the graph

 makeGraph();

 maximumVisit(N, K);

 }

}

// This code is contributed by

// sanjeev2552  
  
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

# Python3 implementation of the above approach

maxx = 100005

graph = [[] for i in range(maxx)]

# Function to perform the DFS calculating the 

# count of the elements in a connected component

def dfs(curr, cnt, visited, duringdfs):

 visited[curr] = 1

 

 # Number of nodes in this component

 cnt += 1

 

 # Stores the nodes which belong 

 # to current component

 duringdfs.append(curr)

 

 for child in graph[curr]:

 

 # If the child is not visited

 if (visited[child] == 0):

 cnt, duringdfs = dfs(child, cnt,

 visited, duringdfs)

 

 return cnt, duringdfs

 

# Function to return the desired 

# count for every node in the graph

def MaximumVisit(n, k):

 # To keep track of nodes we visit

 visited = [0 for i in range(maxx)]

 

 ans = [0 for i in range(maxx)]

 

 duringdfs = []

 

 for i in range(1, n + 1):

 duringdfs.clear()

 

 cnt = 0

 

 # If a node is not visited, perform a DFS as 

 # this node belongs to a different component

 # which is not yet visited

 if (visited[i] == 0):

 cnt = 0

 cnt, duringdfs = dfs(i, cnt,

 visited, duringdfs)

 

 # Now store the count of all the visited

 # nodes for any particular component.

 for x in duringdfs:

 ans[x] = cnt

 

 # Print the result

 for i in range(1, n + 1):

 print(ans[i], end = ' ')

 

 print()

 

 return

# Function to build the graph

def MakeGraph():

 

 graph[1].append(2)

 graph[2].append(1)

 graph[2].append(3)

 graph[3].append(2)

 graph[3].append(4)

 graph[4].append(3)

 graph[5].append(6)

 graph[6].append(5)

 graph[6].append(7)

 graph[7].append(6)

 graph[5].append(7)

 graph[7].append(5)

# Driver code

if __name__=='__main__':

 N = 7

 K = 6

 

 # Build the graph

 MakeGraph()

 

 MaximumVisit(N, K)

# This code is contributed by rutvik_56  
  
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

// C# implementation of the above approach

using System;

using System.Collections;

 

class GFG{

 

static int maxx = 100005;

static ArrayList[] graph = new ArrayList[maxx];

static ArrayList duringdfs = new ArrayList();

static int cnt = 0;

// Function to perform the DFS calculating the

// count of the elements in a connected component

static void dfs(int curr, int[] visited)

{

 visited[curr] = 1;

 

 // Number of nodes in this component

 ++cnt;

 // Stores the nodes which belong

 // to current component

 duringdfs.Add(curr);

 

 foreach(int child in graph[curr])

 {

 

 // If the child is not visited

 if (visited[child] == 0)

 dfs(child, visited);

 }

}

// Function to return the desired

// count for every node in the graph

static void maximumVisit(int n, int k)

{

 

 // To keep track of nodes we visit

 int[] visited = new int[maxx];

 // Mark every node unvisited

 Array.Fill(visited, 0);

 int[] ans = new int[maxx];

 // No of connected elements for each node

 Array.Fill(ans, 0);

 for(int i = 1; i <= n; i++)

 {

 duringdfs.Clear();

 // If a node is not visited, perform

 // a DFS as this node belongs to a

 // different component which is not

 // yet visited

 if (visited[i] == 0)

 {

 cnt = 0;

 dfs(i, visited);

 }

 // Now store the count of all the visited

 // nodes for any particular component.

 foreach(int x in duringdfs)

 ans[x] = cnt;

 }

 // Print the result

 for(int i = 1; i <= n; i++)

 Console.Write(ans[i] + " ");

 

 Console.WriteLine();

 return;

}

// Function to build the graph

static void makeGraph()

{

 

 // Initializing graph

 for(int i = 0; i < maxx; i++)

 graph[i] = new ArrayList();

 graph[1].Add(2);

 graph[2].Add(1);

 graph[2].Add(3);

 graph[3].Add(2);

 graph[3].Add(4);

 graph[4].Add(3);

 graph[5].Add(6);

 graph[6].Add(5);

 graph[6].Add(7);

 graph[7].Add(6);

 graph[5].Add(7);

 graph[7].Add(5);

}

// Driver Code

public static void Main(string[] args)

{

 int N = 7, K = 6;

 

 // Build the graph

 makeGraph();

 maximumVisit(N, K);

}

}

// This code is contributed by pratham76  
  
---  
  
 __

 __

 **Output:**

    
    
    4 4 4 4 3 3 3

**Time Complexity:** O(N)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

