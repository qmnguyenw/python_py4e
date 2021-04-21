Number of subsequences with negative product



  
Given an array **arr[]** of **N** integers, the task is to find the count of
all the subsequences of the array that have a negative products.

 **Examples:**

>  **Input:** arr[] = {1, -5, -6}  
>  **Output:** 4  
>  **Explanation**  
>  {-5}, {-6}, {1, -5} and {1, -6} are the only possible subsequences
>
>  **Input:** arr[] = {2, 3, 1}  
>  **Output:** 0  
>  **Explanation**  
>  There is no such possible subsequence with negative product

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:**  
Generate all the subsequences of the array and compute the product of all the
subsequences. If the product is negative then increment the count by 1.

  

  

 **Efficient Approach:**

  * Count the number of positive and negative elements in the array
  * An odd number of negative elements can be chosen for the subsequence to maintain the negative product. The number of different combinations of subsequences with an odd number of negative elements will be **pow(2, count of negative elements – 1)**
  * Any number of positive elements can be chosen for the subsequence to maintain the negative product. The number of different combinations of subsequences with all the positive elements will be **pow(2, count of positive elements)**

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

 

// Function to return the count of all

// the subsequences with negative product

int cntSubSeq(int arr[], int n)

{

 // To store the count of positive

 // elements in the array

 int pos_count = 0;

 

 // To store the count of negative

 // elements in the array

 int neg_count = 0;

 

 int result;

 

 for (int i = 0; i < n; i++) {

 

 // If the current element

 // is positive

 if (arr[i] > 0)

 pos_count++;

 

 // If the current element

 // is negative

 if (arr[i] < 0)

 neg_count++;

 }

 

 // For all the positive

 // elements of the array

 result = pow(2, pos_count);

 

 // For all the negative

 // elements of the array

 if (neg_count > 0)

 result *= pow(2, neg_count - 1);

 else

 result = 0;

 

 return result;

}

 

// Driver code

int main()

{

 int arr[] = { 3, -4, -1, 6 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << cntSubSeq(arr, n);

 

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

 

// Function to return the count of all 

// the subsequences with negative product 

static int cntSubSeq(int arr[], int n) 

{ 

 // To store the count of positive 

 // elements in the array 

 int pos_count = 0; 

 

 // To store the count of negative 

 // elements in the array 

 int neg_count = 0; 

 

 int result; 

 

 for (int i = 0; i < n; i++) 

 { 

 

 // If the current element 

 // is positive 

 if (arr[i] > 0) 

 pos_count++; 

 

 // If the current element 

 // is negative 

 if (arr[i] < 0) 

 neg_count++; 

 } 

 

 // For all the positive 

 // elements of the array 

 result = (int) Math.pow(2, pos_count); 

 

 // For all the negative 

 // elements of the array 

 if (neg_count > 0) 

 result *= Math.pow(2, neg_count - 1); 

 else

 result = 0 ;

 

 return result; 

} 

 

// Driver code 

public static void main(String[] args) 

{ 

 int arr[] = { 3,-4, -1, 6 }; 

 int n = arr.length; 

 

 System.out.print(cntSubSeq(arr, n)); 

} 

} 

 

// This code is contributed by ANKITKUMAR34   
  
---  
  
__

__

## Python 3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 implementation of the approach

import math 

 

# Function to return the count of all 

# the subsequences with negative product 

def cntSubSeq(arr, n): 

 

 # To store the count of positive 

 # elements in the array 

 pos_count = 0; 

 

 # To store the count of negative 

 # elements in the array 

 neg_count = 0

 

 for i in range (n): 

 

 # If the current element 

 # is positive 

 if (arr[i] > 0) : 

 pos_count += 1

 

 # If the current element 

 # is negative 

 if (arr[i] < 0): 

 neg_count += 1

 

 # For all the positive 

 # elements of the array 

 result = int(math.pow(2, pos_count)) 

 

 # For all the negative 

 # elements of the array 

 if (neg_count > 0): 

 result *= int(math.pow(2, neg_count - 1)) 

 else:

 result = 0

 

 return result 

 

# Driver code 

arr = [ 2, -3, -1, 4 ] 

n = len (arr); 

 

print (cntSubSeq(arr, n))   
  
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

 

// Function to return the count of all 

// the subsequences with negative product 

static int cntSubSeq(int []arr, int n) 

{ 

 // To store the count of positive 

 // elements in the array 

 int pos_count = 0; 

 

 // To store the count of negative 

 // elements in the array 

 int neg_count = 0; 

 

 int result; 

 

 for (int i = 0; i < n; i++) 

 { 

 

 // If the current element 

 // is positive 

 if (arr[i] > 0) 

 pos_count++; 

 

 // If the current element 

 // is negative 

 if (arr[i] < 0) 

 neg_count++; 

 } 

 

 // For all the positive 

 // elements of the array 

 result = (int) Math.Pow(2, pos_count); 

 

 // For all the negative 

 // elements of the array 

 if (neg_count > 0) 

 result *= (int)Math.Pow(2, neg_count - 1); 

 else

 result = 0 ;

 

 return result; 

} 

 

// Driver code 

public static void Main(String[] args) 

{ 

 int []arr = { 3,-4, -1, 6 }; 

 int n = arr.Length; 

 

 Console.Write(cntSubSeq(arr, n)); 

} 

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    8
    

**Time Complexity:** O(n)

 **Another Approach:**  
We can also count the number of subsequences with a negative product by
subtracting **total number of subsequences with positive subsequences** from
**the total number of subsequences**.  
To find the total number of subsequences with a positive product using the
approach discussed in this article.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

