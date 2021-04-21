Find the maximum component size after addition of each edge to the graph



Given an array **arr[][]** which contains the edges of a graph to be used to
construct an undirected graph **G** with **N** nodes, the task is to find the
maximum component size in the graph after each edge is added while
constructing the graph.

 **Examples:**

> **Input:** N = 4, arr[][] = {{1, 2}, {3, 4}, {2, 3}}  
> **Output:** 2 2 4  
> **Explanation:**  
> Initially, the graph has 4 individual nodes 1, 2, 3 and 4.  
> After the first edge is added : 1 – 2, 3, 4 -> maximum component size = 2  
> After the second edge is added : 1 – 2, 3 – 4 -> maximum component size = 2  
> After the third edge is added : 1 – 2 – 3 – 4 -> maximum component size = 4
>
>  **Input:** N = 4, arr[][] = {{2, 3}, {1, 2}, {1, 5}, {2, 4}}  
> **Output:** 2 3 4 5  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The naive approach for this problem is to add the edges
sequentially and at each step apply depth-first search algorithm to find the
size of the largest component.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the

// maximum comake_paironent size

// after addition of each

// edge to the graph

#include <bits/stdc++.h>

using namespace std;

// Function to perform

// Depth First Search

// on the given graph

int dfs(int u, int visited[],

 vector<int>* adj)

{

 // Mark visited

 visited[u] = 1;

 int size = 1;

 // Add each child's

 // comake_paironent size

 for (auto child : adj[u]) {

 if (!visited[child])

 size += dfs(child,

 visited, adj);

 }

 return size;

}

// Function to find the maximum

// comake_paironent size

// after addition of each

// edge to the graph

void maxSize(vector<pair<int, int> > e,

 int n)

{

 // Graph in the adjacency

 // list format

 vector<int> adj[n];

 // Visited array

 int visited[n];

 vector<int> answer;

 // At each step, add a new

 // edge and apply dfs on all

 // the nodes to find the maximum

 // comake_paironent size

 for (auto edge : e) {

 // Add this edge to undirected graph

 adj[edge.first - 1].push_back(

 edge.second - 1);

 adj[edge.second - 1].push_back(

 edge.first - 1);

 // Mark all the nodes

 // as unvisited

 memset(visited, 0,

 sizeof(visited));

 int maxAns = 0;

 // Loop to perform DFS

 // and find the size

 // of the maximum comake_paironent

 for (int i = 0; i < n; i++) {

 if (!visited[i]) {

 maxAns = max(maxAns,

 dfs(i, visited, adj));

 }

 }

 answer.push_back(maxAns);

 }

 // Print the answer

 for (auto i : answer) {

 cout << i << " ";

 }

}

// Driver code

int main()

