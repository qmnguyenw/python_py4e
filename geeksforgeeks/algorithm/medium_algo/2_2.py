Longest Reverse Bitonic Sequence



Given an **arr[]** of length **N** , the task is to find the length of longest
Reverse Bitonic Subsequence. A subsequence is called Reverse Bitonic if it is
first decreasing, then increasing.  
 **Examples:**

>  **Input:** arr[] = {10, 11, 2, 1, 1, 5, 2, 4}  
> **Output:** 5  
>  **Explanation:** The longest subsequence which first decreases than
> increases is {10, 2, 1, 1, 2, 4}
>
> **Input:** arr[] = {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15}  
> **Output:** 7  
> **Explanation:** The longest subsequence which first decreases than
> increases is {12, 10, 6, 1, 9, 11, 15}

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
This problem is a variation of standard Longest Increasing Subsequence (LIS)
problem. Construct two arrays **lis[]** and **lds[]** to store the longest
increasing and decreasing subsequences respectively upto every ith index of
the array using Dynamic Programming. Finally, return the max value of **lds[i]
+ lis[i] – 1** where i ranges from 0 to N-1.

Below is the implementation of the above approach:

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the

// longest Reverse bitonic

// Subsequence

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the length

// of the Longest Reverse Bitonic

// Subsequence in the array

int ReverseBitonic(int arr[], int N)

{

 int i, j;

 

 // Allocate memory for LIS[] and

 // initialize LIS values as 1 for

 // all indexes

 int lds[N];

 for (i = 0; i < N; i++) {

 lds[i] = 1;

 }

 

 // Compute LIS values from left

 // to right for every index

 for (i = 1; i < N; i++) {

 for (j = 0; j < i; j++) {

 if (arr[i] < arr[j]

 && lds[i] < lds[j] + 1) {

 lds[i] = lds[j] + 1;

 }

 }

 }

 

 // Initialize LDS for

 // all indexes as 1

 int lis[N];

 for (i = 0; i < N; i++) {

 lis[i] = 1;

 }

 

 // Compute LDS values for every

 // index from right to left

 for (i = N - 2; i >= 0; i--) {

 for (j = N - 1; j > i; j--) {

 if (arr[i] < arr[j]

 && lis[i] < lis[j] + 1) {

 lis[i] = lis[j] + 1;

 }

 }

 }

 

 // Find the maximum value of

 // lis[i] + lds[i] - 1

 // in the array

 int max = lis[0] + lds[0] - 1;

 for (i = 1; i < N; i++) {

 if (lis[i] + lds[i] - 1 > max) {

 max = lis[i] + lds[i] - 1;

 }

 }

 // Return the maximum

 return max;

}

 

// Driver Program

int main()

