Number of subarrays have bitwise OR >= K



Given an array **arr[]** and an integer **K** , the task is to count the
number of sub-arrays having **bitwise OR ≥ K**.  
 **Examples:**  

> **Input:** arr[] = { 1, 2, 3 } K = 3  
> **Output:** 4  
> Bitwise OR of sub-arrays:  
> { 1 } = 1  
> { 1, 2 } = 3  
> { 1, 2, 3 } = 3  
> { 2 } = 2  
> { 2, 3 } = 3  
> { 3 } = 3  
> 4 sub-arrays have bitwise OR ≥ K  
>  **Input:** arr[] = { 3, 4, 5 } K = 6  
> **Output:** 2  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Naive approach:** Run three nested loops. The outermost loop determines the
starting of the sub-array. The middle loop determines the ending of the sub-
array. The innermost loop traverses the sub-array whose bounds are determined
by the outermost and middle loops. For every sub-array, calculate OR and
update **count = count + 1** if OR is greater than **K**.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <bits/stdc++.h>

using namespace std;

// Function to return the count of required sub-arrays

int countSubArrays(const int* arr, int n, int K)

{

 int count = 0;

 for (int i = 0; i < n; i++) {

 for (int j = i; j < n; j++) {

 int bitwise_or = 0;

 // Traverse sub-array [i..j]

 for (int k = i; k <= j; k++) {

 bitwise_or = bitwise_or | arr[k];

 }

 if (bitwise_or >= K)

 count++;

 }

 }

 return count;

}

// Driver code

int main()

{

 int arr[] = { 3, 4, 5 };

 int n = sizeof(arr) / sizeof(arr[0]);

 int k = 6;

 cout << countSubArrays(arr, n, k);

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

class solution

{

// Function to return the count of required sub-arrays

static int countSubArrays(int arr[], int n, int K)

{

 int count = 0;

 for (int i = 0; i < n; i++) {

 for (int j = i; j < n; j++) {

 int bitwise_or = 0;

 // Traverse sub-array [i..j]

 for (int k = i; k <= j; k++) {

 bitwise_or = bitwise_or | arr[k];

 }

 if (bitwise_or >= K)

 count++;

 }

 }

 return count;

}

// Driver code

public static void main(String args[])

{

 int arr[] = { 3, 4, 5 };

 int n = arr.length;

 int k = 6;

 System.out.println(countSubArrays(arr, n, k));

 

}

}

// This code is contributed by

// Surendra_Gangwar  
  
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

# Function to return the count of

# required sub-arrays

def countSubArrays(arr, n, K) :

 

 count = 0;

 for i in range(n) :

 for j in range(i, n) :

 bitwise_or = 0

 # Traverse sub-array [i..j]

 for k in range(i, j + 1) :

 bitwise_or = bitwise_or | arr[k]

 

 if (bitwise_or >= K) :

 count += 1

 

 return count

# Driver code

if __name__ == "__main__" :

 arr = [ 3, 4, 5 ]

 n = len(arr)

 k = 6

 

 print(countSubArrays(arr, n, k))

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

// C# implementation of the approach

using System;

class GFG

{

// Function to return the count of

// required sub-arrays

static int countSubArrays(int []arr,

 int n, int K)

{

 int count = 0;

 for (int i = 0; i < n; i++)

 {

 for (int j = i; j < n; j++)

 {

 int bitwise_or = 0;

 // Traverse sub-array [i..j]

 for (int k = i; k <= j; k++)

 {

 bitwise_or = bitwise_or | arr[k];

 }

 if (bitwise_or >= K)

 count++;

 }

 }

 return count;

}

// Driver code

public static void Main()

{

 int []arr = { 3, 4, 5 };

 int n = arr.Length;

 int k = 6;

 Console.WriteLine(countSubArrays(arr, n, k));

}

}

// This code is contributed by

// Mohit kumar  
  
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

// PHP implementation of the approach

// Function to return the count of

// required sub-arrays

function countSubArrays($arr, $n, $K)

{

 $count = 0;

 for ($i = 0; $i < $n; $i++)

 {

 for ($j = 0; $j < $n; $j++)

 {

 $bitwise_or = 0;

 // Traverse sub-array [i..j]

 for ($k = $i; $k < $j + 1; $k++)

 $bitwise_or = $bitwise_or | $arr[$k];

 

 if ($bitwise_or >= $K)

 $count += 1;

 }

 }

 return $count;

}

// Driver code

$arr = array( 3, 4, 5 );

$n = count($arr);

$k = 6;

print(countSubArrays($arr, $n, $k));

// This code is contributed by mits

?>  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

 // Javascript implementation of the approach

 

 // Function to return the count of required sub-arrays

 function countSubArrays(arr, n, K)

 {

 let count = 0;

 for (let i = 0; i < n; i++) {

 for (let j = i; j < n; j++) {

 let bitwise_or = 0;

 // Traverse sub-array [i..j]

 for (let k = i; k <= j; k++) {

 bitwise_or = bitwise_or | arr[k];

 }

 if (bitwise_or >= K)

 count++;

 }

 }

 return count;

 }

 

 // Driver code

 let arr = [ 3, 4, 5 ];

 let n = arr.length;

 let k = 6;

 document.write(countSubArrays(arr, n, k));

 

 // This code is contributed by suresh07.

</script>  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    2

