Check if the given permutation is a valid BFS of a given Tree



Given a tree with **N** nodes numbered from **1 to N** and a permutation array
of numbers from **1 to N**. Check if it is possible to obtain the given
permutation array by applying BFS (Breadth First Traversal) on the given tree.  
 **Note:** Traversal will always start from 1.  
 **Example:**

> **Input:** arr[] = { 1 5 2 3 4 6 }  
> Edges of the given tree:  
> 1 – 2  
> 1 – 5  
> 2 – 3  
> 2 – 4  
> 5 – 6  
> **Output:** No  
> **Explanation:**  
> There is no such traversal which is same as the given permutation. The valid
> traversals are:  
> 1 2 5 3 4 6  
> 1 2 5 4 3 6  
> 1 5 2 6 3 4  
> 1 5 2 6 4 3  
>  **Input:** arr[] = { 1 2 3 }  
> Edges of the given tree:  
> 1 – 2  
> 2 – 3  
> **Output:** Yes  
> **Explanation:**  
> The given permutation is a valid one.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** To solve the problem mentioned above we have to follow the
steps given below:

  * In BFS we visit all the neighbors of the current node and push their children in the **queue** in order and repeat this process until the queue is not empty.
  * Suppose there are **two children** of root: A and B. We are free to choose which of them to visit first. Let’s say we visit A first, but now we will have to push children of A in the queue, and we cannot visit children of B before A.
  * So basically we can visit the children of a particular node in any order but the order in which the children of 2 different nodes should be visited is fixed i.e. if A if visited before B, then all the children of A should be visited before all the children of B.
  * We will do the same. We will **make a queue of sets** and in each set, we will push the children of a particular node and traverse the permutation alongside. If the current element of **permutation is found** in the set at the top of the queue, then we will proceed otherwise, we will return false.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to check if the

// given permutation is a valid

// BFS of a given tree

#include <bits/stdc++.h>

using namespace std;

// map for storing the tree

map<int, vector<int> > tree;

// map for marking

// the nodes visited

map<int, int> vis;

// Function to check if

// permutation is valid

bool valid_bfs(vector<int>& v)

{

 int n = (int)v.size();

 queue<set<int> > q;

 set<int> s;

 s.insert(1);

 /*inserting the root in

 the front of queue.*/

 q.push(s);

 int i = 0;

 while (!q.empty() && i < n)

 {

 // If the current node

 // in a permutation

 // is already visited

 // then return false

 if (vis.count(v[i]))

 {

 return 0;

 }

 vis[v[i]] = 1;

 // if all the children of previous

 // nodes are visited then pop the

 // front element of queue.

 if (q.front().size() == 0)

 {

 q.pop();

 }

 // if the current element of the

 // permutation is not found

 // in the set at the top of queue

 // then return false

 if (q.front().find(v[i])

 == q.front().end()) {

 return 0;

 }

 s.clear();

 // push all the children of current

 // node in a set and then push

 // the set in the queue.

 for (auto j : tree[v[i]]) {

 if (vis.count(j)) {

 continue;

 }

 s.insert(j);

 }

 if (s.size() > 0) {

 set<int> temp = s;

 q.push(temp);

 }

 s.clear();

 // erase the current node from

 // the set at the top of queue

 q.front().erase(v[i]);

 // increment the index

 // of permutation

 i++;

 }

 return 1;

}

// Driver code

int main()

{

 tree[1].push_back(2);

 tree[2].push_back(1);

 tree[1].push_back(5);

 tree[5].push_back(1);

 tree[2].push_back(3);

 tree[3].push_back(2);

 tree[2].push_back(4);

 tree[4].push_back(2);

 tree[5].push_back(6);

 tree[6].push_back(5);

 vector<int> arr

 = { 1, 5, 2, 3, 4, 6 };

 if (valid_bfs(arr))

 cout << "Yes" << endl;

 else

 cout << "No" << endl;

 return 0;

}

// This code is contributed by rutvik_56  
  
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

// Java implementation to check if the

// given permutation is a valid

// BFS of a given tree

import java.util.*;

class GFG{

// Map for storing the tree

static HashMap<Integer,

 Vector<Integer> > tree =

 new HashMap<>();

// Map for marking

// the nodes visited

static HashMap<Integer,

 Integer> vis =

