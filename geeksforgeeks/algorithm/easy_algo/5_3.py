Find the K-th minimum element from an array concatenated M times



Given an Array arr[] and two integers **K** and **M**. The problem is to find
the **K-th Minimum element** after concatenating the array to itself **M
times**.

 **Examples:**

    
    
    **Input  :** arr[] = {3, 1, 2}, K = 4, M = 3 
    **Output :** 4'th Minimum element is : 2
    **Explanation** : Concatenate array 3 times (ie., M = 3)
                  arr[] = [3, 1, 2, 3, 1, 2, 3, 1, 2]
                  arr[] = [1, 1, 1, 2, 2, 2, 3, 3, 3]
                  Now 4'th Minimum element is 2
    
    **Input  :** arr[] = {1, 13, 9, 17, 1, 12}, K = 19, M = 7 
    **Output :** 19'th Minimum element is : 9
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Simple Approach :**

  1. Append the given array into a vector or any other array say V for **M** times.
  2. Sort the vector or array **V** in ascending order.
  3. Return the value at index **( K-1 )** of vector **V** i.e., return **V[ K – 1 ].**

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ programme to find the K'th minimum

// element from an array concatenated M times

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the K-th minimum element 

// from an array concatenated M times

int KthMinValAfterMconcatenate(int A[], int N, 

 int M, int K)

{

 vector<int> V;

 

 for (int i = 0; i < M; i++) {

 for (int j = 0; j < N; j++) {

 V.push_back(A[j]);

 }

 }

 

 // sort the elements in ascending order

 sort(V.begin(), V.end());

 

 // return K'th Min element

 // present at K-1 index

 return (V[K - 1]);

}

 

// Driver Code

int main()

{

 int A[] = { 3, 1, 2 };

 

 int M = 3, K = 4;

 int N = sizeof(A) / sizeof(A[0]);

 

 cout << KthMinValAfterMconcatenate(A, N, M, K);

 

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

import java.util.ArrayList;

import java.util.Collections;

 

// Java programme to find the K'th minimum 

// element from an array concatenated M times

class GFG 

{

 

 // Function to find the K-th minimum element 

 // from an array concatenated M times

 static int KthMinValAfterMconcatenate(int[] A, int N,

 int M, int K) 

 {

 ArrayList V = new ArrayList();

 

 for (int i = 0; i < M; i++)

 {

 for (int j = 0; j < N; j++)

 {

 V.add(A[j]);

 }

 }

 

 // sort the elements in ascending order

 Collections.sort(V);

 

 // return K'th Min element

 // present at K-1 index

 return ((int) V.get(K - 1));

 }

 

 // Driver Code

 public static void main(String[] args) 

 {

 int[] A = {3, 1, 2};

 int M = 3, K = 4;

 int N = A.length;

 System.out.println(KthMinValAfterMconcatenate(A, N, M, K));

 }

}

 

/* This code contributed by PrinciRaj1992 */  
  
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

# Python3 program to find the K'th minimum

# element from an array concatenated M times 

 

# Function to find the K-th minimum element 

# from an array concatenated M times 

def KthMinValAfterMconcatenate(A, N, M, K): 

 

 V = [] 

 

 for i in range(0, M): 

 for j in range(0, N): 

 V.append(A[j]) 

 

 # sort the elements in ascending order 

 V.sort() 

 

 # return K'th Min element 

 # present at K-1 index 

 return V[K - 1] 

 

# Driver Code 

if __name__ == "__main__":

 

 A = [3, 1, 2] 

 

 M, K = 3, 4

 N = len(A) 

 

 print(KthMinValAfterMconcatenate(A, N, M, K)) 

 

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

// C# programme to find the K'th minimum

// element from an array concatenated M times

using System;

using System.Collections;

 

class GFG

{

 

// Function to find the K-th minimum element 

// from an array concatenated M times

static int KthMinValAfterMconcatenate(int []A, int N, 

 int M, int K)

{

 ArrayList V=new ArrayList();

 

 for (int i = 0; i < M; i++) 

 {

 for (int j = 0; j < N; j++)

 {

 V.Add(A[j]);

 }

 }

 

 // sort the elements in ascending order

 V.Sort();

 

 // return K'th Min element

 // present at K-1 index

 return ((int)V[K - 1]);

}

 

// Driver Code

static void Main()

{

 int []A = { 3, 1, 2 };

 

 int M = 3, K = 4;

 int N = A.Length;

 

 Console.WriteLine(KthMinValAfterMconcatenate(A, N, M, K));

}

}

 

// This code is contributed by mits  
  
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

// PHP programme to find the K'th minimum 

// element from an array concatenated M times

 

// Function to find the K-th minimum element 

// from an array concatenated M times

function KthMinValAfterMconcatenate($A, $N, 

 $M, $K)

{

 $V = array();

 

 for ($i = 0; $i < $M; $i++) 

 {

 for ($j = 0; $j < $N; $j++) 

 {

 array_push($V, $A[$j]);

 }

 }

 

 // sort the elements in ascending order

 sort($V);

 

 // return K'th Min element

 // present at K-1 index

 return ($V[$K - 1]);

}

 

// Driver Code

$A = array( 3, 1, 2 );

 

$M = 3;

$K = 4;

$N = count($A);

 

echo KthMinValAfterMconcatenate($A, $N, $M, $K);

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    2
    

