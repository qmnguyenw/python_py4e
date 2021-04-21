Find number of edges that can be broken in a tree such that Bitwise OR of
resulting two trees are equal



Given a tree with n nodes and a number associated with every node. We can
break any edge of the tree which will result in the formation of 2 new trees.
We have to count the number of edges such that the Bitwise OR of the nodes
present in the two trees formed after breaking that edge are equal. The value
of every node is ≤ 106.

 **Examples:**

    
    
    **Input:** values[]={2, 3, 32, 43, 8}
             1
            / \
           2   3
          /     \
         4       5
    **Output:** 1
    If we break the edge between 2 and 4 then the Bitwise OR 
    of both the resulting tree will be 43.
    
    **Input:** values[]={1, 3, 2, 3}
            1
          / | \
         2  3  4
    **Output:** 2
    The edge between 1 and 2 can be broken,the Bitwise OR 
    of the resulting two trees will be 3.
    Similarly, the edge between 1 and 4 can also be broken.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem can be solved using simple DFS. Since the value of
the nodes are ≤ 106, it can be represented using 22 binary bits. The Bitwise
OR of the value of the nodes can also be represented in 22 binary bits. The
approach is to find out the number of times each bit is set in all the values
of a sub-tree. For each edge we will check that for each bit from 0 to 21 the
numbers with that particular bit as set are either zero in both the resulting
trees or greater than zero in both the resulting trees and if the condition is
satisfied for all the bits than that edge is counted in the result.

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

#include<bits/stdc++.h>

using namespace std;

 

 int m[1000],x[22];

 

 // Array to store the number of times each bit 

 // is set in all the values of a subtree 

 int a[1000][22];

 

 vector<vector<int>> g; 

 int ans = 0; 

 

 // Function to perform simple DFS 

 void dfs(int u, int p) 

 { 

 for (int i=0;i<g[u].size();i++) { 

 int v = g[u][i];

 if (v != p) { 

 dfs(v, u); 

 

 // Finding the number of times each bit is set 

 // in all the values of a subtree rooted at v 

 for (int i = 0; i < 22; i++) 

 a[u][i] += a[v][i]; 

 } 

 } 

 

 // Checking for each bit whether the numbers 

 // with that particular bit as set are 

 // either zero in both the resulting trees or 

 // greater than zero in both the resulting trees 

 int pp = 0; 

 for (int i = 0; i < 22; i++) { 

 if (!((a[u][i] > 0 && x[i] - a[u][i] > 0) 

 || (a[u][i] == 0 && x[i] == 0))) { 

 pp = 1; 

 break; 

 } 

 } 

 if (pp == 0) 

 ans++; 

 } 

 

 // Driver code 

 int main()

 { 

 

 // Number of nodes 

 int n = 4; 

 

 // ArrayList to store the tree 

 g.resize(n+1); 

 

 // Array to store the value of nodes 

 m[1] = 1; 

 m[2] = 3; 

 m[3] = 2; 

 m[4] = 3; 

 

 

 // Array to store the number of times each bit 

 // is set in all the values in complete tree 

 

 for (int i = 1; i <= n; i++) { 

 int y = m[i]; 

 int k = 0; 

 

 // Finding the set bits in the value of node i 

 while (y != 0) { 

 int p = y % 2; 

 if (p == 1) { 

 x[k]++; 

 a[i][k]++; 

 } 

 y = y / 2; 

 k++; 

 } 

 } 

 

 // push_back edges 

 g[1].push_back(2); 

 g[2].push_back(1); 

 g[1].push_back(3); 

 g[3].push_back(1); 

 g[1].push_back(4); 

 g[4].push_back(1); 

 dfs(1, 0); 

 cout<<(ans); 

} 

//contributed by Arnab Kundu  
  
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

public class GFG {

 static int m[], a[][], x[];

 static ArrayList<Integer> g[];

 static int ans = 0;

 

 // Function to perform simple DFS

 static void dfs(int u, int p)

 {

 for (int v : g[u]) {

 if (v != p) {

 dfs(v, u);

 

 // Finding the number of times each bit is set

 // in all the values of a subtree rooted at v

 for (int i = 0; i < 22; i++)

 a[u][i] += a[v][i];

 }

 }

 

 // Checking for each bit whether the numbers

 // with that particular bit as set are

 // either zero in both the resulting trees or

 // greater than zero in both the resulting trees

 int pp = 0;

 for (int i = 0; i < 22; i++) {

 if (!((a[u][i] > 0 && x[i] - a[u][i] > 0)

 || (a[u][i] == 0 && x[i] == 0))) {

 pp = 1;

 break;

 }

 }

 if (pp == 0)

 ans++;

 }

 

 // Driver code

 public static void main(String args[])

