Find minimum steps required to reach the end of a matrix | Set 2



Given a 2d-matrix consisting of positive integers, the task is to find the
minimum number of steps required to reach the end of the matrix. If we are at
cell **(i, j)** then we can go to all the cells represented by **(i + X, j +
Y)** such that **X ≥ 0** , **Y ≥ 0** and **X + Y = arr[i][j]**. If no path
exists then print **-1**.

 **Examples:**

>  **Input:** arr[][] = {  
> {4, 1, 1},  
> {1, 1, 1},  
> {1, 1, 1}}  
>  **Output:** 1  
> The path will be from {0, 0} -> {2, 2} as manhattan distance  
> between two is 4.  
> Thus, we are reaching there in 1 step.
>
>  **Input:** arr[][] = {  
> {1, 1, 2},  
> {1, 1, 1},  
> {2, 1, 1}}  
>  **Output:** 3

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **simple solution** will be to explore all possible solutions which will
take exponential time.

  

  

An **efficient solution** is to use dynamic programming to solve this problem
in polynomial time. Lets decide the states of dp.  
Let’s say we are at cell **(i, j)**. We will try to find the minimum number of
steps required to reach the cell **(n – 1, n – 1)** from this cell.  
We have **arr[i][j] + 1** possible paths.

The recurrence relation will be

> dp[i][j] = 1 + min(dp[i][j + arr[i][j]], dp[i + 1][j + arr[i][j] – 1], ….,
> dp[i + arr[i][j]][j])

To reduce the number of terms in recurrence relation, we can put an upper
bound on the values of **X** and **Y**. How?  
We know that **i + X < N**. Thus, **X < N – i** otherwise they would go out of
bounds.  
Similarly, **Y < N – j**

>  **0 ≤ Y < N – j** …(1)  
>  **X + Y = arr[i][j]** …(2)  
> Substituting value of **Y** from second into first, we get  
>  **X ≥ arr[i][j] + j – N + 1**

From above we get another lower bound on constraint of **X** i.e. **X ≥
arr[i][j] + j – N + 1**.  
So, new lower bound on **X** becomes **X ≥ max(0, arr[i][j] + j – N + 1)**.  
Also **X ≤ min(arr[i][j], N – i – 1)**.

Our recurrence relation optimises to

> dp[i][j] = 1 + min(dp[i + max(0, arr[i][j] + j – N + 1)][j + arr[i][j] –
> max(0, arr[i][j] + j – N + 1)], …., dp[i + min(arr[i][j], N – i – 1)][j +
> arr[i][j] – min(arr[i][j], N – i – 1)])

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

#define n 3

using namespace std;

 

// 2d array to store

// states of dp

int dp[n][n];

 

// Array to determine whether

// a state has been solved before

int v[n][n];

 

// Function to return the minimum steps required

int minSteps(int i, int j, int arr[][n])

{

 

 // Base cases

 if (i == n - 1 and j == n - 1)

 return 0;

 

 if (i > n - 1 || j > n - 1)

 return 9999999;

 

 // If a state has been solved before

 // it won't be evaluated again

 if (v[i][j])

 return dp[i][j];

 

 v[i][j] = 1;

 dp[i][j] = 9999999;

 

 // Recurrence relation

 for (int k = max(0, arr[i][j] + j - n + 1);

 k <= min(n - i - 1, arr[i][j]); k++) {

 dp[i][j] = min(dp[i][j], minSteps(i + k, j + arr[i][j] - k, arr));

 }

 

 dp[i][j]++;

 

 return dp[i][j];

}

 

// Driver code

int main()

