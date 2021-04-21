Divide array into two parts with equal sum according to the given constraints



Given an array **arr[]** of **N** integers, the task is to select an integer
**x** (which may or may not be present in the array) and remove all of its
occurrences from the array and divide the remaining array into two non-empty
sub-sets such that:

  1. The elements of the first set are strictly smaller than **x**.
  2. The elements of the second set are strictly greater than **x**.
  3. The sum of the elements of both the sets is equal.If such an integer exists then print **Yes** otherwise print **No**.

 **Examples:**

>  **Input:** arr[] = {1, 2, 2, 5}  
>  **Output:** Yes  
> Choose x = 3, after removing all of its occurrences the array becomes arr[]
> = {1, 2, 2, 5}  
> {1, 2, 2} and {5} are the required sub-sets.
>
>  **Input:** arr[] = {2, 1}  
>  **Output:** No
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to first sort the array and for all the numbers
lying between 1 to maximum number present in the array, apply binary search
and check if on removing all its occurrences from the array, sum of elements
present on its left side (which are smaller than it) and sum of elements
present on the right side (which are greater than it) is equal.

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

 

// Function that checks if the given

// conditions are satisfied

void IfExists(int arr[], int n)

{

 // To store the prefix sum

 // of the array elements

 int sum[n];

 

 // Sort the array

 sort(arr, arr + n);

 

 sum[0] = arr[0];

 

 // Compute the prefix sum array

 for (int i = 1; i < n; i++)

 sum[i] = sum[i - 1] + arr[i];

 

 // Maximum element in the array

 int max = arr[n - 1];

 

 // Variable to check if there exists any number

 bool flag = false;

 

 for (int i = 1; i <= max; i++) {

 

 // Stores the index of the largest

 // number present in the array

 // smaller than i

 int findex = 0;

 

 // Stores the index of the smallest

 // number present in the array

 // greater than i

 int lindex = 0;

 

 int l = 0;

 int r = n - 1;

 

 // Find index of smallest number

 // greater than i

 while (l <= r) {

 int m = (l + r) / 2;

 

 if (arr[m] < i) {

 findex = m;

 l = m + 1;

 }

 else

 r = m - 1;

 }

 

 l = 1;

 r = n;

 flag = false;

 

 // Find index of smallest number

 // greater than i

 while (l <= r) {

 int m = (r + l) / 2;

 

 if (arr[m] > i) {

 lindex = m;

 r = m - 1;

 }

 else

 l = m + 1;

 }

 

 // If there exists a number

 if (sum[findex] == sum[n - 1] - sum[lindex - 1]) {

 flag = true;

 break;

 }

 }

 

 // If no such number exists

 // print no

 if (flag)

 cout << "Yes";

 else

 cout << "No";

}

 

// Driver code

int main()

{

 int arr[] = { 1, 2, 2, 5 };

 int n = sizeof(arr) / sizeof(int);

 IfExists(arr, n);

 

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

 

// Function that checks if the given 

// conditions are satisfied 

static void IfExists(int arr[], int n) 

{ 

 // To store the prefix sum 

 // of the array elements 

 int sum[] = new int[n]; 

 

 // Sort the array 

 Arrays.sort(arr); 

 

 sum[0] = arr[0]; 

 

 // Compute the prefix sum array 

 for (int i = 1; i < n; i++) 

 sum[i] = sum[i - 1] + arr[i]; 

 

 // Maximum element in the array 

 int max = arr[n - 1]; 

 

 // Variable to check if there exists any number 

 boolean flag = false; 

 

 for (int i = 1; i <= max; i++) 

 { 

 

 // Stores the index of the largest 

 // number present in the array 

 // smaller than i 

 int findex = 0; 

 

 // Stores the index of the smallest 

 // number present in the array 

 // greater than i 

 int lindex = 0; 

 

 int l = 0; 

 int r = n - 1; 

 

 // Find index of smallest number 

 // greater than i 

 while (l <= r) 

 { 

 int m = (l + r) / 2; 

 

 if (arr[m] < i) 

 { 

 findex = m; 

 l = m + 1; 

 } 

 else

 r = m - 1; 

 } 

 

 l = 1; 

 r = n; 

 flag = false; 

 

 // Find index of smallest number 

 // greater than i 

 while (l <= r) 

 { 

 int m = (r + l) / 2; 

 

 if (arr[m] > i) 

 { 

 lindex = m; 

 r = m - 1; 

 } 

 else

 l = m + 1; 

 } 

 

 // If there exists a number 

 if (sum[findex] == sum[n - 1] - sum[lindex - 1]) 

 { 

 flag = true; 

 break; 

 } 

 } 

 

 // If no such number exists 

 // print no 

 if (flag) 

 System.out.println("Yes"); 

 else

 System.out.println("No"); 

} 

 

// Driver code 

public static void main(String args[])

{ 

 int arr[] = { 1, 2, 2, 5 }; 

 int n = arr.length; 

 IfExists(arr, n); 

}

} 

 

// This code is contributed by Arnab Kundu  
  
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

 

# Function that checks if the given 

# conditions are satisfied 

