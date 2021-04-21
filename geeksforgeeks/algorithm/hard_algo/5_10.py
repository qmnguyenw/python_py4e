Number of sub arrays with negative product



Given an array **arr[]** of **N** integers, the task is to find the count of
subarrays with negative product.

 **Examples:**

>  **Input:** arr[] = {-1, 2, -2}  
>  **Output:** 4  
> Subarray with negative product are {-1}, {-2}, {-1, 2} and {2, -2}.
>
>  **Input:** arr[] = {5, -4, -3, 2, -5}  
>  **Output:** 8

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

  * Replace the positive array elements with **1** and negative array elements with **-1**.
  * Create a prefix product array **pre[]** where **pre[i]** stores the product of all the elements from index **arr[0]** to **arr[i]**.
  * Now, it can be noted that the sub-array **arr[i…j]** has a negative product only if **pre[i] * pre[j]** is negative.
  * Hence, the total count of sub-arrays with negative product will be the product of the count positive and negative elements in the prefix product array.

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

 

// Function to return the count of

// subarrays with negative product

int negProdSubArr(int arr[], int n)

{

 int positive = 1, negative = 0;

 for (int i = 0; i < n; i++) {

 

 // Replace current element with 1

 // if it is positive else replace

 // it with -1 instead

 if (arr[i] > 0)

 arr[i] = 1;

 else

 arr[i] = -1;

 

 // Take product with previous element

 // to form the prefix product

 if (i > 0)

 arr[i] *= arr[i - 1];

 

 // Count positive and negative elements

 // in the prefix product array

 if (arr[i] == 1)

 positive++;

 else

 negative++;

 }

 

 // Return the required count of subarrays

 return (positive * negative);

}

 

// Driver code

int main()

{

 int arr[] = { 5, -4, -3, 2, -5 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << negProdSubArr(arr, n);

 

 return (0);

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

 

 // Function to return the count of 

 // subarrays with negative product 

 static int negProdSubArr(int arr[], int n) 

 { 

 int positive = 1, negative = 0; 

 for (int i = 0; i < n; i++) 

 { 

 

 // Replace current element with 1 

 // if it is positive else replace 

 // it with -1 instead 

 if (arr[i] > 0) 

 arr[i] = 1; 

 else

 arr[i] = -1; 

 

 // Take product with previous element 

 // to form the prefix product 

 if (i > 0) 

 arr[i] *= arr[i - 1]; 

 

 // Count positive and negative elements 

 // in the prefix product array 

 if (arr[i] == 1) 

 positive++; 

 else

 negative++; 

 } 

 

 // Return the required count of subarrays 

 return (positive * negative); 

 } 

 

 // Driver code 

 public static void main (String[] args) 

 { 

 int arr[] = { 5, -4, -3, 2, -5 }; 

 int n = arr.length; 

 

 System.out.println(negProdSubArr(arr, n)); 

 } 

}

 

// This code is contributed by AnkitRai01  
  
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

# subarrays with negative product

def negProdSubArr(arr, n):

 positive = 1

 negative = 0

 for i in range(n):

 

 # Replace current element with 1

 # if it is positive else replace

 # it with -1 instead

 if (arr[i] > 0):

 arr[i] = 1

 else:

 arr[i] = -1

 

 # Take product with previous element

 # to form the prefix product

 if (i > 0):

 arr[i] *= arr[i - 1]

 

 # Count positive and negative elements

 # in the prefix product array

 if (arr[i] == 1):

 positive += 1

 else:

 negative += 1

 

 # Return the required count of subarrays

 return (positive * negative)

 

# Driver code

arr = [5, -4, -3, 2, -5]

n = len(arr)

 

print(negProdSubArr(arr, n))

 

# This code is contributed by Mohit Kumar  
  
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

 // subarrays with negative product 

 static int negProdSubArr(int []arr, int n) 

 { 

 int positive = 1, negative = 0; 

 for (int i = 0; i < n; i++) 

 { 

 

 // Replace current element with 1 

 // if it is positive else replace 

 // it with -1 instead 

 if (arr[i] > 0) 

 arr[i] = 1; 

 else

 arr[i] = -1; 

 

 // Take product with previous element 

 // to form the prefix product 

 if (i > 0) 

 arr[i] *= arr[i - 1]; 

 

 // Count positive and negative elements 

 // in the prefix product array 

 if (arr[i] == 1) 

 positive++; 

 else

 negative++; 

 } 

 

 // Return the required count of subarrays 

 return (positive * negative); 

 } 

 

 // Driver code 

 static public void Main ()

 {

 int []arr = { 5, -4, -3, 2, -5 }; 

 int n = arr.Length; 

 

 Console.Write(negProdSubArr(arr, n)); 

 } 

}

 

// This code is contributed by Sachin.  
  
---  
  
 __

 __

 **Output:**

    
    
    8
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

