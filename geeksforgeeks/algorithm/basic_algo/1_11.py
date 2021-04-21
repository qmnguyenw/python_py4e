Sideways traversal of a Complete Binary Tree



Given a Complete Binary Tree, the task is to print the elements in the
following pattern. Let’s consider the tree to be:

![](https://media.geeksforgeeks.org/wp-content/uploads/20200218123136/Side-
Ways-Traversal-Input.png)

The tree is traversed in the following way:

![](https://media.geeksforgeeks.org/wp-content/uploads/20200218123716/Side-
Ways-Traversal-Output.png)

The output for the above tree is:

  

  

    
    
    1 3 7 11 10 9 8 4 5 6 2

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use the modified breadth first search function
to store all the nodes at every level in an array of vector. Along with it,
the maximum level up to which the tree needs to be traversed is also stored in
a variable. After this precomputation task, the following steps are followed
to get the required answer:

  1. Create a vector **tree[]** where **tree[i]** will store all the nodes of the tree at the level **i**.
  2. Take an integer variable **k** which keeps the track of the level number that is being traversed and another integer variable **path** which keeps the track of the number of cycles that have been completed. A **flag** variable is also created to keep the track of the direction in which the tree is being traversed.
  3. Now, start printing the rightmost nodes at each level until the **maximum level** is reached.
  4. Since the maximum level is reached, the direction has to be changed. In the last level, print elements from rightmost to left. And the value of **maxLevel** variable has to be decremented.
  5. As the tree is being traversed from the lower level to the upper level, the rightmost elements are printed. Since in the next iteration, the **maxlevel** value has been changed, it makes sure that already visited nodes in the last level are not traversed again.

The above steps are repeated until the entire tree is traversed.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to print sideways

// traversal of complete binary tree

 

#include <bits/stdc++.h>

using namespace std;

 

const int sz = 1e5;

int maxLevel = 0;

 

// Adjacency list representation

// of the tree

vector<int> tree[sz + 1];

 

// Boolean array to mark all the

// vertices which are visited

bool vis[sz + 1];

 

// Integer array to store the level

// of each node

int level[sz + 1];

 

// Array of vector where ith index

// stores all the nodes at level i

vector<int> nodes[sz + 1];

 

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

 qu.push({ node, 0 });

 nodes[0].push_back(node);

 vis[node] = true;

 level[1] = 0;

 

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

 level[child] = level[p.first] + 1;

 maxLevel = max(maxLevel, level[child]);

 nodes[level[child]].push_back(child);

 }

 }

 }

}

 

// Utility Function to display the pattern

void display()

{

 // k represents the level no.

 // cycle represents how many

 // cycles has been completed

 int k = 0, path = 0;

 int condn = (maxLevel) / 2 + 1;

 bool flag = true;

 

 // While there are nodes left to traverse

 while (condn--) {

 

 if (flag) {

 

 // Traversing whole level from

 // left to right

 int j = nodes[k].size() - 1;

 for (j = 0; j < nodes[k].size() - path; j++)

 cout << nodes[k][j] << " ";

 

 // Moving to new level

 k++;

 

 // Traversing rightmost unvisited

 // element in path path as we

 // move up to down

 while (k < maxLevel) {

 

 j = nodes[k].size() - 1;

 cout << nodes[k][j - path] << " ";

 k++;

 }

 

 j = nodes[k].size() - 1;

 if (k > path)

 for (j -= path; j >= 0; j--)

 cout << nodes[k][j] << " ";

 

 // Setting value of new maximum

 // level upto which we have to traverse

 // next time

 maxLevel--;

 

 // Updating from which level to

 // start new path

 k--;

 path++;

 

 flag = !flag;

 }

 else {

 

 // Traversing each element of remaing

 // last level from left to right

 int j = nodes[k].size() - 1;

 for (j = 0; j < nodes[k].size() - path; j++)

 cout << nodes[k][j] << " ";

 

 // Decrementing value of Max level

 maxLevel--;

 

 k--;

 

 // Traversing rightmost unvisited

 // element in path as we

 // move down to up

 while (k > path) {

 

 int j = nodes[k].size() - 1;

 cout << nodes[k][j - path] << " ";

 k--;

 }

 

 j = nodes[k].size() - 1;

 

 if (k == path)

 for (j -= path; j >= 0; j--)

 cout << nodes[k][j] << " ";

 

 path++;

 

 // Updating the level number from which

 // a new cycle has to be started

 k++;

 flag = !flag;

 }

 }

}

 

