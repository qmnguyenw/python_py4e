Shortest path with exactly k edges in a directed and weighted graph | Set 2



Given a directed weighted graph and two vertices **S** and **D** in it, the
task is to find the shortest path from **S** to **D** with exactly **K** edges
on the path. If no such path exists, print -1.

 **Examples:**

> **Input:** N = 3, K = 2, ed = {{{1, 2}, 5}, {{2, 3}, 3}, {{3, 1}, 4}}, S =
> 1, D = 3  
> **Output:** 8  
> **Explanation:** The shortest path with two edges will be 1->2->3
>
>  **Input:** N = 3, K = 4, ed = {{{1, 2}, 5}, {{2, 3}, 3}, {{3, 1}, 4}}, S =
> 1, D = 3  
> **Output:** -1  
> **Explanation:** No path with edge length 4 exists from node 1 to 3
>
>  **Input:** N = 3, K = 5, ed = {{{1, 2}, 5}, {{2, 3}, 3}, {{3, 1}, 4}}, S =
> 1, D = 3  
> **Output:** 20  
> **Explanation:** Shortest path will be 1->2->3->1->2->3\.
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** An **O(V^3*K)** approach for this problem has already been
discussed in the previous article. In this article, an **O(E*K)** approach is
discussed for solving this problem.

The idea is to use dynamic-programming to solve this problem.

Let dp[X][J] be the shortest path from node **S** to node **X** using exactly
**J** edges in total. Using this, dp[X][J+1] can be calculated as:

    
    
    dp[X][J+1] = min(arr[Y][J]+weight[{Y, X}])
    for all **Y** which has an edge from **Y** to **X**.

The result for the problem can be computed by following below steps:

  1. Initialise an array, dis[] with initial value as ‘inf’ except dis[S] as 0.
  2. For i equals 1 – K, run a loop 
    * Initialise an array, dis1[] with initial value as ‘inf’.
    * For each edge in the graph,   
dis1[edge.second] = min(dis1[edge.second], dis[edge.first]+weight(edge))

  3. If dist[d] in infinity, return -1, else return dist[d].

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

#define inf 100000000

using namespace std;

// Function to find the smallest path

// with exactly K edges

double smPath(int s, int d,

 vector<pair<pair<int, int>, int> > ed,

 int n, int k)

{

 // Array to store dp

 int dis[n + 1];

 // Initialising the array

 for (int i = 0; i <= n; i++)

 dis[i] = inf;

 dis[s] = 0;

 // Loop to solve DP

 for (int i = 0; i < k; i++) {

 // Initialising next state

 int dis1[n + 1];

 for (int j = 0; j <= n; j++)

 dis1[j] = inf;

 // Recurrence relation

 for (auto it : ed)

 dis1[it.first.second] = min(dis1[it.first.second],

 dis[it.first.first]

 + it.second);

 for (int i = 0; i <= n; i++)

 dis[i] = dis1[i];

 }

 // Returning final answer

 if (dis[d] == inf)

 return -1;

 else

 return dis[d];

}

// Driver code

int main()

{

 int n = 4;

 vector<pair<pair<int, int>, int> > ed;

 // Input edges

 ed = { { { 0, 1 }, 10 },

 { { 0, 2 }, 3 },

 { { 0, 3 }, 2 },

 { { 1, 3 }, 7 },

 { { 2, 3 }, 7 } };

 // Source and Destination

 int s = 0, d = 3;

 // Number of edges in path

 int k = 2;

 // Calling the function

 cout << smPath(s, d, ed, n, k);

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

// Java implementation of the above approach

import java.util.ArrayList;

import java.util.Arrays;

class GFG{

static class Pair<K, V>

{

 K first;

 V second;

 public Pair(K first, V second)

 {

 this.first = first;

 this.second = second;

 }

}

static int inf = 100000000;

// Function to find the smallest path

// with exactly K edges

static int smPath(int s, int d,

 ArrayList<Pair<Pair<Integer, Integer>, Integer>> ed,

 int n, int k)

{

 

 // Array to store dp

 int[] dis = new int[n + 1];

 

 // Initialising the array

 Arrays.fill(dis, inf);

 dis[s] = 0;

 // Loop to solve DP

 for(int i = 0; i < k; i++)

 {

 

 // Initialising next state

 int[] dis1 = new int[n + 1];

 Arrays.fill(dis1, inf);

 // Recurrence relation

 for(Pair<Pair<Integer, Integer>, Integer> it : ed)

 dis1[it.first.second] = Math.min(dis1[it.first.second],

 dis[it.first.first] +

 it.second);

 for(int j = 0; j <= n; j++)

 dis[j] = dis1[j];

 }

 // Returning final answer

 if (dis[d] == inf)

 return -1;

 else

 return dis[d];

}

// Driver code

public static void main(String[] args)

{

 int n = 4;

 // Input edges

 ArrayList<Pair<Pair<Integer, Integer>, Integer>> ed = new
ArrayList<>(

 Arrays.asList(

 new Pair<Pair<Integer, Integer>, Integer>(

 new Pair<Integer, Integer>(0, 1), 10),

 new Pair<Pair<Integer, Integer>, Integer>(

 new Pair<Integer, Integer>(0, 2), 3),

 new Pair<Pair<Integer, Integer>, Integer>(

 new Pair<Integer, Integer>(0, 3), 2),

 new Pair<Pair<Integer, Integer>, Integer>(

 new Pair<Integer, Integer>(1, 3), 7),

 new Pair<Pair<Integer, Integer>, Integer>(

 new Pair<Integer, Integer>(2, 3), 7)

 )

 );

 // Source and Destination

 int s = 0, d = 3;

 // Number of edges in path

 int k = 2;

 // Calling the function

 System.out.println(smPath(s, d, ed, n, k));

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

# Python3 implementation of the above approach

inf = 100000000

# Function to find the smallest path

# with exactly K edges

def smPath(s, d, ed, n, k):

 

 # Array to store dp

 dis = [inf] * (n + 1)

 dis[s] = 0

 # Loop to solve DP

 for i in range(k):

 # Initialising next state

 dis1 = [inf] * (n + 1)

 # Recurrence relation

 for it in ed:

 dis1[it[1]] = min(dis1[it[1]],

 dis[it[0]]+ it[2])

 for i in range(n + 1):

 dis[i] = dis1[i]

 # Returning final answer

 if (dis[d] == inf):

 return -1

 else:

 return dis[d]

# Driver code

if __name__ == '__main__':

 n = 4

 # Input edges

 ed = [ [0, 1 ,10],

 [ 0, 2 ,3],

 [ 0, 3 ,2],

 [ 1, 3 ,7],

 [ 2, 3 ,7] ]

 # Source and Destination

 s = 0

 d = 3

 # Number of edges in path

 k = 2

 # Calling the function

 print(smPath(s, d, ed, n, k))

# This code is contributed by mohit kumar 29  
  
---  
  
 __

 __

 **Output:**

    
    
    10

**Time complexity:** O(E*K)  
**Space complexity:** O(N)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

