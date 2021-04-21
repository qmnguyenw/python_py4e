Largest number in an array that is not a perfect cube



Given an array of n integers. The task is to find the largest number which is
not a perfect cube. Print -1 if there is no number that is a perfect cube.  
 **Examples** :

    
    
    **Input:** arr[] = {16, 8, 25, 2, 3, 10} 
    **Output:** 25
    25 is the largest number that is not a perfect cube. 
    
    **Input:** arr[] = {36, 64, 10, 16, 29, 25}
    **Output:** 36

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

A **Simple Solution** is to sort the elements and sort then numbers and start
checking from back for a non-perfect cube number using cbrt() function. The
first number from the end which is not a perfect cube number is our answer.
The complexity of sorting is O(n log n) and of cbrt() function is log n, so at
the worst case, the complexity is O(n log n).  
An **Efficient Solution** is to iterate for all the elements in O(n) and
compare every time with the maximum element and store the maximum of all non-
perfect cubes.  
Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to find the largest non-perfect

// cube number among n numbers

#include <bits/stdc++.h>

using namespace std;

// Function to check if a number

// is perfect cube number or not

bool checkPerfectcube(int n)

{

 // takes the sqrt of the number

 int d = cbrt(n);

 // checks if it is a perfect

 // cube number

 if (d * d * d == n)

 return true;

 return false;

}

// Function to find the largest non perfect

// cube number in the array

int largestNonPerfectcubeNumber(int a[], int n)

{

 // stores the maximum of all

 // perfect cube numbers

 int maxi = -1;

 // Traverse all elements in the array

 for (int i = 0; i < n; i++) {

 // store the maximum if current

 // element is a non perfect cube

 if (!checkPerfectcube(a[i]))

 maxi = max(a[i], maxi);

 }

 return maxi;

}

// Driver Code

int main()

{

 int a[] = { 16, 64, 25, 2, 3, 10 };

 int n = sizeof(a) / sizeof(a[0]);

 cout << largestNonPerfectcubeNumber(a, n);

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

// Java program to find the largest non-perfect

// cube number among n numbers

import java.io.*;

class GFG {

 

// Function to check if a number

// is perfect cube number or not

static boolean checkPerfectcube(int n)

{

 // takes the sqrt of the number

 int d = (int)Math.cbrt(n);

 // checks if it is a perfect

 // cube number

 if (d * d * d == n)

 return true;

 return false;

}

// Function to find the largest non perfect

// cube number in the array

static int largestNonPerfectcubeNumber(int []a, int n)

{

 // stores the maximum of all

 // perfect cube numbers

 int maxi = -1;

 // Traverse all elements in the array

 for (int i = 0; i < n; i++) {

 // store the maximum if current

 // element is a non perfect cube

 if (!checkPerfectcube(a[i]))

 maxi = Math.max(a[i], maxi);

 }

 return maxi;

}

// Driver Code

 public static void main (String[] args) {

 int a[] = { 16, 64, 25, 2, 3, 10 };

 int n = a.length;

 System.out.print( largestNonPerfectcubeNumber(a, n));

 }

}

// This code is contributed

// by inder_verma  
  
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

# Python 3 program to find the largest

# non-perfect cube number among n numbers

import math

# Function to check if a number

# is perfect cube number or not

def checkPerfectcube(n):

 

 # takes the sqrt of the number

 cube_root = n ** (1./3.)

 if round(cube_root) ** 3 == n:

 return True

 else:

 return False

# Function to find the largest non

# perfect cube number in the array

def largestNonPerfectcubeNumber(a, n):

 

 # stores the maximum of all

 # perfect cube numbers

 maxi = -1

 # Traverse all elements in the array

 for i in range(0, n, 1):

 

 # store the maximum if current

 # element is a non perfect cube

 if (checkPerfectcube(a[i]) == False):

 maxi = max(a[i], maxi)

 

 return maxi

# Driver Code

if __name__ == '__main__':

 a = [16, 64, 25, 2, 3, 10]

 n = len(a)

 print(largestNonPerfectcubeNumber(a, n))

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

// C# program to find the largest non-perfect

// cube number among n numbers

using System;

public class GFG {

 // Function to check if a number

 // is perfect cube number or not

 static bool checkPerfectcube(int n)

 {

 // takes the sqrt of the number

 int d = (int)Math.Ceiling(Math.Pow(n, (double)1 / 3));

 // checks if it is a perfect

 // cube number

 if (d * d * d == n)

 return true;

 return false;

 }

 // Function to find the largest non perfect

 // cube number in the array

 static int largestNonPerfectcubeNumber(int []a, int n)

 {

 // stores the maximum of all

 // perfect cube numbers

 int maxi = -1;

 // Traverse all elements in the array

 for (int i = 0; i < n; i++) {

 // store the maximum if current

 // element is a non perfect cube

 if (checkPerfectcube(a[i])==false)

 maxi = Math.Max(a[i], maxi);

 }

 return maxi;

 }

 // Driver Code

 public static void Main () {

 int []a = { 16, 64, 25, 2, 3, 10 };

 int n = a.Length;

 Console.WriteLine( largestNonPerfectcubeNumber(a, n));

 }

}

/*This code is contributed by PrinciRaj1992*/  
  
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

// PHP program to find the largest non-perfect

// cube number among n numbers

// Function to check if a number

// is perfect cube number or not

function checkPerfectcube($n)

{

 // takes the sqrt of the number

 $d = (int)round(pow($n, 1/3));

 // checks if it is a perfect

 // cube number

 if ($d * $d * $d == $n)

 return true;

 return false;

}

// Function to find the largest non perfect

// cube number in the array

function largestNonPerfectcubeNumber($a, $n)

{

 // stores the maximum of all

 // perfect cube numbers

 $maxi = -1;

 // Traverse all elements in the array

 for ($i = 0; $i < $n; $i++) {

 // store the maximum if current

 // element is a non perfect cube

 if (!checkPerfectcube($a[$i]))

 $maxi = max($a[$i], $maxi);

 }

 return $maxi;

}

// Driver Code

 $a = array( 16, 64, 25, 2, 3, 10 );

 $n = count($a);

 echo largestNonPerfectcubeNumber($a, $n);

// this code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    25

**Time Complexity :** O(n)

 **Auxiliary Space:** O(1)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

