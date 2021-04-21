Minimum labelled node to be removed from undirected Graph such that there is
no cycle



Given an **undirected graph** of **N** nodes labelled from 1 to N, the task is
to find the minimum labelled node that should be removed from the graph such
that the resulting graph has no cycle.

**Note:** If the initial graph has no cycle, i.e. no node needs to be removed,
print -1.

 **Examples:**

> **Input:** N = 5, edges[][] = {{5, 1}, {5, 2}, {1, 2}, {2, 3}, {2, 4}}  
> **Output:** 1  
> **Explanation:**  
> If node 1 is removed, the resultant graph has no cycle. Similarly, the cycle
> can be avoided by removing node 2 also.  
> Since we have to find the minimum labelled node, the answer is 1.
>
>  **Input:** N = 5, edges[][] = {{4, 5}, {4, 1}, {4, 2}, {4, 3}, {5, 1}, {5,
> 2}}  
> **Output:** 4
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The naive approach for this problem would be to remove
each vertex individually and check whether the resulting graph has a cycle or
not. The time complexity for this approach is quadratic.

**Efficient Approach:** The idea is to apply depth-first search on the given
graph and observing the dfs tree formed.

  * A Back Edge is referred to as the edge that is not part of the constructed DFS tree and is an edge between some node v and one of the ancestors of v.
  * Clearly all those edges of the graph which are not a part of the DFS tree are back edges.
  * If there are no back edges in the graph, then the graph has no cycle. So, the answer will be **-1** in this case.

If there are back edges in the graph, then we need to find the minimum edge.
In order to do this, we need to check if the cycle is removed on removing a
specific edge from the graph. Therefore, let **v** be a vertex which we are
currently checking. Therefore, the **following conditions must be followed by
vertex v** such that on removing, it would lead to no cycle:

  * **v** must lie on the tree path connecting the endpoints of each back edge in the graph.   
**Proof:** Suppose there exists some back edge x-y, such that v doesn’t lie on
the tree path. If we remove v, we would still be able to traverse from x to y,
and back to x via the back edge, indicating that the cycle is not removed.

  * The subtree of v must have at-most one back edge to any ancestor of v.   
**Proof:** Let the subtree S has to back edges w-x and y-z such that w and y
are in S and x and z are ancestors of v. If we remove v, clearly a cycle still
exists consisting of the path between w to y, the path from x to z and the two
back edges w-x and y-z, i.e. cycle is not removed.

Therefore, the idea is to keep a track of back edges, and an indicator for the
number of back edges in the subtree of a node to any of its ancestors. To keep
a track of back edges we will use a modified DFS graph colouring algorithm.  
In order to check if the subtree v has at-most one back edge to any ancestor
of v or not, we implement dfs such that it returns the depth of two highest
edges from the subtree of v. We maintain an array where every index ‘i’ in the
array stores if the condition 2 from the above is satisfied by the node ‘i’ or
not. Similarly, two arrays are implemented, one for the child and another for
the parent to see if the node v lies on the tree path connecting the
endpoints.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// minimum labelled node to be

// removed such that there is no

// cycle in the undirected graph

#include <bits/stdc++.h>

using namespace std;

const int MAX = 100005;

int totBackEdges;

int countAdj[MAX], small[MAX];

// Variables to store if a node V has

// at-most one back edge and store the

// depth of the node for the edge

int isPossible[MAX], depth[MAX];

vector<int> adj[MAX];

int vis[MAX];

// Function to swap the pairs of the graph

void change(pair<int, int>& p, int x)

{

 // If the second value is

 // greater than x

 if (p.second > x)

 p.second = x;

 // Put the pair in the ascending

 // order internally

 if (p.first > p.second)

 swap(p.first, p.second);

}

// Function to perform the DFS

pair<int, int> dfs(int v, int p = -1, int de = 0)

{

 // Initialise with the large value

 pair<int, int> answer(100000000, 100000000);

 // Storing the depth of this vertex

 depth[v] = de;

 // Mark the vertex as visited

 vis[v] = 1;

 isPossible[v] = 1;

 // Iterating through the graph

 for (int u : adj[v]) {

 // If the node is a child node

 if (u ^ p) {

 // If the child node is unvisited

 if (!vis[u]) {

 // Move to the child and increase

 // the depth

 auto x = dfs(u, v, de + 1);

 // increase according to algorithm

 small[v] += small[u];

 change(answer, x.second);

 change(answer, x.first);

 // If the node is not having

 // exactly K backedges

 if (x.second < de)

 isPossible[v] = 0;

 }

 // If the child is already visited

 // and in current dfs

 // (because colour is 1)

 // then this is a back edge

 else if (vis[u] == 1) {

 totBackEdges++;

 // Increase the countAdj values

 countAdj[v]++;

 countAdj[u]++;

 small[p]++;

 small[u]--;

 change(answer, depth[u]);

 }

 }

 }

 // Colour this vertex 2 as

 // we are exiting out of

 // dfs for this node

 vis[v] = 2;

 return answer;

}

