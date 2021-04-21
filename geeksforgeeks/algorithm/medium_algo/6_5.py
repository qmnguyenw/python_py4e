Minimum cost to reverse edges such that there is path between every pair of
nodes



Given a connected, directional graph. Each node is connected to exactly two
other nodes. There is weight associated with each edge denoting the cost to
reverse its direction. The task is to find the minimum cost to reverse some
edges of the graph such that it is possible to go from each node to every
other node.

 **Examples:**

    
    
    **Input:** 
    5
    1 2 7
    5 1 8
    5 4 5
    3 4 1
    3 2 10
    **Output:** 15
    
    ![](https://media.geeksforgeeks.org/wp-content/uploads/20191114133502/Minimum-cost-to-reverse-the-edges-such-that-its-possible-to-go-from-each-node-to-every-other-node..jpg)
    
    **Input:**
    6
    1 5 4
    5 3 8
    2 4 15
    1 6 16
    2 3 23
    4 6 42
    **Output:** 39
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  * In order to reach from each node to every other node, the graph must form a ring i.e Direct all edges on it in one of 2 directions either clockwise or anti-clockwise. Let us denote the cost of redirecting all the clockwise edges to anticlockwise direction as cost1 and vice versa as cost2. The answer is clearly the minimum of these two costs.
  * Maintain two boolean arrays start and end. The start and end arrays denote whether there is an edge starting from or ending at a given node. Whenever we encounter an edge going from node a to node b, we first check the condition if there is an edge already starting from node a or ending at node b. If there is an edge that satisfying the condition, the edge is in the opposite direction to the edge already present. In this case, we update cost2 and store the edge is the opposite direction. Otherwise, we update the cost1. This way we are able to maintain the costs of both orientations. Finally, print the minimum cost.

Below is the implementation of above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code to find

// the minimum cost to

// reverse the edges

#include <bits/stdc++.h>

using namespace std;

 

// Function to calculate

// min cost for reversing

// the edges

int minCost(vector<vector<int> >& graph, int n)

{

 

 int cost1 = 0, cost2 = 0;

 // bool array to mark

 // start and end node

 // of a graph

 bool start[n + 1] = { false };

 bool end[n + 1] = { false };

 

 for (int i = 0; i < n; i++) {

 

 int a = graph[i][0];

 int b = graph[i][1];

 int c = graph[i][2];

 

 // This edge must

 // start from b and end at a

 if (start[a] || end[b]) {

 cost2 += c;

 start[b] = true;

 end[a] = true;

 }

 

 // This edge must

 // start from a and end at b

 else {

 cost1 += c;

 start[a] = true;

 end[b] = true;

 }

 }

 

 // Return minimum of

 // both posibilities

 return min(cost1, cost2);

}

 

// Driver code

int main()

{

 int n = 5;

 // Adjacency list representation

 // of a graph

 vector<vector<int> > graph = {

 { 1, 2, 7 },

 { 5, 1, 8 },

 { 5, 4, 5 },

 { 3, 4, 1 },

 { 3, 2, 10 }

 };

 

 int ans = minCost(graph, n);

 cout << ans << '\n';

 

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

// Java code to find the minimum cost to

// reverse the edges

class GFG 

{

 

// Function to calculate min cost for 

// reversing the edges

static int minCost(int[][] graph, int n)

{

 

 int cost1 = 0, cost2 = 0;

 

 // bool array to mark start and 

 // end node of a graph

 boolean []start = new boolean[n + 1];

 boolean []end = new boolean[n + 1];

 

 for (int i = 0; i < n; i++) 

 {

 int a = graph[i][0];

 int b = graph[i][1];

 int c = graph[i][2];

 

 // This edge must start from b

 // and end at a

 if (start[a] || end[b]) 

 {

 cost2 += c;

 start[b] = true;

 end[a] = true;

 }

 

 // This edge must start from a

 // and end at b

 else

 {

 cost1 += c;

 start[a] = true;

 end[b] = true;

 }

 }

 

 // Return minimum of both posibilities

 return Math.min(cost1, cost2);

}

 

// Driver code

public static void main(String[] args) 

{

 int n = 5;

 

 // Adjacency list representation

 // of a graph

 int [][]graph = {{ 1, 2, 7 },

 { 5, 1, 8 },

 { 5, 4, 5 },

 { 3, 4, 1 },

 { 3, 2, 10 }};

 

 int ans = minCost(graph, n);

 System.out.println(ans);

}

}

 

// This code is contributed by Rajput-Ji  
  
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

# Python code to find the minimum cost to

# reverse the edges

 

# Function to calculate min cost for 

# reversing the edges

def minCost(graph, n):

 

 cost1, cost2 = 0, 0;

 

 # bool array to mark start and 

 # end node of a graph

 start = [False]*(n + 1);

 end = [False]*(n + 1);

 

 for i in range(n): 

 a = graph[i][0];

 b = graph[i][1];

 c = graph[i][2];

 

 # This edge must start from b

 # and end at a

 if (start[a] or end[b]):

 cost2 += c;

 start[b] = True;

 end[a] = True;

 

 # This edge must start from a

 # and end at b

 else:

 cost1 += c;

 start[a] = True;

 end[b] = True;

 

 # Return minimum of both posibilities

 return min(cost1, cost2);

 

# Driver code

if __name__ == '__main__':

 n = 5;

 

 # Adjacency list representation

 # of a graph

 graph = [[ 1, 2, 7 ],

 [ 5, 1, 8 ],

 [ 5, 4, 5 ],

 [ 3, 4, 1 ],

 [ 3, 2, 10 ]];

 

 ans = minCost(graph, n);

 print(ans);

 

# This code is contributed by 29AjayKumar  
  
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

// C# code to find the minimum cost to

// reverse the edges

using System;

 

class GFG 

{

 

// Function to calculate min cost for 

// reversing the edges

static int minCost(int[,] graph, int n)

{

 int cost1 = 0, cost2 = 0;

 

 // bool array to mark start and 

 // end node of a graph

 Boolean []start = new Boolean[n + 1];

 Boolean []end = new Boolean[n + 1];

 

 for (int i = 0; i < n; i++) 

 {

 int a = graph[i, 0];

 int b = graph[i, 1];

 int c = graph[i, 2];

 

 // This edge must start from b

 // and end at a

 if (start[a] || end[b]) 

 {

 cost2 += c;

 start[b] = true;

 end[a] = true;

 }

 

 // This edge must start from a

 // and end at b

 else

 {

 cost1 += c;

 start[a] = true;

 end[b] = true;

 }

 }

 

 // Return minimum of both posibilities

 return Math.Min(cost1, cost2);

}

 

// Driver code

public static void Main(String[] args) 

{

 int n = 5;

 

 // Adjacency list representation

 // of a graph

 int [,]graph = {{ 1, 2, 7 },

 { 5, 1, 8 },

 { 5, 4, 5 },

 { 3, 4, 1 },

 { 3, 2, 10 }};

 

 int ans = minCost(graph, n);

 Console.WriteLine(ans);

}

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    15
    

**Time Complexity:** O(N) where N is number of edges

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

