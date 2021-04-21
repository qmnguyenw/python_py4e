Find the repeating and the missing number using two equations



Given an array **arr[]** of size **N** , each integer from the range **[1,
N]** appears exactly once except **A** which appears **twice** and **B** which
is **missing**. The task is to find the numbers **A** and **B**.  
 **Examples:**  

> **Input:** arr[] = {1, 2, 2, 3, 4}  
> **Output:**  
> A = 2  
> B = 5  
>  **Input:** arr[] = {5, 3, 4, 1, 1}  
> **Output:**  
> A = 1  
> B = 2  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:** From the sum of first **N** natural numbers,  

> SumN = 1 + 2 + 3 + … + N = (N * (N + 1)) / 2  
> And, let the sum of all the array elements be **Sum**. Now,  
> SumN = Sum – A + B  
> A – B = Sum – SumN …(equation 1)  
>
>
>  
>
>
>  
>

And from the sum of the squares of first **N** natural numbers,  

> SumSqN = 12 \+ 22 \+ 32 \+ … + N2 = (N * (N + 1) * (2 * n + 1)) / 6  
> And, let the sum of the squares of all the array elements be **SumSq**. Now,  
> SumSq = SumSqN + A2 – B2  
> SumSq – SumSqN = (A + B) * (A – B) …(equation 2)  
>

Put value of (A – B) from equation 1 in equation 2,  
SumSq – SumSqN = (A + B) * (Sum – SumN)  
A + B = (SumSq – SumSqN) / (Sum – SumN) …(equation 3)  
Solving equation 1 and equation 3 will give,  

> **B = (((SumSq – SumSqN) / (Sum – SumN)) + SumN – Sum) / 2**  
> And, **A = Sum – SumN + B**  
>

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

//C++ implementation of the approach

#include <cmath>

#include<bits/stdc++.h>

#include <iostream>

using namespace std;

 // Function to print the required numbers

 void findNumbers(int arr[], int n)

 {

 // Sum of first n natural numbers

 int sumN = (n * (n + 1)) / 2;

 // Sum of squares of first n natural numbers

 int sumSqN = (n * (n + 1) * (2 * n + 1)) / 6;

 // To store the sum and sum of squares

 // of the array elements

 int sum = 0, sumSq = 0, i;

 for (i = 0; i < n; i++) {

 sum += arr[i];

 sumSq = sumSq + (pow(arr[i], 2));

 }

 int B = (((sumSq - sumSqN) / (sum - sumN)) + sumN - sum) / 2;

 int A = sum - sumN + B;

 cout << "A = " ;

 cout << A << endl;

 cout << "B = " ;

 cout << B << endl;

 }

 // Driver code

int main() {

 int arr[] = { 1, 2, 2, 3, 4 };

 int n = sizeof(arr)/sizeof(arr[0]);

 findNumbers(arr, n);

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

public class GFG {

 // Function to print the required numbers

 static void findNumbers(int arr[], int n)

 {

 // Sum of first n natural numbers

 int sumN = (n * (n + 1)) / 2;

 // Sum of squares of first n natural numbers

 int sumSqN = (n * (n + 1) * (2 * n + 1)) / 6;

 // To store the sum and sum of squares

 // of the array elements

 int sum = 0, sumSq = 0, i;

 for (i = 0; i < n; i++) {

 sum += arr[i];

 sumSq += Math.pow(arr[i], 2);

 }

 int B = (((sumSq - sumSqN) / (sum - sumN)) + sumN - sum) / 2;

 int A = sum - sumN + B;

 System.out.println("A = " + A + "\nB = " + B);

 }

 // Driver code

 public static void main(String[] args)

 {

 int arr[] = { 1, 2, 2, 3, 4 };

 int n = arr.length;

 findNumbers(arr, n);

 }

}  
  
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

import math

# Function to print the required numbers

def findNumbers(arr, n):

 

 # Sum of first n natural numbers

 sumN = (n * (n + 1)) / 2;

 # Sum of squares of first n natural numbers

 sumSqN = (n * (n + 1) * (2 * n + 1)) /
6;

 # To store the sum and sum of squares

 # of the array elements

 sum = 0;

 sumSq = 0;

 for i in range(0,n):

 sum = sum + arr[i];

 sumSq = sumSq + (math.pow(arr[i], 2));

 

 B = (((sumSq - sumSqN) / (sum - sumN)) + sumN -
sum) / 2;

 A = sum - sumN + B;

 print("A = ",int(A)) ;

 print("B = ",int(B));

 

# Driver code

arr = [ 1, 2, 2, 3, 4 ];

n = len(arr);

findNumbers(arr, n);

#This code is contributed by Shivi_Aggarwal   
  
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

public class GFG {

 // Function to print the required numbers

 static void findNumbers(int []arr, int n)

 {

 // Sum of first n natural numbers

 int sumN = (n * (n + 1)) / 2;

 // Sum of squares of first n natural numbers

 int sumSqN = (n * (n + 1) * (2 * n + 1)) / 6;

 // To store the sum and sum of squares

 // of the array elements

 int sum = 0, sumSq = 0, i;

 for (i = 0; i < n; i++) {

 sum += arr[i];

 sumSq += (int)Math.Pow(arr[i], 2);

 }

 int B = (((sumSq - sumSqN) / (sum - sumN)) + sumN - sum) / 2;

 int A = sum - sumN + B;

 Console.WriteLine("A = " + A + "\nB = " + B);

 }

 // Driver code

 public static void Main()

 {

 int []arr = { 1, 2, 2, 3, 4 };

 int n = arr.Length;

 findNumbers(arr, n);

 }

}

// This code is contributed by PrinciRaj1992  
  
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

// Function to print the required numbers

function findNumbers($arr, $n)

{

 // Sum of first n natural numbers

 $sumN = ($n * ($n + 1)) / 2;

 // Sum of squares of first n

 // natural numbers

 $sumSqN = ($n * ($n + 1) *

 (2 * $n + 1)) / 6;

 // To store the sum and sum of

 // squares of the array elements

 $sum = 0 ;

 $sumSq = 0 ;

 for ($i = 0; $i < $n; $i++)

 {

 $sum += $arr[$i];

 $sumSq += pow($arr[$i], 2);

 }

 $B = ((($sumSq - $sumSqN) / ($sum - $sumN)) +

 $sumN - $sum) / 2;

 $A = $sum - $sumN + $B;

 echo "A = ", $A, "\nB = ", $B;

}

// Driver code

$arr = array( 1, 2, 2, 3, 4 );

$n = sizeof($arr) ;

findNumbers($arr, $n);

// This code is contributed by Ryuga

?>  
  
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

// Javascript implementation of the approach

// Function to print the required numbers

function findNumbers(arr, n)

{

 // Sum of first n natural numbers

 sumN = (n * (n + 1)) / 2;

 // Sum of squares of first n

 // natural numbers

 sumSqN = (n * (n + 1) *

 (2 * n + 1)) / 6;

 // To store the sum and sum of

 // squares of the array elements

 let sum = 0 ;

 let sumSq = 0 ;

 for (let i = 0;i < n; i++)

 {

 sum += arr[i];

 sumSq += Math.pow(arr[i], 2);

 }

 B = (((sumSq - sumSqN) / (sum - sumN)) +

 sumN - sum) / 2;

 A = sum - sumN + B;

 document.write( "A = "+ A, "<br>B = ", B);

}

// Driver code

let arr = [ 1, 2, 2, 3, 4 ];

n = arr.length ;

findNumbers(arr, n);

// This code is contributed

// by bobby

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    A = 2
    B = 5

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

