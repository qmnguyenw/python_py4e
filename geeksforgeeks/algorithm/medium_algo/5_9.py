Find the smallest subarray having atleast one duplicate



Given an array arr of **N** elements, the task is to find the length of the
smallest subarray of the given array that contains at least one duplicate
element. A subarray is formed from consecutive elements of an array. If no
such array exists, print “-1”.

 **Examples:**

    
    
    **Input:** arr = {1, 2, 3, 1, 5, 4, 5}
    **Output:** 3
    **Explanation:**
    ![](https://media.geeksforgeeks.org/wp-content/uploads/20191029232735/array11-300x58.jpg)
    
    **Input:** arr = {4, 7, 11, 3, 1, 2, 4}
    **Output:** 7
    **Explanation:**
    ![](https://media.geeksforgeeks.org/wp-content/uploads/20191029233004/array21-300x57.jpg)
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:**

  * The trick is to find all pairs of two elements with equal value. Since these two elements have equal value, the subarray enclosing them would have at least a single duplicate and will be one of the candidates for the answer.
  * A **simple solution** is to use two nested loops to find every pair of elements.If the two elements are equal then update the maximum length obtained so far.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find

// the smallest subarray having

// atleast one duplicate

#include <bits/stdc++.h>

using namespace std;

 

// Function to calculate

// SubArray Length

int subArrayLength(int arr[], int n)

{

 

 int minLen = INT_MAX;

 

 for (int i = 1; i < n; i++) {

 for (int j = 0; j < i; j++) {

 // If the two elements are equal,

 // then the subarray arr[i..j]

 // will definitely have a duplicate

 if (arr[i] == arr[j]) {

 // Update the minimum length

 // obtained so far

 minLen = min(minLen, i - j + 1);

 }

 }

 }

 if (minLen == INT_MAX) {

 return -1;

 }

 

 return minLen;

}

// Driver Code

int main()

{

 int n = 7;

 int arr[] = { 1, 2, 3, 1, 5, 4, 5 };

 

 int ans = subArrayLength(arr, n);

 cout << ans << '\n';

 

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

// Java program to find

// the smallest subarray having 

// atleast one duplicate

 

class GFG

{

 

 final static int INT_MAX = Integer.MAX_VALUE;

 

 // Function to calculate 

 // SubArray Length 

 static int subArrayLength(int arr[], int n) 

 { 

 

 int minLen = INT_MAX; 

 

 for (int i = 1; i < n; i++) 

 { 

 for (int j = 0; j < i; j++) 

 { 

 // If the two elements are equal, 

 // then the subarray arr[i..j] 

 // will definitely have a duplicate 

 if (arr[i] == arr[j]) 

 { 

 // Update the minimum length 

 // obtained so far 

 minLen = Math.min(minLen, i - j + 1); 

 } 

 } 

 } 

 if (minLen == INT_MAX)

 { 

 return -1; 

 } 

 

 return minLen; 

 } 

 

 // Driver Code 

 public static void main(String[] args)

 { 

 int n = 7; 

 int arr[] = { 1, 2, 3, 1, 5, 4, 5 }; 

 

 int ans = subArrayLength(arr, n); 

 System.out.println(ans); 

 

 } 

}

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for above approach

n = 7

arr = [1, 2, 3, 1, 5, 4, 5]

minLen = n + 1

 

for i in range(1, n):

 for j in range(0, i):

 if arr[i]== arr[j]:

 minLen = min(minLen, i-j + 1)

 

if minLen == n + 1:

 print("-1")

else:

 print(minLen)  
  
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

// C# program to find

// the smallest subarray having 

// atleast one duplicate

using System;

 

class GFG

{

 

 static int INT_MAX = int.MaxValue;

 

 // Function to calculate 

 // SubArray Length 

 static int subArrayLength(int []arr, int n) 

 { 

 

 int minLen = INT_MAX; 

 

 for (int i = 1; i < n; i++) 

 { 

 for (int j = 0; j < i; j++) 

 { 

 // If the two elements are equal, 

 // then the subarray arr[i..j] 

 // will definitely have a duplicate 

 if (arr[i] == arr[j]) 

 { 

 // Update the minimum length 

 // obtained so far 

 minLen = Math.Min(minLen, i - j + 1); 

 } 

 } 

 } 

 if (minLen == INT_MAX)

 { 

 return -1; 

 } 

 

 return minLen; 

 } 

 

 // Driver Code 

 public static void Main()

 { 

 int n = 7; 

 int []arr = { 1, 2, 3, 1, 5, 4, 5 }; 

 

 int ans = subArrayLength(arr, n); 

 Console.WriteLine(ans); 

 

 } 

}

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    3
    

