Increment odd positioned elements by 1 and decrement even positioned elements
by 1 in an Array



Given an array **arr[]** , the task is increment all the **odd positioned
elements** by **1** and decrement all the **even positioned elements** by
**1**.  
 **Examples:**

> **Input:** arr[] = {3, 6, 8}  
> **Output:** 4 5 9  
>  **Input:** arr[] = {9, 7, 3}  
> **Output:** 10 6 4

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Traverse the array element by element and if the current
element’s position is odd then increment it by 1 else decrement it by 1. Prin
the contents of the updated array in the end.  
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

// Utility function to print

// the contents of an array

void printArr(int arr[], int n)

{

 for (int i = 0; i < n; i++)

 cout << arr[i] << " ";

}

// Function to increment all the odd

// positioned elements by 1 and decrement

// all the even positioned elements by 1

void updateArr(int arr[], int n)

{

 for (int i = 0; i < n; i++)

 // If current element is odd positioned

 if ((i + 1) % 2 == 1)

 arr[i]++;

 // If even positioned

 else

 arr[i]--;

 // Print the updated array

 printArr(arr, n);

}

// Driver code

int main()

{

 int arr[] = { 3, 6, 8 };

 int n = sizeof(arr) / sizeof(arr[0]);

 updateArr(arr, n);

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

class GfG

{

// Utility function to print

// the contents of an array

static void printArr(int arr[], int n)

{

 for (int i = 0; i < n; i++)

 System.out.print(arr[i] + " ");

}

// Function to increment all the odd

// positioned elements by 1 and decrement

// all the even positioned elements by 1

static void updateArr(int arr[], int n)

{

 for (int i = 0; i < n; i++)

 // If current element is odd positioned

 if ((i + 1) % 2 == 1)

 arr[i]++;

 // If even positioned

 else

 arr[i]--;

 // Print the updated array

 printArr(arr, n);

}

// Driver code

public static void main(String[] args)

{

 int arr[] = { 3, 6, 8 };

 int n = arr.length;

 updateArr(arr, n);

}

}

// This code is contributed by Prerna Saini  
  
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

# Utility function to print

# the contents of an array

def printArr(arr, n):

 for i in range(0, n):

 print(arr[i], end = " ");

# Function to increment all the odd

# positioned elements by 1 and decrement

# all the even positioned elements by 1

def updateArr(arr, n):

 for i in range(0, n):

 # If current element is odd positioned

 if ((i + 1) % 2 == 1):

 arr[i] += 1;

 # If even positioned

 else:

 arr[i] -= 1;

 # Print the updated array

 printArr(arr, n);

# Driver code

if __name__ == '__main__':

 arr = [3, 6, 8];

 n = len(arr);

 updateArr(arr, n);

# This code contributed by PrinciRaj1992  
  
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

class GfG

{

// Utility function to print

// the contents of an array

static void printArr(int []arr, int n)

{

 for (int i = 0; i < n; i++)

 System.Console.Write(arr[i] + " ");

}

// Function to increment all the odd

// positioned elements by 1 and decrement

// all the even positioned elements by 1

static void updateArr(int []arr, int n)

{

 for (int i = 0; i < n; i++)

 // If current element is odd positioned

 if ((i + 1) % 2 == 1)

 arr[i]++;

 // If even positioned

 else

 arr[i]--;

 // Print the updated array

 printArr(arr, n);

}

// Driver code

static void Main()

{

 int []arr = { 3, 6, 8 };

 int n = arr.Length;

 updateArr(arr, n);

}

}

// This code is contributed by mits  
  
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

// Utility function to print

// the contents of an array

function printArr($arr, $n)

{

 for ($i = 0; $i < $n; $i++)

 echo $arr[$i] . " ";

}

// Function to increment all the odd

// positioned elements by 1 and decrement

// all the even positioned elements by 1

function updateArr($arr, $n)

{

 for ($i = 0; $i < $n; $i++)

 // If current element is odd positioned

 if (($i + 1) % 2 == 1)

 $arr[$i]++;

 // If even positioned

 else

 $arr[$i]--;

 // Print the updated array

 printArr($arr, $n);

}

// Driver code

$arr = array( 3, 6, 8 );

$n = count($arr);

updateArr($arr, $n);

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    4 5 9

_**Time Complexity:** O(n)_

 _ **Auxiliary Space:** O(1)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

