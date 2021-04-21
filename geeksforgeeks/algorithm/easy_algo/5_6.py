Find the longest Fibonacci-like subarray of the given array



Given an array of **N** elements, the task is to find the longest subarray
which is Fibonacci-like.

A Fibonacci-like sub-array is defined as an array in which:

    
    
    **A[i]=A[i-1]+A[i-2]** where i>2
    
    and, A[1] and A[2] can be anything.
    

**Examples:**

    
    
    **Input :** N = 5, arr[] = {2, 4, 6, 10, 2}
    **Output :** 4
    The sub-array 2, 4, 6, 10 is Fibonacci like.
    
    **Input :** N = 3, arr[] = {0, 0, 0}
    **Output :** 3
    The entire array is Fibonacci-like.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

The idea is to observe that any array of length of less than or equal to 2 is
Fibonacci-like. Now, for arrays of length greater than 2:

  

  

  1. Maintain a variable **len** initialized to 2 and a variable **mx** to store the maximum length so far.
  2. Start traversing the array from 3rd index.
  3. If the fibonacci like array can be extended for this index, i.e. if a[i] = a[i-1] + a[i-2]
    * Then increment the value of variable **len** by 1.
    * Otherwise reinitialize the variable **len** to 2.
    * Store the maximum of mx and len in the variable mx for current iteration.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find length of longest

// Fibonacci-like subarray

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the length of the 

// longest Fibonacci-like subarray

int longestFibonacciSubarray(int n, int a[])

{

 // Any 2 terms are Fibonacci-like

 if (n <= 2)

 return n;

 

 int len = 2;

 

 int mx = INT_MIN;

 

 for (int i = 2; i < n; i++) {

 

 // If previous subarray can be extended

 if (a[i] == a[i - 1] + a[i - 2])

 len++;

 

 // Any 2 terms are Fibonacci-like

 else

 len = 2;

 

 // Find the maximum length

 mx = max(mx, len);

 }

 

 return mx;

}

 

// Driver Code

int main()

{

 int n = 5;

 int a[] = {2, 4, 6, 10, 2};

 

 cout << longestFibonacciSubarray(n, a);

 

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

// Java program to find length of longest

// Fibonacci-like subarray 

class GFG 

{

 

 // Function to find the length of the 

 // longest Fibonacci-like subarray 

 static int longestFibonacciSubarray(int n, int a[]) 

 { 

 // Any 2 terms are Fibonacci-like 

 if (n <= 2) 

 return n; 

 

 int len = 2; 

 

 int mx = Integer.MIN_VALUE; 

 

 for (int i = 2; i < n; i++)

 { 

 

 // If previous subarray can be extended 

 if (a[i] == a[i - 1] + a[i - 2]) 

 len++; 

 

 // Any 2 terms are Fibonacci-like 

 else

 len = 2; 

 

 // Find the maximum length 

 mx = Math.max(mx, len); 

 } 

 return mx; 

 } 

 

 // Driver Code 

 public static void main (String[] args) 

 { 

 int n = 5; 

 int a[] = {2, 4, 6, 10, 2}; 

 

 System.out.println(longestFibonacciSubarray(n, a)); 

 } 

}

 

// This code is contributed by Ryuga  
  
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

# Python3 program to find Length of

# longest Fibonacci-like subarray

 

# Function to find the Length of the 

# longest Fibonacci-like subarray

def longestFibonacciSubarray(n, a):

 

 # Any 2 terms are Fibonacci-like

 if (n <= 2):

 return n

 

 Len = 2

 

 mx = -10**9

 

 for i in range(2, n):

 

 # If previous subarray can be extended

 if (a[i] == a[i - 1] + a[i - 2]):

 Len += 1

 

 # Any 2 terms are Fibonacci-like

 else:

 Len = 2

 

 # Find the maximum Length

 mx = max(mx, Len)

 

 return mx

 

# Driver Code

n = 5

a = [2, 4, 6, 10, 2]

 

print(longestFibonacciSubarray(n, a))

 

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

// C# program to find length of longest

// Fibonacci-like subarray 

using System;

 

class GFG 

{

 

 // Function to find the length of the 

 // longest Fibonacci-like subarray 

 static int longestFibonacciSubarray(int n, int[] a) 

 { 

 // Any 2 terms are Fibonacci-like 

 if (n <= 2) 

 return n; 

 

 int len = 2; 

 

 int mx = int.MinValue; 

 

 for (int i = 2; i < n; i++)

 { 

 

 // If previous subarray can be extended 

 if (a[i] == a[i - 1] + a[i - 2]) 

 len++; 

 

 // Any 2 terms are Fibonacci-like 

 else

 len = 2; 

 

 // Find the maximum length 

 mx = Math.Max(mx, len); 

 } 

 return mx; 

 } 

 

 // Driver Code 

 public static void Main () 

 { 

 int n = 5; 

 int[] a = {2, 4, 6, 10, 2}; 

 

 Console.WriteLine(longestFibonacciSubarray(n, a)); 

 } 

}

 

// This code is contributed by Code_Mech.  
  
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

// PHP program to find length of longest

// Fibonacci-like subarray

 

// Function to find the length of the 

// longest Fibonacci-like subarray

function longestFibonacciSubarray($n, $a)

{

 // Any 2 terms are Fibonacci-like

 if ($n <= 2)

 return $n;

 

 $len = 2;

 

 $mx = PHP_INT_MIN;

 

 for ($i = 2; $i < $n; $i++) 

 {

 

 // If previous subarray can be extended

 if ($a[$i] == $a[$i - 1] + $a[$i - 2])

 $len++;

 

 // Any 2 terms are Fibonacci-like

 else

 $len = 2;

 

 // Find the maximum length

 $mx = max($mx, $len);

 }

 

 return $mx;

}

 

// Driver Code

$n = 5;

$a = array(2, 4, 6, 10, 2);

 

echo longestFibonacciSubarray($n, $a);

 

// This code is contributed 

// by Akanksha Rai 

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    

**Time Complexity:** O(N)  
 **Auxiliary Space** : O(1)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

