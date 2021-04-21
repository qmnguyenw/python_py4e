Shortest path in a directed graph by Dijkstra’s algorithm



Given a directed graph and a **source vertex** in the graph, the task is to
find the shortest distance and path from source to target vertex in the given
graph where edges are weighted (non-negative) and directed from parent vertex
to source vertices.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  * Mark all vertices unvisited. Create a set of all unvisited vertices.
  * Assign zero distance value to source vertex and infinity distance value to all other vertices.
  * Set the source vertex as current vertex
  * For current vertex, consider all of its unvisited children and calculate their tentative distances through the current. (distance of current + weight of the corresponding edge) Compare the newly calculated distance to the current assigned value (can be infinity for some vertices) and assign the smaller one.
  * After considering all the unvisited children of the current vertex, mark the _current_ as visited and remove it from the unvisited set.
  * Similarly, continue for all the vertex until all the nodes are visited.

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

// shortest path in a directed

// graph from source vertex to

// the destination vertex

#include <bits/stdc++.h>

#define infi 1000000000

using namespace std;

// Class of the node

class Node {

public:

 int vertexNumber;

 // Adjacency list that shows the

 // vertexNumber of child vertex

 // and the weight of the edge

 vector<pair<int, int> > children;

 Node(int vertexNumber)

 {

 this->vertexNumber = vertexNumber;

 }

 // Function to add the child for

 // the given node

 void add_child(int vNumber, int length)

 {

 pair<int, int> p;

 p.first = vNumber;

 p.second = length;

 children.push_back(p);

 }

};

// Function to find the distance of

// the node from the given source

// vertex to the destination vertex

vector<int> dijkstraDist(

 vector<Node*> g,

 int s, vector<int>& path)

{

 // Stores distance of each

 // vertex from source vertex

 vector<int> dist(g.size());

 // Boolean array that shows

 // whether the vertex 'i'

 // is visited or not

 bool visited[g.size()];

 for (int i = 0; i < g.size(); i++) {

 visited[i] = false;

 path[i] = -1;

 dist[i] = infi;

 }

 dist[s] = 0;

 path[s] = -1;

 int current = s;

 // Set of vertices that has

 // a parent (one or more)

 // marked as visited

 unordered_set<int> sett;

 while (true) {

 // Mark current as visited

 visited[current] = true;

 for (int i = 0;

 i < g[current]->children.size();

 i++) {

 int v = g[current]->children[i].first;

 if (visited[v])

 continue;

 // Inserting into the

 // visited vertex

 sett.insert(v);

 int alt

 = dist[current]

 + g[current]->children[i].second;

 // Condition to check the distance

 // is correct and update it

 // if it is minimum from the previous

 // computed distance

 if (alt < dist[v]) {

 dist[v] = alt;

 path[v] = current;

 }

 }

 sett.erase(current);

 if (sett.empty())

 break;

 // The new current

 int minDist = infi;

 int index = 0;

 // Loop to update the distance

 // of the vertices of the graph

 for (int a: sett) {

 if (dist[a] < minDist) {

 minDist = dist[a];

 index = a;

 }

 }

 current = index;

 }

 return dist;

}

// Function to print the path

// from the source vertex to

// the destination vertex

void printPath(vector<int> path,

 int i, int s)

{

 if (i != s) {

 // Condition to check if

 // there is no path between

 // the vertices

 if (path[i] == -1) {

 cout << "Path not found!!";

 return;

 }

 printPath(path, path[i], s);

 cout << path[i] << " ";

 }

}

// Driver Code

int main()