 new HashMap<>();

// Function to check if

// permutation is valid

static boolean valid_bfs(List<Integer> v)

{

 int n = (int)v.size();

 Queue<HashSet<Integer> > q =

 new LinkedList<>();

 HashSet<Integer> s = new HashSet<>();

 s.add(1);

 // Inserting the root in

 // the front of queue.

 q.add(s);

 int i = 0;

 while (!q.isEmpty() && i < n)

 {

 // If the current node

 // in a permutation

 // is already visited

 // then return false

 if (vis.containsKey(v.get(i)))

 {

 return false;

 }

 vis.put(v.get(i), 1);

 // If all the children of previous

 // nodes are visited then pop the

 // front element of queue.

 if (q.peek().size() == 0)

 {

 q.remove();

 }

 // If the current element of the

 // permutation is not found

 // in the set at the top of queue

 // then return false

 if (!q.peek().contains(v.get(i)))

 {

 return false;

 }

 s.clear();

 // Push all the children of current

 // node in a set and then push

 // the set in the queue.

 for (int j : tree.get(v.get(i)))

 {

 if (vis.containsKey(j))

 {

 continue;

 }

 s.add(j);

 }

 if (s.size() > 0)

 {

 HashSet<Integer> temp = s;

 q.add(temp);

 }

 s.clear();

 // Erase the current node from

 // the set at the top of queue

 q.peek().remove(v.get(i));

 // Increment the index

 // of permutation

 i++;

 }

 return true;

}

// Driver code

public static void main(String[] args)

{

 for (int i = 1; i <= 6; i++)

 {

 tree.put(i, new Vector<Integer>());

 }

 

 tree.get(1).add(2);

 tree.get(2).add(1);

 tree.get(1).add(5);

 tree.get(5).add(1);

 tree.get(2).add(3);

 tree.get(3).add(2);

 tree.get(2).add(4);

 tree.get(4).add(2);

 tree.get(5).add(6);

 tree.get(6).add(5);

 Integer []arr1 = {1, 5, 2, 3, 4, 6};

 List<Integer> arr = Arrays.asList(arr1);

 if (valid_bfs(arr))

 System.out.print("Yes" + "\n");

 else

 System.out.print("No" + "\n");

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

# Python3 implementation to check if the

# given permutation is a valid

# BFS of a given tree

 

# map for storing the tree

tree=dict()

 

# map for marking

# the nodes visited

vis=dict()

 

# Function to check if

# permutation is valid

def valid_bfs( v):

 n = len(v)

 

 q=[]

 s=set()

 s.add(1);

 

 '''inserting the root in

 the front of queue.'''

 q.append(s);

 i = 0;

 

 while (len(q)!=0 and i < n):

 

 # If the current node

 # in a permutation

 # is already visited

 # then return false

 if (v[i] in vis):

 return 0;

 

 vis[v[i]] = 1;

 

 # if all the children of previous

 # nodes are visited then pop the

 # front element of queue.

 if (len(q[0])== 0):

 q.pop(0);

 

 # if the current element of the

 # permutation is not found

 # in the set at the top of queue

 # then return false

 if (v[i] not in q[0]):

 return 0;

 

 s.clear();

 

 # append all the children of current

 # node in a set and then append

 # the set in the queue.

 for j in tree[v[i]]:

 

 if (j in vis):

 continue;

 

 s.add(j);

 

 if (len(s) > 0):

 

 temp = s;

 q.append(temp);

 

 s.clear();

 

 # erase the current node from

 # the set at the top of queue

 q[0].discard(v[i]);

 

 # increment the index

 # of permutation

 i+=1

 

 return 1;

 

# Driver code

if __name__=="__main__":

 tree[1]=[]

 tree[2]=[]

 tree[5]=[]

 tree[3]=[]

 tree[2]=[]

 tree[4]=[]

 tree[6]=[]

 tree[1].append(2);

 tree[2].append(1);

 tree[1].append(5);

 tree[5].append(1);

 tree[2].append(3);

 tree[3].append(2);

 tree[2].append(4);

 tree[4].append(2);

 tree[5].append(6);

 tree[6].append(5);

 

 arr = [ 1, 5, 2, 3, 4, 6 ]

 

 if (valid_bfs(arr)):

 print("Yes")

 else:

 print("No")  
  
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

// C# implementation to check

// if the given permutation

// is a valid BFS of a given tree

using System;

using System.Collections.Generic;

class GFG{

// Map for storing the tree

static Dictionary<int,

 List<int>> tree = new Dictionary<int,

 List<int>>();

// Map for marking

// the nodes visited

static Dictionary<int,

 int> vis = new Dictionary<int,

 int>();

// Function to check if

// permutation is valid

static bool valid_bfs(List<int> v)

{

 int n = (int)v.Count;

 Queue<HashSet<int>> q =

 new Queue<HashSet<int>>();

 HashSet<int> s = new HashSet<int>();

 s.Add(1);

 // Inserting the root in

 // the front of queue.

 q.Enqueue(s);

 int i = 0;

 while (q.Count != 0 && i < n)

 {

 // If the current node

 // in a permutation

 // is already visited

 // then return false

 if (vis.ContainsKey(v[i]))

 {

 return false;

 }

 vis.Add(v[i], 1);

 // If all the children of previous

 // nodes are visited then pop the

 // front element of queue.

 if (q.Peek().Count == 0)

 {

 q.Dequeue();

 }

 // If the current element of the

 // permutation is not found

 // in the set at the top of queue

 // then return false

 if (!q.Peek().Contains(v[i]))

 {

 return false;

 }

 

 s.Clear();

 // Push all the children of current

 // node in a set and then push

 // the set in the queue.

 foreach (int j in tree[v[i]])

 {

 if (vis.ContainsKey(j))

 {

 continue;

 }

 s.Add(j);

 }

 if (s.Count > 0)

 {

 HashSet<int> temp = s;

 q.Enqueue(temp);

 }

 s.Clear();

 // Erase the current node from

 // the set at the top of queue

 q.Peek().Remove(v[i]);

 // Increment the index

 // of permutation

 i++;

 }

 return true;

}

// Driver code

public static void Main(String[] args)

{

 for (int i = 1; i <= 6; i++)

 {

 tree.Add(i, new List<int>());

 }

 tree[1].Add(2);

 tree[2].Add(1);

 tree[1].Add(5);

 tree[5].Add(1);

 tree[2].Add(3);

 tree[3].Add(2);

 tree[2].Add(4);

 tree[4].Add(2);

 tree[5].Add(6);

 tree[6].Add(5);

 int []arr1 = {1, 5, 2, 3, 4, 6};

 List<int> arr = new List<int>();

 arr.AddRange(arr1);

 if (valid_bfs(arr))

 Console.Write("Yes" + "\n");

 else

 Console.Write("No" + "\n");

}

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    No

_**Time complexity:** O(N * log N)_  
 **Similar articles:** Check if the given permutation is a valid DFS of graph

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

