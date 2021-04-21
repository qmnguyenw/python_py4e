Maximize the maximum among minimum of K consecutive sub-arrays



Given an integer **K** and an array **arr[]** , the task is to split the array
arr[] into K consecutive subarrays to find the **maximum possible value** of
the _maximum among the minimum value of **K** consecutive sub-arrays_.

 **Examples:**

>  **Input:** arr[] = {1, 2, 3, 4, 5}, K = 2  
>  **Output:** 5  
> Split the array as [1, 2, 3, 4] and [5]. The minimum of the 2 consecutive
> sub-arrays is 1 and 5.  
> Maximum(1, 5) = 5. This splitting ensures maximum possible value.
>
>  **Input:** arr[] = {-4, -5, -3, -2, -1}, K = 1  
>  **Output:** -5  
> Only one sub-array is possible. Hence, min(-4, -5, -3, -2, -1) = -5

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The solution can be split into 3 possible cases:

  

  

  1.  **When K = 1:** In this case, the answer is always equal to the **minimum** of the array, since the array is split into only one sub-array i.e the array itself.
  2.  **When K ≥ 3:** In this case, the answer is always equal to the **maximum** of the array. When the array has to be split into 3 or more segments, then always keep one segment containing only a single element from the array i.e. the maximum element.
  3.  **When K = 2:** This is the trickiest case. There will only be a prefix and a suffix as there can be only two sub-arrays. Maintain an array of prefix minimums and suffix minimums. Then for every element **arr[i]** , update **ans = max(ans, max(prefix min value at i, suffix minimum value at i + 1))**.

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

using namespace std;

 

// Function to return maximum possible value

// of maximum of minimum of K sub-arrays

int maximizeMinimumOfKSubarrays(const int* arr, int n, int
k)

{

 int m = INT_MAX;

 int M = INT_MIN;

 

 // Compute maximum and minimum

 // of the array

 for (int i = 0; i < n; i++) {

 m = min(m, arr[i]);

 M = max(M, arr[i]);

 }

 

 // If k = 1 then return the

 // minimum of the array

 if (k == 1) {

 return m;

 }

 // If k >= 3 then return the

 // maximum of the array

 else if (k >= 3) {

 return M;

 }

 

 // If k = 2 then maintain prefix

 // and suffix minimums

 else {

 

 // Arrays to store prefix

 // and suffix minimums

 int L[n], R[n];

 

 L[0] = arr[0];

 R[n - 1] = arr[n - 1];

 

 // Prefix minimum

 for (int i = 1; i < n; i++)

 L[i] = min(L[i - 1], arr[i]);

 

 // Suffix minimum

 for (int i = n - 2; i >= 0; i--)

 R[i] = min(R[i + 1], arr[i]);

 

 int maxVal = INT_MIN;

 

 // Get the maximum possible value

 for (int i = 0; i < n - 1; i++)

 maxVal = max(maxVal, max(L[i], R[i + 1]));

 

 return maxVal;

 }

}

 

// Driver code

int main()

