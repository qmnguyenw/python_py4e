Smallest Pair Sum in an array



Given an array of distinct integers **arr[]** , the task is to find a pair
which has the minimum sum and print the sum.

 **Examples:**

>  **Input:** arr[] = {1, 2, 3}  
>  **Output:** 3  
> The pair (1, 2) will have the minimum sum pair i.e. 1 + 2 = 3
>
>  **Input:** arr[] = {3, 5, 6, 2}  
>  **Output:** 5

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

  * Find the minimum element from the array and store it in **min**.
  * Find the second minimum element from the array and store it in **secondMin**.
  * Print **min + secondMin**.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to print the sum of the minimum pair

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the sum of

// the minimum pair from the array

int smallest_pair(int a[], int n)

{

 int min = INT_MAX, secondMin = INT_MAX;

 for (int j = 0; j < n; j++) {

 

 // If found new minimum

 if (a[j] < min) {

 

 // Minimum now becomes second minimum

 secondMin = min;

 

 // Update minimum

 min = a[j];

 }

 

 // If current element is > min and < secondMin

 else if ((a[j] < secondMin) && a[j] != min)

 

 // Update secondMin

 secondMin = a[j];

 }

 

 // Return the sum of the minimum pair

 return (secondMin + min);

}

 

// Driver code

int main()

{

 int arr[] = { 1, 2, 3 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << smallest_pair(arr, n);

 

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

// Java program to print the sum

// of the minimum pair

import java .io.*;

 

class GFG

{

// Function to return the sum of

// the minimum pair from the array

static int smallest_pair(int[] a, int n)

{

 int min = Integer.MAX_VALUE, secondMin = Integer.MAX_VALUE;

 for (int j = 0; j < n; j++) 

 {

 

 // If found new minimum

 if (a[j] < min)

 {

 

 // Minimum now becomes second minimum

 secondMin = min;

 

 // Update minimum

 min = a[j];

 }

 

 // If current element is > min and < secondMin

 else if ((a[j] < secondMin) && a[j] != min)

 

 // Update secondMin

 secondMin = a[j];

 }

 

 // Return the sum of the minimum pair

 return (secondMin + min);

}

 

// Driver code

public static void main(String[] args)

{

 int[] arr = { 1, 2, 3 };

 int n = arr.length;

 

 System.out.println(smallest_pair(arr, n));

}

}

 

// This code is contributed 

// by inder_verma  
  
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

# Python3 program to print the

# sum of the minimum pair 

import sys

 

# Function to return the sum of 

# the minimum pair from the array 

def smallest_pair(a, n) :

 

 min = sys.maxsize

 secondMin = sys.maxsize

 

 for j in range(n) : 

 

 # If found new minimum 

 if (a[j] < min) :

 

 # Minimum now becomes 

 # second minimum 

 secondMin = min

 

 # Update minimum 

 min = a[j]

 

 # If current element is > min 

 # and < secondMin 

 elif ((a[j] < secondMin) and

 a[j] != min) :

 

 # Update secondMin 

 secondMin = a[j] 

 

 # Return the sum of the minimum pair 

 return (secondMin + min)

 

# Driver code 

if __name__ == "__main__" : 

 

 arr = [ 1, 2, 3 ] 

 n = len(arr) 

 

 print(smallest_pair(arr, n)) 

 

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

// C# program to print the sum

// of the minimum pair

using System;

 

class GFG

{

// Function to return the sum of

// the minimum pair from the array

static int smallest_pair(int[] a, int n)

{

 int min = int.MaxValue, secondMin = int.MaxValue;

 for (int j = 0; j < n; j++) 

 {

 

 // If found new minimum

 if (a[j] < min)

 {

 

 // Minimum now becomes second minimum

 secondMin = min;

 

 // Update minimum

 min = a[j];

 }

 

 // If current element is > min and < secondMin

 else if ((a[j] < secondMin) && a[j] != min)

 

 // Update secondMin

 secondMin = a[j];

 }

 

 // Return the sum of the minimum pair

 return (secondMin + min);

}

 

// Driver code

public static void Main()

{

 int[] arr = { 1, 2, 3 };

 int n = arr.Length;

 

 Console.Write(smallest_pair(arr, n));

}

}

 

// This code is contributed 

// by Akanksha Rai  
  
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

// PHP program to print the sum 

// of the minimum pair 

 

// Function to return the sum of 

// the minimum pair from the array 

function smallest_pair($a, $n) 

{ 

 $min = PHP_INT_MAX;

 $secondMin = PHP_INT_MAX; 

 for ($j = 0; $j < $n; $j++) 

 { 

 

 // If found new minimum 

 if ($a[$j] < $min) 

 { 

 

 // Minimum now becomes 

 // second minimum 

 $secondMin = $min; 

 

 // Update minimum 

 $min = $a[$j]; 

 } 

 

 // If current element is > min 

 // and < secondMin 

 else if (($a[$j] < $secondMin) &&

 $a[$j] != $min) 

 

 // Update secondMin 

 $secondMin = $a[$j]; 

 } 

 

 // Return the sum of the minimum pair 

 return ($secondMin + $min); 

} 

 

// Driver code 

$arr = array( 1, 2, 3 ); 

$n = sizeof($arr); 

echo smallest_pair($arr, $n); 

 

// This code is contributed by ajit

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

