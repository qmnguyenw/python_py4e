Program to find covariance



Given a two set of random variable, find Covariance. Covariance is a measure
of how much two random variables vary together. It’s similar to variance, but
where variance tells you how a single variable varies, covariance tells you
how two variables vary together. Covariance can be calculated by using the
formula  
![{\\displaystyle \\operatorname {cov} \(X,Y\)={\\frac {1}{n}}\\sum
_{i=1}^{n}\(x_{i}-x'\)\(y_{i}-y'\).}   ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-ff8a999cea764d09283226fdc3c64e37_l3.png)  
Where x’ and y’ are the means of two given sets.

Examples:

    
    
    Input : arr1[] = {65.21, 64.75, 65.26, 65.76, 65.96}
            arr2[] = {67.25, 66.39, 66.12, 65.70, 66.64}
    Output : -0.0580511
    
    Input : arr1[] = {5, 20, 40, 80, 100}
            arr2[] = {10, 24, 33, 54, 10}
    Output : 187.75

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to find

// covariance of two set.

#include<bits/stdc++.h>

using namespace std;

// Function to find mean.

float mean(float arr[], int n)

{

 float sum = 0;

 for(int i = 0; i < n; i++)

 sum = sum + arr[i];

 return sum / n;

}

// Function to find covariance.

float covariance(float arr1[], float arr2[], int n)

{

 float sum = 0;

 for(int i = 0; i < n; i++)

 sum = sum + (arr1[i] - mean(arr1, n)) *

 (arr2[i] - mean(arr2, n));

 return sum / (n - 1);

}

// Driver function.

int main()

{

 float arr1[] = {65.21, 64.75, 65.26, 65.76, 65.96};

 int n = sizeof(arr1) / sizeof(arr1[0]);

 

 float arr2[] = {67.25, 66.39, 66.12, 65.70, 66.64};

 int m = sizeof(arr2) / sizeof(arr2[0]);

 

 if (m == n)

 cout << covariance(arr1, arr2, m);

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

// Java Program to find

// covariance of two set.

import java.io.*;

class GFG {

// Function to find mean.

static float mean(float arr[], int n)

{

 float sum = 0;

 

 for(int i = 0; i < n; i++)

 sum = sum + arr[i];

 

 return sum / n;

}

// Function to find covariance.

static float covariance(float arr1[],

 float arr2[], int n)

{

 float sum = 0;

 

 for(int i = 0; i < n; i++)

 sum = sum + (arr1[i] - mean(arr1, n)) *

 (arr2[i] - mean(arr2, n));

 return sum / (n - 1);

}

// Driver code

 public static void main (String[] args) {

 

 float arr1[] = {65.21f, 64.75f,

 65.26f, 65.76f, 65.96f};

 int n = arr1.length;

 

 float arr2[] = {67.25f, 66.39f,

 66.12f, 65.70f, 66.64f};

 

 int m = arr2.length;

 

 if (m == n)

 

 System.out.println(covariance(arr1, arr2, m));

 

 }

}

// This code is contributed by Gitanjali.  
  
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

# Python3 Program to find

# covariance of two set.

import math

# Function to find mean.

def mean(arr, n):

 

 sum = 0

 for i in range(0, n):

 sum = sum + arr[i]

 

 return sum / n

# Function to find covariance.

def covariance(arr1, arr2, n):

 sum = 0

 for i in range(0, n):

 sum = (sum + (arr1[i] - mean(arr1, n)) *

 (arr2[i] - mean(arr2, n)))

 

 return sum / (n - 1)

# Driver method

arr1 = [65.21, 64.75, 65.26, 65.76, 65.96]

n = len(arr1)

arr2 = [67.25, 66.39, 66.12, 65.70, 66.64]

m = len(arr2)

if (m == n):

 print (covariance(arr1, arr2, m))

# This code is contributed by Gitanjali.  
  
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

// C# Program to find

// covariance of two set.

using System;

class GFG {

 // Function to find mean.

 static float mean(float []arr, int n)

 {

 float sum = 0;

 

 for(int i = 0; i < n; i++)

 sum = sum + arr[i];

 

 return sum / n;

 }

 

 // Function to find covariance.

 static float covariance(float []arr1,

 float []arr2, int n)

 {

 float sum = 0;

 

 for(int i = 0; i < n; i++)

 sum = sum + (arr1[i] - mean(arr1, n)) *

 (arr2[i] - mean(arr2, n));

 return sum / (n - 1);

 }

 

 // Driver code

 public static void Main () {

 

 float []arr1 = {65.21f, 64.75f,

 65.26f, 65.76f, 65.96f};

 int n = arr1.Length;

 

 float []arr2 = {67.25f, 66.39f,

 66.12f, 65.70f, 66.64f};

 

 int m = arr2.Length;

 

 if (m == n)

 

 Console.WriteLine(covariance(arr1, arr2, m));

 

 }

}

// This code is contributed by vt_m.  
  
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

// PHP Program to find

// covariance of two set.

// Function to find mean.

function mean( $arr, $n)

{

 $sum = 0;

 for( $i = 0; $i < $n; $i++)

 $sum = $sum + $arr[$i];

 return $sum / $n;

}

// Function to find covariance.

function covariance( $arr1, $arr2, $n)

{

 $sum = 0;

 for( $i = 0; $i < $n; $i++)

 $sum = $sum + ($arr1[$i] -

 mean($arr1, $n)) *

 ($arr2[$i] -

 mean($arr2, $n));

 return $sum / ($n - 1);

}

// Driver function.

$arr1 = array(65.21, 64.75, 65.26,

 65.76, 65.96);

$n = count($arr1);

 

$arr2 = array(67.25, 66.39, 66.12,

 65.70, 66.64);

$m =count($arr2);

 

if ($m == $n)

 echo covariance($arr1, $arr2, $m);

// This code is contributed by anuj_67.

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

// Javascript program to find

// covariance of two set.

// Function to find mean.

function mean(arr, n)

{

 let sum = 0;

 for(let i = 0; i < n; i++)

 sum = sum + arr[i];

 

 return sum / n;

}

// Function to find covariance.

function covariance(arr1, arr2, n)

{

 let sum = 0;

 for(let i = 0; i < n; i++)

 sum = sum + (arr1[i] - mean(arr1, n)) *

 (arr2[i] - mean(arr2, n));

 

 return sum / (n - 1);

}

// Driver code

let arr1 = [ 65.21, 64.75, 65.26, 65.76, 65.96 ];

let n = arr1.length;

let arr2 = [ 67.25, 66.39, 66.12, 65.70, 66.64 ];

let m = arr2.length;

if (m == n)

 document.write(covariance(arr1, arr2, m));

 

// This code is contributed by souravmahato348

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    -0.0580511

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

