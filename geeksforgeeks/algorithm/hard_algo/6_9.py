Arrange given numbers to form the smallest number



Given an array **arr[]** of integer elements, the task is to arrange them in
such a way that these numbers form the smallest possible number.  
For example, if the given array is {5, 6, 2, 9, 21, 1} then the arrangement
will be 1212569.

 **Examples:**

>  **Input:** arr[] = {5, 6, 2, 9, 21, 1}  
>  **Output:** 1212569
>
>  **Input:** arr[] = {1, 2, 1, 12, 33, 211, 50}  
>  **Output:** 111221123350

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** If all the given numbers are of at most one digit then simple
approach is sorting all numbers in ascending order. But if there are sum
number which have more than a single digit then this approach will not work.  
Therefore, we have to sort the array by comparing any two elements in the
following way:  
If the elements are **A** and **B** , then compare **(A + B)** with **(B +
A)** where **+** represents **concatenation**.

  

  

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

#include <algorithm>

#include <iostream>

using namespace std;

 

// Utility function to print

// the contents of an array

void printArr(int arr[], int n)

{

 for (int i = 0; i < n; i++)

 cout << arr[i];

}

 

// A comparison function that return true

// if 'AB' is smaller than 'BA' when

// we concatenate two numbers 'A' and 'B'

// For example, it will return true if

// we pass 12 and 24 as arguments.

// This function will be used by sort() function

bool compare(int num1, int num2)

{

 // to_string function is predefined function

 // to convert a number in string

 

 // Convert first number to string format

 string A = to_string(num1);

 

 // Convert second number to string format

 string B = to_string(num2);

 

 // Check if 'AB' is smaller or 'BA'

 // and return bool value since

 // comparison operator '<=' returns

 // true or false

 return (A + B) <= (B + A);

}

 

// Function to print the arrangement

// with the smallest value

void printSmallest(int N, int arr[])

{

 // If we pass the name of the comparison

 // function it will sort the array

 // according to the compare function

 sort(arr, arr + N, compare);

 

 // Print the sorted array

 printArr(arr, N);

}

 

// Driver code

int main()

