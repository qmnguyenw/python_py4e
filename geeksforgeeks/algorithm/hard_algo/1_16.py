Longest subarray having sum K | Set 2



Given an array **arr[]** of size **N** containing integers. The task is to
find the length of the longest sub-array having sum equal to the given value
**K**.

 **Examples:**

> **Input:** arr[] = {2, 3, 4, 2, 1, 1}, K = 10  
> **Output:** 4  
> **Explanation:**  
> The subarray {3, 4, 2, 1} gives summation as 10.
>
>  **Input:** arr[] = {6, 8, 14, 9, 4, 11, 10}, K = 13  
> **Output:** 2  
> **Explanation:**  
> The subarray {9, 4} gives summation as 13.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** Please refer to this article.  
 **Time Complexity:** _O(N 2)_  
**Auxiliary Space:** _O(1)_

 **Efficient Approach:** The idea is to use Binary Search to find the subarray
of maximum length having sum **K**. Below are the steps:

  

  

  1. Create a prefix sum array(say **pref[]** ) from the given array **arr[]**.
  2. For each element in the prefix array **pref[]** do Binary Search: 
    * Initialize **ans** , **start** and **end** variable as **-1, 0 and N** respectively.
    * Find the middle index(say **mid** ).
    * If **pref[mid] – val ≤ K** then update the start variable to **mid + 1** and **ans** to **mid**.
    * Else update the end variable to **mid – 1**.
  3. Return the value of **ans** from the above binary search.
  4. If current subarray length is less than **(ans – i)** , then update the maximum length to **(ans – i)**.

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

// To store the prefix sum array

vector<int> v;

// Function for searching the

// lower bound of the subarray

int bin(int val, int k, int n)

{

 int lo = 0;

 int hi = n;

 int mid;

 int ans = -1;

 // Iterate until low less

 // than equal to high

 while (lo <= hi) {

 mid = lo + (hi - lo) / 2;

 // For each mid finding sum

 // of sub array less than

 // or equal to k

 if (v[mid] - val <= k) {

 lo = mid + 1;

 ans = mid;

 }

 else

 hi = mid - 1;

 }

 // Return the final answer

 return ans;

}

// Function to find the length of

// subarray with sum K

void findSubarraySumK(int arr[], int N, int K)

{

 // Initialize sum to 0

 int sum = 0;

 v.push_back(0);

 // Push the prefix sum of the

 // array arr[] in prefix[]

 for (int i = 0; i < N; i++) {

 sum += arr[i];

 v.push_back(sum);

 }

 int l = 0, ans = 0, r;

 for (int i = 0; i < N; i++) {

 // Search r for each i

 r = bin(v[i], K, N);

 // Update ans

 ans = max(ans, r - i);

 }

 // Print the length of subarray

 // found in the array

 cout << ans;

}

// Driver Code

int main()

