Travelling Salesman Problem implementation using BackTracking



 **Travelling Salesman Problem (TSP):** Given a set of cities and distance
between every pair of cities, the problem is to find the shortest possible
route that visits every city exactly once and returns back to the starting
point.

Note the difference between **Hamiltonian Cycle** and TSP. The Hamiltoninan
cycle problem is to find if there exist a tour that visits every city exactly
once. Here we know that Hamiltonian Tour exists (because the graph is
complete) and in fact many such tours exist, the problem is to find a minimum
weight Hamiltonian Cycle.  
For example, consider the graph shown in the figure. A TSP tour in the graph
is 1 -> 2 -> 4 -> 3 -> 1\. The cost of the tour is 10 + 25 + 30 + 15 which is
80.

The problem is a famous NP hard problem. There is no polynomial time know
solution for this problem.

![TSP](https://i.ibb.co/tDzdWnj/TSP.png)

>  **Output of Given Graph:**  
>  Minimum weight Hamiltonian Cycle : 10 + 25 + 30 + 15 = 80
>
>  
>
>
>  
>

 **Approach:** In this post, implementation of simple solution is discussed.

  * Consider city 1 (let say 0th node) as the starting and ending point. Since route is cyclic, we can consider any point as starting point.
  * Start traversing from the source to its adjacent nodes in dfs manner.
  * Calculate cost of every traversal and keep track of minimum cost and keep on updating the value of minimum cost stored value.
  * Return the permutation with minimum cost.

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

#include <bits/stdc++.h>

using namespace std;

#define V 4

 

// Function to find the minimum weight Hamiltonian Cycle

void tsp(int graph[][V], vector<bool>& v, int currPos,

 int n, int count, int cost, int& ans)

{

 

 // If last node is reached and it has a link

 // to the starting node i.e the source then

 // keep the minimum value out of the total cost

 // of traversal and "ans"

 // Finally return to check for more possible values

 if (count == n && graph[currPos][0]) {

 ans = min(ans, cost + graph[currPos][0]);

 return;

 }

 

 // BACKTRACKING STEP

 // Loop to traverse the adjacency list

 // of currPos node and increasing the count

 // by 1 and cost by graph[currPos][i] value

 for (int i = 0; i < n; i++) {

 if (!v[i] && graph[currPos][i]) {

 

 // Mark as visited

 v[i] = true;

 tsp(graph, v, i, n, count + 1,

 cost + graph[currPos][i], ans);

 

 // Mark ith node as unvisited

 v[i] = false;

 }

 }

};

 

// Driver code

int main()

{

 // n is the number of nodes i.e. V

 int n = 4;

 

 int graph[][V] = {

 { 0, 10, 15, 20 },

 { 10, 0, 35, 25 },

 { 15, 35, 0, 30 },

 { 20, 25, 30, 0 }

 };

 

 // Boolean array to check if a node

 // has been visited or not

 vector<bool> v(n);

 for (int i = 0; i < n; i++)

 v[i] = false;

 

 // Mark 0th node as visited

 v[0] = true;

 int ans = INT_MAX;

 

 // Find the minimum weight Hamiltonian Cycle

 tsp(graph, v, 0, n, 1, 0, ans);

 

 // ans is the minimum weight Hamiltonian Cycle

 cout << ans;

 

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

class GFG 

{

 

 // Function to find the minimum weight 

 // Hamiltonian Cycle

 static int tsp(int[][] graph, boolean[] v, 

 int currPos, int n, 

 int count, int cost, int ans) 

 {

 

 // If last node is reached and it has a link

 // to the starting node i.e the source then

 // keep the minimum value out of the total cost

 // of traversal and "ans"

 // Finally return to check for more possible values

 if (count == n && graph[currPos][0] > 0) 

 {

 ans = Math.min(ans, cost + graph[currPos][0]);

 return ans;

 }

 

 // BACKTRACKING STEP

 // Loop to traverse the adjacency list

 // of currPos node and increasing the count

 // by 1 and cost by graph[currPos,i] value

 for (int i = 0; i < n; i++) 

 {

 if (v[i] == false && graph[currPos][i] > 0) 

 {

 

 // Mark as visited

 v[i] = true;

 ans = tsp(graph, v, i, n, count + 1,

 cost + graph[currPos][i], ans);

 

 // Mark ith node as unvisited

 v[i] = false;

 }

 }

 return ans;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 

 // n is the number of nodes i.e. V

 int n = 4;

 

 int[][] graph = {{0, 10, 15, 20},

 {10, 0, 35, 25},

 {15, 35, 0, 30},

 {20, 25, 30, 0}};

 

 // Boolean array to check if a node

 // has been visited or not

 boolean[] v = new boolean[n];

 

 // Mark 0th node as visited

 v[0] = true;

 int ans = Integer.MAX_VALUE;

 

 // Find the minimum weight Hamiltonian Cycle

 ans = tsp(graph, v, 0, n, 1, 0, ans);

 

 // ans is the minimum weight Hamiltonian Cycle

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

# Python3 implementation of the approach

V = 4

answer = []

 

# Function to find the minimum weight 

# Hamiltonian Cycle

def tsp(graph, v, currPos, n, count, cost):

 

 # If last node is reached and it has 

 # a link to the starting node i.e 

 # the source then keep the minimum 

 # value out of the total cost of 

 # traversal and "ans"

 # Finally return to check for 

 # more possible values

 if (count == n and graph[currPos][0]):

 answer.append(cost + graph[currPos][0])

 return

 

 # BACKTRACKING STEP

 # Loop to traverse the adjacency list

 # of currPos node and increasing the count

 # by 1 and cost by graph[currPos][i] value

 for i in range(n):

 if (v[i] == False and graph[currPos][i]):

 

 # Mark as visited

 v[i] = True

 tsp(graph, v, i, n, count + 1, 

 cost + graph[currPos][i])

 

 # Mark ith node as unvisited

 v[i] = False

 

# Driver code

 

# n is the number of nodes i.e. V

if __name__ == '__main__':

 n = 4

 graph= [[ 0, 10, 15, 20 ],

 [ 10, 0, 35, 25 ],

 [ 15, 35, 0, 30 ],

 [ 20, 25, 30, 0 ]]

 

 # Boolean array to check if a node

 # has been visited or not

 v = [False for i in range(n)]

 

 # Mark 0th node as visited

 v[0] = True

 

 # Find the minimum weight Hamiltonian Cycle

 tsp(graph, v, 0, n, 1, 0)

 

 # ans is the minimum weight Hamiltonian Cycle

 print(min(answer))

 

# This code is contributed by mohit kumar  
  
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

 

class GFG

{

 

// Function to find the minimum weight Hamiltonian Cycle

static int tsp(int [,]graph, bool []v, int currPos,

 int n, int count, int cost, int ans)

{

 

 // If last node is reached and it has a link

 // to the starting node i.e the source then

 // keep the minimum value out of the total cost

 // of traversal and "ans"

 // Finally return to check for more possible values

 if (count == n && graph[currPos,0] > 0) 

 {

 ans = Math.Min(ans, cost + graph[currPos,0]);

 return ans;

 }

 

 // BACKTRACKING STEP

 // Loop to traverse the adjacency list

 // of currPos node and increasing the count

 // by 1 and cost by graph[currPos,i] value

 for (int i = 0; i < n; i++) {

 if (v[i] == false && graph[currPos,i] > 0)

 {

 

 // Mark as visited

 v[i] = true;

 ans = tsp(graph, v, i, n, count + 1,

 cost + graph[currPos,i], ans);

 

 // Mark ith node as unvisited

 v[i] = false;

 }

 }

 return ans;

}

 

// Driver code

static void Main()

{

 // n is the number of nodes i.e. V

 int n = 4;

 

 int [,]graph = {

 { 0, 10, 15, 20 },

 { 10, 0, 35, 25 },

 { 15, 35, 0, 30 },

 { 20, 25, 30, 0 }

 };

 

 // Boolean array to check if a node

 // has been visited or not

 bool[] v = new bool[n];

 

 // Mark 0th node as visited

 v[0] = true;

 int ans = int.MaxValue;

 

 // Find the minimum weight Hamiltonian Cycle

 ans = tsp(graph, v, 0, n, 1, 0, ans);

 

 // ans is the minimum weight Hamiltonian Cycle

 Console.Write(ans);

 

}

}

 

// This code is contributed by mits  
  
---  
  
 __

 __

 **Output:**

    
    
    80
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