def IfExists(arr, n) :

 

 # To store the prefix sum 

 # of the array elements 

 sum = [0] * n; 

 

 # Sort the array 

 arr.sort(); 

 

 sum[0] = arr[0]; 

 

 # Compute the prefix sum array 

 for i in range(1, n) : 

 sum[i] = sum[i - 1] + arr[i]; 

 

 # Maximum element in the array 

 max = arr[n - 1]; 

 

 # Variable to check if there 

 # exists any number 

 flag = False; 

 

 for i in range(1, max + 1) :

 

 # Stores the index of the largest 

 # number present in the array 

 # smaller than i 

 findex = 0; 

 

 # Stores the index of the smallest 

 # number present in the array 

 # greater than i 

 lindex = 0; 

 

 l = 0; 

 r = n - 1; 

 

 # Find index of smallest number 

 # greater than i 

 while (l <= r) :

 m = (l + r) // 2; 

 

 if (arr[m] < i) :

 findex = m; 

 l = m + 1; 

 

 else :

 r = m - 1; 

 

 l = 1; 

 r = n; 

 flag = False; 

 

 # Find index of smallest number 

 # greater than i 

 while (l <= r) : 

 m = (r + l) // 2; 

 

 if (arr[m] > i) : 

 lindex = m; 

 r = m - 1; 

 

 else :

 l = m + 1; 

 

 # If there exists a number 

 if (sum[findex] == sum[n - 1] -

 sum[lindex - 1]) : 

 flag = True; 

 break; 

 

 # If no such number exists 

 # print no 

 if (flag) : 

 print("Yes"); 

 else :

 print("No"); 

 

# Driver code 

if __name__ == "__main__" : 

 

 arr = [ 1, 2, 2, 5 ]; 

 

 n = len(arr) ;

 IfExists(arr, n); 

 

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

 

// Function that checks if the given 

// conditions are satisfied 

static void IfExists(int[] arr, int n) 

{ 

 // To store the prefix sum 

 // of the array elements 

 int[] sum = new int[n]; 

 

 // Sort the array 

 Array.Sort(arr); 

 

 sum[0] = arr[0]; 

 

 // Compute the prefix sum array 

 for (int i = 1; i < n; i++) 

 sum[i] = sum[i - 1] + arr[i]; 

 

 // Maximum element in the array 

 int max = arr[n - 1]; 

 

 // Variable to check if there exists any number 

 bool flag = false; 

 

 for (int i = 1; i <= max; i++) 

 { 

 

 // Stores the index of the largest 

 // number present in the array 

 // smaller than i 

 int findex = 0; 

 

 // Stores the index of the smallest 

 // number present in the array 

 // greater than i 

 int lindex = 0; 

 

 int l = 0; 

 int r = n - 1; 

 

 // Find index of smallest number 

 // greater than i 

 while (l <= r) 

 { 

 int m = (l + r) / 2; 

 

 if (arr[m] < i) 

 { 

 findex = m; 

 l = m + 1; 

 } 

 else

 r = m - 1; 

 } 

 

 l = 1; 

 r = n; 

 flag = false; 

 

 // Find index of smallest number 

 // greater than i 

 while (l <= r) 

 { 

 int m = (r + l) / 2; 

 

 if (arr[m] > i) 

 { 

 lindex = m; 

 r = m - 1; 

 } 

 else

 l = m + 1; 

 } 

 

 // If there exists a number 

 if (sum[findex] == sum[n - 1] - sum[lindex - 1]) 

 { 

 flag = true; 

 break; 

 } 

 } 

 

 // If no such number exists 

 // print no 

 if (flag) 

 Console.WriteLine("Yes"); 

 else

 Console.WriteLine("No"); 

} 

 

// Driver code 

public static void Main()

{ 

 int[] arr = { 1, 2, 2, 5 }; 

 int n = arr.Length; 

 IfExists(arr, n); 

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

// PHP implementation of the approach

 

// Function that checks if the given

// conditions are satisfied

function IfExists($arr, $n)

{

 // To store the prefix $sum

 // of the array elements

 $sum = array_fill(0, $n, 0);

 

 // Sort the array

 sort($arr);

 

 $sum[0] = $arr[0];

 

 // Compute the prefix sum array

 for ($i = 1; $i < $n; $i++)

 $sum[$i] = $sum[$i - 1] + $arr[$i];

 

 // Maximum element in the array

 $max = $arr[$n - 1];

 

 // Variable to check if there exists any number

 $flag = false;

 

 for ($i = 1; $i <= $max; $i++) 

 {

 

 // Stores the index of the largest

 // number present in the array

 // smaller than i

 $findex = 0;

 

 // Stores the index of the smallest

 // number present in the array

 // greater than i

 $lindex = 0;

 

 $l = 0;

 $r = $n - 1;

 

 // Find index of smallest number

 // greater than i

 while ($l <= $r) 

 {

 $m = ($l + $r) / 2; 

 if ($arr[$m] < $i) 

 {

 $findex = $m;

 $l = $m + 1;

 }

 else

 $r = $m - 1;

 }

 

 $l = 1;

 $r = $n;

 $flag = false;

 

 // Find index of smallest number

 // greater than i

 while ($l <= $r)

 {

 $m = ($r + $l) / 2;

 

 if ($arr[$m] > $i) 

 {

 $lindex = $m;

 $r = $m - 1;

 }

 else

 $l = $m + 1;

 }

 

 // If there exists a number

 if ($sum[$findex] == $sum[$n - 1] -

 $sum[$lindex - 1])

 {

 $flag = true;

 break;

 }

 }

 

 // If no such number exists

 // print no

 if ($flag == true)

 echo "Yes";

 else

 echo "No";

}

 

// Driver code

$arr = array(1, 2, 2, 5 );

$n = sizeof($arr);

IfExists($arr, $n);

 

// This code is contributed by ihritik

?>  
  
---  
  
 __

 __

 **Output:**

        
        
        Yes
        

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

