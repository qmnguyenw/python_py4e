Count maximum elements of an array whose absolute difference does not exceed K



Given an array **A** and positive integer **K**. The task is to find maximum
number elements for which the absolute difference of any of the pair does not
exceed **K**.

 **Examples:**

>  **Input:** A[] = {1, 26, 17, 12, 15, 2}, K = 5  
>  **Output:** 3  
> There are maximum **3** values so that the absolute difference of each pair  
> does not exceed K(K=5) ie., {12, 15, 17}
>
>  **Input:** A[] = {1, 2, 5, 10, 8, 3}, K = 4  
>  **Output:** 4  
> There are maximum **4** values so that the absolute difference of each pair  
> does not exceed K(K=4) ie., {1, 2, 3, 5}

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

  1. Sort the given Array in ascending order.
  2. Iterate from index i = 0 to n.
  3. For every A[i] count how many values which are in range A[i] to A[i] + K  
ie., A[i]<= A[j] <= A[i]+K

  4. Return Max Count

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

 

// Function to return the maximum elements

// in which absolute difference of any pair

// does not exceed K

int maxCount(int A[], int N, int K)

{

 int maximum = 0;

 int i = 0, j = 0;

 int start = 0;

 int end = 0;

 

 // Sort the Given array

 sort(A, A + N);

 

 // Find max elements

 for (i = 0; i < N; i++) {

 

 // Count all elements which are in range

 // A[i] to A[i] + K

 while (j < N && A[j] <= A[i] + K)

 j++;

 if (maximum < (j - i)) {

 maximum = (j - i);

 start = i;

 end = j;

 }

 }

 

 // Return the max count

 return maximum;

}

 

// Driver code

int main()

{

 int A[] = { 1, 26, 17, 12, 15, 2 };

 int N = sizeof(A) / sizeof(A[0]);

 int K = 5;

 cout << maxCount(A, N, K);

 

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

import java.util.*;

 

class GFG 

{

 

// Function to return the maximum elements 

// in which absolute difference of any pair 

// does not exceed K 

static int maxCount(int A[], int N, int K) 

{ 

 int maximum = 0; 

 int i = 0, j = 0; 

 int start = 0; 

 int end = 0; 

 

 // Sort the Given array 

 Arrays.sort(A); 

 

 // Find max elements 

 for (i = 0; i < N; i++)

 { 

 

 // Count all elements which are in range 

 // A[i] to A[i] + K 

 while (j < N && A[j] <= A[i] + K) 

 j++; 

 if (maximum < (j - i)) 

 { 

 maximum = (j - i); 

 start = i; 

 end = j; 

 } 

 } 

 

 // Return the max count 

 return maximum; 

} 

 

// Driver code 

public static void main(String[] args)

{

 int A[] = { 1, 26, 17, 12, 15, 2 }; 

 int N = A.length; 

 int K = 5; 

 System.out.println(maxCount(A, N, K));

}

}

 

// This code has been contributed by 29AjayKumar  
  
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

 

def maxCount(A, N, K):

 

 maximum = 0

 start = 0

 end = 0

 j = 0

 

 # Sort the Array

 A.sort()

 

 # Find max elements

 for i in range(0, N):

 while(j < N and A[j] <= A[i] + K):

 j += 1

 if maximum < (j - i ):

 maximum = (j - i)

 start = i;

 end = j; 

 

 # Return the maximum

 return maximum

 

# Driver code

A = [1, 26, 17, 12, 15, 2] 

N = len(A)

K = 5

 

print(maxCount(A, N, K))  
  
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

 

// Function to return the maximum elements 

// in which absolute difference of any pair 

// does not exceed K 

static int maxCount(int []A, int N, int K) 

{ 

 int maximum = 0; 

 int i = 0, j = 0; 

 int start = 0; 

 int end = 0; 

 

 // Sort the Given array 

 Array.Sort(A); 

 

 // Find max elements 

 for (i = 0; i < N; i++)

 { 

 

 // Count all elements which are in range 

 // A[i] to A[i] + K 

 while (j < N && A[j] <= A[i] + K) 

 j++; 

 if (maximum < (j - i)) 

 { 

 maximum = (j - i); 

 start = i; 

 end = j; 

 } 

 } 

 

 // Return the max count 

 return maximum; 

} 

 

// Driver code 

public static void Main()

{

 int []A = { 1, 26, 17, 12, 15, 2 }; 

 int N = A.Length; 

 int K = 5; 

 Console.Write(maxCount(A, N, K));

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

 

// Function to return the maximum 

// elements in which absolute difference 

// of any pair does not exceed K 

function maxCount($A, $N, $K) 

{ 

 $maximum = 0; 

 $i = 0;

 $j = 0; 

 $start = 0; 

 $end = 0; 

 

 // Sort the Given array 

 sort($A); 

 

 // Find max elements 

 for ($i = 0; $i < $N; $i++)

 { 

 

 // Count all elements which 

 // are in range A[i] to A[i] + K 

 while ($j < $N && 

 $A[$j] <= $A[$i] + $K) 

 $j++; 

 if ($maximum < ($j - $i)) 

 { 

 $maximum = ($j - $i); 

 $start = $i; 

 $end = $j; 

 } 

 } 

 

 // Return the max count 

 return $maximum; 

} 

 

// Driver code 

$A = array( 1, 26, 17, 12, 15, 2 ); 

$N = Count($A); 

$K = 5; 

echo maxCount($A, $N, $K); 

 

// This code is contributed 

// by Arnab Kundu

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

