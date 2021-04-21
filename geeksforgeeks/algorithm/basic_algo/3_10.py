Maximum sum subarray such that start and end values are same



Given an array of N positive numbers, the task is to find a contiguous
subarray (L-R) such that **a[L]=a[R]** and sum of **a[L] + a[L+1] +…+ a[R] is
maximum.**

 **Examples:**

    
    
    **Input:** arr[] = {1, 3, 2, 2, 3}
    **Output:** 10
    Subarray [3, 2, 2, 3] starts and ends with 3 and has sum = 10
    
    **Input:** arr[] = {1, 3, 2, 2, 3}
    **Output:** 10
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** For every element in the array, let’s find 2 values: First
(Leftmost) occurrence in the array and Last (Rightmost) occurrence in the
array. Since all numbers are positive, increasing the number of terms can only
increase the sum. Hence for every number in the array, we find the sum between
it’s leftmost and rightmost occurrence, which can be done quickly using prefix
sums. We can keep track of the maximum value found so far and print it in the
end.

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

 

// Function to find the maximum sum

int maxValue(int a[], int n)

{

 unordered_map<int, int> first, last;

 int pr[n];

 pr[0] = a[0];

 

 for (int i = 1; i < n; i++) {

 

 // Build prefix sum array

 pr[i] = pr[i - 1] + a[i];

 

 // If the value hasn't been encountered before,

 // It is the first occurrence

 if (first[a[i]] == 0)

 first[a[i]] = i;

 

 // Keep updating the last occurrence

 last[a[i]] = i;

 }

 

 int ans = 0;

 

 // Find the maximum sum with same first and last value

 for (int i = 0; i < n; i++) {

 int start = first[a[i]];

 int end = last[a[i]];

 ans = max(ans, pr[end] - pr[start - 1]);

 }

 return ans;

}

 

// Driver Code

int main()

{

 int arr[] = { 1, 3, 5, 2, 4, 18, 2, 3 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << maxValue(arr, n);

 

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

import java.io.*;

import java.util.*;

 

class GFG {

 

 // Function to find the maximum sum

 static int maxValue(int a[], int n)

 {

 HashMap<Integer, Integer> first = new HashMap<>();

 HashMap<Integer, Integer> last = new HashMap<>();

 for (int i = 0; i < n; i++) {

 first.put(a[i], 0);

 last.put(a[i], 0);

 }

 

 int[] pr = new int[n];

 pr[0] = a[0];

 

 for (int i = 1; i < n; i++) {

 

 // Build prefix sum array

 pr[i] = pr[i - 1] + a[i];

 

 // If the value hasn't been encountered before,

 // It is the first occurrence

 if (Integer.parseInt(String.valueOf(first.get(a[i]))) == 0)

 first.put(a[i], i);

 

 // Keep updating the last occurrence

 last.put(a[i], i);

 }

 

 int ans = 0;

 

 // Find the maximum sum with same first and last value

 for (int i = 0; i < n; i++) {

 int start = Integer.parseInt(String.valueOf(first.get(a[i])));

 int end = Integer.parseInt(String.valueOf(last.get(a[i])));

 if (start != 0)

 ans = Math.max(ans, pr[end] - pr[start - 1]);

 }

 

 return ans;

 }

 

 // Driver Code

 public static void main(String args[])

 {

 int[] arr = { 1, 3, 5, 2, 4, 18, 2, 3
};

 int n = arr.length;

 System.out.print(maxValue(arr, n));

 }

}

 

// This code is contributed by rachana soma  
  
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

from collections import defaultdict

 

# Function to find the maximum sum 

def maxValue(a, n): 

 

 first = defaultdict(lambda:0)

 last = defaultdict(lambda:0)

 

 pr = [None] * n 

 pr[0] = a[0] 

 

 for i in range(1, n): 

 

 # Build prefix sum array 

 pr[i] = pr[i - 1] + a[i] 

 

 # If the value hasn't been encountered before, 

 # It is the first occurrence 

 if first[a[i]] == 0: 

 first[a[i]] = i 

 

 # Keep updating the last occurrence 

 last[a[i]] = i 

 

 

 ans = 0

 

 # Find the maximum sum with same first and last value 

 for i in range(0, n): 

 start = first[a[i]] 

 end = last[a[i]] 

 ans = max(ans, pr[end] - pr[start - 1]) 

 

 return ans 

 

 

# Driver Code 

if __name__ == "__main__": 

 

 arr = [1, 3, 5, 2, 4, 18, 2, 3] 

 n = len(arr) 

 

 print(maxValue(arr, n)) 

 

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

using System.Collections.Generic;

 

class GFG 

{

 

 // Function to find the maximum sum

 static int maxValue(int []a, int n)

 {

 Dictionary<int, 

 int> first = new Dictionary<int, 

 int>();

 Dictionary<int, 

 int> last = new Dictionary<int, 

 int>();

 

 for (int i = 0; i < n; i++) 

 {

 first[a[i]] = 0;

 last[a[i]] = 0;

 }

 

 int[] pr = new int[n];

 pr[0] = a[0];

 

 for (int i = 1; i < n; i++) 

 {

 

 // Build prefix sum array

 pr[i] = pr[i - 1] + a[i];

 

 // If the value hasn't been encountered before,

 // It is the first occurrence

 if (first[a[i]] == 0)

 first[a[i]] = i;

 

 // Keep updating the last occurrence

 last[a[i]] = i;

 }

 

 int ans = 0;

 

 // Find the maximum sum with 

 // same first and last value

 for (int i = 0; i < n; i++) 

 {

 int start = first[a[i]];

 int end = last[a[i]];

 if (start != 0)

 ans = Math.Max(ans, pr[end] - pr[start - 1]);

 }

 return ans;

 }

 

 // Driver Code

 static void Main()

 {

 int[] arr = { 1, 3, 5, 2, 4, 18, 2, 3 };

 int n = arr.Length;

 Console.Write(maxValue(arr, n));

 }

}

 

// This code is contributed by mohit kumar  
  
---  
  
 __

 __

 **Output:**

    
    
    37
    

**Time Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

