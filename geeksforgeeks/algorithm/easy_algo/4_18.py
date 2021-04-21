Maximum array sum that can be obtained after exactly k changes



Given an array **arr[]** of **n** integers and an integer **k**. The task is
to maximize the sum of the array after performing the given operation exactly
**k** times. In a single operation, any element of the array can be multiplies
by **-1** i.e. the sign of the element can be changed.

 **Examples:**

>  **Input:** arr[] = {-5, 4, 1, 3, 2}, k = 4  
>  **Output:** 13  
> Change the sign of -5 once and then change the sign of 1 three times.  
> Thus it changes to -1 and the sum will be 5 + 4 + (-1) + 3 + 2 = 13.
>
>  **Input:** arr[] = {-1, -1, 1}, k = 1  
>  **Output:** 1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** If the count of negative elements in the array is **count** ,

  

  

  1. If **count ≥ k** then the sign of exactly **k** negative numbers will be changed starting from the smallest.
  2. If **count < k** then change the sign of all the negative elements to positive and for the remaining operations i.e. **rem = k – count** ,
    * If **rem % 2 = 0** then no changes will be done to the current array as changing the sign of an element twice gives the original number.
    * If **rem % 2 = 1** then change the sign of the smallest element from the updated array.
  3. Finally, print the sum of the elements of the updated array.

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

 

// Utility function to return the sum

// of the array elements

int sumArr(int arr[], int n)

{

 int sum = 0;

 for (int i = 0; i < n; i++)

 sum += arr[i];

 

 return sum;

}

 

// Function to return the maximized sum

// of the array after performing

// the given operation exactly k times

int maxSum(int arr[], int n, int k)

{

 // Sort the array elements

 sort(arr, arr + n);

 

 int i = 0;

 // Change signs of the negative elements

 // starting from the smallest

 while (i < n && k > 0 && arr[i] < 0) {

 arr[i] *= -1;

 k--;

 i++;

 }

 

 // If a single operation has to be

 // performed then it must be performed

 // on the smallest positive element

 if (k % 2 == 1) {

 

 // To store the index of the

 // minimum element

 int min = 0;

 for (i = 1; i < n; i++)

 

 // Update the minimum index

 if (arr[min] > arr[i])

 min = i;

 

 // Perform remaining operation

 // on the smallest element

 arr[min] *= -1;

 }

 

 // Return the sum of the updated array

 return sumArr(arr, n);

}

 

// Driver code

int main()

