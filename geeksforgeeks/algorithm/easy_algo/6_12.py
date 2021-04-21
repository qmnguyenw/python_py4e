Minimum number of moves to make all elements equal



Given an array containing N elements and an integer K. It is allowed to
perform the following operation any number of times on the given array:

  * Insert the K-th element at the end of the array and delete the first element of the array.

The task is to find the minimum number of moves needed to make all elements of
the array equal. Print -1 if it is not possible.

 **Examples:**

    
    
    **Input :** arr[] = {1, 2, 3, 4}, K = 4
    **Output :** 3
    Step 1: 2 3 4 4
    Step 2: 3 4 4 4
    Step 3: 4 4 4 4
    
    **Input :** arr[] = {2, 1}, K = 1
    **Output :** -1
    The array will keep alternating between 1, 2 and 
    2, 1 regardless of how many moves you apply.
    

Let’s look at the operations with respect to the original array, first we copy
a[k] to the end, then a[k+1] and so on. To make sure that we only copy equal
elements, all elements in the range K to N should be equal.

So, to find the minimum number of moves, we need to remove all elements in
range 1 to K that are not equal to a[k]. Hence, we need to keep applying
operations until we reach the rightmost term in range 1 to K that is not equal
to a[k].

  

  

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to find minimum number of

// operations to make all array Elements

// equal

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find minimum number of operations

// to make all array Elements equal

int countMinimumMoves(int arr[], int n, int k)

{

 int i;

 

 // Check if it is possible or not

 // That is if all the elements from

 // index K to N are not equal

 for (i = k - 1; i < n; i++)

 if (arr[i] != arr[k - 1])

 return -1;

 

 // Find minimum number of moves

 for (i = k - 1; i >= 0; i--)

 if (arr[i] != arr[k - 1])

 return i + 1;

 

 // Elements are already equal

 return 0;

}

 

// Driver Code

int main()

{

 int arr[] = { 1, 2, 3, 4 };

 int K = 4;

 

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << countMinimumMoves(arr, n, K);

 

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

// Java Program to find minimum number of

// operations to make all array Elements

// equal

 

 

import java.io.*;

 

class GFG {

 

 

 

// Function to find minimum number of operations

// to make all array Elements equal

static int countMinimumMoves(int arr[], int n, int k)

{

 int i;

 

 // Check if it is possible or not

 // That is if all the elements from

 // index K to N are not equal

 for (i = k - 1; i < n; i++)

 if (arr[i] != arr[k - 1])

 return -1;

 

 // Find minimum number of moves

 for (i = k - 1; i >= 0; i--)

 if (arr[i] != arr[k - 1])

 return i + 1;

 

 // Elements are already equal

 return 0;

}

 

// Driver Code

 

 public static void main (String[] args) {

 int arr[] = { 1, 2, 3, 4 };

 int K = 4;

 

 int n = arr.length;

 

 System.out.print(countMinimumMoves(arr, n, K));

 }

}

// This code is contributed by shs   
  
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

# Python3 Program to find minimum

# number of operations to make all 

# array Elements equal

 

# Function to find minimum number 

# of operations to make all array

# Elements equal

def countMinimumMoves(arr, n, k) :

 

 # Check if it is possible or not

 # That is if all the elements from

 # index K to N are not equal

 for i in range(k - 1, n) :

 if (arr[i] != arr[k - 1]) :

 return -1

 

 # Find minimum number of moves

 for i in range(k - 1, -1, -1) :

 if (arr[i] != arr[k - 1]) :

 return i + 1

 

 # Elements are already equal

 return 0

 

# Driver Code

if __name__ == "__main__" :

 

 arr = [ 1, 2, 3, 4 ]

 K = 4

 

 n = len(arr)

 

 print(countMinimumMoves(arr, n, K))

 

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

// C# Program to find minimum number of

// operations to make all array Elements

// equal

using System;

 

class GFG 

{

 

// Function to find minimum number 

// of operations to make all array

// Elements equal

static int countMinimumMoves(int []arr, 

 int n, int k)

{

 int i;

 

 // Check if it is possible or not

 // That is if all the elements from

 // index K to N are not equal

 for (i = k - 1; i < n; i++)

 if (arr[i] != arr[k - 1])

 return -1;

 

 // Find minimum number of moves

 for (i = k - 1; i >= 0; i--)

 if (arr[i] != arr[k - 1])

 return i + 1;

 

 // Elements are already equal

 return 0;

}

 

// Driver Code

public static void Main ()

{

 int []arr = { 1, 2, 3, 4 };

 int K = 4;

 

 int n = arr.Length;

 

 Console.Write(countMinimumMoves(arr, n, K));

}

}

 

// This code is contributed 

// by 29AjayKumar  
  
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

// PHP Program to find minimum number of

// operations to make all array Elements

// equal

 

// Function to find minimum number 

// of operations to make all array 

// Elements equal

function countMinimumMoves($arr, $n, $k)

{

 

 // Check if it is possible or not

 // That is if all the elements from

 // index K to N are not equal

 for ($i = $k - 1; $i < $n; $i++)

 if ($arr[$i] != $arr[$k - 1])

 return -1;

 

 // Find minimum number of moves

 for ($i = $k - 1; $i >= 0; $i--)

 if ($arr[$i] != $arr[$k - 1])

 return $i + 1;

 

 // Elements are already equal

 return 0;

}

 

// Driver Code

$arr = array(1, 2, 3, 4);

$K = 4;

 

$n = sizeof($arr);

 

echo countMinimumMoves($arr, $n, $K);

 

// This code is contributed 

// by Akanksha Rai

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Time Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

