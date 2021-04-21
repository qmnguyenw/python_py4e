Count number of triplets in an array having sum in the range [a, b]



Given an array of distinct integers and a range [a, b], the task is to count
the number of triplets having a sum in the range [a, b].

 **Examples:**

    
    
    Input : arr[] = {8, 3, 5, 2}
            range = [7, 11]
    Output : 1
    There is only one triplet {2, 3, 5}
    having sum 10 in range [7, 11].
    
    Input : arr[] = {2, 7, 5, 3, 8, 4, 1, 9}
            range = [8, 16]
    Output : 36
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **naive** approach is to run three loops to consider all the triplets one by
one. Find the sum of each triplet and increment the count if the sum lies in a
given range [a, b].

Below is the implementation of above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count triplets with

// sum that lies in given range [a, b].

#include <bits/stdc++.h>

 

using namespace std;

 

// Function to count triplets

int countTriplets(int arr[], int n, int a, int b)

{

 // Initialize result

 int ans = 0;

 

 // Fix the first element as A[i]

 for (int i = 0; i < n - 2; i++) {

 

 // Fix the second element as A[j]

 for (int j = i + 1; j < n - 1; j++) {

 

 // Now look for the third number

 for (int k = j + 1; k < n; k++)

 

 if (arr[i] + arr[j] + arr[k] >= a

 && arr[i] + arr[j] + arr[k] <= b)

 ans++;

 }

 }

 

 return ans;

}

 

// Driver Code

int main()

{

 int arr[] = { 2, 7, 5, 3, 8, 4, 1, 9 };

 int n = sizeof arr / sizeof arr[0];

 int a = 8, b = 16;

 cout << countTriplets(arr, n, a, b) << endl;

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

// Java program to count triplets

// with sum that lies in given 

// range [a, b].

import java.util.*;

 

class GFG

{

 

// Function to count triplets

public static int countTriplets(int []arr, int n,

 int a, int b)

{

 // Initialize result

 int ans = 0;

 

 // Fix the first 

 // element as A[i]

 for (int i = 0; i < n - 2; i++)

 {

 

 // Fix the second 

 // element as A[j]

 for (int j = i + 1; j < n - 1; j++) 

 {

 

 // Now look for the

 // third number

 for (int k = j + 1; k < n; k++)

 {

 if (arr[i] + arr[j] + arr[k] >= a &&

 arr[i] + arr[j] + arr[k] <= b)

 {ans++;}

 }

 }

 }

 

 return ans;

}

 

// Driver Code

public static void main(String[] args)

{

 int[] arr = { 2, 7, 5, 3, 8, 4, 1, 9 };

 int n = arr.length;

 int a = 8, b = 16;

 System.out.println("" + countTriplets(arr, n, 

 a, b));

}

}

 

// This code is contributed 

// by Harshit Saini   
  
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

# Python3 program to count

# triplets with sum that 

# lies in given range [a, b].

 

# Function to count triplets

def countTriplets(arr, n, a, b):

 

 # Initialize result

 ans = 0

 

 # Fix the first 

 # element as A[i]

 for i in range(0, n - 2):

 

 # Fix the second 

 # element as A[j]

 for j in range(i + 1, n - 1):

 

 # Now look for 

 # the third number

 for k in range(j + 1, n):

 

 if ((arr[i] + arr[j] + arr[k] >= a) 

 and (arr[i] + arr[j] + arr[k] <= b)):

 ans += 1

 

 return ans

 

# Driver code

if __name__ == "__main__":

 

 arr = [ 2, 7, 5, 3, 8, 4, 1, 9 ]

 n = len(arr)

 a = 8; b = 16

 print(countTriplets(arr, n, a, b))

 

# This code is contributed 

# by Harshit Saini  
  
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

// C# program to count triplets

// with sum that lies in given 

// range [a, b].

using System;

 

class GFG

{

 

// Function to count triplets

public static int countTriplets(int []arr, int n,

 int a, int b)

{

 // Initialize result

 int ans = 0;

 

 // Fix the first 

 // element as A[i]

 for (int i = 0; 

 i < n - 2; i++)

 {

 

 // Fix the second 

 // element as A[j]

 for (int j = i + 1; 

 j < n - 1; j++) 

 {

 

 // Now look for the

 // third number

 for (int k = j + 1;

 k < n; k++)

 {

 if (arr[i] + arr[j] + arr[k] >= a &&

 arr[i] + arr[j] + arr[k] <= b)

 {ans++;}

 }

 }

 }

 

 return ans;

}

 

// Driver Code

public static void Main()

{

 int[] arr = {2, 7, 5, 3, 8, 4, 1, 9};

 int n = arr.Length;

 int a = 8, b = 16;

 Console.WriteLine("" + countTriplets(arr, n, 

 a, b));

}

}

 

// This code is contributed 

// by Akanksha Rai(Abby_akku)   
  
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

// PHP program to count triplets with

// sum that lies in given range [a, b].

 

// Function to count triplets

function countTriplets($arr, $n, $a, $b)

{

 // Initialize result

 $ans = 0;

 

 // Fix the first element as A[i]

 for ($i = 0; $i < $n - 2; $i++)

 {

 

 // Fix the second element as A[j]

 for ($j = $i + 1; $j < $n - 1; $j++) 

 {

 

 // Now look for the third number

 for ($k = $j + 1; $k < $n; $k++)

 

 if ($arr[$i] + $arr[$j] + $arr[$k] >= $a &&


 $arr[$i] + $arr[$j] + $arr[$k] <= $b)

 $ans++;

 }

 }

 

 return $ans;

}

 

// Driver Code

$arr = array( 2, 7, 5, 3, 8, 4, 1, 9 );

$n = sizeof($arr);

$a = 8; $b = 16;

echo countTriplets($arr, $n, $a, $b) . "\n";

 

// This code is contributed 

// by Akanksha Rai(Abby_akku)

?>  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    36
    