{

 

 int arr[] = { 0, 8, 4, 12, 2, 10, 6,

 14, 1, 9, 5, 13, 3, 11,

 7, 15 };

 int N = sizeof(arr) / sizeof(arr[0]);

 printf("Length of LBS is %d\n",

 ReverseBitonic(arr, N));

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

// Java program to find the

// longest Reverse bitonic

// Subsequence

import java.io.*; 

 

class GFG{ 

 

// Function to return the length

// of the Longest Reverse Bitonic

// Subsequence in the array

static int ReverseBitonic(int arr[], int N)

{

 int i, j;

 

 // Allocate memory for LIS[] and

 // initialize LIS values as 1 for

 // all indexes

 int[] lds = new int[N];

 for(i = 0; i < N; i++)

 {

 lds[i] = 1;

 }

 

 // Compute LIS values from left

 // to right for every index

 for(i = 1; i < N; i++) 

 {

 for(j = 0; j < i; j++)

 {

 if (arr[i] < arr[j] && 

 lds[i] < lds[j] + 1)

 {

 lds[i] = lds[j] + 1;

 }

 }

 }

 

 // Initialize LDS for

 // all indexes as 1

 int[] lis = new int[N];

 for(i = 0; i < N; i++)

 {

 lis[i] = 1;

 }

 

 // Compute LDS values for every

 // index from right to left

 for(i = N - 2; i >= 0; i--)

 {

 for(j = N - 1; j > i; j--) 

 {

 if (arr[i] < arr[j] && 

 lis[i] < lis[j] + 1)

 {

 lis[i] = lis[j] + 1;

 }

 }

 }

 

 // Find the maximum value of

 // lis[i] + lds[i] - 1

 // in the array

 int max = lis[0] + lds[0] - 1;

 for(i = 1; i < N; i++) 

 {

 if (lis[i] + lds[i] - 1 > max)

 {

 max = lis[i] + lds[i] - 1;

 }

 }

 // Return the maximum

 return max;

}

 

// Driver code 

public static void main (String[] args) 

{ 

 int arr[] = { 0, 8, 4, 12, 

 2, 10, 6, 14,

 1, 9, 5, 13, 

 3, 11, 7, 15 };

 

 int N = arr.length;

 

 System.out.println("Length of LBS is " + 

 ReverseBitonic(arr, N));

} 

} 

 

// This code is contributed by jana_sayantan  
  
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

# Python3 program to find the

# longest Reverse bitonic 

# Subsequence 

 

# Function to return the length 

# of the Longest Reverse Bitonic 

# Subsequence in the array 

def ReverseBitonic(arr): 

 

 N = len(arr) 

 

 # Allocate memory for LIS[] and 

 # initialize LIS values as 1 

 # for all indexes 

 lds = [1 for i in range(N + 1)] 

 

 # Compute LIS values from left to right 

 for i in range(1, N): 

 for j in range(0 , i): 

 if ((arr[i] < arr[j]) and

 (lds[i] < lds[j] + 1)): 

 lds[i] = lds[j] + 1

 

 # Allocate memory for LDS and 

 # initialize LDS values for 

 # all indexes 

 lis = [1 for i in range(N + 1)] 

 

 # Compute LDS values from right to left

 # Loop from n-2 downto 0 

 for i in reversed(range(N - 1)): 

 

 # Loop from n-1 downto i-1 

 for j in reversed(range(i - 1, N)): 

 if (arr[i] < arr[j] and

 lis[i] < lis[j] + 1): 

 lis[i] = lis[j] + 1

 

 # Return the maximum value of

 # (lis[i] + lds[i] - 1) 

 maximum = lis[0] + lds[0] - 1

 for i in range(1, N): 

 maximum = max((lis[i] +

 lds[i] - 1), maximum) 

 

 return maximum 

 

# Driver code

arr = [ 0, 8, 4, 12, 

 2, 10, 6, 14, 

 1, 9, 5, 13, 

 3, 11, 7, 15 ] 

 

print("Length of LBS is", ReverseBitonic(arr))

 

# This code is contributed by grand_master  
  
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

// C# program to find the

// longest Reverse bitonic

// Subsequence

using System; 

 

class GFG{ 

 

// Function to return the length

// of the Longest Reverse Bitonic

// Subsequence in the array

static int ReverseBitonic(int[] arr, int N)

{

 int i, j;

 

 // Allocate memory for LIS[] and

 // initialize LIS values as 1 for

 // all indexes

 int[] lds = new int[N];

 for(i = 0; i < N; i++)

 {

 lds[i] = 1;

 }

 

 // Compute LIS values from left

 // to right for every index

 for(i = 1; i < N; i++) 

 {

 for(j = 0; j < i; j++)

 {

 if (arr[i] < arr[j] && 

 lds[i] < lds[j] + 1)

 {

 lds[i] = lds[j] + 1;

 }

 }

 }

 

 // Initialize LDS for

 // all indexes as 1

 int[] lis = new int[N];

 for(i = 0; i < N; i++)

 {

 lis[i] = 1;

 }

 

 // Compute LDS values for every

 // index from right to left

 for(i = N - 2; i >= 0; i--)

 {

 for(j = N - 1; j > i; j--) 

 {

 if (arr[i] < arr[j] && 

 lis[i] < lis[j] + 1)

 {

 lis[i] = lis[j] + 1;

 }

 }

 }

 

 // Find the maximum value of

 // lis[i] + lds[i] - 1

 // in the array

 int max = lis[0] + lds[0] - 1;

 for(i = 1; i < N; i++) 

 {

 if (lis[i] + lds[i] - 1 > max)

 {

 max = lis[i] + lds[i] - 1;

 }

 }

 

 // Return the maximum

 return max;

}

 

// Driver code 

public static void Main () 

{ 

 int[] arr = new int[] { 0, 8, 4, 12, 

 2, 10, 6, 14,

 1, 9, 5, 13, 

 3, 11, 7, 15 };

 

 int N = arr.Length;

 

 Console.WriteLine("Length of LBS is " + 

 ReverseBitonic(arr, N));

} 

}

 

// This code is contributed by sanjoy_62  
  
---  
  
 __

 __

 **Output:**

    
    
    Length of LBS is 7
    

_**Time Complexity:** O(N2) _  
_**Auxiliary Space:** O(N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

