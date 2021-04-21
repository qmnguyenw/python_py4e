Travelling Salesman Problem | Greedy Approach



Given a 2D matrix **tsp[][]** , where each row has the array of distances from
that indexed city to all the other cities and **-1** denotes that there
doesn’t exist a path between those two indexed cities. The task is to print
minimum cost in TSP cycle.  
 **Examples:**

> **Input:**  
> tsp[][] = {{-1, 10, 15, 20},  
> {10, -1, 35, 25},  
> {15, 35, -1, 30},  
> {20, 25, 30, -1}};  
> Below is the given graph:  
>
>
> ![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Euler12.png)
>
> **Output:** 80  
> **Explanation:**  
> We are trying to find out the path/route with the minimum cost such that our
> aim of visiting all cities once and return back to the source city is
> achieved. The path through which we can achieve that, can be represented as
> 1 -> 2 -> 4 -> 3 -> 1\. Here, we started from city 1 and ended on the same
> visiting all other cities once on our way. The cost of our path/route is
> calculated as follows:  
> 1 -> 2 = 10  
> 2 -> 4 = 25  
> 4 -> 3 = 30  
> 3 -> 1 = 15  
> (All the costs are taken from the given 2D Array)  
> Hence, total cost = 10 + 25 + 30 + 15 = 80  
>  **Input:**  
> tsp[][] = {{-1, 30, 25, 10},  
> {15, -1, 20, 40},  
> {10, 20, -1, 25},  
> {30, 10, 20, -1}};  
> **Output:** 50

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

We introduced Travelling Salesman Problem and discussed Naive and Dynamic
Programming Solutions for the problem in the previous post. Both of the
solutions are infeasible. In fact, there is no polynomial-time solution
available for this problem as the problem is a known NP-Hard problem. There
are approximate algorithms to solve the problem though.  
This problem can be related to the Hamiltonian Cycle problem, in a way that
here we know a Hamiltonian cycle exists in the graph, but our job is to find
the cycle with minimum cost. Also, in a particular TSP graph, there can be
many hamiltonian cycles but we need to output only one that satisfies our
required aim of the problem.  
 **Approach:** This problem can be solved using Greedy Technique. Below are
the steps:

  

  

  1. Create two primary data holders: 
    * A list that holds the indices of the cities in terms of the input matrix of distances between cities.
    * Result array which will have all cities that can be displayed out to the console in any manner.
  2. Perform traversal on the given adjacency matrix **tsp[][]** for all the city and if the cost of the reaching any city from current city is less than current cost the update the cost.
  3. Generate the minimum path cycle using the above step and return there minimum cost.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <bits/stdc++.h>

using namespace std;

// Function to find the minimum

// cost path for all the paths

void findMinRoute(vector<vector<int> > tsp)

{

 int sum = 0;

 int counter = 0;

 int j = 0, i = 0;

 int min = INT_MAX;

 map<int, int> visitedRouteList;

 // Starting from the 0th indexed

 // city i.e., the first city

 visitedRouteList[0] = 1;

 int route[tsp.size()];

 // Traverse the adjacency

 // matrix tsp[][]

 while (i < tsp.size() && j < tsp[i].size())

 {

 // Corner of the Matrix

 if (counter >= tsp[i].size() - 1)

 {

 break;

 }

 // If this path is unvisited then

 // and if the cost is less then

 // update the cost

 if (j != i && (visitedRouteList[j] == 0))

 {

 if (tsp[i][j] < min)

 {

 min = tsp[i][j];

 route[counter] = j + 1;

 }

 }

 j++;

 // Check all paths from the

 // ith indexed city

 if (j == tsp[i].size())

 {

 sum += min;

 min = INT_MAX;

 visitedRouteList[route[counter] - 1] = 1;

 j = 0;

 i = route[counter] - 1;

 counter++;

 }

 }

 // Update the ending city in array

 // from city which was last visited

 i = route[counter - 1] - 1;

 for (j = 0; j < tsp.size(); j++)

 {

 if ((i != j) && tsp[i][j] < min)

 {

 min = tsp[i][j];

 route[counter] = j + 1;

 }

 }

 sum += min;

 // Started from the node where

 // we finished as well.

 cout << ("Minimum Cost is : ");

 cout << (sum);

}

// Driver Code

int main()

{

 

 // Input Matrix

 vector<vector<int> > tsp = { { -1, 10, 15, 20 },

 { 10, -1, 35, 25 },

 { 15, 35, -1, 30 },

 { 20, 25, 30, -1 } };

 // Function Call

 findMinRoute(tsp);

}

