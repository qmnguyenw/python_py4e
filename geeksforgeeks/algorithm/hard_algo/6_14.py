Check if the array can be sorted using swaps between given indices only



Given an array **arr[]** of size **N** consisting of distinct integers from
range **[0, N – 1]** arranged in a random order. Also given a few pairs where
each pair denotes the indices where the elements of the array can be swapped.
There is no limit on the number of swaps allowed. The task is to find if it is
possible to arrange the array in ascending order using these swaps. If
possible then print **Yes** else print **No**.  
 **Examples:**  

> **Input:** arr[] = {0, 4, 3, 2, 1, 5}, pairs[][] = {{1, 4}, {2, 3}}  
> **Output:** Yes  
> swap(arr[1], arr[4]) -> arr[] = {0, 1, 3, 2, 4, 5}  
> swap(arr[2], arr[3]) -> arr[] = {0, 1, 2, 3, 4, 5}  
>  **Input:** arr[] = {1, 2, 3, 0, 4}, pairs[][] = {{2, 3}}  
> **Output:** No  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The given problem can be considered as a graph problem where
**N** denotes the total number of nodes in the graph and each swapping pair
denotes an undirected edge in the graph. We have to find out if it is possible
to convert the input array in the form of **{0, 1, 2, 3, …, N – 1}**.  
Let us call the above array as B. Now find out all the connected components of
both the arrays and if the elements differ for at least one component then the
answer is **No** else the answer is **Yes**.  
Below is the implementation of the above approach:  

## CPP

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

// Function that returns true if the array elements

// can be sorted with the given operation

bool canBeSorted(int N, vector<int> a, int P,

vector<pair<int, int> > vp)

{

 // To create the adjacency list of the graph

 vector<int> v[N];

 // Boolean array to mark the visited nodes

 bool vis[N] = { false };

 // Creating adjacency list for undirected graph

 for (int i = 0; i < P; i++) {

 v[vp[i].first].push_back(vp[i].second);

 v[vp[i].second].push_back(vp[i].first);

 }

 for (int i = 0; i < N; i++) {

 // If not already visited

 // then apply BFS

 if (!vis[i]) {

 queue<int> q;

 vector<int> v1;

 vector<int> v2;

 // Set visited to true

 vis[i] = true;

 // Push the node to the queue

 q.push(i);

 // While queue is not empty

 while (!q.empty()) {

 int u = q.front();

 v1.push_back(u);

 v2.push_back(a[u]);

 q.pop();

 // Check all the adjacent nodes

 for (auto s : v[u]) {

 // If not visited

 if (!vis[s]) {

 // Set visited to true

 vis[s] = true;

 q.push(s);

 }

 }

 }

 sort(v1.begin(), v1.end());

 sort(v2.begin(), v2.end());

 // If the connected component does not

 // contain same elements then return false

 if (v1 != v2)

 return false;

 }

 }

 return true;

}

// Driver code

int main()

{

 vector<int> a = { 0, 4, 3, 2, 1, 5 };

 int n = a.size();

 vector<pair<int, int> > vp = { { 1, 4 }, { 2, 3 } };

 int p = vp.size();

 if (canBeSorted(n, a, p, vp))

 cout << "Yes";

 else

 cout << "No";

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

import java.io.*;

import java.util.*;

class GFG

{

 

 // Function that returns true if the array elements

 // can be sorted with the given operation

 static boolean canBeSorted(int N, ArrayList<Integer> a,

 int p, ArrayList<ArrayList<Integer>> vp)

 {

 

 // To create the adjacency list of the graph

 ArrayList<ArrayList<Integer>> v = new
ArrayList<ArrayList<Integer>>();

 for(int i = 0; i < N; i++)

 {

 v.add(new ArrayList<Integer>());

 }

 

 // Boolean array to mark the visited nodes

 boolean[] vis = new boolean[N];

 // Creating adjacency list for undirected graph

 for (int i = 0; i < p; i++)

 {

 v.get(vp.get(i).get(0)).add(vp.get(i).get(1));

 v.get(vp.get(i).get(1)).add(vp.get(i).get(0));

 }

 for (int i = 0; i < N; i++)

 {

 

 // If not already visited

 // then apply BFS

 if (!vis[i])

 {

 Queue<Integer> q = new LinkedList<>();

 ArrayList<Integer> v1 = new ArrayList<Integer>();

 ArrayList<Integer> v2 = new ArrayList<Integer>();

 // Set visited to true 

 vis[i] = true;

 // Push the node to the queue

 q.add(i);

 // While queue is not empty

 while (q.size() > 0)

 {

 int u = q.poll();

 v1.add(u);

 v2.add(a.get(u));

 // Check all the adjacent nodes

 for(int s: v.get(u))

 {

 

 // If not visited

 if (!vis[s])

 {

 

 // Set visited to true

 vis[s] = true;

 q.add(s);

 }

 }

 }

 Collections.sort(v1);

 Collections.sort(v2);

 // If the connected component does not

 // contain same elements then return false

 if(!v1.equals(v2))

 {

 return false;

 }

 }

 }

 return true;

 }

 // Driver code

 public static void main (String[] args)

 {

 ArrayList<Integer> a = new ArrayList<Integer>(Arrays.asList(0,
4, 3, 2, 1, 5));

 int n = a.size();

 ArrayList<ArrayList<Integer>> vp = new
ArrayList<ArrayList<Integer>>();

 vp.add(new ArrayList<Integer>(Arrays.asList(1, 4)));

 vp.add(new ArrayList<Integer>(Arrays.asList(2, 3)));

 int p = vp.size();

 if (canBeSorted(n, a, p, vp))

 {

 System.out.println("Yes"); 

 }

 else

 {

 System.out.println("No");

 }

 }

}

// This code is contributed by avanitrachhadiya2155  
  
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

# Function that returns true if the array elements

# can be sorted with the given operation

def canBeSorted(N, a, P, vp):

 # To create the adjacency list of the graph

 v = [[] for i in range(N)]

 # Boolean array to mark the visited nodes

 vis = [False]*N

 # Creating adjacency list for undirected graph

 for i in range(P):

 v[vp[i][0]].append(vp[i][1])

 v[vp[i][1]].append(vp[i][0])

 for i in range(N):

 # If not already visited

 # then apply BFS

 if (not vis[i]):

 q = queue()

 v1 = []

 v2 = []

 # Set visited to true

 vis[i] = True

 # Push the node to the queue

 q.append(i)

 # While queue is not empty

 while (len(q) > 0):

 u = q.popleft()

 v1.append(u)

 v2.append(a[u])

 # Check all the adjacent nodes

 for s in v[u]:

 # If not visited

 if (not vis[s]):

 # Set visited to true

 vis[s] = True

 q.append(s)

 v1 = sorted(v1)

 v2 = sorted(v2)

 # If the connected component does not

 # contain same elements then return false

 if (v1 != v2):

 return False

 return True

# Driver code

if __name__ == '__main__':

 a = [0, 4, 3, 2, 1, 5]

 n = len(a)

 vp = [ [ 1, 4 ], [ 2, 3 ] ]

 p = len(vp)

 if (canBeSorted(n, a, p, vp)):

 print("Yes")

 else:

 print("No")

# This code is contributed by mohit kumar 29  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