{

 int arr[] = { 5, 6, 2, 9, 21, 1 };

 int N = sizeof(arr) / sizeof(arr[0]);

 printSmallest(N, arr);

 

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

class GFG

{

 

 // Utility function to print

 // the contents of an array

 public static void printArr(int[] arr, int n) 

 {

 for (int i = 0; i < n; i++)

 System.out.print(arr[i]);

 }

 

 // A comparison function that return negative

 // if 'AB' is smaller than 'BA' when

 // we concatenate two numbers 'A' and 'B'

 // For example, it will return negative value if

 // we pass 12 and 24 as arguments.

 // This function will be used during sort

 public static int compare(int num1, int num2)

 {

 

 // toString function is predefined function

 // to convert a number in string

 

 // Convert first number to string format

 String A = Integer.toString(num1);

 

 // Convert second number to string format

 String B = Integer.toString(num2);

 

 // Check if 'AB' is smaller or 'BA'

 // and return integer value

 return (A+B).compareTo(B+A);

 }

 

 // Function to print the arrangement

 // with the smallest value

 public static void printSmallest(int N, int[] arr) 

 {

 

 // Sort using compare function which

 // is defined above

 for (int i = 0; i < N; i++)

 {

 for (int j = i + 1; j < N; j++)

 {

 if (compare(arr[i], arr[j]) > 0)

 {

 int temp = arr[i];

 arr[i] = arr[j];

 arr[j] = temp;

 }

 }

 }

 

 // Print the sorted array

 printArr(arr, N);

 }

 

 // Driver code

 public static void main(String[] args) 

 {

 int[] arr = { 5, 6, 2, 9, 21, 1 };

 int N = arr.length;

 printSmallest(N, arr);

 }

}

 

// This code is contributed by

// sanjeev2552  
  
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

 print(arr[i], end = "")

 

# A comparison function that return true

# if 'AB' is smaller than 'BA' when

# we concatenate two numbers 'A' and 'B'

# For example, it will return true if

# we pass 12 and 24 as arguments.

# This function will be used by sort() function

def compare(num1, num2):

 

 # Convert first number to string format

 A = str(num1)

 

 # Convert second number to string format

 B = str(num2)

 

 # Check if 'AB' is smaller or 'BA'

 # and return bool value since

 # comparison operator '<=' returns

 # true or false

 return int(A + B) <= int(B + A)

 

def sort(arr):

 

 for i in range(len(arr)):

 for j in range(i + 1, len(arr)):

 

 if compare(arr[i], arr[j]) == False:

 arr[i], arr[j] = arr[j], arr[i]

 

# Function to print the arrangement

# with the smallest value

def printSmallest(N, arr):

 

 # If we pass the name of the comparison

 # function it will sort the array

 # according to the compare function

 sort(arr)

 

 # Print the sorted array

 printArr(arr, N)

 

# Driver code

if __name__ == "__main__":

 

 arr = [5, 6, 2, 9, 21, 1]

 N = len(arr)

 printSmallest(N, arr)

 

# This code is contributed by Rituraj Jain  
  
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

// C# implementation for above approach

using System;

 

class GFG

{

 

 // Utility function to print

 // the contents of an array

 public static void printArr(int[] arr, int n) 

 {

 for (int i = 0; i < n; i++)

 Console.Write(arr[i]);

 }

 

 // A comparison function that return negative

 // if 'AB' is smaller than 'BA' when

 // we concatenate two numbers 'A' and 'B'

 // For example, it will return negative value if

 // we pass 12 and 24 as arguments.

 // This function will be used during sort

 public static int compare(int num1, int num2)

 {

 

 // toString function is predefined function

 // to convert a number in string

 

 // Convert first number to string format

 String A = num1.ToString();

 

 // Convert second number to string format

 String B = num2.ToString();

 

 // Check if 'AB' is smaller or 'BA'

 // and return integer value

 return (A+B).CompareTo(B+A);

 }

 

 // Function to print the arrangement

 // with the smallest value

 public static void printSmallest(int N, int[] arr) 

 {

 

 // Sort using compare function which

 // is defined above

 for (int i = 0; i < N; i++)

 {

 for (int j = i + 1; j < N; j++)

 {

 if (compare(arr[i], arr[j]) > 0)

 {

 int temp = arr[i];

 arr[i] = arr[j];

 arr[j] = temp;

 }

 }

 }

 

 // Print the sorted array

 printArr(arr, N);

 }

 

 // Driver code

 public static void Main(String[] args) 

 {

 int[] arr = { 5, 6, 2, 9, 21, 1 };

 int N = arr.Length;

 printSmallest(N, arr);

 }

}

 

// This code is contributed by Rajput-Ji  
  
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

 echo $arr[$i]; 

} 

 

// A comparison function that return true 

// if 'AB' is smaller than 'BA' when 

// we concatenate two numbers 'A' and 'B' 

// For example, it will return true if 

// we pass 12 and 24 as arguments. 

// This function will be used by sort() function 

function compare($num1, $num2) 

{ 

 // to_string function is predefined function 

 // to convert a number in string 

 

 // Convert first number to string format 

 $A = (string)$num1 ; 

 

 // Convert second number to string format 

 $B = (string)$num2 ; 

 

 // Check if 'AB' is smaller or 'BA' 

 // and return bool value since 

 // comparison operator '<=' returns 

 // true or false 

 if((int)($A . $B) <= (int)($B . $A))

 {

 return true;

 }

 else

 return false;

} 

 

 

function sort_arr($arr)

{

 

 for ($i = 0; $i < count($arr) ; $i++)

 {

 for ($j = $i + 1;$j < count($arr) ; $j++)

 {

 if (compare($arr[$i], $arr[$j]) == false)

 {

 $temp = $arr[$i] ;

 $arr[$i] = $arr[$j] ;

 $arr[$j] = $temp ;

 }

 }

 }

 return $arr ;

 }

 

// Function to print the arrangement 

// with the smallest value 

function printSmallest($N, $arr) 

{ 

 // If we pass the name of the comparison 

 // function it will sort the array 

 // according to the compare function 

 $arr = sort_arr($arr); 

 

 // Print the sorted array 

 printArr($arr, $N); 

} 

 

 // Driver code 

 $arr = array(5, 6, 2, 9, 21, 1 ); 

 $N = count($arr); 

 printSmallest($N, $arr); 

 

 // This code is contributed by Ryuga

 

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    1212569
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