// This code is contributed by grand_master.  
  
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

// Java program for the above approach

import java.util.*;

public class TSPGreedy {

 // Function to find the minimum

 // cost path for all the paths

 static void findMinRoute(int[][] tsp)

 {

 int sum = 0;

 int counter = 0;

 int j = 0, i = 0;

 int min = Integer.MAX_VALUE;

 List<Integer> visitedRouteList

 = new ArrayList<>();

 // Starting from the 0th indexed

 // city i.e., the first city

 visitedRouteList.add(0);

 int[] route = new int[tsp.length];

 // Traverse the adjacency

 // matrix tsp[][]

 while (i < tsp.length

 && j < tsp[i].length) {

 // Corner of the Matrix

 if (counter >= tsp[i].length - 1) {

 break;

 }

 // If this path is unvisited then

 // and if the cost is less then

 // update the cost

 if (j != i

 && !(visitedRouteList.contains(j))) {

 if (tsp[i][j] < min) {

 min = tsp[i][j];

 route[counter] = j + 1;

 }

 }

 j++;

 // Check all paths from the

 // ith indexed city

 if (j == tsp[i].length) {

 sum += min;

 min = Integer.MAX_VALUE;

 visitedRouteList.add(route[counter] - 1);

 j = 0;

 i = route[counter] - 1;

 counter++;

 }

 }

 // Update the ending city in array

 // from city which was last visited

 i = route[counter - 1] - 1;

 for (j = 0; j < tsp.length; j++) {

 if ((i != j) && tsp[i][j] < min) {

 min = tsp[i][j];

 route[counter] = j + 1;

 }

 }

 sum += min;

 // Started from the node where

 // we finished as well.

 System.out.print("Minimum Cost is : ");

 System.out.println(sum);

 }

 // Driver Code

 public static void

 main(String[] args)

 {

 // Input Matrix

 int[][] tsp = {

 { -1, 10, 15, 20 },

 { 10, -1, 35, 25 },

 { 15, 35, -1, 30 },

 { 20, 25, 30, -1 }

 };

 // Function Call

 findMinRoute(tsp);

 }

}  
  
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

// C# program for the above approach

using System;

using System.Collections.Generic;

class TSPGreedy{

// Function to find the minimum

// cost path for all the paths

static void findMinRoute(int[,] tsp)

{

 int sum = 0;

 int counter = 0;

 int j = 0, i = 0;

 int min = int.MaxValue;

 

 List<int> visitedRouteList = new List<int>();

 // Starting from the 0th indexed

 // city i.e., the first city

 visitedRouteList.Add(0);

 int[] route = new int[tsp.Length];

 // Traverse the adjacency

 // matrix tsp[,]

 while (i < tsp.GetLength(0) &&

 j < tsp.GetLength(1))

 {

 // Corner of the Matrix

 if (counter >= tsp.GetLength(0) - 1)

 {

 break;

 }

 // If this path is unvisited then

 // and if the cost is less then

 // update the cost

 if (j != i &&

 !(visitedRouteList.Contains(j)))

 {

 if (tsp[i, j] < min)

 {

 min = tsp[i, j];

 route[counter] = j + 1;

 }

 }

 j++;

 // Check all paths from the

 // ith indexed city

 if (j == tsp.GetLength(0))

 {

 sum += min;

 min = int.MaxValue;

 visitedRouteList.Add(route[counter] - 1);

 

 j = 0;

 i = route[counter] - 1;

 counter++;

 }

 }

 // Update the ending city in array

 // from city which was last visited

 i = route[counter - 1] - 1;

 for(j = 0; j < tsp.GetLength(0); j++)

 {

 if ((i != j) && tsp[i, j] < min)

 {

 min = tsp[i, j];

 route[counter] = j + 1;

 }

 }

 sum += min;

 // Started from the node where

 // we finished as well.

 Console.Write("Minimum Cost is : ");

 Console.WriteLine(sum);

}

// Driver Code

public static void Main(String[] args)

{

 

 // Input Matrix

 int[,] tsp = { { -1, 10, 15, 20 },

 { 10, -1, 35, 25 },

 { 15, 35, -1, 30 },

 { 20, 25, 30, -1 } };

 // Function call

 findMinRoute(tsp);

}

}

// This code is contributed by Amit Katiyar  
  
---  
  
 __

 __

 **Output**

    
    
    Minimum Cost is : 80

 _ **Time Complexity:** O(N2*log2N) _  
_**Auxiliary Space:** O(N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