// Function to find the minimum labelled

// node to be removed such that

// there is no cycle in the undirected graph

int minNodetoRemove(

 int n,

 vector<pair<int, int> > edges)

{

 // Construct the graph

 for (int i = 0; i < edges.size(); i++) {

 adj[edges[i].first]

 .push_back(edges[i].second);

 adj[edges[i].second]

 .push_back(edges[i].first);

 }

 // Mark visited as false for each node

 memset(vis, 0, sizeof(vis));

 totBackEdges = 0;

 // Apply dfs on all unmarked nodes

 for (int v = 1; v <= n; v++) {

 if (!vis[v])

 dfs(v);

 }

 // If no backedges in the initial graph

 // this means that there is no cycle

 // So, return -1

 if (totBackEdges == 0)

 return -1;

 int node = -1;

 // Iterate through the vertices and

 // return the first node that

 // satisfies the condition

 for (int v = 1; v <= n; v++) {

 // Check whether the count sum of

 // small[v] and count is the same as

 // the total back edges and

 // if the vertex v can be removed

 if (countAdj[v] + small[v]

 == totBackEdges

 && isPossible[v]) {

 node = v;

 }

 if (node != -1)

 break;

 }

 return node;

}

// Driver code

int main()

{

 int N = 5;

 vector<pair<int, int> > edges;

 edges.push_back(make_pair(5, 1));

 edges.push_back(make_pair(5, 2));

 edges.push_back(make_pair(1, 2));

 edges.push_back(make_pair(2, 3));

 edges.push_back(make_pair(2, 4));

 cout << minNodetoRemove(N, edges);

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

// Java implementation to find the

// minimum labelled node to be

// removed such that there is no

// cycle in the undirected graph

import java.util.ArrayList;

import java.util.Arrays;

class Pair

{

 int first, second;

 public Pair(int first, int second)

 {

 this.first = first;

 this.second = second;

 }

}

class GFG{

static final int MAX = 100005;

static int totBackEdges;

static int[] countAdj = new int[MAX];

static int[] small = new int[MAX];

// Variables to store if a node V has

// at-most one back edge and store the

// depth of the node for the edge

static int[] isPossible = new int[MAX];

static int[] depth = new int[MAX];

@SuppressWarnings("unchecked")

static ArrayList<Integer>[] adj = new ArrayList[MAX];

static int[] vis = new int[MAX];

// Function to swap the pairs of the graph

static void change(Pair p, int x)

{

 

 // If the second value is

 // greater than x

 if (p.second > x)

 p.second = x;

 // Put the Pair in the ascending

 // order internally

 if (p.first > p.second)

 {

 int tmp = p.first;

 p.first = p.second;

 p.second = tmp;

 }

}

// Function to perform the DFS

static Pair dfs(int v, int p, int de)

{

 

 // Initialise with the large value

 Pair answer = new Pair(100000000, 100000000);

 // Storing the depth of this vertex

 depth[v] = de;

 // Mark the vertex as visited

 vis[v] = 1;

 isPossible[v] = 1;

 // Iterating through the graph

 for(int u : adj[v])

 {

 

 // If the node is a child node

 if ((u ^ p) != 0)

 {

 

 // If the child node is unvisited

 if (vis[u] == 0)

 {

 

 // Move to the child and increase

 // the depth

 Pair x = dfs(u, v, de + 1);

 // increase according to algorithm

 small[v] += small[u];

 change(answer, x.second);

 change(answer, x.first);

 // If the node is not having

 // exactly K backedges

 if (x.second < de)

 isPossible[v] = 0;

 }

 // If the child is already visited

 // and in current dfs

 // (because colour is 1)

 // then this is a back edge

 else if (vis[u] == 1)

 {

 totBackEdges++;

 // Increase the countAdj values

 countAdj[v]++;

 countAdj[u]++;

 small[p]++;

 small[u]--;

 change(answer, depth[u]);

 }

 }

 }

 // Colour this vertex 2 as

 // we are exiting out of

 // dfs for this node

 vis[v] = 2;

 return answer;

}

// Function to find the minimum labelled

// node to be removed such that

// there is no cycle in the undirected graph

static int minNodetoRemove(int n, ArrayList<Pair> edges)

{

 

 // Construct the graph

 for(int i = 0; i < edges.size(); i++)

 {

 adj[edges.get(i).first].add(

 edges.get(i).second);

 adj[edges.get(i).second].add(

 edges.get(i).first);

 }

 // Mark visited as false for each node

 Arrays.fill(vis, 0);

 totBackEdges = 0;

 // Apply dfs on all unmarked nodes

 for(int v = 1; v <= n; v++)

 {

 if (vis[v] == 0)

 dfs(v, -1, 0);

 }

 // If no backedges in the initial graph

 // this means that there is no cycle

 // So, return -1

 if (totBackEdges == 0)

 return -1;

 int node = -1;

 // Iterate through the vertices and

 // return the first node that

 // satisfies the condition

 for(int v = 1; v <= n; v++)

 {

 

 // Check whether the count sum of

 // small[v] and count is the same as

 // the total back edges and

 // if the vertex v can be removed

 if ((countAdj[v] + small[v] == totBackEdges) &&

 isPossible[v] != 0)

 {

 node = v;

 }

 

 if (node != -1)

 break;

 }

 return node;

}

// Driver code

public static void main(String[] args)

{

 int N = 5;

 

 ArrayList<Pair> edges = new ArrayList<>();

 for(int i = 0; i < MAX; i++)

 {

 adj[i] = new ArrayList<>();

 }

 

 edges.add(new Pair(5, 1));

 edges.add(new Pair(5, 2));

 edges.add(new Pair(1, 2));

 edges.add(new Pair(2, 3));

 edges.add(new Pair(2, 4));

 System.out.println(minNodetoRemove(N, edges));

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

# Python3 implementation to find the

# minimum labelled node to be

# removed such that there is no

# cycle in the undirected graph 

MAX = 100005; 

totBackEdges = 0

countAdj = [0 for i in range(MAX)]

small = [0 for i in range(MAX)]

 

# Variables to store if a node V has

# at-most one back edge and store the

# depth of the node for the edge

isPossible = [0 for i in range(MAX)]

depth = [0 for i in range(MAX)]

adj = [[] for i in range(MAX)]

vis = [0 for i in range(MAX)]

# Function to swap the pairs of the graph

def change(p, x):

 # If the second value is

 # greater than x

 if (p[1] > x):

 p[1] = x;

 

 # Put the pair in the ascending

 # order internally

 if (p[0] > p[1]):

 

 tmp = p[0];

 p[0] = p[1];

 p[1] = tmp;

 

# Function to perform the DFS

def dfs(v, p = -1, de = 0):

 global vis, totBackEdges

 

 # Initialise with the large value

 answer = [100000000, 100000000]

 

 # Storing the depth of this vertex

 depth[v] = de;

 

 # Mark the vertex as visited

 vis[v] = 1;

 isPossible[v] = 1;

 

 # Iterating through the graph

 for u in adj[v]:

 

 # If the node is a child node

 if ((u ^ p) != 0):

 

 # If the child node is unvisited

 if (vis[u] == 0):

 

 # Move to the child and increase

 # the depth

 x = dfs(u, v, de + 1);

 

 # increase according to algorithm

 small[v] += small[u];

 

 change(answer, x[1]);

 change(answer, x[0]);

 

 # If the node is not having

 # exactly K backedges

 if (x[1] < de):

 isPossible[v] = 0;

 

 # If the child is already visited

 # and in current dfs

 # (because colour is 1)

 # then this is a back edge

 elif (vis[u] == 1):

 totBackEdges += 1

 

 # Increase the countAdj values

 countAdj[v] += 1

 countAdj[u] += 1

 small[p] += 1

 small[u] -= 1

 change(answer, depth[u]);

 

 # Colour this vertex 2 as

 # we are exiting out of

 # dfs for this node

 vis[v] = 2;

 return answer;

 

# Function to find the minimum labelled

# node to be removed such that

# there is no cycle in the undirected graph

def minNodetoRemove( n, edges):

 

 # Construct the graph

 for i in range(len(edges)):

 

 adj[edges[i][0]].append(edges[i][1]);

 adj[edges[i][1]].append(edges[i][0]);

 

 global vis, totBackEdges

 

 # Mark visited as false for each node

 vis = [0 for i in range(len(vis))] 

 totBackEdges = 0;

 

 # Apply dfs on all unmarked nodes

 for v in range(1, n + 1): 

 if (vis[v] == 0):

 dfs(v);

 

 # If no backedges in the initial graph

 # this means that there is no cycle

 # So, return -1

 if (totBackEdges == 0):

 return -1; 

 node = -1;

 

 # Iterate through the vertices and

 # return the first node that

 # satisfies the condition

 for v in range(1, n + 1):

 

 # Check whether the count sum of

 # small[v] and count is the same as

 # the total back edges and

 # if the vertex v can be removed

 if ((countAdj[v] + small[v] == totBackEdges) and
isPossible[v] != 0):

 node = v; 

 if (node != -1):

 break; 

 return node;

 

# Driver code

if __name__=='__main__': 

 N = 5;

 edges = []

 edges.append([5, 1]);

 edges.append([5, 2]);

 edges.append([1, 2]);

 edges.append([2, 3]);

 edges.append([2, 4]); 

 print(minNodetoRemove(N, edges));

 # This code is contributed by Pratham76  
  
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

// C# implementation to find the

// minimum labelled node to be

// removed such that there is no

// cycle in the undirected graph

 

using System;

using System.Collections;

using System.Collections.Generic;

class GFG

{

 

static int MAX = 100005;

 

static int totBackEdges;

static int []countAdj = new int[MAX];

static int []small = new int[MAX];

 

// Variables to store if a node V has

// at-most one back edge and store the

// depth of the node for the edge

static int []isPossible = new int[MAX];

static int []depth = new int[MAX];

static ArrayList adj = new ArrayList();

static int []vis = new int[MAX];

class pair

{

 public int first, second;

 public pair(int first, int second)

 {

 this.first = first;

 this.second = second;

 }

}

 

// Function to swap the pairs of the graph

static void change(ref pair p, int x)

{

 // If the second value is

 // greater than x

 if (p.second > x)

 p.second = x;

 

 // Put the pair in the ascending

 // order internally

 if (p.first > p.second)

 { 

 int tmp = p.first;

 p.first = p.second;

 p.second = tmp;

 }

}

 

// Function to perform the DFS

static pair dfs(int v, int p = -1, int de = 0)

{

 // Initialise with the large value

 pair answer = new pair(100000000, 100000000);

 

 // Storing the depth of this vertex

 depth[v] = de;

 

 // Mark the vertex as visited

 vis[v] = 1;

 isPossible[v] = 1;

 

 // Iterating through the graph

 foreach (int u in (ArrayList)adj[v]) {

 

 // If the node is a child node

 if ((u ^ p) != 0) {

 

 // If the child node is unvisited

 if (vis[u] == 0) {

 

 // Move to the child and increase

 // the depth

 pair x = dfs(u, v, de + 1);

 

 // increase according to algorithm

 small[v] += small[u];

 

 change(ref answer, x.second);

 change(ref answer, x.first);

 

 // If the node is not having

 // exactly K backedges

 if (x.second < de)

 isPossible[v] = 0;

 }

 

 // If the child is already visited

 // and in current dfs

 // (because colour is 1)

 // then this is a back edge

 else if (vis[u] == 1) {

 totBackEdges++;

 

 // Increase the countAdj values

 countAdj[v]++;

 countAdj[u]++;

 small[p]++;

 small[u]--;

 change(ref answer, depth[u]);

 }

 }

 }

 

 // Colour this vertex 2 as

 // we are exiting out of

 // dfs for this node

 vis[v] = 2;

 return answer;

}

 

// Function to find the minimum labelled

// node to be removed such that

// there is no cycle in the undirected graph

static int minNodetoRemove(

 int n,

 ArrayList edges)

{

 

 // Construct the graph

 for (int i = 0; i < edges.Count; i++) {

 ((ArrayList)adj[((pair)edges[i]).first])

 .Add(((pair)edges[i]).second);

 ((ArrayList)adj[((pair)edges[i]).second])

 .Add(((pair)edges[i]).first);

 }

 

 // Mark visited as false for each node

 Array.Fill(vis, 0);

 

 totBackEdges = 0;

 

 // Apply dfs on all unmarked nodes

 for (int v = 1; v <= n; v++) {

 if (vis[v] == 0)

 dfs(v);

 }

 

 // If no backedges in the initial graph

 // this means that there is no cycle

 // So, return -1

 if (totBackEdges == 0)

 return -1;

 

 int node = -1;

 

 // Iterate through the vertices and

 // return the first node that

 // satisfies the condition

 for (int v = 1; v <= n; v++) {

 

 // Check whether the count sum of

 // small[v] and count is the same as

 // the total back edges and

 // if the vertex v can be removed

 if ((countAdj[v] + small[v] == totBackEdges) && isPossible[v] != 0) {

 node = v;

 }

 if (node != -1)

 break;

 }

 

 return node;

}

 

// Driver code

static void Main()

{

 int N = 5;

 ArrayList edges = new ArrayList();

 for(int i = 0; i < MAX; i++)

 {

 adj.Add(new ArrayList());

 }

 edges.Add(new pair(5, 1));

 edges.Add(new pair(5, 2));

 edges.Add(new pair(1, 2));

 edges.Add(new pair(2, 3));

 edges.Add(new pair(2, 4));

 

 Console.Write(minNodetoRemove(N, edges));

 }

}

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    1

**Time Complexity:** _O(N + M)_ , where N is the number of nodes and M is the
number of edges.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

