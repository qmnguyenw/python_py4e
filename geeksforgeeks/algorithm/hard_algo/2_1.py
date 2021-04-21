Maximum sum possible for every node by including it in a segment of N-Ary Tree



Given an **N-Ary** tree containing **N** nodes and an array **weight [ ]**
that denotes the **weight** of the nodes which can be **positive** or
**negative** , the task for every node is to print the **maximum sum**
possible by a sequence of nodes including the current node.

 **Examples:**

    
    
     **Input:** N = 7
    weight[] = [-8, 9, 7, -4, 5, -10, -6]
    N-Ary tree:
                    -8
                   /   \
                  9      7
                /  \    / 
              -4    5 -10
              /
            -6
    **Output:** 13 14 13 10 14 3 4
    
    **Explanations:**
    Node -8: [-8 + 9 + 7 + 5] = 13
    Node 9: [9 + 5] = 14
    Node 3: [7 + (-8) + 9 + 5] = 13
    Node 4: [-4 + 9 + 5] = 10
    Node: [5 + 9] = 14
    Node 6: [-10 + 7 + (-8) + 9 + 5] = 3
    Node 7: [-6 + (-4) + 9 + 5] = 4
    
    **Input:** N = 6
    weight[] = [2, -7, -5, 8, 4, -10]
    N-Ary tree:
                     2
                   /   \
                 -7    -5
                 / \     \
                8   4    -10
    **Output:** 7 7 2 8 7 -8

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** This problem can be solved using Dp on Trees technique by
applying two DFS.

  * Apply the first DFS to store the maximum sum possible for every node by including them in a sequence with their respective **successors**. Store the maximum possible sum in **dp1[].** array.
  * Maximum possible value for each node in the first DFS can be obtained by:

> dp1[node] += maximum(0, dp1[child1], dp1[child2], …)  
>

  * Perform the second **Dfs** to update the maximum sum for each node in **dp1[]** by including them in a sequence with their **ancestors** also. The maximum values stored in **dp2[]** for every node are the required answers.
  * Maximum possible value for each node in the second DFS can be obtained by:

>  **dp2[node] = dp1[node] + maximum(0, maxSumAncestors)**  
>  Best answer can be obtained by including or excluding the maximum sum
> possible for its ancestors  
> where **maxSumAncestors = dp2[parent] – maximum(0, dp1[node])** , i.e.
> including or excluding contribution of the maximum sum of the current node
> stored in dp1[]  
>
>
>  
>
>
>  
>

Refer to the pictorial explanation for better understanding:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200612172809/graph114.png)

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to calculate the maximum

// sum possible for every node by including

// it in a segment of the N-Ary Tree

#include <bits/stdc++.h>

using namespace std;

// Stores the maximum

// sum possible for every node

// by including them in a segment

// with their successors

int dp1[100005];

// Stores the maximum

// sum possible for every node

// by including them in a segment

// with their ancestors

int dp2[100005];

// Store the maximum sum

// for every node by

// including it in a

// segment with its successors

void dfs1(int u, int par,

 vector<int> g[],

 int weight[])

{

 dp1[u] = weight[u];

 for (auto c: g[u]) {

 if (c != par) {

 dfs1(c, u, g, weight);

 dp1[u] += max(0, dp1);

 }

 }

}

// Update the maximum sums

// for each node by including

// them in a sequence with

// their ancestors

void dfs2(int u, int par,

 vector<int> g[],

 int weight[])

{

 // Condition to check,

 // if current node is not root

 if (par != 0) {

 int maxSumAncestors = dp2[par]

 - max(0, dp1[u]);

 dp2[u] = dp1[u] + max(0,

 maxSumAncestors);

 }

 for (auto c: g[u]) {

 if (c != par) {

 dfs2(c, u, g, weight);

 }

 }

}

// Add edges

void addEdge(int u, int v, vector<int> g[])

{

 g[u].push_back(v);

 g[v].push_back(u);

}

// Function to find the maximum

// answer for each node

