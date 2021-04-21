Find the number of elements greater than k in a sorted array



Given a sorted array **arr[]** of integers and an integer **k** , the task is
to find the count of elements in the array which are greater than **k**.
**Note** that **k** may or may not be present in the array.

 **Examples:**

>  **Input:** arr[] = {2, 3, 5, 6, 6, 9}, k = 6  
>  **Output:** 1
>
>  **Input:** arr[] = {1, 1, 2, 5, 5, 7}, k = 8  
>  **Output:** 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to perform binary search and find the number of
elements greater than k.

  

  

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

 

// Function to return the count of elements

// from the array which are greater than k

int countGreater(int arr[], int n, int k)

{

 int l = 0;

 int r = n - 1;

 

 // Stores the index of the left most element

 // from the array which is greater than k

 int leftGreater = n;

 

 // Finds number of elements greater than k

 while (l <= r) {

 int m = l + (r - l) / 2;

 

 // If mid element is greater than

 // k update leftGreater and r

 if (arr[m] > k) {

 leftGreater = m;

 r = m - 1;

 }

 

 // If mid element is less than

 // or equal to k update l

 else

 l = m + 1;

 }

 

 // Return the count of elements greater than k

 return (n - leftGreater);

}

 

// Driver code

int main()

{

 int arr[] = { 3, 3, 4, 7, 7, 7, 11, 13, 13 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 int k = 7;

 

 cout << countGreater(arr, n, k);

 

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

class GFG

{

 

// Function to return the count of elements

// from the array which are greater than k

static int countGreater(int arr[], int n, int k)

{

 int l = 0;

 int r = n - 1;

 

 // Stores the index of the left most element

 // from the array which is greater than k

 int leftGreater = n;

 

 // Finds number of elements greater than k

 while (l <= r) {

 int m = l + (r - l) / 2;

 

 // If mid element is greater than

 // k update leftGreater and r

 if (arr[m] > k) {

 leftGreater = m;

 r = m - 1;

 }

 

 // If mid element is less than

 // or equal to k update l

 else

 l = m + 1;

 }

 

 // Return the count of elements greater than k

 return (n - leftGreater);

}

 

// Driver code

public static void main(String[] args)

{

 int arr[] = { 3, 3, 4, 7, 7, 7, 11, 13,
13 };

 int n = arr.length;

 

 int k = 7;

 

 System.out.println(countGreater(arr, n, k));

}

}

 

// This code is contributed by Code_Mech  
  
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

 

# Function to return the count of elements

# from the array which are greater than k

def countGreater(arr, n, k):

 l = 0

 r = n - 1

 

 # Stores the index of the left most element

 # from the array which is greater than k

 leftGreater = n

 

 # Finds number of elements greater than k

 while (l <= r):

 m = int(l + (r - l) / 2)

 

 # If mid element is greater than

 # k update leftGreater and r

 if (arr[m] > k):

 leftGreater = m

 r = m - 1

 

 # If mid element is less than

 # or equal to k update l

 else:

 l = m + 1

 

 # Return the count of elements 

 # greater than k

 return (n - leftGreater)

 

# Driver code

if __name__ == '__main__':

 arr = [3, 3, 4, 7, 7, 7, 11, 13,
13]

 n = len(arr)

 k = 7

 

 print(countGreater(arr, n, k))

# This code is contributed by

# Surendra_Gangwar  
  
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

 

// Function to return the count of elements

// from the array which are greater than k

static int countGreater(int[]arr, int n, int k)

{

 int l = 0;

 int r = n - 1;

 

 // Stores the index of the left most element

 // from the array which is greater than k

 int leftGreater = n;

 

 // Finds number of elements greater than k

 while (l <= r) 

 {

 int m = l + (r - l) / 2;

 

 // If mid element is greater than

 // k update leftGreater and r

 if (arr[m] > k) 

 {

 leftGreater = m;

 r = m - 1;

 }

 

 // If mid element is less than

 // or equal to k update l

 else

 l = m + 1;

 }

 

 // Return the count of elements greater than k

 return (n - leftGreater);

}

 

// Driver code

public static void Main()

{

 int[] arr = { 3, 3, 4, 7, 7, 7, 11, 13, 13 };

 int n = arr.Length;

 

 int k = 7;

 

 Console.WriteLine(countGreater(arr, n, k));

}

}

 

// This code is contributed by Code_Mech  
  
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

 

// Function to return the count of elements

// from the array which are greater than k

function countGreater($arr, $n, $k)

{

 $l = 0;

 $r = $n - 1;

 

 // Stores the index of the left most element

 // from the array which is greater than k

 $leftGreater = $n;

 

 // Finds number of elements greater than k

 while ($l <= $r) 

 {

 $m = $l + (int)(($r - $l) / 2);

 

 // If mid element is greater than

 // k update leftGreater and r

 if ($arr[$m] > $k) 

 {

 $leftGreater = $m;

 $r = $m - 1;

 }

 

 // If mid element is less than

 // or equal to k update l

 else

 $l = $m + 1;

 }

 

 // Return the count of elements greater than k

 return ($n - $leftGreater);

}

 

// Driver code

$arr = array(3, 3, 4, 7, 7, 7, 11, 13, 13);

$n = sizeof($arr);

$k = 7;

 

echo countGreater($arr, $n, $k);

 

// This code is contributed

// by Akanksha Rai  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Time Complexity:** O(log(n)) where n is the number of elements in the array.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