{

 int N = 4;

 vector<pair<int, int> > E;

 E.push_back(make_pair(1, 2));

 E.push_back(make_pair(3, 4));

 E.push_back(make_pair(2, 3));

 maxSize(E, N);

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

// Java program to find the maximum

// comake_paironent size after

// addition of each edge to the graph

import java.util.*;

@SuppressWarnings("unchecked")

class GFG{

 

static class pair

{

 int Key, Value;

 

 pair(int Key, int Value)

 {

 this.Key = Key;

 this.Value = Value;

 }

}

 

// Function to perform Depth First

// Search on the given graph

static int dfs(int u, int []visited,

 ArrayList []adj)

{

 

 // Mark visited

 visited[u] = 1;

 int size = 1;

 

 // Add each child's

 // comake_paironent size

 for(int child : (ArrayList<Integer>)adj[u])

 {

 if (visited[child] == 0)

 size += dfs(child,

 visited, adj);

 }

 return size;

}

 

// Function to find the maximum

// comake_paironent size after

// addition of each edge to the graph

static void maxSize(ArrayList e,

 int n)

{

 

 // Graph in the adjacency

 // list format

 ArrayList []adj = new ArrayList[n];

 

 for(int i = 0; i < n; i++)

 {

 adj[i] = new ArrayList();

 }

 

 // Visited array

 int []visited = new int[n];

 

 ArrayList answer = new ArrayList();

 

 // At each step, add a new

 // edge and apply dfs on all

 // the nodes to find the maximum

 // comake_paironent size

 for(pair edge : (ArrayList<pair>)e)

 {

 

 // Add this edge to undirected graph

 adj[edge.Key - 1].add(

 edge.Value - 1);

 adj[edge.Value - 1].add(

 edge.Key - 1);

 

 // Mark all the nodes

 // as unvisited

 Arrays.fill(visited,0);

 

 int maxAns = 0;

 

 // Loop to perform DFS and find the

 // size of the maximum comake_paironent

 for(int i = 0; i < n; i++)

 {

 if (visited[i] == 0)

 {

 maxAns = Math.max(maxAns,

 dfs(i, visited, adj));

 }

 }

 answer.add(maxAns);

 }

 

 // Print the answer

 for(int i : (ArrayList<Integer>) answer)

 {

 System.out.print(i + " ");

 }

}

 

// Driver code

public static void main(String[] args)

{

 int N = 4;

 

 ArrayList E = new ArrayList();

 E.add(new pair(1, 2));

 E.add(new pair(3, 4));

 E.add(new pair(2, 3));

 

 maxSize(E, N);

}

}

// This code is contributed by pratham76  
  
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

// C# program to find the

// maximum comake_paironent size

// after addition of each

// edge to the graph

using System;

using System.Collections;

using System.Collections.Generic;

class GFG{

 

// Function to perform

// Depth First Search

// on the given graph

static int dfs(int u, int []visited,

 ArrayList []adj)

{

 

 // Mark visited

 visited[u] = 1;

 int size = 1;

 

 // Add each child's

 // comake_paironent size

 foreach (int child in adj[u])

 {

 if (visited[child] == 0)

 size += dfs(child,

 visited, adj);

 }

 return size;

}

 

// Function to find the maximum

// comake_paironent size

// after addition of each

// edge to the graph

static void maxSize(ArrayList e,

 int n)

{

 

 // Graph in the adjacency

 // list format

 ArrayList []adj = new ArrayList[n];

 

 for(int i = 0; i < n; i++)

 {

 adj[i] = new ArrayList();

 }

 

 // Visited array

 int []visited = new int[n];

 

 ArrayList answer = new ArrayList();

 

 // At each step, add a new

 // edge and apply dfs on all

 // the nodes to find the maximum

 // comake_paironent size

 foreach(KeyValuePair<int, int> edge in e)

 {

 

 // Add this edge to undirected graph

 adj[edge.Key - 1].Add(

 edge.Value - 1);

 adj[edge.Value - 1].Add(

 edge.Key - 1);

 

 // Mark all the nodes

 // as unvisited

 Array.Fill(visited,0);

 

 int maxAns = 0;

 

 // Loop to perform DFS

 // and find the size

 // of the maximum comake_paironent

 for(int i = 0; i < n; i++)

 {

 if (visited[i] == 0)

 {

 maxAns = Math.Max(maxAns,

 dfs(i, visited, adj));

 }

 }

 answer.Add(maxAns);

 }

 

 // Print the answer

 foreach(int i in answer)

 {

 Console.Write(i + " ");

 }

}

 

// Driver code

public static void Main(string[] args)

{

 int N = 4;

 ArrayList E = new ArrayList();

 E.Add(new KeyValuePair<int, int>(1, 2));

 E.Add(new KeyValuePair<int, int>(3, 4));

 E.Add(new KeyValuePair<int, int>(2, 3));

 

 maxSize(E, N);

}

}

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    2 2 4

**Time Complexity:** _O(|E| * N)_

 **Efficient Approach:** The idea is to use the concept of Disjoint Set (Union
by rank and Path compression) to solve the problem more efficiently.

  * Each node is initially a disjoint set within itself. As and when the edges are added, the disjoint sets are merged together forming larger components. In the disjoint set implementation, we will make the ranking system based on component sizes i.e when merging of two components is performed the larger component’s root will be considered the final root after the merge operation.
  * One way to find the largest size component after each edge addition is to traverse the size array (size[i] represents the size of the component in which node ‘i’ belongs), but this is inefficient when the number of nodes in the graph is high.
  * A more efficient way is to store the component sizes of all the root in some ordered data structure like sets.
  * When two components are merged, all we need to do is remove the previous component sizes from the set and add the combined component size. So at each step, we would be able to find the largest component size in logarithmic complexity.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the maximum

// component size after the addition of

// each edge to the graph

#include <bits/stdc++.h>

using namespace std;

// Variables for implementing DSU

int par[100005];

int size[100005];

// Root of the component of node i

int root(int i)

{

 if (par[i] == i)

 return i;

 // Finding the root and applying

 // path compression

 else

 return par[i] = root(par[i]);

}

// Function to merge two components

void merge(int a, int b)

{

 // Find the roots of both

 // the components

 int p = root(a);

 int q = root(b);

 // If both the nodes already belong

 // to the same compenent

 if (p == q)

 return;

 // Union by rank, the rank in

 // this case is the size of

 // the component.

 // Smaller size will be

 // merged into larger,

 // so the larger's root

 // will be the final root

 if (size[p] > size[q])

 swap(p, q);

 par[p] = q;

 size[q] += size[p];

}

// Function to find the

// maximum component size

// after the addition of

// each edge to the graph

void maxSize(vector<pair<int, int> > e, int n)

{

 // Initialising the disjoint set

 for (int i = 1; i < n + 1; i++) {

 // Each node is the root and

 // each component size is 1

 par[i] = i;

 size[i] = 1;

 }

 vector<int> answer;

 // A multiset is being used to store

 // the size of the components

 // because multiple components

 // can have same sizes

 multiset<int> compSizes;

 for (int i = 1; i <= n; i++)

 compSizes.insert(size[i]);

 // At each step; add a new edge,

 // merge the components

 // and find the max

 // sized component

 for (auto edge : e) {

 // Merge operation is required only when

 // both the nodes don't belong to the

 // same component

 if (root(edge.first) != root(edge.second)) {

 // Sizes of the compenents

 int size1 = size[root(edge.first)];

 int size2 = size[root(edge.second)];

 // Remove the previous component sizes

 compSizes.erase(compSizes.find(size1));

 compSizes.erase(compSizes.find(size2));

 // Perform the merge operation

 merge(edge.first, edge.second);

 // Insert the combined size

 compSizes.insert(size1 + size2);

 }

 // Maximum value in the multiset is

 // the max component size

 answer.push_back(*compSizes.rbegin());

 }

 // Printing the answer

 for (int i = 0; i < answer.size(); i++) {

 cout << answer[i] << " ";

 }

}

// Driver code

int main()

{

 int N = 4;

 vector<pair<int, int> > E;

 E.push_back(make_pair(1, 2));

 E.push_back(make_pair(3, 4));

 E.push_back(make_pair(2, 3));

 maxSize(E, N);

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    2 2 4

**Time Complexity:** _O(|E| * log(N))_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