void maxSumSegments(vector<int> g[],

 int weight[],

 int n)

{

 // Compute the maximum sums

 // with successors

 dfs1(1, 0, g, weight);

 // Store the computed maximums

 for (int i = 1; i <= n; i++) {

 dp2[i] = dp1[i];

 }

 // Update the maximum sums

 // by including their

 // ancestors

 dfs2(1, 0, g, weight);

}

// Print the desired result

void printAns(int n)

{

 for (int i = 1; i <= n; i++) {

 cout << dp2[i] << " ";

 }

}

// Driver Program

int main()

{

 // Number of nodes

 int n = 6;

 int u, v;

 // graph

 vector<int> g[100005];

 // Add edges

 addEdge(1, 2, g);

 addEdge(1, 3, g);

 addEdge(2, 4, g);

 addEdge(2, 5, g);

 addEdge(3, 6, g);

 addEdge(4, 7, g);

 // Weight of each node

 int weight[n + 1];

 weight[1] = -8;

 weight[2] = 9;

 weight[3] = 7;

 weight[4] = -4;

 weight[5] = 5;

 weight[6] = -10;

 weight[7] = -6;

 // Compute the max sum

 // of segments for each

 // node

 maxSumSegments(g, weight, n);

 // Print the answer

 // for every node

 printAns(n);

 return 0;

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

# Python3 program to calculate the maximum

# sum possible for every node by including

# it in a segment of the N-Ary Tree

 

# Stores the maximum

# sum possible for every node

# by including them in a segment

# with their successors

dp1 = [0 for i in range(100005)]

 

# Stores the maximum sum possible

# for every node by including them

# in a segment with their ancestors

dp2 = [0 for i in range(100005)]

 

# Store the maximum sum for every

# node by including it in a

# segment with its successors

def dfs1(u, par, g, weight):

 

 dp1[u] = weight[u]

 

 for c in g[u]:

 if (c != par):

 dfs1(c, u, g, weight)

 dp1[u] += max(0, dp1)

 

# Update the maximum sums

# for each node by including

# them in a sequence with

# their ancestors

def dfs2(u, par, g, weight):

 # Condition to check,

 # if current node is not root

 if (par != 0):

 maxSumAncestors = dp2[par] - max(0, dp1[u])

 dp2[u] = dp1[u] + max(0, maxSumAncestors)

 

 for c in g[u]:

 if (c != par):

 dfs2(c, u, g, weight)

 

# Add edges

def addEdge(u, v, g):

 g[u].append(v)

 g[v].append(u)

# Function to find the maximum

# answer for each node

def maxSumSegments(g, weight, n):

 

 # Compute the maximum sums

 # with successors

 dfs1(1, 0, g, weight)

 

 # Store the computed maximums

 for i in range(1, n + 1):

 dp2[i] = dp1[i]

 

 # Update the maximum sums

 # by including their

 # ancestors

 dfs2(1, 0, g, weight)

# Print the desired result

def printAns(n):

 for i in range(1, n):

 print(dp2[i], end = ' ')

 

# Driver code

if __name__=='__main__':

 

 # Number of nodes

 n = 7

 u = 0

 v = 0

 

 # Graph

 g = [[] for i in range(100005)]

 

 # Add edges

 addEdge(1, 2, g)

 addEdge(1, 3, g)

 addEdge(2, 4, g)

 addEdge(2, 5, g)

 addEdge(3, 6, g)

 addEdge(4, 7, g)

 

 # Weight of each node

 weight=[0 for i in range(n + 1)]

 weight[1] = -8

 weight[2] = 9

 weight[3] = 7

 weight[4] = -4

 weight[5] = 5

 weight[6] = -10

 weight[7] = -6

 

 # Compute the max sum

 # of segments for each

 # node

 maxSumSegments(g, weight, n)

 

 # Print the answer

 # for every node

 printAns(n)

# This code is contributed by pratham76  
  
---  
  
 __

 __

 **Output:**

    
    
    13 14 13 10 14 3

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

