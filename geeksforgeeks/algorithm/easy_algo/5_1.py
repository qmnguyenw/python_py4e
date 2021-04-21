Find the modified array after performing k operations of given type



Given an array **arr[]** of **n** integers and an integer **K**. In one
operation every element of the array is replaced by the difference of that
element and the maximum value of the array. The task is to print the array
after performing **K** operations.  
 **Examples:**  

> **Input:** arr[] = {4, 8, 12, 16}, k = 2  
> **Output:** 0 4 8 12  
> k = 1, arr[] = {12, 8, 4, 0}  
> k = 2, arr[] = {0, 4, 8, 12}  
>  **Input:** arr[] = {14, 28, 14, 106, 223}, k = 12  
> **Output:** 0 14 0 92 209  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** There are two possible cases:  

  1. If **k is odd** then the new array will be **max(arr) – arr[i]** for all **i** in range **[0, n)**.
  2. If **k is even** then the new array will be **arr[i] – min(arr)** for all **i** in range **[0, n)**.

 **For example:**  

  

  

> Let arr[] = {4, 8, 12, 16}  
> For k = 1, arr[] = (12, 8, 4, 0}  
> For k = 2, arr[] = (0, 4, 8, 12}  
> For k = 3, arr[] = (12, 8, 4, 0}  
> For k = 4, arr[] = (0, 4, 8, 12}  
> It can be observed that the array is repeating after every 2 operations.  
>

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

// Utility function to print

// the contents of an array

void printArray(int arr[], int n)

{

 for (int i = 0; i < n; i++)

 cout << arr[i] << " ";

}

// Function to remove the minimum value of

// the array from every element of the array

void removeMin(int arr[], int n)

{

 int i, minVal = arr[0];

 // Get the minimum value from the array

 for (i = 1; i < n; i++)

 minVal = min(minVal, arr[i]);

 // Remove the minimum value from

 // every element of the array

 for (i = 0; i < n; i++)

 arr[i] = arr[i] - minVal;

}

// Function to remove every element of the

// array from the maximum value of the array

void removeFromMax(int arr[], int n)

{

 int i, maxVal = arr[0];

 // Get the maximum value from the array

 for (i = 1; i < n; i++)

 maxVal = max(maxVal, arr[i]);

 // Remove every element of the array from

 // the maximum value of the array

 for (i = 0; i < n; i++)

 arr[i] = maxVal - arr[i];

}

// Function to print the modified array

// after k operations

void modifyArray(int arr[], int n, int k)

{

 // If k is odd then remove the minimum element

 // of the array from every element of the array

 if (k % 2 == 0)

 removeMin(arr, n);

 // Else remove every element of the array from

 // the maximum value from the array

 else

 removeFromMax(arr, n);

 // Print the modified array

 printArray(arr, n);

}

// Driver code

int main()

