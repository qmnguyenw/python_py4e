Sort an Array which contain 1 to N values in O(N) using Cycle Sort



 **Prerequisite:** Cycle Sort  
Given an array **arr[]** of elements from **1 to N** , the task is to sort the
given array in **O(N)** time.  
 **Examples:**

> **Input:** arr[] = { 2, 1, 5, 4, 3}  
> **Output:** 1 2 3 4 5  
> **Explanation:**  
> Since arr[0] = 2 is not at correct position, then swap arr[0] with
> arr[arr[0] – 1]  
> Now array becomes: arr[] = {1, 2, 5, 4, 3}  
> Now arr[2] = 5 is not at correct position, then swap arr[3] with arr[arr[3]
> – 1]  
> Now the array becomes: arr[] = {1, 2, 3, 4, 5}  
> Now the array is sorted.  
>  **Input:** arr[] = {1, 2, 3, 4, 5, 6}  
> **Output:** 1 2 3 4 5 6  
> **Explanation:**  
> The array is already sorted.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** This problem can be solved using Greedy Approach. Below are the
steps:

  * Traverse the given array **arr[]**.
  * If the current element is not at the correct position i.e., **arr[i] is not equal to i+1** then, swap the current element with the element with its correct position.   
**For Example:**  

> Let arr[] = {2, 1, 4, 5, 3}  
> Since, arr[0] = 2, which is not at it’s correct position 1.  
> Then swap this element with it’s correct position, i.e., swap(arr[0],
> arr[2-1])  
> Then array becomes: arr[] = {1, 2, 4, 5, 3}  
>

  * If the current element is at the correct position then check for the next element.
  * Repeat the above steps until we reach the end of the array.

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

#include "bits/stdc++.h"

using namespace std;

// Function to swap two a & b value

void swap(int* a, int* b)

{

 int temp = *a;

 *a = *b;

 *b = temp;

}

// Function to print array element

void printArray(int arr[], int N)

{

 // Traverse the array

 for (int i = 0; i < N; i++) {

 cout << arr[i] << ' ';

 }

}

// Function to sort the array in O(N)

void sortArray(int arr[], int N)

{

 // Traverse the array

 for (int i = 0; i < N;) {

 // If the current element is

 // at correct position

 if (arr[i] == i + 1) {

 i++;

 }

 // Else swap the current element

 // with it's correct position

 else {

 swap(&arr;[i], &arr;[arr[i] - 1]);

 }

 }

}

// Driver Code

int main()

{

 int arr[] = { 2, 1, 5, 3, 4 };

 int N = sizeof(arr) / sizeof(arr[0]);

 // Function call to sort the array

 sortArray(arr, N);

 // Function call to print the array

 printArray(arr, N);

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

// Java program for the above approach

class Main{

 

// Function to print array element

public static void printArray(int arr[], int N)

{

 

 // Traverse the array

 for(int i = 0; i < N; i++)

 {

 System.out.print(arr[i] + " ");

 }

}

 

// Function to sort the array in O(N)

public static void sortArray(int arr[], int N)

{

 // Traverse the array

 for(int i = 0; i < N;)

 {

 // If the current element is

 // at correct position

 if (arr[i] == i + 1)

 {

 i++;

 }

 

 // Else swap the current element

 // with it's correct position

 else

 {

 // Swap the value of

 // arr[i] and arr[arr[i]-1]

 int temp1 = arr[i];

 int temp2 = arr[arr[i] - 1];

 arr[i] = temp2;

 arr[temp1 - 1] = temp1;

 }

 }

}

// Driver Code 

public static void main(String[] args)

{

 int arr[] = { 2, 1, 5, 3, 4 };

 int N = arr.length;

 // Function call to sort the array

 sortArray(arr, N);

 // Function call to print the array

 printArray(arr, N);

}

}

// This code is contributed by divyeshrabadiya07  
  
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

# Function to print array element

def printArray(arr, N):

 

 # Traverse the array

 for i in range(N):

 print(arr[i], end = ' ')

 

# Function to sort the array in O(N)

def sortArray(arr, N):

 

 i = 0

 

 # Traverse the array

 while i < N:

 

 # If the current element is

 # at correct position

 if arr[i] == i + 1:

 i += 1

 

 # Else swap the current element

 # with it's correct position

 else:

 

 # Swap the value of

 # arr[i] and arr[arr[i]-1]

 temp1 = arr[i]

 temp2 = arr[arr[i] - 1]

 arr[i] = temp2

 arr[temp1 - 1] = temp1

 

# Driver code

if __name__=='__main__':

 

 arr = [ 2, 1, 5, 3, 4 ]

 N = len(arr)

 

 # Function call to sort the array

 sortArray(arr, N)

 

 # Function call to print the array

 printArray(arr, N)

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

 

// Function to print array element

public static void printArray(int []arr, int N)

{ 

 // Traverse the array

 for(int i = 0; i < N; i++)

 {

 Console.Write(arr[i] + " ");

 }

}

 

// Function to sort the array in O(N)

public static void sortArray(int []arr, int N)

{

 // Traverse the array

 for(int i = 0; i < N; )

 {

 // If the current element is

 // at correct position

 if (arr[i] == i + 1)

 {

 i++;

 }

 

 // Else swap the current element

 // with it's correct position

 else

 {

 // Swap the value of

 // arr[i] and arr[arr[i]-1]

 int temp1 = arr[i];

 int temp2 = arr[arr[i] - 1];

 arr[i] = temp2;

 arr[temp1 - 1] = temp1;

 }

 }

}

// Driver Code 

public static void Main(String[] args)

{

 int []arr = {2, 1, 5, 3, 4};

 int N = arr.Length;

 // Function call to sort the array

 sortArray(arr, N);

 // Function call to print the array

 printArray(arr, N);

}

}

// This code is contributed by shikhasingrajput  
  
---  
  
 __

 __

 **Output:**

    
    
    1 2 3 4 5
    
    
    
    

_**Time Complexity:** O(N)_, where N is the length of the array.  
_**Auxiliary Space:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

