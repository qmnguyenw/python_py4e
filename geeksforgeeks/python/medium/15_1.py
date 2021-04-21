Print all the peaks and troughs in an Array of Integers



Given an array of integers **arr[]** , the task is to print a list of all the
peaks and another list of all the troughs present in the array. A peak is an
element in the array which is greater than its neighbouring elements.
Similarly, a trough is an element which is smaller than its neighbouring
elements.

 **Examples:**

>  **Input:** arr[] = {5, 10, 5, 7, 4, 3, 5}  
>  **Output:**  
>  Peaks : 10 7 5  
> Troughs : 5 5 3
>
>  **Input:** arr[] = {1, 2, 3, 4, 5}  
>  **Output:**  
>  Peaks : 5  
> Troughs : 1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** For every element of the array, check whether the current
element is a peak (the element has to be greater than its neighbouring
elements) or a trough (the element has to be smaller than its neighbouring
elements).  
 **Note** that the first and the last element of the array will have a single
neighbour.

  

  

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

#include <iostream>

using namespace std;

 

// Function that returns true if num is

// greater than both arr[i] and arr[j]

static bool isPeak(int arr[], int n, int num,

 int i, int j)

{

 

 // If num is smaller than the element

 // on the left (if exists)

 if (i >= 0 && arr[i] > num)

 return false;

 

 // If num is smaller than the element

 // on the right (if exists)

 if (j < n && arr[j] > num)

 return false;

 return true;

}

 

// Function that returns true if num is

// smaller than both arr[i] and arr[j]

static bool isTrough(int arr[], int n, int num,

 int i, int j)

{

 

 // If num is greater than the element

 // on the left (if exists)

 if (i >= 0 && arr[i] < num)

 return false;

 

 // If num is greater than the element

 // on the right (if exists)

 if (j < n && arr[j] < num)

 return false;

 return true;

}

 

void printPeaksTroughs(int arr[], int n)

{

 cout << "Peaks : ";

 

 // For every element

 for (int i = 0; i < n; i++) {

 

 // If the current element is a peak

 if (isPeak(arr, n, arr[i], i - 1, i + 1))

 cout << arr[i] << " ";

 }

 cout << endl;

 

 cout << "Troughs : ";

 

 // For every element

 for (int i = 0; i < n; i++) {

 

 // If the current element is a trough

 if (isTrough(arr, n, arr[i], i - 1, i + 1))

 cout << arr[i] << " ";

 }

}

 

// Driver code

int main()

{

 int arr[] = { 5, 10, 5, 7, 4, 3, 5 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 printPeaksTroughs(arr, n);

 

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

 

 // Function that returns true if num is

 // greater than both arr[i] and arr[j]

 static boolean isPeak(int arr[], int n, int num,

 int i, int j) 

 {

 

 // If num is smaller than the element

 // on the left (if exists)

 if (i >= 0 && arr[i] > num)

 {

 return false;

 }

 

 // If num is smaller than the element

 // on the right (if exists)

 if (j < n && arr[j] > num)

 {

 return false;

 }

 return true;

 }

 

 // Function that returns true if num is

 // smaller than both arr[i] and arr[j]

 static boolean isTrough(int arr[], int n, int num,

 int i, int j)

 {

 

 // If num is greater than the element

 // on the left (if exists)

 if (i >= 0 && arr[i] < num) 

 {

 return false;

 }

 

 // If num is greater than the element

 // on the right (if exists)

 if (j < n && arr[j] < num) 

 {

 return false;

 }

 return true;

 }

 

 static void printPeaksTroughs(int arr[], int n)

 {

 System.out.print("Peaks : ");

 

 // For every element

 for (int i = 0; i < n; i++) 

 {

 

 // If the current element is a peak

 if (isPeak(arr, n, arr[i], i - 1, i + 1))

 {

 System.out.print(arr[i] + " ");

 }

 }

 System.out.println("");

 

 System.out.print("Troughs : ");

 

 // For every element

 for (int i = 0; i < n; i++)

 {

 

 // If the current element is a trough

 if (isTrough(arr, n, arr[i], i - 1, i + 1)) 

 {

 System.out.print(arr[i] + " ");

 }

 }

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int arr[] = {5, 10, 5, 7, 4, 3, 5};

 int n = arr.length;

 

 printPeaksTroughs(arr, n);

 }

}

 

// This code is contributed by Rajput-Ji  
  
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

 

# Function that returns true if num is

# greater than both arr[i] and arr[j]

def isPeak(arr, n, num, i, j):

 

 # If num is smaller than the element

 # on the left (if exists)

 if (i >= 0 and arr[i] > num):

 return False

 

 # If num is smaller than the element

 # on the right (if exists)

 if (j < n and arr[j] > num):

 return False

 return True

 

# Function that returns true if num is

# smaller than both arr[i] and arr[j]

def isTrough(arr, n, num, i, j):

 

 # If num is greater than the element

 # on the left (if exists)

 if (i >= 0 and arr[i] < num):

 return False

 

 # If num is greater than the element

 # on the right (if exists)

 if (j < n and arr[j] < num):

 return False

 return True

 

def printPeaksTroughs(arr, n):

 

 print("Peaks : ", end = "")

 

 # For every element

 for i in range(n):

 

 # If the current element is a peak

 if (isPeak(arr, n, arr[i], i - 1, i + 1)):

 print(arr[i], end = " ")

 print()

 

 print("Troughs : ", end = "")

 

 # For every element

 for i in range(n):

 

 # If the current element is a trough

 if (isTrough(arr, n, arr[i], i - 1, i + 1)):

 print(arr[i], end = " ")

 

# Driver code

arr = [5, 10, 5, 7, 4, 3, 5]

n = len(arr)

 

printPeaksTroughs(arr, n)

 

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

 

 // Function that returns true if num is

 // greater than both arr[i] and arr[j]

 static Boolean isPeak(int []arr, int n, int num,

 int i, int j) 

 {

 

 // If num is smaller than the element

 // on the left (if exists)

 if (i >= 0 && arr[i] > num)

 {

 return false;

 }

 

 // If num is smaller than the element

 // on the right (if exists)

 if (j < n && arr[j] > num)

 {

 return false;

 }

 return true;

 }

 

 // Function that returns true if num is

 // smaller than both arr[i] and arr[j]

 static Boolean isTrough(int []arr, int n, int num,

 int i, int j)

 {

 

 // If num is greater than the element

 // on the left (if exists)

 if (i >= 0 && arr[i] < num) 

 {

 return false;

 }

 

 // If num is greater than the element

 // on the right (if exists)

 if (j < n && arr[j] < num) 

 {

 return false;

 }

 return true;

 }

 

 static void printPeaksTroughs(int []arr, int n)

 {

 Console.Write("Peaks : ");

 

 // For every element

 for (int i = 0; i < n; i++) 

 {

 

 // If the current element is a peak

 if (isPeak(arr, n, arr[i], i - 1, i + 1))

 {

 Console.Write(arr[i] + " ");

 }

 }

 Console.WriteLine("");

 

 Console.Write("Troughs : ");

 

 // For every element

 for (int i = 0; i < n; i++)

 {

 

 // If the current element is a trough

 if (isTrough(arr, n, arr[i], i - 1, i + 1)) 

 {

 Console.Write(arr[i] + " ");

 }

 }

 }

 

 // Driver code

 public static void Main(String[] args)

 {

 int []arr = {5, 10, 5, 7, 4, 3, 5};

 int n = arr.Length;

 

 printPeaksTroughs(arr, n);

 }

}

 

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    Peaks : 10 7 5 
    Troughs : 5 5 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

