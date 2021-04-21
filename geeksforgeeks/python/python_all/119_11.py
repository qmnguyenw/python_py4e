Reduce every element of the array to it’s half retaining the sum zero



Given an array **arr[]** of **N** integers with total element sum equal to
zero. The task is to reduce every element to it’s half such that the total sum
remain zero. For every odd element **X** in the array, it could be reduced to
either **(X + 1) / 2** or **(X – 1) / 2**.

 **Examples:**

>  **Input:** arr[] = {-7, 14, -7}  
>  **Output:** -4 7 -3  
> -4 + 7 -3 = 0
>
>  **Input:** arr[] = {-14, 14}  
>  **Output:** -7 7

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** All the even elements could be divided by 2 but for odd
elements, they have to be alternatively reduced to **(X + 1) / 2** and **(X –
1) / 2** in order to retain the original sum (i.e. 0) in the final array.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include<bits/stdc++.h>

using namespace std;

 

// Function to reduce every 

// element to it's half such that 

// the total sum remain zero

void half(int arr[], int n)

{ 

 int i;

 

 // Flag to swith between alternating 

 // odd numbers in the array 

 int flag = 0;

 

 // For every element of the array 

 for (i = 0; i < n; i++)

 { 

 

 // If its even then reduce it to half 

 if (arr[i] % 2 == 0 ) 

 cout << arr[i] / 2 << " ";

 

 // If its odd 

 else

 {

 

 // Reduce the odd elements 

 // alternatively 

 if (flag == 0)

 {

 cout << arr[i] / 2 - 1 << " ";

 

 // Switch flag 

 flag = 1;

 }

 else

 {

 int q = arr[i] / 2;

 cout<<q <<" ";

 

 // Switch flag 

 flag = 0;

 }

 }

 }

}

 

// Driver code 

int main () 

{

 int arr[] = {-7, 14, -7};

 int len = sizeof(arr)/sizeof(arr[0]);

 half(arr, len) ;

 return 0;

}

 

// This code is contributed by Rajput-Ji  
  
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

class GFG 

{

 

// Function to reduce every 

// element to it's half such that 

// the total sum remain zero 

static void half(int arr[], int n)

{ 

 int i;

 

 // Flag to swith between alternating 

 // odd numbers in the array 

 int flag = 0;

 

 // For every element of the array 

 for (i = 0; i < n; i++)

 { 

 

 // If its even then reduce it to half 

 if (arr[i] % 2 == 0 ) 

 System.out.print(arr[i] / 2 + " ");

 

 // If its odd 

 else

 {

 

 // Reduce the odd elements 

 // alternatively 

 if (flag == 0)

 {

 System.out.print(arr[i] / 2 - 1 + " ");

 

 // Switch flag 

 flag = 1;

 }

 else

 {

 int q = arr[i] / 2;

 System.out.print(q + " ");

 

 // Switch flag 

 flag = 0;

 }

 }

 }

}

 

// Driver code 

public static void main (String[] args) 

{

 int arr[] = {-7, 14, -7};

 int len = arr.length;

 half(arr, len) ;

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

 

# Function to reduce every

# element to it's half such that 

# the total sum remain zero

def half(arr, n) :

 

 # Flag to swith between alternating 

 # odd numbers in the array

 flag = 0

 

 # For every element of the array

 for i in range(n):

 

 # If its even then reduce it to half

 if arr[i] % 2 == 0 :

 print(arr[i]//2, end =" ")

 

 # If its odd

 else :

 

 # Reduce the odd elements 

 # alternatively

 if flag == 0:

 print(arr[i]//2, end =" ")

 

 # Switch flag

 flag = 1

 else :

 q = arr[i]//2

 q+= 1

 print(q, end =" ")

 

 # Switch flag

 flag = 0

 

# Driver code

arr = [-7, 14, -7]

half(arr, len(arr))  
  
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

 

class GFG 

{

 

// Function to reduce every 

// element to it's half such that 

// the total sum remain zero 

static void half(int []arr, int n)

{ 

 int i;

 

 // Flag to swith between alternating 

 // odd numbers in the array 

 int flag = 0;

 

 // For every element of the array 

 for (i = 0; i < n; i++)

 { 

 

 // If its even then reduce it to half 

 if (arr[i] % 2 == 0 ) 

 Console.Write(arr[i] / 2 + " ");

 

 // If its odd 

 else

 {

 

 // Reduce the odd elements 

 // alternatively 

 if (flag == 0)

 {

 Console.Write(arr[i] / 2 - 1 + " ");

 

 // Switch flag 

 flag = 1;

 }

 else

 {

 int q = arr[i] / 2;

 Console.Write(q + " ");

 

 // Switch flag 

 flag = 0;

 }

 }

 }

}

 

// Driver code 

public static void Main () 

{

 int [] arr = {-7, 14, -7};

 int len = arr.Length;

 half(arr, len) ;

}

}

 

// This code is contributed by mohit kumar 29  
  
---  
  
 __

 __

 **Output:**

    
    
    -4 7 -3
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

