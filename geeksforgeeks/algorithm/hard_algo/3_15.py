Minimum increment or decrement required to sort the array | Top-down Approach



Given an array **arr[]** of **N** integers, the task is to sort the array in
increasing order by performing minimum number of operations. In a single
operation, an element of the array can either be incremented or decremented by
1. Print the minimum number of operations required.  
 **Examples:**

>  **Input:** arr[] = {5, 4, 3, 2, 1}  
> **Output:** 6  
> **Explanation:**  
> The sorted array of arr[] is {3, 3, 3, 3, 3}  
> Therefore the minimum increments/decrement are:  
> At index 0, 5 – **3** = 2 (decrement 2)  
> At index 1, 4 – **3** = 1 (decrement 1)  
> At index 3, 2 + 1 = **3** (increment 1)  
> At index 4, 1 + 2 = **3** (increment 2)  
> The total increment/decrement is 2 + 1 + 1 + 2 = 6.  
>  **Input:** arr[] = {1, 2, 3, 4}  
> **Output:** 0  
> **Explanation:**  
> The array is already sorted.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Bottom-up Approach:** This problem can be solved using Dynamic Programming.
A Bottom-up Approach to this problem statement is discussed in this article.  
**Top-Down Approach:** Here we will use Top-down Dynamic Programming to solve
this problem.  
Let 2D array (say dp[i][j]) used to store the upto index **i** where last
element is at index **j**.  
Below are the steps:  

  1. To make the array element in sorted by using the given operations, we know that an element cannot become greater than the maximum value of the array and less than the minimum value of the array(say **m** ) by increment or decrement.
  2. Therefore, Fix an element(say **X** ) at **ith** position, then **(i-1)th** position value(say **Y** ) can be in the range **[m, X]**.
  3. Keep placing the smaller element less than or equals to **arr[i]** at **(i-1)th** position for every index **i** of **arr[]** and calculate the minimum increment or decrement by adding **abs(arr[i] – Y)**.
  4. Therefore the recurrence relation for the above mentioned approach can be written as:  

>  
>
>
> dp[i][j] = min(dp[i][j], abs(arr[i] – Y) + recursive_function(i-1, Y))  
> where m ≤ Y ≤ arr[j].
>
>  
>
>
>  
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

// C++ program of the above approach

#include <bits/stdc++.h>

using namespace std;

// Dp array to memoized

// the value recursive call

int dp[1000][1000];

// Function to find the minimum increment

// or decrement needed to make the array

// sorted

int minimumIncDec(int arr[], int N,

 int maxE, int minE)

{

 // If only one element is present,

 // then arr[] is sorted

 if (N == 0) {

 return 0;

 }

 // If dp[N][maxE] is precalculated,

 // then return the result

 if (dp[N][maxE])

 return dp[N][maxE];

 int ans = INT_MAX;

 // Iterate from minE to maxE which

 // placed at previous index

 for (int k = minE; k <= maxE; k++) {

 // Update the answer according to

 // recurrence relation

 int x = minimumIncDec(arr, N - 1, k, minE);

 ans = min(ans,x + abs(arr[N - 1] - k));

 }

 // Memoized the value

 // for dp[N][maxE]

 dp[N][maxE] = ans;

 // Return the final result

 return dp[N][maxE];

}

// Driver Code

int main()

