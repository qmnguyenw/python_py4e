Double Knapsack | Dynamic Programming



Given an array ‘arr’ containing the weight of ‘N’ distinct items, and two
knapsacks that can withstand ‘W1’ and ‘W2’ weights, the task is to find the
sum of the largest subset of the array ‘arr’, that can be fit in the two
knapsacks. Its not allowed to break any items in two, i.e an item should be
put in one of the bags as a whole.

 **Examples:**

>  **Input :** arr[] = {8, 3, 2}  
> W1 = 10, W2 = 3  
>  **Output :** 13  
> First and third objects go in the first knapsack. The second object goes in
> the second knapsack. Thus, the total weight becomes 13.
>
>  **Input :** arr[] = {8, 5, 3}  
> W1 = 10, W2 = 3  
>  **Output :** 11

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Solution:**  
A recursive solution is to try out all the possible ways of filling the two
knapsacks and choose the one giving the maximum weight.  
To optimize the above idea, we need to determine the states of DP, that we
will build up our solution upon. After little observation, we can determine
that this can be represented in three states **(i, w1_r, w2_r)**. Here ‘i’
means the index of the element we are trying to store, w1_r means the
remaining space of first knapsack, and w2_r means the remaining space of
second knapsack. Thus, the problem can be solved using a 3-dimensional
dynamic-programming with a recurrence relation

  

  

    
    
    DP[i][w1_r][w2_r] = max( DP[i + 1][w1_r][w2_r],
                        arr[i] + DP[i + 1][w1_r - arr[i]][w2_r],
                        arr[i] + DP[i + 1][w1_r][w2_r - arr[i]])
    

The explanation for the above recurrence relation is as follows:

> For each ‘i’, we can either:
>
>   1. Don’t select the item ‘i’.
>   2. Fill the item ‘i’ in first knapsack.
>   3. Fill the item ‘i’ in second knapsack.
>

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

#define maxN 31

#define maxW 31

using namespace std;

 

// 3D array to store

// states of DP

int dp[maxN][maxW][maxW];

 

// w1_r represents remaining capacity of 1st knapsack

// w2_r represents remaining capacity of 2nd knapsack

// i represents index of the array arr we are working on

int maxWeight(int* arr, int n, int w1_r, int w2_r, int
i)

{

 // Base case

 if (i == n)

 return 0;

 if (dp[i][w1_r][w2_r] != -1)

 return dp[i][w1_r][w2_r];

 

 // Variables to store the result of three

 // parts of recurrence relation

 int fill_w1 = 0, fill_w2 = 0, fill_none = 0;

 

 if (w1_r >= arr[i])

 fill_w1 = arr[i] + 

 maxWeight(arr, n, w1_r - arr[i], w2_r, i + 1);

 

 if (w2_r >= arr[i])

 fill_w2 = arr[i] + 

 maxWeight(arr, n, w1_r, w2_r - arr[i], i + 1);

 

 fill_none = maxWeight(arr, n, w1_r, w2_r, i + 1);

 

 // Store the state in the 3D array

 dp[i][w1_r][w2_r] = max(fill_none, max(fill_w1, fill_w2));

 

 return dp[i][w1_r][w2_r];

}

 

// Driver code

int main()