{

 // Given array arr[]

 int arr[] = { 6, 8, 14, 9, 4, 11, 10 };

 int N = sizeof(arr) / sizeof(arr[0]);

 // Given sum K

 int K = 13;

 // Function Call

 findSubarraySumK(arr, N, K);

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

// Java program for the above approach

import java.util.*;

class GFG {

 // To store the prefix sum array

 static Vector<Integer> v = new Vector<Integer>();

 // Function for searching the

 // lower bound of the subarray

 static int bin(int val, int k, int n)

 {

 int lo = 0;

 int hi = n;

 int mid;

 int ans = -1;

 // Iterate until low less

 // than equal to high

 while (lo <= hi) {

 mid = lo + (hi - lo) / 2;

 // For each mid finding sum

 // of sub array less than

 // or equal to k

 if (v.get(mid) - val <= k) {

 lo = mid + 1;

 ans = mid;

 }

 else

 hi = mid - 1;

 }

 // Return the final answer

 return ans;

 }

 // Function to find the length of

 // subarray with sum K

 static void findSubarraySumK(int arr[], int N, int K)

 {

 // Initialize sum to 0

 int sum = 0;

 v.add(0);

 // Push the prefix sum of the

 // array arr[] in prefix[]

 for (int i = 0; i < N; i++) {

 sum += arr[i];

 v.add(sum);

 }

 int l = 0, ans = 0, r;

 for (int i = 0; i < v.size(); i++) {

 // Search r for each i

 r = bin(v.get(i), K, N);

 // Update ans

 ans = Math.max(ans, r - i);

 }

 // Print the length of subarray

 // found in the array

 System.out.print(ans);

 }

 // Driver Code

 public static void main(String[] args)

 {

 // Given array arr[]

 int arr[] = { 6, 8, 14, 9, 4, 11, 10 };

 int N = arr.length;

 // Given sum K

 int K = 13;

 // Function call

 findSubarraySumK(arr, N, K);

 }

}

// This code is contributed by gauravrajput1  
  
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

# Python3 program for the above approach

# To store the prefix sum1 array

v = []

# Function for searching the

# lower bound of the subarray

def bin1(val, k, n):

 global v

 lo = 0

 hi = n

 mid = 0

 ans = -1

 # Iterate until low less

 # than equal to high

 while (lo <= hi):

 mid = lo + ((hi - lo) // 2)

 # For each mid finding sum1

 # of sub array less than

 # or equal to k

 if (v[mid] - val <= k):

 lo = mid + 1

 ans = mid

 else:

 hi = mid - 1

 # Return the final answer

 return ans

# Function to find the length of

# subarray with sum1 K

def findSubarraysum1K(arr, N, K):

 global v

 # Initialize sum1 to 0

 sum1 = 0

 v.append(0)

 # Push the prefix sum1 of the

 # array arr[] in prefix[]

 for i in range(N):

 sum1 += arr[i]

 v.append(sum1)

 l = 0

 ans = 0

 r = 0

 for i in range(len(v)):

 # Search r for each i

 r = bin1(v[i], K, N)

 # Update ans

 ans = max(ans, r - i)

 # Print the length of subarray

 # found in the array

 print(ans)

# Driver Code

if __name__ == '__main__':

 # Given array arr[]

 arr = [6, 8, 14, 9, 4, 11, 10]

 N = len(arr)

 # Given sum1 K

 K = 13

 # Function Call

 findSubarraysum1K(arr, N, K)

# This code is contributed by ipg2016107  
  
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

class GFG {

 // To store the prefix sum array

 static List<int> v = new List<int>();

 // Function for searching the

 // lower bound of the subarray

 static int bin(int val, int k, int n)

 {

 int lo = 0;

 int hi = n;

 int mid;

 int ans = -1;

 // Iterate until low less

 // than equal to high

 while (lo <= hi) {

 mid = lo + (hi - lo) / 2;

 // For each mid finding sum

 // of sub array less than

 // or equal to k

 if (v[mid] - val <= k) {

 lo = mid + 1;

 ans = mid;

 }

 else

 hi = mid - 1;

 }

 // Return the final answer

 return ans;

 }

 // Function to find the length of

 // subarray with sum K

 static void findSubarraySumK(int[] arr, int N, int K)

 {

 // Initialize sum to 0

 int sum = 0;

 v.Add(0);

 // Push the prefix sum of the

 // array []arr in prefix[]

 for (int i = 0; i < N; i++) {

 sum += arr[i];

 v.Add(sum);

 }

 int ans = 0, r;

 for (int i = 0; i < v.Count; i++) {

 // Search r for each i

 r = bin(v[i], K, N);

 // Update ans

 ans = Math.Max(ans, r - i);

 }

 // Print the length of subarray

 // found in the array

 Console.Write(ans);

 }

 // Driver Code

 public static void Main(String[] args)

 {

 // Given array []arr

 int[] arr = { 6, 8, 14, 9, 4, 11, 10 };

 int N = arr.Length;

 // Given sum K

 int K = 13;

 // Function call

 findSubarraySumK(arr, N, K);

 }

}

// This code is contributed by gauravrajput1  
  
---  
  
 __

 __

 **Output**

    
    
    2

 **Time Complexity:** _O(N*log 2N)_  
**Auxiliary Space:** _O(N)_

 **Efficient approach:** For a **O(N) approach** , please refer to the
efficient approach of this article.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