 {

 

 // Number of nodes

 int n = 4;

 

 // ArrayList to store the tree

 g = new ArrayList[n + 1];

 

 // Array to store the value of nodes

 m = new int[n + 1];

 m[1] = 1;

 m[2] = 3;

 m[3] = 2;

 m[4] = 3;

 

 // Array to store the number of times each bit

 // is set in all the values of a subtree

 a = new int[n + 1][22];

 

 // Array to store the number of times each bit

 // is set in all the values in complete tree

 x = new int[22];

 for (int i = 1; i <= n; i++) {

 g[i] = new ArrayList<>();

 int y = m[i];

 int k = 0;

 

 // Finding the set bits in the value of node i

 while (y != 0) {

 int p = y % 2;

 if (p == 1) {

 x[k]++;

 a[i][k]++;

 }

 y = y / 2;

 k++;

 }

 }

 

 // Add edges

 g[1].add(2);

 g[2].add(1);

 g[1].add(3);

 g[3].add(1);

 g[1].add(4);

 g[4].add(1);

 dfs(1, 0);

 System.out.println(ans);

 }

}  
  
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

m, x = [0] * 1000, [0] * 22

 

# Array to store the number of times each bit 

# is set in all the values of a subtree 

a = [[0 for i in range(22)] 

 for j in range(1000)]

ans = 0

 

# Function to perform simple DFS 

def dfs(u, p):

 

 global ans

 for i in range(0, len(g[u])): 

 v = g[u][i] 

 if v != p: 

 dfs(v, u) 

 

 # Finding the number of times 

 # each bit is set in all the 

 # values of a subtree rooted at v 

 for i in range(0, 22): 

 a[u][i] += a[v][i] 

 

 # Checking for each bit whether the numbers 

 # with that particular bit as set are 

 # either zero in both the resulting trees or 

 # greater than zero in both the resulting trees 

 pp = 0

 for i in range(0, 22): 

 if (not((a[u][i] > 0 and

 x[i] - a[u][i] > 0) 

 or (a[u][i] == 0 and x[i] == 0))): 

 pp = 1

 break

 

 if pp == 0: 

 ans += 1

 

# Driver code 

if __name__ == "__main__":

 

 # Number of nodes 

 n = 4

 

 # ArrayList to store the tree 

 g = [[] for i in range(n+1)]

 

 # Array to store the value of nodes 

 m[1] = 1

 m[2] = 3

 m[3] = 2

 m[4] = 3

 

 # Array to store the number of times 

 # each bit is set in all the values

 # in complete tree 

 for i in range(1, n+1): 

 y, k = m[i], 0

 

 # Finding the set bits in the 

 # value of node i 

 while y != 0: 

 p = y % 2

 if p == 1: 

 x[k] += 1

 a[i][k] += 1

 

 y = y // 2

 k += 1

 

 # append edges 

 g[1].append(2) 

 g[2].append(1) 

 g[1].append(3) 

 g[3].append(1) 

 g[1].append(4) 

 g[4].append(1) 

 dfs(1, 0) 

 print(ans) 

 

# This code is contributed by Rituraj Jain  
  
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

using System;

using System.Collections.Generic;

 

class GFG 

{

 static int []m;

 static int [,]a;

 static int []x;

 static List<int> []g;

 static int ans = 0;

 

 // Function to perform simple DFS

 static void dfs(int u, int p)

 {

 foreach (int v in g[u])

 {

 if (v != p) 

 {

 dfs(v, u);

 

 // Finding the number of times each bit is set

 // in all the values of a subtree rooted at v

 for (int i = 0; i < 22; i++)

 a[u,i] += a[v,i];

 }

 }

 

 // Checking for each bit whether the numbers

 // with that particular bit as set are

 // either zero in both the resulting trees or

 // greater than zero in both the resulting trees

 int pp = 0;

 for (int i = 0; i < 22; i++) 

 {

 if (!((a[u,i] > 0 && x[i] - a[u,i] > 0)

 || (a[u,i] == 0 && x[i] == 0)))

 {

 pp = 1;

 break;

 }

 }

 if (pp == 0)

 ans++;

 }

 

 // Driver code

 public static void Main(String []args)

 {

 

 // Number of nodes

 int n = 4;

 

 // ArrayList to store the tree

 g = new List<int>[n + 1];

 

 // Array to store the value of nodes

 m = new int[n + 1];

 m[1] = 1;

 m[2] = 3;

 m[3] = 2;

 m[4] = 3;

 

 // Array to store the number of times each bit

 // is set in all the values of a subtree

 a = new int[n + 1,22];

 

 // Array to store the number of times each bit

 // is set in all the values in complete tree

 x = new int[22];

 for (int i = 1; i <= n; i++) 

 {

 g[i] = new List<int>();

 int y = m[i];

 int k = 0;

 

 // Finding the set bits in the value of node i

 while (y != 0) 

 {

 int p = y % 2;

 if (p == 1) 

 {

 x[k]++;

 a[i,k]++;

 }

 y = y / 2;

 k++;

 }

 }

 

 // Add edges

 g[1].Add(2);

 g[2].Add(1);

 g[1].Add(3);

 g[3].Add(1);

 g[1].Add(4);

 g[4].Add(1);

 dfs(1, 0);

 Console.WriteLine(ans);

 }

}

 

// This code contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

