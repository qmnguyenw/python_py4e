Maximum length of subarray such that all elements are equal in the subarray



Given an array **arr[]** of N integers, the task is to find the maximum length
subarray that contains similar elements.  
 **Examples:**  

> **Input:** arr[] = {1, 2, 3, 4, 5, 5, 5, 5, 5, 2, 2, 1, 1}  
> **Output:** 5  
> **Explanation:**  
> The subarray {5, 5, 5, 5, 5} has maximum length 5 with identical elements.  
>  **Input:** arr[] = {1, 2, 3, 4}  
> **Output:** 1  
> **Explanation:**  
> All identical element subarray are {1}, {2}, {3}, and {4} which is of length
> 1.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to traverse the array store the **maximum length**
and **current length** of the subarray which has the same elements. Below are
the steps:  

  1. Traverse the array and check if the current element is equal to the next element then increase the value of the current length variable.
  2. Now, compare the current length with max length to update the maximum length of the subarray.
  3. If the current element is not equal to the next element then reset the length to **1** and continue this for all the elements of the array.

Below is the implementation of the above approach:  

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

#include <iostream>

using namespace std;

// Function to find the longest

// subarray with same element

int longest_subarray(int arr[], int d)

{

 int i = 0, j = 1, e = 0;

 for (i = 0; i < d - 1; i++) {

 // Check if the elements

 // are same then we can

 // increment the length

 if (arr[i] == arr[i + 1]) {

 j = j + 1;

 }

 else {

 // Reinitialize j

 j = 1;

 }

 // Compare the maximum

 // length e with j

 if (e < j) {

 e = j;

 }

 }

 // Return max length

 return e;

}

// Driver Code

int main()

{

 // Given array arr[]

 int arr[] = { 1, 2, 3, 4 };

 int N = sizeof(arr) / sizeof(arr[0]);

 // Function Call

 cout << longest_subarray(arr, N);

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

// Java program for the above approach

import java.util.*;

class GFG{

// Function to find the longest

// subarray with same element

static int longest_subarray(int arr[], int d)

{

 int i = 0, j = 1, e = 0;

 for(i = 0; i < d - 1; i++)

 {

 

 // Check if the elements

 // are same then we can

 // increment the length

 if (arr[i] == arr[i + 1])

 {

 j = j + 1;

 }

 else

 {

 

 // Reinitialize j

 j = 1;

 }

 

 // Compare the maximum

 // length e with j

 if (e < j)

 {

 e = j;

 }

 }

 // Return max length

 return e;

}

// Driver Code

public static void main(String[] args)

{

 

 // Given array arr[]

 int arr[] = { 1, 2, 3, 4 };

 int N = arr.length;

 // Function Call

 System.out.print(longest_subarray(arr, N));

}

}

// This code is contributed by 29AjayKumar  
  
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

# Python3 program for the above approach

# Function to find the longest

# subarray with same element

def longest_subarray(arr, d):

 

 (i, j, e) = (0, 1, 0)

 

 for i in range(d - 1):

 

 # Check if the elements

 # are same then we can

 # increment the length

 if arr[i] == arr[i + 1]:

 j += 1

 else:

 

 # Reinitialize j

 j = 1

 

 # Compare the maximum

 # length e with j

 if e < j:

 e = j

 

 # Return max length

 return e

# Driver code

# Given list arr[]

arr = [ 1, 2, 3, 4 ]

N = len(arr)

# Function call

print(longest_subarray(arr, N))

# This code is contributed by rutvik_56  
  
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

// C# program for the above approach

using System;

class GFG{

 

// Function to find the longest

// subarray with same element

static int longest_subarray(int []arr, int d)

{

 int i = 0, j = 1, e = 0;

 

 for(i = 0; i < d - 1; i++)

 {

 

 // Check if the elements

 // are same then we can

 // increment the length

 if (arr[i] == arr[i + 1])

 {

 j = j + 1;

 }

 else

 {

 

 // Reinitialize j

 j = 1;

 }

 

 // Compare the maximum

 // length e with j

 if (e < j)

 {

 e = j;

 }

 }

 

 // Return max length

 return e;

}

 

// Driver Code

public static void Main(String[] args)

{

 

 // Given array []arr

 int []arr = { 1, 2, 3, 4 };

 int N = arr.Length;

 

 // Function Call

 Console.Write(longest_subarray(arr, N));

}

}

// This code is contributed by 29AjayKumar  
  
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

// javascript program for the above approach

 // Function to find the longest

 // subarray with same element

 function longest_subarray(arr , d)

 {

 var i = 0, j = 1, e = 0;

 for (i = 0; i < d - 1; i++)

 {

 // Check if the elements

 // are same then we can

 // increment the length

 if (arr[i] == arr[i + 1])

 {

 j = j + 1;

 }

 else

 {

 // Reinitialize j

 j = 1;

 }

 // Compare the maximum

 // length e with j

 if (e < j) {

 e = j;

 }

 }

 // Return max length

 return e;

 }

 // Driver Code

 

 // Given array arr

 var arr = [ 1, 2, 3, 4 ];

 var N = arr.length;

 // Function Call

 document.write(longest_subarray(arr, N));

// This code is contributed by todaysgaurav

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    1

**Time Complexity:** _O(N)_  
**Auxiliary Space:** _O(1)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