{

 int arr[] = { -5, 4, 1, 3, 2 };

 int n = sizeof(arr) / sizeof(arr[0]);

 int k = 4;

 

 cout << maxSum(arr, n, k) << endl;

 

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

// Java implementation of the above approach

import java.util.Arrays;

 

class GFG 

{

 

// Utility function to return the sum

// of the array elements

static int sumArr(int arr[], int n)

{

 int sum = 0;

 for (int i = 0; i < n; i++)

 sum += arr[i];

 

 return sum;

}

 

// Function to return the maximized sum

// of the array after performing

// the given operation exactly k times

static int maxSum(int arr[], int n, int k)

{

 // Sort the array elements

 Arrays.sort(arr);

 

 int i = 0;

 

 // Change signs of the negative elements

 // starting from the smallest

 while (i < n && k > 0 && arr[i] < 0)

 {

 arr[i] *= -1;

 k--;

 i++;

 }

 

 // If a single operation has to be

 // performed then it must be performed

 // on the smallest positive element

 if (k % 2 == 1) 

 {

 

 // To store the index of the

 // minimum element

 int min = 0;

 for (i = 1; i < n; i++)

 

 // Update the minimum index

 if (arr[min] > arr[i])

 min = i;

 

 // Perform remaining operation

 // on the smallest element

 arr[min] *= -1;

 }

 

 // Return the sum of the updated array

 return sumArr(arr, n);

}

 

// Driver code

public static void main(String[] args)

{

 int arr[] = { -5, 4, 1, 3, 2 };

 int n = arr.length;

 int k = 4;

 

 System.out.println(maxSum(arr, n, k));

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

# Python 3 implementation of the approach

 

# Utility function to return the sum

# of the array elements

def sumArr(arr, n):

 sum = 0

 for i in range(n):

 sum += arr[i]

 

 return sum

 

# Function to return the maximized sum

# of the array after performing

# the given operation exactly k times

def maxSum(arr, n, k):

 

 # Sort the array elements

 arr.sort(reverse = False)

 

 i = 0

 

 # Change signs of the negative elements

 # starting from the smallest

 while (i < n and k > 0 and arr[i] < 0):

 arr[i] *= -1

 k -= 1

 i += 1

 

 # If a single operation has to be

 # performed then it must be performed

 # on the smallest positive element

 if (k % 2 == 1):

 

 # To store the index of the

 # minimum element

 min = 0

 for i in range(1, n):

 

 # Update the minimum index

 if (arr[min] > arr[i]):

 min = i

 

 # Perform remaining operation

 # on the smallest element

 arr[min] *= -1

 

 # Return the sum of the updated array

 return sumArr(arr, n)

 

# Driver code

if __name__ == '__main__':

 arr = [-5, 4, 1, 3, 2]

 n = len(arr)

 k = 4

 

 print(maxSum(arr, n, k))

 

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

// C# implementation of the above approach

using System; 

using System.Linq; 

 

class GFG 

{ 

 

// Utility function to return the sum 

// of the array elements 

static int sumArr(int [] arr, int n) 

{ 

 int sum = 0; 

 for (int i = 0; i < n; i++) 

 sum += arr[i]; 

 

 return sum; 

} 

 

// Function to return the maximized sum 

// of the array after performing 

// the given operation exactly k times 

static int maxSum(int [] arr, int n, int k) 

{ 

 // Sort the array elements 

 Array.Sort(arr); 

 

 int i = 0; 

 

 // Change signs of the negative elements 

 // starting from the smallest 

 while (i < n && k > 0 && arr[i] < 0) 

 { 

 arr[i] *= -1; 

 k--; 

 i++; 

 } 

 

 // If a single operation has to be 

 // performed then it must be performed 

 // on the smallest positive element 

 if (k % 2 == 1) 

 { 

 

 // To store the index of the 

 // minimum element 

 int min = 0; 

 for (i = 1; i < n; i++) 

 

 // Update the minimum index 

 if (arr[min] > arr[i]) 

 min = i; 

 

 // Perform remaining operation 

 // on the smallest element 

 arr[min] *= -1; 

 } 

 

 // Return the sum of the updated array 

 return sumArr(arr, n); 

} 

 

// Driver code 

static void Main() 

{ 

 int []arr= { -5, 4, 1, 3, 2 }; 

 int n = arr.Length; 

 int k = 4; 

 

 Console.WriteLine(maxSum(arr, n, k)); 

} 

} 

 

// This code is contributed by mohit kumar 29  
  
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

 

// Utility function to return the sum

// of the array elements

function sumArr($arr, $n)

{

 $sum = 0;

 for ($i = 0; $i < $n; $i++)

 $sum += $arr[$i];

 

 return $sum;

}

 

// Function to return the maximized sum

// of the array after performing

// the given operation exactly k times

function maxSum($arr, $n, $k)

{

 // Sort the array elements

 sort($arr);

 

 $i = 0;

 // Change signs of the negative elements

 // starting from the smallest

 while ($i < $n && $k > 0 &&

 $arr[$i] < 0)

 {

 $arr[$i] *= -1;

 $k--;

 $i++;

 }

 

 // If a single operation has to be

 // performed then it must be performed

 // on the smallest positive element

 if ($k % 2 == 1) 

 {

 

 // To store the index of the

 // minimum element

 $min = 0;

 for ($i = 1; $i < $n; $i++)

 

 // Update the minimum index

 if ($arr[$min] > $arr[$i])

 $min = $i;

 

 // Perform remaining operation

 // on the smallest element

 $arr[$min] *= -1;

 }

 

 // Return the sum of the updated array

 return sumArr($arr, $n);

}

 

// Driver code

$arr = array( -5, 4, 1, 3, 2 );

$n = sizeof($arr);

$k = 4;

 

echo maxSum($arr, $n, $k), "\n";

 

// This code is contributed by ajit.

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    13
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