{

 vector<Node*> v;

 int n = 4, s = 0, e = 5;

 // Loop to create the nodes

 for (int i = 0; i < n; i++) {

 Node* a = new Node(i);

 v.push_back(a);

 }

 // Creating directed

 // weighted edges

 v[0]->add_child(1, 1);

 v[0]->add_child(2, 4);

 v[1]->add_child(2, 2);

 v[1]->add_child(3, 6);

 v[2]->add_child(3, 3);

 vector<int> path(v.size());

 vector<int> dist

 = dijkstraDist(v, s, path);

 // Loop to print the distance of

 // every node from source vertex

 for (int i = 0; i < dist.size(); i++) {

 if (dist[i] == infi) {

 cout << i << " and " << s

 << " are not connected"

 << endl;

 continue;

 }

 cout << "Distance of " << i

 << "th vertex from source vertex "

 << s << " is: "

 << dist[i] << endl;

 }

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

// Java implementation to find the

// shortest path in a directed

// graph from source vertex to

// the destination vertex

import java.util.ArrayList;

import java.util.HashSet;

import java.util.List;

import java.util.Set;

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

static final int infi = 1000000000;

// Class of the node

static class Node

{

 int vertexNumber;

 // Adjacency list that shows the

 // vertexNumber of child vertex

 // and the weight of the edge

 List<Pair> children;

 Node(int vertexNumber)

 {

 this.vertexNumber = vertexNumber;

 children = new ArrayList<>();

 }

 // Function to add the child for

 // the given node

 void add_child(int vNumber, int length)

 {

 Pair p = new Pair(vNumber, length);

 children.add(p);

 }

}

// Function to find the distance of

// the node from the given source

// vertex to the destination vertex

static int[] dijkstraDist(List<Node> g,

 int s, int[] path)

{

 

 // Stores distance of each

 // vertex from source vertex

 int[] dist = new int[g.size()];

 // Boolean array that shows

 // whether the vertex 'i'

 // is visited or not

 boolean[] visited = new boolean[g.size()];

 for(int i = 0; i < g.size(); i++)

 {

 visited[i] = false;

 path[i] = -1;

 dist[i] = infi;

 }

 dist[s] = 0;

 path[s] = -1;

 int current = s;

 // Set of vertices that has

 // a parent (one or more)

 // marked as visited

 Set<Integer> sett = new HashSet<>();

 while (true)

 {

 

 // Mark current as visited

 visited[current] = true;

 for(int i = 0;

 i < g.get(current).children.size();

 i++)

 {

 int v = g.get(current).children.get(i).first;

 

 if (visited[v])

 continue;

 // Inserting into the

 // visited vertex

 sett.add(v);

 int alt = dist[current] +

 g.get(current).children.get(i).second;

 // Condition to check the distance

 // is correct and update it

 // if it is minimum from the previous

 // computed distance

 if (alt < dist[v])

 {

 dist[v] = alt;

 path[v] = current;

 }

 }

 sett.remove(current);

 

 if (sett.isEmpty())

 break;

 // The new current

 int minDist = infi;

 int index = 0;

 // Loop to update the distance

 // of the vertices of the graph

 for(int a : sett)

 {

 if (dist[a] < minDist)

 {

 minDist = dist[a];

 index = a;

 }

 }

 current = index;

 }

 return dist;

}

// Function to print the path

// from the source vertex to

// the destination vertex

void printPath(int[] path, int i, int s)

{

 if (i != s)

 {

 

 // Condition to check if

 // there is no path between

 // the vertices

 if (path[i] == -1)

 {

 System.out.println("Path not found!!");

 return;

 }

 printPath(path, path[i], s);

 System.out.print(path[i] + " ");

 }

}

// Driver Code

public static void main(String[] args)

{

 List<Node> v = new ArrayList<>();

 int n = 4, s = 0, e = 5;

 // Loop to create the nodes

 for(int i = 0; i < n; i++)

 {

 Node a = new Node(i);

 v.add(a);

 }

 // Creating directed

 // weighted edges

 v.get(0).add_child(1, 1);

 v.get(0).add_child(2, 4);

 v.get(1).add_child(2, 2);

 v.get(1).add_child(3, 6);

 v.get(2).add_child(3, 3);

 int[] path = new int[v.size()];

 int[] dist = dijkstraDist(v, s, path);

 // Loop to print the distance of

 // every node from source vertex

 for(int i = 0; i < dist.length; i++)

 {

 if (dist[i] == infi)

 {

 System.out.printf("%d and %d are not " +

 "connected\n", i, s);

 continue;

 }

 System.out.printf("Distance of %dth vertex " +

 "from source vertex %d is: %d\n",

 i, s, dist[i]);

 }

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

# shortest path in a directed

# graph from source vertex to

# the destination vertex

class Pair:

 def __init__(self, first, second):

 self.first = first

 self.second = second

infi = 1000000000;

 

# Class of the node

class Node:

 

 # Adjacency list that shows the

 # vertexNumber of child vertex

 # and the weight of the edge 

 def __init__(self, vertexNumber): 

 self.vertexNumber = vertexNumber

 self.children = []

 

 # Function to add the child for

 # the given node

 def Add_child(self, vNumber, length): 

 p = Pair(vNumber, length);

 self.children.append(p);

 

# Function to find the distance of

# the node from the given source

# vertex to the destination vertex

def dijkstraDist(g, s, path):

 

 # Stores distance of each

 # vertex from source vertex

 dist = [infi for i in range(len(g))]

 

 # bool array that shows

 # whether the vertex 'i'

 # is visited or not

 visited = [False for i in range(len(g))]

 

 for i in range(len(g)): 

 path[i] = -1

 dist[s] = 0;

 path[s] = -1;

 current = s;

 

 # Set of vertices that has

 # a parent (one or more)

 # marked as visited

 sett = set() 

 while (True):

 

 # Mark current as visited

 visited[current] = True;

 for i in range(len(g[current].children)): 

 v = g[current].children[i].first; 

 if (visited[v]):

 continue;

 

 # Inserting into the

 # visited vertex

 sett.add(v);

 alt = dist[current] + g[current].children[i].second;

 

 # Condition to check the distance

 # is correct and update it

 # if it is minimum from the previous

 # computed distance

 if (alt < dist[v]): 

 dist[v] = alt;

 path[v] = current; 

 if current in sett: 

 sett.remove(current); 

 if (len(sett) == 0):

 break;

 

 # The new current

 minDist = infi;

 index = 0;

 

 # Loop to update the distance

 # of the vertices of the graph

 for a in sett: 

 if (dist[a] < minDist): 

 minDist = dist[a];

 index = a; 

 current = index; 

 return dist;

 

# Function to print the path

# from the source vertex to

# the destination vertex

def printPath(path, i, s):

 if (i != s):

 

 # Condition to check if

 # there is no path between

 # the vertices

 if (path[i] == -1): 

 print("Path not found!!");

 return; 

 printPath(path, path[i], s);

 print(path[i] + " ");

 

# Driver Code

if __name__=='__main__':

 

 v = []

 n = 4

 s = 0;

 

 # Loop to create the nodes

 for i in range(n):

 a = Node(i);

 v.append(a);

 

 # Creating directed

 # weighted edges

 v[0].Add_child(1, 1);

 v[0].Add_child(2, 4);

 v[1].Add_child(2, 2);

 v[1].Add_child(3, 6);

 v[2].Add_child(3, 3);

 path = [0 for i in range(len(v))];

 dist = dijkstraDist(v, s, path);

 

 # Loop to print the distance of

 # every node from source vertex

 for i in range(len(dist)):

 if (dist[i] == infi):

 

 print("{0} and {1} are not " +

 "connected".format(i, s));

 continue; 

 print("Distance of {}th vertex from source vertex {} is:
{}".format(

 i, s, dist[i]));

 

 # This code is contributed by pratham76  
  
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

// shortest path in a directed

// graph from source vertex to

// the destination vertex

using System;

using System.Collections;

using System.Collections.Generic;

 

class Pair

{

 public int first, second;

 

 public Pair(int first, int second)

 {

 this.first = first;

 this.second = second;

 }

}

 

class GFG

{

 

static int infi = 1000000000;

 

// Class of the node

class Node

{

 public int vertexNumber;

 

 // Adjacency list that shows the

 // vertexNumber of child vertex

 // and the weight of the edge

 public List<Pair> children;

 

 public Node(int vertexNumber)

 {

 this.vertexNumber = vertexNumber;

 children = new List<Pair>();

 }

 

 // Function to Add the child for

 // the given node

 public void Add_child(int vNumber, int length)

 {

 Pair p = new Pair(vNumber, length);

 children.Add(p);

 }

}

 

// Function to find the distance of

// the node from the given source

// vertex to the destination vertex

static int[] dijkstraDist(List<Node> g,

 int s, int[] path)

{

 

 // Stores distance of each

 // vertex from source vertex

 int[] dist = new int[g.Count];

 

 // bool array that shows

 // whether the vertex 'i'

 // is visited or not

 bool[] visited = new bool[g.Count];

 for(int i = 0; i < g.Count; i++)

 {

 visited[i] = false;

 path[i] = -1;

 dist[i] = infi;

 }

 dist[s] = 0;

 path[s] = -1;

 int current = s;

 

 // Set of vertices that has

 // a parent (one or more)

 // marked as visited

 HashSet<int> sett = new HashSet<int>();

 

 while (true)

 {

 

 // Mark current as visited

 visited[current] = true;

 for(int i = 0;

 i < g[current].children.Count;

 i++)

 {

 int v = g[current].children[i].first; 

 if (visited[v])

 continue;

 

 // Inserting into the

 // visited vertex

 sett.Add(v);

 int alt = dist[current] +

 g[current].children[i].second;

 

 // Condition to check the distance

 // is correct and update it

 // if it is minimum from the previous

 // computed distance

 if (alt < dist[v])

 {

 dist[v] = alt;

 path[v] = current;

 }

 }

 sett.Remove(current);

 

 if (sett.Count == 0)

 break;

 

 // The new current

 int minDist = infi;

 int index = 0;

 

 // Loop to update the distance

 // of the vertices of the graph

 foreach(int a in sett)

 {

 if (dist[a] < minDist)

 {

 minDist = dist[a];

 index = a;

 }

 }

 current = index;

 }

 return dist;

}

 

// Function to print the path

// from the source vertex to

// the destination vertex

void printPath(int[] path, int i, int s)

{

 if (i != s)

 {

 

 // Condition to check if

 // there is no path between

 // the vertices

 if (path[i] == -1)

 {

 Console.WriteLine("Path not found!!");

 return;

 }

 printPath(path, path[i], s);

 Console.WriteLine(path[i] + " ");

 }

}

 

// Driver Code

public static void Main(string[] args)

{

 List<Node> v = new List<Node>();

 int n = 4, s = 0;

 

 // Loop to create the nodes

 for(int i = 0; i < n; i++)

 {

 Node a = new Node(i);

 v.Add(a);

 }

 

 // Creating directed

 // weighted edges

 v[0].Add_child(1, 1);

 v[0].Add_child(2, 4);

 v[1].Add_child(2, 2);

 v[1].Add_child(3, 6);

 v[2].Add_child(3, 3);

 

 int[] path = new int[v.Count];

 int[] dist = dijkstraDist(v, s, path);

 

 // Loop to print the distance of

 // every node from source vertex

 for(int i = 0; i < dist.Length; i++)

 {

 if (dist[i] == infi)

 {

 Console.Write("{0} and {1} are not " +

 "connected\n", i, s);

 continue;

 }

 Console.Write("Distance of {0}th vertex " +

 "from source vertex {1} is: {2}\n",

 i, s, dist[i]);

 }

}

}

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**  
Distance of 0th vertex from source vertex 0 is: 0  
Distance of 1th vertex from source vertex 0 is: 1  
Distance of 2th vertex from source vertex 0 is: 3  
Distance of 3th vertex from source vertex 0 is: 6  

**Time Complexity:** ![{\\displaystyle \\Theta \(\(|V|^{2}\)\\log |V|\)}
](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
cbf4ca942e8c30a6ce47e7227b92ae29_l3.png)  
**Related articles:** We have already discussed the shortest path in directed
graph using Topological Sorting, in this article: Shortest path in Directed
Acyclic graph  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

