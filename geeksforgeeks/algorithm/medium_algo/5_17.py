Knapsack with large Weights



Given a knapsack with capacity **C** and two arrays **w[]** and **val[]**
representing the weights and values of **N** distinct items, the task is to
find the maximum value you can put into the knapsack. Items cannot be broken
and an item with weight **X** takes **X** capacity of the knapsack.

 **Examples:**

>  **Input:** w[] = {3, 4, 5}, val[] = {30, 50, 60}, C = 8  
>  **Output:** 90  
> We take objects ‘1’ and ‘3’.  
> The total value we get is (30 + 60) = 90.  
> Total weight is 8, thus it fits in the given capacity
>
>  **Input:** w[] = {10000}, val[] = {10}, C = 100000  
>  **Output:** 10

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The traditional famous 0-1 knapsack problem can be solved in
O(N*C) time but if the capacity of the knapsack is huge then a 2D N*C array
can’t make be made. Luckily, it can be solved by redefining the states of the
dp.  
Let’s have a look at the states of the DP first.

  

  

 **dp[V][i]** represents the minimum weight subset of the subarray
**arr[i…N-1]** required to get a value of at least **V**. The recurrence
relation will be:

> dp[V][i] = min(dp[V][i+1], w[i] + dp[V – val[i]][i + 1])

So, for each **V** from **0** to the maximum value of **V** possible, try to
find if the given **V** can be represented with the given array. The largest
such **V** that can be represented becomes the required answer.

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

 

#define V_SUM_MAX 1000

#define N_MAX 100

#define W_MAX 10000000

 

// To store the states of DP

int dp[V_SUM_MAX + 1][N_MAX];

bool v[V_SUM_MAX + 1][N_MAX];

 

// Function to solve the recurrence relation

int solveDp(int r, int i, int* w, int* val, int n)

{

 // Base cases

 if (r <= 0)

 return 0;

 if (i == n)

 return W_MAX;

 if (v[r][i])

 return dp[r][i];

 

 // Marking state as solved

 v[r][i] = 1;

 

 // Recurrence relation

 dp[r][i]

 = min(solveDp(r, i + 1, w, val, n),

 w[i] + solveDp(r - val[i],

 i + 1, w, val, n));

 return dp[r][i];

}

 

// Function to return the maximum weight

int maxWeight(int* w, int* val, int n, int c)

{

 

 // Iterating through all possible values

 // to find the the largest value that can

 // be represented by the given weights

 for (int i = V_SUM_MAX; i >= 0; i--) {

 if (solveDp(i, 0, w, val, n) <= c) {

 return i;

 }

 }

 return 0;

}

 

// Driver code

int main()

{

 int w[] = { 3, 4, 5 };

 int val[] = { 30, 50, 60 };

 int n = sizeof(w) / sizeof(int);

 int C = 8;

 

 cout << maxWeight(w, val, n, C);

 

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

 static final int V_SUM_MAX = 1000;

 static final int N_MAX = 100;

 static final int W_MAX = 10000000;

 

 // To store the states of DP 

 static int dp[][] = new int[V_SUM_MAX + 1][N_MAX]; 

 static boolean v[][] = new boolean [V_SUM_MAX + 1][N_MAX]; 

 

 // Function to solve the recurrence relation 

 static int solveDp(int r, int i, int w[], 

 int val[], int n) 

 { 

 // Base cases 

 if (r <= 0) 

 return 0; 

 

 if (i == n) 

 return W_MAX; 

 

 if (v[r][i]) 

 return dp[r][i]; 

 

 // Marking state as solved 

 v[r][i] = true; 

 

 // Recurrence relation 

 dp[r][i] = Math.min(solveDp(r, i + 1, w, val, n), 

 w[i] + solveDp(r - val[i], 

 i + 1, w, val, n)); 

 

 return dp[r][i]; 

 } 

 

 // Function to return the maximum weight 

 static int maxWeight(int w[], int val[], 

 int n, int c) 

 { 

 

 // Iterating through all possible values 

 // to find the the largest value that can 

 // be represented by the given weights 

 for (int i = V_SUM_MAX; i >= 0; i--)

 { 

 if (solveDp(i, 0, w, val, n) <= c) 

 { 

 return i; 

 } 

 } 

 return 0; 

 } 

 

 // Driver code 

 public static void main (String[] args)

 { 

 int w[] = { 3, 4, 5 }; 

 int val[] = { 30, 50, 60 }; 

 int n = w.length; 

 int C = 8; 

 

 System.out.println(maxWeight(w, val, n, C)); 

 } 

}

 

