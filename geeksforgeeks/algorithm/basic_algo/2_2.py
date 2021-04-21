Print all leaf nodes of an n-ary tree using DFS



Given an array **edge[][2]** where **(edge[i][0], edge[i][1])** defines an
edge in the n-ary tree, the task is to print all the leaf nodes of the given
tree using.

 **Examples:**

    
    
    **Input:** edge[][] = {{1, 2}, {1, 3}, {2, 4}, {2, 5}, {3, 6}}
    **Output:** 4 5 6
        1
       / \
      2   3
     / \   \
    4   5   6
    
    **Input:** edge[][] = {{1, 5}, {1, 7}, {5, 6}}
    **Output:** 6 7

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** DFS can be used to traverse the complete tree. We will keep
track of parent while traversing to avoid the visited node array. Initially
for every node we can set a flag and if the node have at least one child (i.e.
non-leaf node) then we will reset the flag. The nodes with no children are the
leaf nodes.

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

// Function to perform DFS on the tree

void dfs(list<int> t[], int node, int parent)

{

 int flag = 1;

 // Iterating the children of current node

 for (auto ir : t[node]) {

 // There is at least a child

 // of the current node

 if (ir != parent) {

 flag = 0;

 dfs(t, ir, node);

 }

 }

 // Current node is connected to only

 // its parent i.e. it is a leaf node

 if (flag == 1)

 cout << node << " ";

}

// Driver code

int main()

{

 // Adjacency list

 list<int> t[1005];

 // List of all edges

 pair<int, int> edges[] = { { 1, 2 },

 { 1, 3 },

 { 2, 4 },

 { 3, 5 },

 { 3, 6 },

 { 3, 7 },

 { 6, 8 } };

 // Count of edges

 int cnt = sizeof(edges) / sizeof(edges[0]);

 // Number of nodes

 int node = cnt + 1;

 // Create the tree

 for (int i = 0; i < cnt; i++) {

 t[edges[i].first].push_back(edges[i].second);

 t[edges[i].second].push_back(edges[i].first);

 }

 // Function call

 dfs(t, 1, 0);

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

class GFG

{

 

// Pair class

static class pair

{

 int first,second;

 pair(int a, int b)

 {

 first = a;

 second = b;

 }

}

// Function to perform DFS on the tree

static void dfs(Vector t, int node, int parent)

{

 int flag = 1;

 

 // Iterating the children of current node

 for (int i = 0; i < ((Vector)t.get(node)).size(); i++)

 {

 int ir = (int)((Vector)t.get(node)).get(i);

 

 // There is at least a child

 // of the current node

 if (ir != parent)

 {

 flag = 0;

 dfs(t, ir, node);

 }

 }

 // Current node is connected to only

 // its parent i.e. it is a leaf node

 if (flag == 1)

 System.out.print( node + " ");

}

// Driver code

public static void main(String args[])

{

 // Adjacency list

 Vector t = new Vector();

 // List of all edges

 pair edges[] = { new pair( 1, 2 ),

 new pair( 1, 3 ),

 new pair( 2, 4 ),

 new pair( 3, 5 ),

 new pair( 3, 6 ),

 new pair( 3, 7 ),

 new pair( 6, 8 ) };

 // Count of edges

 int cnt = edges.length;

 // Number of nodes

 int node = cnt + 1;

 

 for(int i = 0; i < 1005; i++)

 {

 t.add(new Vector());

 }

 // Create the tree

 for (int i = 0; i < cnt; i++)

 {

 ((Vector)t.get(edges[i].first)).add(edges[i].second);

 ((Vector)t.get(edges[i].second)).add(edges[i].first);

 }

 // Function call

 dfs(t, 1, 0);

}

}

// This code is contributed by Arnab Kundu  
  
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

t = [[] for i in range(1005)]

# Function to perform DFS on the tree

def dfs(node, parent):

 flag = 1

 # Iterating the children of current node

 for ir in t[node]:

 # There is at least a child

 # of the current node

 if (ir != parent):

 flag = 0

 dfs(ir, node)

 # Current node is connected to only

 # its parent i.e. it is a leaf node

 if (flag == 1):

 print(node, end = " ")

# Driver code

# List of all edges

edges = [[ 1, 2 ],

 [ 1, 3 ],

 [ 2, 4 ],

 [ 3, 5 ],

 [ 3, 6 ],

 [ 3, 7 ],

 [ 6, 8 ]]

# Count of edges

cnt = len(edges)

# Number of nodes

node = cnt + 1

# Create the tree

for i in range(cnt):

 t[edges[i][0]].append(edges[i][1])

 t[edges[i][1]].append(edges[i][0])

# Function call

dfs(1, 0)

# This code is contributed by Mohit Kumar  
  
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

using System.Collections;

using System.Collections.Generic;

using System;

class GFG{

 

// Pair class

class pair

{

 public int first, second;

 public pair(int a, int b)

 {

 first = a;

 second = b;

 }

}

// Function to perform DFS on the tree

static void dfs(ArrayList t, int node,

 int parent)

{

 int flag = 1;

 

 // Iterating the children of current node

 for(int i = 0;

 i < ((ArrayList)t[node]).Count;

 i++)

 {

 int ir = (int)((ArrayList)t[node])[i];

 

 // There is at least a child

 // of the current node

 if (ir != parent)

 {

 flag = 0;

 dfs(t, ir, node);

 }

 }

 // Current node is connected to only

 // its parent i.e. it is a leaf node

 if (flag == 1)

 Console.Write( node + " ");

}

// Driver code

public static void Main(string []args)

{

 

 // Adjacency list

 ArrayList t = new ArrayList();

 // List of all edges

 pair []edges = { new pair(1, 2),

 new pair(1, 3),

 new pair(2, 4),

 new pair(3, 5),

 new pair(3, 6),

 new pair(3, 7),

 new pair(6, 8) };

 // Count of edges

 int cnt = edges.Length;

 

 for(int i = 0; i < 1005; i++)

 {

 t.Add(new ArrayList());

 }

 // Create the tree

 for(int i = 0; i < cnt; i++)

 {

 ((ArrayList)t[edges[i].first]).Add(

 edges[i].second);

 ((ArrayList)t[edges[i].second]).Add(

 edges[i].first);

 }

 // Function call

 dfs(t, 1, 0);

}

}

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    4 5 8 7

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