{

 // Input array

 int arr[] = { 8, 2, 3 };

 

 // Initializing the array with -1

 memset(dp, -1, sizeof(dp));

 

 // Number of elements in the array

 int n = sizeof(arr) / sizeof(arr[0]);

 

 // Capacity of knapsacks

 int w1 = 10, w2 = 3;

 

 // Function to be called

 cout << maxWeight(arr, n, w1, w2, 0);

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

// Java implementation of the above approach

 

class GFG

{

 static int maxN = 31;

 static int maxW = 31;

 

 // 3D array to store

 // states of DP

 static int dp [][][] = new int[maxN][maxW][maxW];

 

 // w1_r represents remaining capacity of 1st knapsack

 // w2_r represents remaining capacity of 2nd knapsack

 // i represents index of the array arr we are working on

 static int maxWeight(int arr [] , int n, int w1_r, int
w2_r, int i)

 {

 // Base case

 if (i == n)

 return 0;

 if (dp[i][w1_r][w2_r] != -1)

 return dp[i][w1_r][w2_r];

 

 // Variables to store the result of three

 // parts of recurrence relation

 int fill_w1 = 0, fill_w2 = 0, fill_none = 0;

 

 if (w1_r >= arr[i])

 fill_w1 = arr[i] + 

 maxWeight(arr, n, w1_r - arr[i], w2_r, i + 1);

 

 if (w2_r >= arr[i])

 fill_w2 = arr[i] + 

 maxWeight(arr, n, w1_r, w2_r - arr[i], i + 1);

 

 fill_none = maxWeight(arr, n, w1_r, w2_r, i + 1);

 

 // Store the state in the 3D array

 dp[i][w1_r][w2_r] = Math.max(fill_none, Math.max(fill_w1, fill_w2));

 

 return dp[i][w1_r][w2_r];

 }

 

 // Driver code

 public static void main (String[] args) 

 {

 

 // Input array

 int arr[] = { 8, 2, 3 };

 

 // Initializing the array with -1

 

 for (int i = 0; i < maxN ; i++)

 for (int j = 0; j < maxW ; j++)

 for (int k = 0; k < maxW ; k++)

 dp[i][j][k] = -1;

 

 // Number of elements in the array

 int n = arr.length;

 

 // Capacity of knapsacks

 int w1 = 10, w2 = 3;

 

 // Function to be called

 System.out.println(maxWeight(arr, n, w1, w2, 0));

 }

}

 

// This code is contributed by ihritik  
  
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

 

# w1_r represents remaining capacity of 1st knapsack 

# w2_r represents remaining capacity of 2nd knapsack 

# i represents index of the array arr we are working on 

def maxWeight(arr, n, w1_r, w2_r, i): 

 

 # Base case 

 if i == n:

 return 0

 if dp[i][w1_r][w2_r] != -1: 

 return dp[i][w1_r][w2_r] 

 

 # Variables to store the result of three 

 # parts of recurrence relation 

 fill_w1, fill_w2, fill_none = 0, 0, 0

 

 if w1_r >= arr[i]:

 fill_w1 = arr[i] + maxWeight(arr, n, w1_r - arr[i], 

 w2_r, i + 1) 

 

 if w2_r >= arr[i]:

 fill_w2 = arr[i] + maxWeight(arr, n, w1_r, 

 w2_r - arr[i], i + 1) 

 

 fill_none = maxWeight(arr, n, w1_r, w2_r, i + 1) 

 

 # Store the state in the 3D array 

 dp[i][w1_r][w2_r] = max(fill_none, max(fill_w1,

 fill_w2)) 

 

 return dp[i][w1_r][w2_r] 

 

 

# Driver code 

if __name__ == "__main__": 

 

 # Input array 

 arr = [8, 2, 3] 

 maxN, maxW = 31, 31

 

 # 3D array to store 

 # states of DP 

 dp = [[[-1] * maxW] * maxW] * maxN

 

 # Number of elements in the array 

 n = len(arr) 

 

 # Capacity of knapsacks 

 w1, w2 = 10, 3

 

 # Function to be called 

 print(maxWeight(arr, n, w1, w2, 0)) 

 

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

// C# implementation of the above approach

using System;

 

class GFG

{

 static int maxN = 31;

 static int maxW = 31;

 

 // 3D array to store

 // states of DP

 static int [ , , ] dp = new int[maxN, maxW, maxW];

 

 // w1_r represents remaining capacity of 1st knapsack

 // w2_r represents remaining capacity of 2nd knapsack

 // i represents index of the array arr we are working on

 static int maxWeight(int [] arr, int n, int w1_r,

 int w2_r, int i)

 {

 // Base case

 if (i == n)

 return 0;

 if (dp[i ,w1_r, w2_r] != -1)

 return dp[i, w1_r, w2_r];

 

 // Variables to store the result of three

 // parts of recurrence relation

 int fill_w1 = 0, fill_w2 = 0, fill_none = 0;

 

 if (w1_r >= arr[i])

 fill_w1 = arr[i] + 

 maxWeight(arr, n, w1_r - arr[i], w2_r, i + 1);

 

 if (w2_r >= arr[i])

 fill_w2 = arr[i] + 

 maxWeight(arr, n, w1_r, w2_r - arr[i], i + 1);

 

 fill_none = maxWeight(arr, n, w1_r, w2_r, i + 1);

 

 // Store the state in the 3D array

 dp[i, w1_r, w2_r] = Math.Max(fill_none, Math.Max(fill_w1, fill_w2));

 

 return dp[i, w1_r, w2_r];

 }

 

 // Driver code

 public static void Main () 

 {

 

 // Input array

 int [] arr = { 8, 2, 3 };

 

 // Initializing the array with -1

 

 for (int i = 0; i < maxN ; i++)

 for (int j = 0; j < maxW ; j++)

 for (int k = 0; k < maxW ; k++)

 dp[i, j, k] = -1;

 

 // Number of elements in the array

 int n = arr.Length;

 

 // Capacity of knapsacks

 int w1 = 10, w2 = 3;

 

 // Function to be called

 Console.WriteLine(maxWeight(arr, n, w1, w2, 0));

 }

}

 

// This code is contributed by ihritik  
  
---  
  
 __

 __

 **Output:**

    
    
    13
    

**  
Time complexity:** O(N*W1*W2).

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

