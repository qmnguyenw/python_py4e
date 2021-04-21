Array Manipulation and Sum



Given an array **arr[]** of **N** integers and an integer **S**. The task is
to find an element **K** in the array such that if all the elements from the
array **> K** are made equal to **K** then the sum of all the elements of the
resultant array becomes equal to **S**. If it is not possible to find such an
element then print **-1** .

 **Examples:**

>  **Input:** M = 15, arr[] = {12, 3, 6, 7, 8}  
>  **Output:** 3  
> Resultant array = {3, 3, 3, 3, 3}  
> Sum of the array elements = 15 = S
>
>  **Input:** M = 5, arr[] = {1, 3, 2, 5, 8}  
>  **Output:** 1

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Sort the array. Traverse the array considering that the value
of **K** is equal to the current element and then check if **sum of the
previous elements + (K * number of remaining elements) = S**. If **yes** then
print the value of **K** , if no such element found then print **-1** in the
end.

  

  

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

 

// Function to return the required element

int getElement(int a[], int n, int S)

{

 // Sort the array

 sort(a, a + n);

 

 int sum = 0;

 

 for (int i = 0; i < n; i++) {

 

 // If current element

 // satisfies the condition

 if (sum + (a[i] * (n - i)) == S)

 return a[i];

 sum += a[i];

 }

 

 // No element found

 return -1;

}

 

// Driver code

int main()

{

 int S = 5;

 int a[] = { 1, 3, 2, 5, 8 };

 int n = sizeof(a) / sizeof(a[0]);

 

 cout << getElement(a, n, S);

 

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

//Java implementation of the approach

import java.util.Arrays;

 

class GFG

{

 // Function to return the required element

 static int getElement(int a[], int n, int S)

 {

 // Sort the array

 Arrays.sort(a);

 

 int sum = 0;

 

 for (int i = 0; i < n; i++) 

 {

 

 // If current element

 // satisfies the condition

 if (sum + (a[i] * (n - i)) == S)

 return a[i];

 sum += a[i];

 }

 

 // No element found

 return -1;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int S = 5;

 int a[] = { 1, 3, 2, 5, 8 };

 int n = a.length;

 

 System.out.println(getElement(a, n, S));

 }

}

 

// This code is contributed by Mukul singh.  
  
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

# Python3 implementation of the approach

 

# Function to return the required element 

def getElement(a, n, S) :

 

 # Sort the array 

 a.sort(); 

 

 sum = 0; 

 

 for i in range(n) :

 

 # If current element 

 # satisfies the condition 

 if (sum + (a[i] * (n - i)) == S) :

 return a[i]; 

 

 sum += a[i]; 

 

 # No element found 

 return -1; 

 

# Driver Code

if __name__ == "__main__" :

 

 S = 5; 

 a = [ 1, 3, 2, 5, 8 ]; 

 n = len(a) ;

 

 print(getElement(a, n, S)) ;

 

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

 // Function to return the required element

 static int getElement(int[] a, int n, int S)

 {

 // Sort the array

 Array.Sort(a);

 

 int sum = 0;

 

 for (int i = 0; i < n; i++) 

 {

 

 // If current element

 // satisfies the condition

 if (sum + (a[i] * (n - i)) == S)

 return a[i];

 sum += a[i];

 }

 

 // No element found

 return -1;

 }

 

 // Driver code

 public static void Main()

 {

 int S = 5;

 int[] a = { 1, 3, 2, 5, 8 };

 int n = a.Length;

 

 Console.WriteLine(getElement(a, n, S));

 }

}

 

// This code is contributed by Mukul singh.  
  
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

 

// Function to return the required element

function getElement($a, $n, $S)

{

 // Sort the array

 sort($a, 0);

 

 $sum = 0;

 

 for ($i = 0; $i < $n; $i++) 

 {

 

 // If current element

 // satisfies the condition

 if ($sum + ($a[$i] * 

 ($n - $i)) == $S)

 return $a[$i];

 $sum += $a[$i];

 }

 

 // No element found

 return -1;

}

 

// Driver code

$S = 5;

$a = array(1, 3, 2, 5, 8);

$n = sizeof($a);

 

echo getElement($a, $n, $S);

 

// This code is contributed 

// by Akanksha Rai

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