{

 int arr[] = { 1, 2, 3, 4, 5 };

 int n = sizeof(arr) / sizeof(arr[0]);

 int k = 2;

 

 cout << maximizeMinimumOfKSubarrays(arr, n, k);

 

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

class GFG {

 

 // Function to return maximum possible value

 // of maximum of minimum of K sub-arrays

 static int maximizeMinimumOfKSubarrays(int arr[], int n,
int k)

 {

 int m = Integer.MAX_VALUE;

 int M = Integer.MIN_VALUE;

 

 // Compute maximum and minimum

 // of the array

 for (int i = 0; i < n; i++) {

 m = Math.min(m, arr[i]);

 M = Math.max(M, arr[i]);

 }

 

 // If k = 1 then return the

 // minimum of the array

 if (k == 1) {

 return m;

 }

 

 // If k >= 3 then return the

 // maximum of the array

 else if (k >= 3) {

 return M;

 }

 

 // If k = 2 then maintain prefix

 // and suffix minimums

 else {

 

 // Arrays to store prefix

 // and suffix minimums

 int L[] = new int[n], R[] = new int[n];

 

 L[0] = arr[0];

 R[n - 1] = arr[n - 1];

 

 // Prefix minimum

 for (int i = 1; i < n; i++)

 L[i] = Math.min(L[i - 1], arr[i]);

 

 // Suffix minimum

 for (int i = n - 2; i >= 0; i--)

 R[i] = Math.min(R[i + 1], arr[i]);

 

 int maxVal = Integer.MIN_VALUE;

 

 // Get the maximum possible value

 for (int i = 0; i < n - 1; i++)

 maxVal = Math.max(maxVal, Math.max(L[i], R[i + 1]));

 

 return maxVal;

 }

 }

 

 // Driver code

 public static void main(String args[])

 {

 int arr[] = { 1, 2, 3, 4, 5 };

 int n = arr.length;

 int k = 2;

 

 System.out.println(maximizeMinimumOfKSubarrays(arr, n, k));

 }

}

 

// This code is contributed by Arnab Kundu  
  
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

import sys

 

# Function to return maximum possible value 

# of maximum of minimum of K sub-arrays 

def maximizeMinimumOfKSubarrays(arr, n, k) :

 

 m = sys.maxsize; 

 M = -(sys.maxsize - 1); 

 

 # Compute maximum and minimum 

 # of the array 

 for i in range(n) :

 m = min(m, arr[i]); 

 M = max(M, arr[i]); 

 

 # If k = 1 then return the 

 # minimum of the array 

 if (k == 1) :

 return m;

 

 # If k >= 3 then return the 

 # maximum of the array 

 elif (k >= 3) :

 return M;

 

 # If k = 2 then maintain prefix 

 # and suffix minimums 

 else :

 

 # Arrays to store prefix 

 # and suffix minimums

 L = [0] * n;

 R = [0] * n;

 

 L[0] = arr[0];

 R[n - 1] = arr[n - 1]; 

 

 # Prefix minimum

 for i in range(1, n) :

 L[i] = min(L[i - 1], arr[i]); 

 

 # Suffix minimum

 for i in range(n - 2, -1, -1) :

 R[i] = min(R[i + 1], arr[i]); 

 

 maxVal = -(sys.maxsize - 1); 

 

 # Get the maximum possible value

 for i in range(n - 1) :

 maxVal = max(maxVal, max(L[i], 

 R[i + 1])); 

 

 return maxVal; 

 

# Driver code 

if __name__ == "__main__" : 

 

 arr = [ 1, 2, 3, 4, 5 ]; 

 n = len(arr);

 k = 2; 

 

 print(maximizeMinimumOfKSubarrays(arr, n, k));

 

# This code is contributed by Ryuga  
  
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

// C# implemenatation of above approach

using System;

 

public class GFG {

 

 // Function to return maximum possible value

 // of maximum of minimum of K sub-arrays

 static int maximizeMinimumOfKSubarrays(int[] arr, int n,
int k)

 {

 int m = int.MaxValue;

 int M = int.MinValue;

 

 // Compute maximum and minimum

 // of the array

 for (int i = 0; i < n; i++) {

 m = Math.Min(m, arr[i]);

 M = Math.Max(M, arr[i]);

 }

 

 // If k = 1 then return the

 // minimum of the array

 if (k == 1) {

 return m;

 }

 

 // If k >= 3 then return the

 // maximum of the array

 else if (k >= 3) {

 return M;

 }

 

 // If k = 2 then maintain prefix

 // and suffix minimums

 else {

 

 // Arrays to store prefix

 // and suffix minimums

 int[] L = new int[n];

 int[] R = new int[n];

 

 L[0] = arr[0];

 R[n - 1] = arr[n - 1];

 

 // Prefix minimum

 for (int i = 1; i < n; i++)

 L[i] = Math.Min(L[i - 1], arr[i]);

 

 // Suffix minimum

 for (int i = n - 2; i >= 0; i--)

 R[i] = Math.Min(R[i + 1], arr[i]);

 

 int maxVal = int.MinValue;

 

 // Get the maximum possible value

 for (int i = 0; i < n - 1; i++)

 maxVal = Math.Max(maxVal, Math.Max(L[i], R[i + 1]));

 

 return maxVal;

 }

 }

 

 // Driver code

 public static void Main()

 {

 int[] arr = { 1, 2, 3, 4, 5 };

 int n = arr.Length;

 int k = 2;

 

 Console.WriteLine(maximizeMinimumOfKSubarrays(arr, n, k));

 }

}

/* This code contributed by PrinciRaj1992 */  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP implementation of the above approach

 

// Function to return maximum possible value

// of maximum of minimum of K sub-arrays

function maximizeMinimumOfKSubarrays($arr, $n, $k)

{

 $m = PHP_INT_MAX;

 $M = PHP_INT_MIN;

 

 // Compute maximum and minimum

 // of the array

 for ($i = 0; $i < $n; $i++)

 {

 $m = min($m, $arr[$i]);

 $M = max($M, $arr[$i]);

 }

 

 // If k = 1 then return the

 // minimum of the array

 if ($k == 1)

 {

 return $m;

 }

 

 // If k >= 3 then return the

 // maximum of the array

 else if ($k >= 3) 

 {

 return $M;

 }

 

 // If k = 2 then maintain prefix

 // and suffix minimums

 else

 {

 

 // Arrays to store prefix

 // and suffix minimums

 $L[0] = $arr[0];

 $R[$n - 1] = $arr[$n - 1];

 

 // Prefix minimum

 for ($i = 1; $i < $n; $i++)

 $L[$i] = min($L[$i - 1], $arr[$i]);

 

 // Suffix minimum

 for ($i = $n - 2; $i >= 0; $i--)

 $R[$i] = min($R[$i + 1], $arr[$i]);

 

 $maxVal = PHP_INT_MIN;

 

 // Get the maximum possible value

 for ($i = 0; $i < $n - 1; $i++)

 $maxVal = max($maxVal, 

 max($L[$i], $R[$i + 1]));

 

 return $maxVal;

 }

}

 

// Driver code

$arr = array( 1, 2, 3, 4, 5 );

$n = sizeof($arr);

$k = 2;

 

echo maximizeMinimumOfKSubarrays($arr, $n, $k);

 

// This code is contributed 

// by Akanksha Rai

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