{

 int arr[] = { 5, 4, 3, 2, 1 };

 int N = sizeof(arr) / sizeof(arr[0]);

 // Find the minimum and maximum

 // element from the arr[]

 int minE = *min_element(arr, arr + N);

 int maxE = *max_element(arr, arr + N);

 // Function Call

 cout << minimumIncDec(

 arr, N, maxE, minE);

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

// Java program of the above approach

import java.util.*;

class GFG{

// Dp array to memoized

// the value recursive call

static int [][]dp = new int[1000][1000];

// Function to find the minimum increment

// or decrement needed to make the array

// sorted

static int minimumIncDec(int arr[], int N,

 int maxE, int minE)

{

 

 // If only one element is present,

 // then arr[] is sorted

 if (N == 0)

 {

 return 0;

 }

 

 // If dp[N][maxE] is precalculated,

 // then return the result

 if (dp[N][maxE] != 0)

 return dp[N][maxE];

 int ans = Integer.MAX_VALUE;

 // Iterate from minE to maxE which

 // placed at previous index

 for(int k = minE; k <= maxE; k++)

 {

 // Update the answer according to

 // recurrence relation

 int x = minimumIncDec(arr, N - 1, k, minE);

 ans = Math.min(ans,

 x + Math.abs(arr[N - 1] - k));

 }

 // Memoized the value

 // for dp[N][maxE]

 dp[N][maxE] = ans;

 // Return the final result

 return dp[N][maxE];

}

// Driver Code

public static void main(String[] args)

{

 int arr[] = { 5, 4, 3, 2, 1 };

 int N = arr.length;

 // Find the minimum and maximum

 // element from the arr[]

 int minE = Arrays.stream(arr).min().getAsInt();

 int maxE = Arrays.stream(arr).max().getAsInt();

 // Function call

 System.out.print(minimumIncDec(

 arr, N, maxE, minE));

}

}

// This code is contributed by amal kumar choubey  
  
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

# Python3 program of the above approach

import sys

# Dp array to memoized

# the value recursive call

dp = [[ 0 for x in range(1000)]

 for y in range(1000)]

# Function to find the minimum increment

# or decrement needed to make the array

# sorted

def minimumIncDec(arr, N, maxE, minE):

 # If only one element is present,

 # then arr[] is sorted

 if (N == 0):

 return 0

 # If dp[N][maxE] is precalculated,

 # then return the result

 if (dp[N][maxE]):

 return dp[N][maxE]

 ans = sys.maxsize

 # Iterate from minE to maxE which

 # placed at previous index

 for k in range(minE, maxE + 1):

 # Update the answer according to

 # recurrence relation

 x = minimumIncDec(arr, N - 1, k, minE)

 ans = min(ans, x + abs(arr[N - 1] - k))

 # Memoized the value

 # for dp[N][maxE]

 dp[N][maxE] = ans

 # Return the final result

 return dp[N][maxE]

# Driver Code

if __name__ == "__main__":

 arr = [ 5, 4, 3, 2, 1 ]

 N = len(arr)

 # Find the minimum and maximum

 # element from the arr[]

 minE = min(arr)

 maxE = max(arr)

 # Function Call

 print(minimumIncDec(arr, N, maxE, minE))

# This code is contributed by chitranayal  
  
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

// C# program of the above approach

using System;

using System.Linq;

class GFG{

// Dp array to memoized

// the value recursive call

static int [,]dp = new int[1000, 1000];

// Function to find the minimum increment

// or decrement needed to make the array

// sorted

static int minimumIncDec(int []arr, int N,

 int maxE, int minE)

{

 

 // If only one element is present,

 // then []arr is sorted

 if (N == 0)

 {

 return 0;

 }

 

 // If dp[N,maxE] is precalculated,

 // then return the result

 if (dp[N, maxE] != 0)

 return dp[N, maxE];

 int ans = int.MaxValue;

 // Iterate from minE to maxE which

 // placed at previous index

 for(int k = minE; k <= maxE; k++)

 {

 // Update the answer according to

 // recurrence relation

 int x = minimumIncDec(arr, N - 1, k, minE);

 ans = Math.Min(ans,

 x + Math.Abs(arr[N - 1] - k));

 }

 // Memoized the value

 // for dp[N,maxE]

 dp[N, maxE] = ans;

 // Return the readonly result

 return dp[N,maxE];

}

// Driver Code

public static void Main(String[] args)

{

 int []arr = { 5, 4, 3, 2, 1 };

 int N = arr.Length;

 // Find the minimum and maximum

 // element from the []arr

 int minE = arr.Min();

 int maxE = arr.Max();

 // Function call

 Console.Write(minimumIncDec(arr, N,

 maxE, minE));

}

}

// This code is contributed by Rohit_ranjan  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    
    
    
    

_**Time Complexity:** O(N2) _  
_**Auxiliary Space:** O(N2)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