{

 int arr[] = { 4, 8, 12, 16 };

 int n = sizeof(arr) / sizeof(arr[0]);

 int k = 2;

 modifyArray(arr, n, k);

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

class GFG {

 // Utility function to print

 // the contents of an array

 static void printArray(int arr[], int n)

 {

 for (int i = 0; i < n; i++)

 System.out.print(arr[i] + " ");

 }

 // Function to remove the minimum value of

 // the array from every element of the array

 static void removeMin(int arr[], int n)

 {

 int i, minVal = arr[0];

 // Get the minimum value from the array

 for (i = 1; i < n; i++)

 minVal = Math.min(minVal, arr[i]);

 // Remove the minimum value from

 // every element of the array

 for (i = 0; i < n; i++)

 arr[i] = arr[i] - minVal;

 }

 // Function to remove every element of the

 // array from the maximum value of the array

 static void removeFromMax(int arr[], int n)

 {

 int i, maxVal = arr[0];

 // Get the maximum value from the array

 for (i = 1; i < n; i++)

 maxVal = Math.max(maxVal, arr[i]);

 // Remove every element of the array from

 // the maximum value of the array

 for (i = 0; i < n; i++)

 arr[i] = maxVal - arr[i];

 }

 // Function to print the modified array

 // after k operations

 static void modifyArray(int arr[], int n, int k)

 {

 // If k is odd then remove the minimum element

 // of the array from every element of the array

 if (k % 2 == 0)

 removeMin(arr, n);

 // Else remove every element of the array from

 // the maximum value from the array

 else

 removeFromMax(arr, n);

 // Print the modified array

 printArray(arr, n);

 }

 // Driver code

 public static void main(String args[])

 {

 int arr[] = { 4, 8, 12, 16 };

 int n = arr.length;

 int k = 2;

 modifyArray(arr, n, k);

 }

}  
  
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

# Python 3 implementation of the approach

# Utility function to print

# the contents of an array

def printArray(arr, n) :

 for i in range(n) :

 print(arr[i], end = " ");

# Function to remove the minimum

# value of the array from every

# element of the array

def removeMin(arr, n) :

 

 minVal = arr[0];

 # Get the minimum value from

 # the array

 for i in range(1, n) :

 minVal = min(minVal, arr[i]);

 # Remove the minimum value from

 # every element of the array

 for i in range(n) :

 arr[i] = arr[i] - minVal;

# Function to remove every element

# of the array from the maximum

# value of the array

def removeFromMax(arr, n) :

 

 maxVal = arr[0];

 # Get the maximum value from

 # the array

 for i in range(1, n) :

 maxVal = max(maxVal, arr[i]);

 # Remove every element of the

 # array from the maximum value

 # of the array

 for i in range(n) :

 arr[i] = maxVal - arr[i];

# Function to print the modified 

# array after k operations

def modifyArray(arr, n, k) :

 # If k is odd then remove the minimum

 # element of the array from every

 # element of the array

 if (k % 2 == 0) :

 removeMin(arr, n);

 # Else remove every element of

 # the array from the maximum

 # value from the array

 else :

 removeFromMax(arr, n);

 # Print the modified array

 printArray(arr, n);

# Driver code

if __name__ == "__main__" :

 arr = [ 4, 8, 12, 16 ];

 n = len(arr)

 

 k = 2;

 modifyArray(arr, n, k);

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

class GFG {

 // Utility function to print

 // the contents of an array

 static void printArray(int[] arr, int n)

 {

 for (int i = 0; i < n; i++)

 Console.Write(arr[i] + " ");

 }

 // Function to remove the minimum value of

 // the array from every element of the array

 static void removeMin(int[] arr, int n)

 {

 int i, minVal = arr[0];

 // Get the minimum value from the array

 for (i = 1; i < n; i++)

 minVal = Math.Min(minVal, arr[i]);

 // Remove the minimum value from

 // every element of the array

 for (i = 0; i < n; i++)

 arr[i] = arr[i] - minVal;

 }

 // Function to remove every element of the

 // array from the maximum value of the array

 static void removeFromMax(int[] arr, int n)

 {

 int i, maxVal = arr[0];

 // Get the maximum value from the array

 for (i = 1; i < n; i++)

 maxVal = Math.Max(maxVal, arr[i]);

 // Remove every element of the array from

 // the maximum value of the array

 for (i = 0; i < n; i++)

 arr[i] = maxVal - arr[i];

 }

 // Function to print the modified array

 // after k operations

 static void modifyArray(int[] arr, int n, int k)

 {

 // If k is odd then remove the minimum element

 // of the array from every element of the array

 if (k % 2 == 0)

 removeMin(arr, n);

 // Else remove every element of the array from

 // the maximum value from the array

 else

 removeFromMax(arr, n);

 // Print the modified array

 printArray(arr, n);

 }

 // Driver code

 public static void Main(String[] args)

 {

 int[] arr = { 4, 8, 12, 16 };

 int n = arr.Length;

 int k = 2;

 modifyArray(arr, n, k);

 }

}  
  
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

// Utility function to print

// the contents of an array

function printArray($arr, $n)

{

 for ($i = 0; $i < $n; $i++)

 echo $arr[$i] . " ";

}

// Function to remove the minimum value of

// the array from every element of the array

function removeMin(&$arr, $n)

{

 $minVal = $arr[0];

 // Get the minimum value from the array

 for ($i = 1; $i < $n; $i++)

 $minVal = min($minVal, $arr[$i]);

 // Remove the minimum value from

 // every element of the array

 for ($i = 0; $i < $n; $i++)

 $arr[$i] = $arr[$i] - $minVal;

}

// Function to remove every element of the

// array from the maximum value of the array

function removeFromMax(&$arr, $n)

{

 $maxVal = $arr[0];

 // Get the maximum value from the array

 for ($i = 1; $i < $n; $i++)

 $maxVal = max($maxVal, $arr[$i]);

 // Remove every element of the array from

 // the maximum value of the array

 for ($i = 0; $i < $n; $i++)

 $arr[$i] = $maxVal - $arr[$i];

}

// Function to print the modified array

// after k operations

function modifyArray($arr, $n, $k)

{

 // If k is odd then remove the minimum element

 // of the array from every element of the array

 if ($k % 2 == 0)

 removeMin($arr, $n);

 // Else remove every element of the array

 // from the maximum value from the array

 else

 removeFromMax($arr, $n);

 // Print the modified array

 printArray($arr, $n);

}

// Driver code

$arr = array( 4, 8, 12, 16 );

$n = count($arr);

$k = 2;

modifyArray($arr, $n, $k);

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

// Utility function to print

// the contents of an array

function printArray(arr, n)

{

 for (var i = 0; i < n; i++)

 document.write(arr[i] + " ");

}

// Function to remove the minimum value of

// the array from every element of the array

function removeMin(arr, n)

{

 var i, minVal = arr[0];

 // Get the minimum value from the array

 for (i = 1; i < n; i++)

 minVal = Math.min(minVal, arr[i]);

 // Remove the minimum value from

 // every element of the array

 for (i = 0; i < n; i++)

 arr[i] = arr[i] - minVal;

}

// Function to remove every element of the

// array from the maximum value of the array

function removeFromMax(arr, n)

{

 var i, maxVal = arr[0];

 // Get the maximum value from the array

 for (i = 1; i < n; i++)

 maxVal = Math.max(maxVal, arr[i]);

 // Remove every element of the array from

 // the maximum value of the array

 for (i = 0; i < n; i++)

 arr[i] = maxVal - arr[i];

}

// Function to print the modified array

// after k operations

function modifyArray(arr, n, k)

{

 // If k is odd then remove the minimum element

 // of the array from every element of the array

 if (k % 2 == 0)

 removeMin(arr, n);

 // Else remove every element of the array from

 // the maximum value from the array

 else

 removeFromMax(arr, n);

 // Print the modified array

 printArray(arr, n);

}

// Driver code

arr = [ 4, 8, 12, 16 ]

var n = arr.length;

var k = 2;

modifyArray(arr, n, k);

// This code is contributed by noob2000.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    0 4 8 12

**Time Complexity:** O(n)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