{

 int arr[n][n] = { { 4, 1, 2 },

 { 1, 1, 1 },

 { 2, 1, 1 } };

 

 int ans = minSteps(0, 0, arr);

 if (ans >= 9999999)

 cout << -1;

 else

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

class GFG {

 

 static int n = 3;

 

 // 2d array to store

 // states of dp

 static int[][] dp = new int[n][n];

 

 // Array to determine whether

 // a state has been solved before

 static int[][] v = new int[n][n];

 

 // Function to return the minimum steps required

 static int minSteps(int i, int j, int arr[][])

 {

 

 // Base cases

 if (i == n - 1 && j == n - 1) {

 return 0;

 }

 

 if (i > n - 1 || j > n - 1) {

 return 9999999;

 }

 

 // If a state has been solved before

 // it won't be evaluated again

 if (v[i][j] == 1) {

 return dp[i][j];

 }

 

 v[i][j] = 1;

 dp[i][j] = 9999999;

 

 // Recurrence relation

 for (int k = Math.max(0, arr[i][j] + j - n + 1);

 k <= Math.min(n - i - 1, arr[i][j]); k++) {

 dp[i][j] = Math.min(dp[i][j],

 minSteps(i + k, j + arr[i][j] - k, arr));

 }

 

 dp[i][j]++;

 

 return dp[i][j];

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int arr[][] = { { 4, 1, 2 },

 { 1, 1, 1 },

 { 2, 1, 1 } };

 

 int ans = minSteps(0, 0, arr);

 if (ans >= 9999999) {

 System.out.println(-1);

 }

 else {

 System.out.println(ans);

 }

 }

}

 

// This code contributed by Rajput-Ji  
  
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

 

import numpy as np 

n = 3

 

# 2d array to store 

# states of dp 

dp = np.zeros((n,n))

 

# Array to determine whether 

# a state has been solved before 

v = np.zeros((n,n)); 

 

# Function to return the minimum steps required 

def minSteps(i, j, arr) : 

 

 # Base cases 

 if (i == n - 1 and j == n - 1) :

 return 0; 

 

 if (i > n - 1 or j > n - 1) :

 return 9999999; 

 

 # If a state has been solved before 

 # it won't be evaluated again 

 if (v[i][j]) :

 return dp[i][j]; 

 

 v[i][j] = 1; 

 dp[i][j] = 9999999; 

 

 # Recurrence relation 

 for k in range(max(0, arr[i][j] + j - n +
1),min(n - i - 1, arr[i][j]) + 1) :

 dp[i][j] = min(dp[i][j], minSteps(i + k, j + arr[i][j] -
k, arr)); 

 

 

 dp[i][j] += 1; 

 

 return dp[i][j]; 

 

 

# Driver code 

if __name__ == "__main__" : 

 

 arr = [ 

 [ 4, 1, 2 ], 

 [ 1, 1, 1 ], 

 [ 2, 1, 1 ] 

 ]; 

 

 ans = minSteps(0, 0, arr); 

 if (ans >= 9999999) :

 print(-1); 

 else :

 print(ans); 

 

# This code is contributed by AnkitRai01  
  
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

 static int n = 3;

 

 // 2d array to store

 // states of dp

 static int[,] dp = new int[n, n];

 

 // Array to determine whether

 // a state has been solved before

 static int[,] v = new int[n, n];

 

 // Function to return the minimum steps required

 static int minSteps(int i, int j, int [,]arr)

 {

 

 // Base cases

 if (i == n - 1 && j == n - 1)

 {

 return 0;

 }

 

 if (i > n - 1 || j > n - 1) 

 {

 return 9999999;

 }

 

 // If a state has been solved before

 // it won't be evaluated again

 if (v[i, j] == 1) 

 {

 return dp[i, j];

 }

 

 v[i, j] = 1;

 dp[i, j] = 9999999;

 

 // Recurrence relation

 for (int k = Math.Max(0, arr[i,j] + j - n + 1);

 k <= Math.Min(n - i - 1, arr[i,j]); k++)

 {

 dp[i,j] = Math.Min(dp[i,j],

 minSteps(i + k, j + arr[i,j] - k, arr));

 }

 

 dp[i,j]++;

 

 return dp[i,j];

 }

 

 // Driver code

 static public void Main ()

 {

 int [,]arr = { { 4, 1, 2 },

 { 1, 1, 1 },

 { 2, 1, 1 } };

 

 int ans = minSteps(0, 0, arr);

 if (ans >= 9999999) 

 {

 Console.WriteLine(-1);

 }

 else

 {

 Console.WriteLine(ans);

 }

 }

}

 

// This code contributed by ajit.  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    

The time complexity of the above approach will be O(n3). Each state takes O(n)
time in worst case to solve.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

