Find the path from root to the given nodes of a tree for multiple queries



Given a tree with **N** vertices numbered from **0** to **N – 1** (0th node is
the root node). Also, given **q** queries containing nodes in the tree. The
task is to find the path from the root node to the given node for multiple
queries.

 **Examples:**

    
    
    **Input:** N = 6, q[] = {2, 4}
    Tree:
                        0
                       / \
                      1   2
                      |
                      3
                     / \
                    4   5
    **Output:**
    0 2
    0 1 3 4
    The path from root node to node 2 is 0 -> 2.
    The path from root node to node 4 is 0 -> 1 -> 3 -> 4.
    
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The path from any root vertex to any vertex ‘i’ is the path
from the root vertex to its parent followed by the parent itself. This can be
achieved by modifying the Breadth-First-Traversal of the tree. In the path
list, for each unvisited vertex, add the copy of the path of its parent to its
list and then add the parent to the list.

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

const int sz = 1e5;

// Adjacency list representation

// of the tree

vector<int> tree[sz];

// Boolean array to mark all the

// vertices which are visited

bool vis[sz];

// Array of vector where ith index

// stores the path from the root

// node to the ith node

vector<int> path[sz];

// Utility function to create an

// edge between two vertices

void addEdge(int a, int b)

{

 // Add a to b's list

 tree[a].push_back(b);

 // Add b to a's list

 tree[b].push_back(a);

}

// Modified Breadth-First Function

void bfs(int node)

{

 // Create a queue of {child, parent}

 queue<pair<int, int> > qu;

 // Push root node in the front of

 // the queue and mark as visited

 qu.push({ node, -1 });

 vis[node] = true;

 while (!qu.empty()) {

 pair<int, int> p = qu.front();

 // Dequeue a vertex from queue

 qu.pop();

 vis[p.first] = true;

 // Get all adjacent vertices of the dequeued

 // vertex s. If any adjacent has not

 // been visited then enqueue it

 for (int child : tree[p.first]) {

 if (!vis[child]) {

 qu.push({ child, p.first });

 // Path from the root to this vertex is

 // the path from root to the parent

 // of this vertex followed by the

 // parent itself

 path[child] = path[p.first];

 path[child].push_back(p.first);

 }

 }

 }

}

// Utility Function to print the

// path from root to given node

void displayPath(int node)

{

 vector<int> ans = path[node];

 for (int k : ans) {

 cout << k << " ";

 }

 cout << node << '\n';

}

// Driver code

int main()

{

 // Number of vertices

 int n = 6;

 addEdge(0, 1);

 addEdge(0, 2);

 addEdge(1, 3);

 addEdge(3, 4);

 addEdge(3, 5);

 // Calling modified bfs function

 bfs(0);

 // Display paths from root vertex

 // to the given vertices

 displayPath(2);

 displayPath(4);

 displayPath(5);

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

// Java implementation of the approach

import java.util.*;

@SuppressWarnings("unchecked")

class GFG {

 static class Pair<T, V> {

 T first;

 V second;

 Pair() {

 }

 Pair(T first, V second) {

 this.first = first;

 this.second = second;

 }

 }

 static int sz = (int) 1e5;

 // Adjacency list representation

 // of the tree

 static Vector<Integer>[] tree = new Vector[sz];

 // Boolean array to mark all the

 // vertices which are visited

 static boolean[] vis = new boolean[sz];

 // Array of vector where ith index

 // stores the path from the root

 // node to the ith node

 static Vector<Integer>[] path = new Vector[sz];

 // Utility function to create an

 // edge between two vertices

 static void addEdge(int a, int b) {

 // Add a to b's list

 tree[a].add(b);

 // Add b to a's list

 tree[b].add(a);

 }

 // Modified Breadth-First Function

 static void bfs(int node) {

 // Create a queue of {child, parent}

 Queue<Pair<Integer, Integer>> qu = new LinkedList<>();

 // Push root node in the front of

 // the queue and mark as visited

 qu.add(new Pair<>(node, -1));

 vis[node] = true;

 while (!qu.isEmpty()) {

 // Dequeue a vertex from queue

 Pair<Integer, Integer> p = qu.poll();

 vis[p.first] = true;

 // Get all adjacent vertices of the dequeued

 // vertex s. If any adjacent has not

 // been visited then enqueue it

 for (int child : tree[p.first]) {

 if (!vis[child]) {

 qu.add(new Pair<>(child, p.first));

 // Path from the root to this vertex is

 // the path from root to the parent

 // of this vertex followed by the

 // parent itself

 path[child] = (Vector<Integer>) path[p.first].clone();

 path[child].add(p.first);

 }

 }

 }

 }

 // Utility Function to print the

 // path from root to given node

 static void displayPath(int node) {

 for (int k : path[node]) {

 System.out.print(k + " ");

 }

 System.out.println(node);

 }

 // Driver Code

 public static void main(String[] args) {

 for (int i = 0; i < sz; i++) {

 tree[i] = new Vector<>();

 path[i] = new Vector<>();

 vis[i] = false;

 }

 // Number of vertices

 int n = 6;

 addEdge(0, 1);

 addEdge(0, 2);

 addEdge(1, 3);

 addEdge(3, 4);

 addEdge(3, 5);

 // Calling modified bfs function

 bfs(0);

 // Display paths from root vertex

 // to the given vertices

 displayPath(2);

 displayPath(4);

 displayPath(5);

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

# Python3 implementation of the approach

from collections import deque as queue

sz = 7

# Adjacency list representation

# of the tree

tree = [[] for i in range(sz)]

# Boolean array to mark all the

# vertices which are visited

vis = [False] * sz

# Array of vector where ith index

# stores the path from the root

# node to the ith node

path = [[] for i in range(sz)]

# Utility function to create an

# edge between two vertices

def addEdge(a, b):

 # Add a to b's list

 tree[a].append(b)

 # Add b to a's list

 tree[b].append(a)

# Modified Breadth-First Function

def bfs(node):

 # Create a queue of {child, parent}

 qu = queue()

 # Push root node in the front of

 # the queue and mark as visited

 qu.append([node, -1])

 vis[node] = True

 while (len(qu) > 0):

 p = qu.popleft()

 

 #print(p,p[0],p[1])

 # Dequeue a vertex from queue

 # qu.pop()

 vis[p[0]] = True

 # Get all adjacent vertices of

 # the dequeued vertex s. If any

 # adjacent has not been visited

 # then enqueue it

 for child in tree[p[0]]:

 if (vis[child] == False):

 qu.append([child, p[0]])

 # Path from the root to this

 # vertex is the path from root

 # to the parent of this vertex

 # followed by the parent itself

 for u in path[p[0]]:

 path[child].append(u)

 path[child].append(p[0])

 

 #print(child,":",path[0])

# Utility Function to prthe

# path from root to given node

def displayPath(node):

 

 ans = path[node]

 for k in ans:

 print(k, end = " ")

 

 print(node)

# Driver code

if __name__ == '__main__':

 # Number of vertices

 n = 6

 addEdge(0, 1)

 addEdge(0, 2)

 addEdge(1, 3)

 addEdge(3, 4)

 addEdge(3, 5)

 # Calling modified bfs function

 bfs(0)

 # Display paths from root vertex

 # to the given vertices

 displayPath(2)

 displayPath(4)

 displayPath(5)

# This code is contributed by mohit kumar 29  
  
---  
  
 __

 __

 **Output:**

    
    
    0 2
    0 1 3 4
    0 1 3 5
    
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