// Driver code

int main()

{

 

 // Initialising the above mentioned

 // complete binary tree

 for (int i = 1; i <= 5; i++) {

 

 // Adding edge to a binary tree

 addEdge(i, 2 * i);

 addEdge(i, 2 * i + 1);

 }

 

 // Calling modified bfs function

 bfs(1);

 

 display();

 

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

// Java program to print sideways

// traversal of complete binary tree

import java.util.*;

 

class GFG

{

 

static class pair

{ 

 int first, second; 

 public pair(int first, int second) 

 { 

 this.first = first; 

 this.second = second; 

 } 

} 

static int sz = (int) 1e5;

static int maxLevel = 0;

 

// Adjacency list representation

// of the tree

static Vector<Integer> []tree = new Vector[sz + 1];

 

// Boolean array to mark all the

// vertices which are visited

static boolean []vis = new boolean[sz + 1];

 

// Integer array to store the level

// of each node

static int []level = new int[sz + 1];

 

// Array of vector where ith index

// stores all the nodes at level i

static Vector<Integer> []nodes = new Vector[sz + 1];

 

// Utility function to create an

// edge between two vertices

static void addEdge(int a, int b)

{

 

 // Add a to b's list

 tree[a].add(b);

 

 // Add b to a's list

 tree[b].add(a);

}

 

// Modified Breadth-First Function

static void bfs(int node)

{

 

 // Create a queue of {child, parent}

 Queue<pair > qu = new LinkedList<>();

 

 // Push root node in the front of

 // the queue and mark as visited

 qu.add(new pair( node, 0 ));

 nodes[0].add(node);

 vis[node] = true;

 level[1] = 0;

 

 while (!qu.isEmpty()) {

 

 pair p = qu.peek();

 

 // Dequeue a vertex from queue

 qu.remove();

 vis[p.first] = true;

 

 // Get all adjacent vertices of the dequeued

 // vertex s. If any adjacent has not

 // been visited then enqueue it

 for (int child : tree[p.first]) {

 

 if (!vis[child]) {

 qu.add(new pair( child, p.first ));

 level[child] = level[p.first] + 1;

 maxLevel = Math.max(maxLevel, level[child]);

 nodes[level[child]].add(child);

 }

 }

 }

}

 

// Utility Function to display the pattern

static void display()

{

 // k represents the level no.

 // cycle represents how many

 // cycles has been completed

 int k = 0, path = 0;

 int condn = (maxLevel) / 2 + 1;

 boolean flag = true;

 

 // While there are nodes left to traverse

 while (condn-- > 0) {

 

 if (flag) {

 

 // Traversing whole level from

 // left to right

 int j = nodes[k].size() - 1;

 for (j = 0; j < nodes[k].size() - path; j++)

 System.out.print(nodes[k].get(j)+ " ");

 

 // Moving to new level

 k++;

 

 // Traversing rightmost unvisited

 // element in path path as we

 // move up to down

 while (k < maxLevel) {

 

 j = nodes[k].size() - 1;

 System.out.print(nodes[k].get(j - path)+ " ");

 k++;

 }

 

 j = nodes[k].size() - 1;

 if (k > path)

 for (j -= path; j >= 0; j--)

 System.out.print(nodes[k].get(j)+ " ");

 

 // Setting value of new maximum

 // level upto which we have to traverse

 // next time

 maxLevel--;

 

 // Updating from which level to

 // start new path

 k--;

 path++;

 

 flag = !flag;

 }

 else {

 

 // Traversing each element of remaing

 // last level from left to right

 int j = nodes[k].size() - 1;

 for (j = 0; j < nodes[k].size() - path; j++)

 System.out.print(nodes[k].get(j)+ " ");

 

 // Decrementing value of Max level

 maxLevel--;

 

 k--;

 

 // Traversing rightmost unvisited

 // element in path as we

 // move down to up

 while (k > path) {

 

 int c = nodes[k].size() - 1;

 System.out.print(nodes[k].get(c - path)+ " ");

 k--;

 }

 

 j = nodes[k].size() - 1;

 

 if (k == path)

 for (j -= path; j >= 0; j--)

 System.out.print(nodes[k].get(j)+ " ");

 

 path++;

 

 // Updating the level number from which

 // a new cycle has to be started

 k++;

 flag = !flag;

 }

 }

}

 

// Driver code

public static void main(String[] args)

{

 

 for (int i = 0; i < tree.length; i++) {

 tree[i] = new Vector<>();

 nodes[i] = new Vector<>();

 }

 

 // Initialising the above mentioned

 // complete binary tree

 for (int i = 1; i <= 5; i++) {

 

 // Adding edge to a binary tree

 addEdge(i, 2 * i);

 addEdge(i, 2 * i + 1);

 }

 

 // Calling modified bfs function

 bfs(1);

 

 display();

}

}

 

// This code is contributed by 29AjayKumar  
  
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

# Python3 program to prsideways

# traversal of complete binary tree

from collections import deque

 

sz = 10**5

maxLevel = 0

 

# Adjacency list representation

# of the tree

tree = [[] for i in range(sz + 1)]

 

# Boolean array to mark all the

# vertices which are visited

vis = [False]*(sz + 1)

 

# Integer array to store the level

# of each node

level = [0]*(sz + 1)

 

# Array of vector where ith index

# stores all the nodes at level i

nodes = [[] for i in range(sz + 1)]

 

# Utility function to create an

# edge between two vertices

def addEdge(a, b):

 

 # Add a to b's list

 tree[a].append(b)

 

 # Add b to a's list

 tree[b].append(a)

 

# Modified Breadth-First Function

def bfs(node):

 global maxLevel

 

 # Create a queue of {child, parent}

 qu = deque()

 

 # Push root node in the front of

 # the queue and mark as visited

 qu.append([node, 0])

 nodes[0].append(node)

 vis[node] = True

 level[1] = 0

 

 while (len(qu) > 0):

 

 p = qu.popleft()

 

 # Dequeue a vertex from queue

 vis[p[0]] = True

 

 # Get all adjacent vertices of the dequeued

 # vertex s. If any adjacent has not

 # been visited then enqueue it

 for child in tree[p[0]]:

 

 if (vis[child] == False):

 qu.append([child, p[0]])

 level[child] = level[p[0]] + 1

 maxLevel = max(maxLevel, level[child])

 nodes[level[child]].append(child)

 

# Utility Function to display the pattern

def display():

 global maxLevel

 

 # k represents the level no.

 # cycle represents how many

 # cycles has been completed

 k = 0

 path = 0

 condn = (maxLevel) // 2 + 1

 flag = True

 

 # While there are nodes left to traverse

 while (condn):

 

 if (flag):

 

 # Traversing whole level from

 # left to right

 j = len(nodes[k]) - 1

 for j in range(len(nodes[k])- path):

 print(nodes[k][j],end=" ")

 

 # Moving to new level

 k += 1

 

 # Traversing rightmost unvisited

 # element in path path as we

 # move up to down

 while (k < maxLevel):

 

 j = len(nodes[k]) - 1

 print(nodes[k][j - path], end=" ")

 k += 1

 

 j = len(nodes[k]) - 1

 if (k > path):

 while j >= 0:

 j -= path

 print(nodes[k][j], end=" ")

 j -= 1

 

 # Setting value of new maximum

 # level upto which we have to traverse

 # next time

 maxLevel -= 1

 

 # Updating from which level to

 # start new path

 k -= 1

 path += 1

 

 flag = not flag

 else:

 

 # Traversing each element of remaing

 # last level from left to right

 j = len(nodes[k]) - 1

 for j in range(len(nodes[k]) - path):

 print(nodes[k][j], end=" ")

 

 # Decrementing value of Max level

 maxLevel -= 1

 

 k -= 1

 

 # Traversing rightmost unvisited

 # element in path as we

 # move down to up

 while (k > path):

 

 j = len(nodes[k]) - 1

 print(nodes[k][j - path], end=" ")

 k -= 1

 

 j = len(nodes[k]) - 1

 

 if (k == path):

 while j >= 0:

 j -= path

 print(nodes[k][j],end=" ")

 j -= 1

 

 path += 1

 

 # Updating the level number from which

 # a new cycle has to be started

 k += 1

 flag = not flag

 condn -= 1

 

# Driver code

if __name__ == '__main__':

 

 # Initialising the above mentioned

 # complete binary tree

 for i in range(1,6):

 

 # Adding edge to a binary tree

 addEdge(i, 2 * i)

 addEdge(i, 2 * i + 1)

 

 # Calling modified bfs function

 bfs(1)

 

 display()

 

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

// C# program to print sideways

// traversal of complete binary tree

using System;

using System.Collections.Generic;

 

class GFG

{

 

class pair

{ 

 public int first, second; 

 public pair(int first, int second) 

 { 

 this.first = first; 

 this.second = second; 

 } 

} 

static int sz = (int) 1e5;

static int maxLevel = 0;

 

// Adjacency list representation

// of the tree

static List<int> []tree = new List<int>[sz + 1];

 

// Boolean array to mark all the

// vertices which are visited

static bool []vis = new bool[sz + 1];

 

// int array to store the level

// of each node

static int []level = new int[sz + 1];

 

// Array of vector where ith index

// stores all the nodes at level i

static List<int> []nodes = new List<int>[sz + 1];

 

// Utility function to create an

// edge between two vertices

static void addEdge(int a, int b)

{

 

 // Add a to b's list

 tree[a].Add(b);

 

 // Add b to a's list

 tree[b].Add(a);

}

 

// Modified Breadth-First Function

static void bfs(int node)

{

 

 // Create a queue of {child, parent}

 Queue<pair> qu = new Queue<pair>();

 

 // Push root node in the front of

 // the queue and mark as visited

 qu.Enqueue(new pair( node, 0 ));

 nodes[0].Add(node);

 vis[node] = true;

 level[1] = 0;

 

 while (qu.Count != 0) {

 

 pair p = qu.Peek();

 

 // Dequeue a vertex from queue

 qu.Dequeue();

 vis[p.first] = true;

 

 // Get all adjacent vertices of the dequeued

 // vertex s. If any adjacent has not

 // been visited then enqueue it

 foreach (int child in tree[p.first]) {

 

 if (!vis[child]) {

 qu.Enqueue(new pair( child, p.first ));

 level[child] = level[p.first] + 1;

 maxLevel = Math.Max(maxLevel, level[child]);

 nodes[level[child]].Add(child);

 }

 }

 }

}

 

// Utility Function to display the pattern

static void display()

{

 // k represents the level no.

 // cycle represents how many

 // cycles has been completed

 int k = 0, path = 0;

 int condn = (maxLevel) / 2 + 1;

 bool flag = true;

 

 // While there are nodes left to traverse

 while (condn-- > 0) {

 

 if (flag) {

 

 // Traversing whole level from

 // left to right

 int j = nodes[k].Count - 1;

 for (j = 0; j < nodes[k].Count - path; j++)

 Console.Write(nodes[k][j]+ " ");

 

 // Moving to new level

 k++;

 

 // Traversing rightmost unvisited

 // element in path path as we

 // move up to down

 while (k < maxLevel) {

 

 j = nodes[k].Count - 1;

 Console.Write(nodes[k][j - path]+ " ");

 k++;

 }

 

 j = nodes[k].Count - 1;

 if (k > path)

 for (j -= path; j >= 0; j--)

 Console.Write(nodes[k][j]+ " ");

 

 // Setting value of new maximum

 // level upto which we have to traverse

 // next time

 maxLevel--;

 

 // Updating from which level to

 // start new path

 k--;

 path++;

 

 flag = !flag;

 }

 else {

 

 // Traversing each element of remaing

 // last level from left to right

 int j = nodes[k].Count - 1;

 for (j = 0; j < nodes[k].Count - path; j++)

 Console.Write(nodes[k][j]+ " ");

 

 // Decrementing value of Max level

 maxLevel--;

 

 k--;

 

 // Traversing rightmost unvisited

 // element in path as we

 // move down to up

 while (k > path) {

 

 int c = nodes[k].Count - 1;

 Console.Write(nodes[k]+ " ");

 k--;

 }

 

 j = nodes[k].Count - 1;

 

 if (k == path)

 for (j -= path; j >= 0; j--)

 Console.Write(nodes[k][j]+ " ");

 

 path++;

 

 // Updating the level number from which

 // a new cycle has to be started

 k++;

 flag = !flag;

 }

 }

}

 

// Driver code

public static void Main(String[] args)

{

 

 for (int i = 0; i < tree.Length; i++) {

 tree[i] = new List<int>();

 nodes[i] = new List<int>();

 }

 

 // Initialising the above mentioned

 // complete binary tree

 for (int i = 1; i <= 5; i++) {

 

 // Adding edge to a binary tree

 addEdge(i, 2 * i);

 addEdge(i, 2 * i + 1);

 }

 

 // Calling modified bfs function

 bfs(1);

 

 display();

}

}

 

// This code contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    1 3 7 11 10 9 8 4 5 6 2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