// This code is contributed by AnkitRai01  
  
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

V_SUM_MAX = 1000

N_MAX = 100

W_MAX = 10000000

 

# To store the states of DP

dp = [[ 0 for i in range(N_MAX)]

 for i in range(V_SUM_MAX + 1)]

v = [[ 0 for i in range(N_MAX)]

 for i in range(V_SUM_MAX + 1)]

 

# Function to solve the recurrence relation

def solveDp(r, i, w, val, n):

 

 # Base cases

 if (r <= 0):

 return 0

 if (i == n):

 return W_MAX

 if (v[r][i]):

 return dp[r][i]

 

 # Marking state as solved

 v[r][i] = 1

 

 # Recurrence relation

 dp[r][i] = min(solveDp(r, i + 1, w, val, n), 

 w[i] + solveDp(r - val[i], i + 1,

 w, val, n))

 return dp[r][i]

 

# Function to return the maximum weight

def maxWeight( w, val, n, c):

 

 # Iterating through all possible values

 # to find the the largest value that can

 # be represented by the given weights

 for i in range(V_SUM_MAX, -1, -1):

 if (solveDp(i, 0, w, val, n) <= c):

 return i

 

 return 0

 

# Driver code

if __name__ == '__main__':

 w = [3, 4, 5]

 val = [30, 50, 60]

 n = len(w)

 C = 8

 

 print(maxWeight(w, val, n, C))

 

# This code is contributed by Mohit Kumar  
  
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

 static readonly int V_SUM_MAX = 1000;

 static readonly int N_MAX = 100;

 static readonly int W_MAX = 10000000;

 

 // To store the states of DP 

 static int [,]dp = new int[V_SUM_MAX + 1, N_MAX]; 

 static bool [,]v = new bool [V_SUM_MAX + 1, N_MAX]; 

 

 // Function to solve the recurrence relation 

 static int solveDp(int r, int i, int []w, 

 int []val, int n) 

 { 

 // Base cases 

 if (r <= 0) 

 return 0; 

 

 if (i == n) 

 return W_MAX; 

 

 if (v[r, i]) 

 return dp[r, i]; 

 

 // Marking state as solved 

 v[r, i] = true; 

 

 // Recurrence relation 

 dp[r, i] = Math.Min(solveDp(r, i + 1, w, val, n), 

 w[i] + solveDp(r - val[i], 

 i + 1, w, val, n)); 

 

 return dp[r, i]; 

 } 

 

 // Function to return the maximum weight 

 static int maxWeight(int []w, int []val, 

 int n, int c) 

 { 

 

 // Iterating through all possible values 

 // to find the the largest value that can 

 // be represented by the given weights 

 for (int i = V_SUM_MAX; i >= 0; i--)

 { 

 if (solveDp(i, 0, w, val, n) <= c) 

 { 

 return i; 

 } 

 } 

 return 0; 

 } 

 

 // Driver code 

 public static void Main(String[] args)

 { 

 int []w = { 3, 4, 5 }; 

 int []val = { 30, 50, 60 }; 

 int n = w.Length; 

 int C = 8; 

 

 Console.WriteLine(maxWeight(w, val, n, C)); 

 } 

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    90
    

**Time Complexity:** O(V_sum * N) where V_sum is the sum of all the values in
the array val[].

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

