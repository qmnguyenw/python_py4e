Reach the numbers by making jumps of two given lengths



Given integers **k** , **d1** , **d2** and an integer array **arr[]**.
Starting from number **k** you are allowed to make jumps of size **d1** and
**d2** i.e. all the possible moves from **k** are:  

  * **k + d1** and **k – d1**
  *  **k + d2** and **k – d2**

The task is to find which of the numbers from the array are reachable from
**k** making any number of jumps and any given jump is either of size **d1**
or **d2**. For every number print **1** if its reachable else print **0**.  
 **Examples:**  

> **Input:** k = 10, d1 = 4, d2 = 6, arr[] = {10, 15, 20}  
> **Output:** 1 0 1  
> 10 can be reached from k with no extra move.  
> 20 can be reached with k + d1 + d2 = 10 + 4 + 6 = 20  
>  **Input:** k = 8, d1 = 3, d2 = 2, arr[] = {9, 4}  
> **Output:** 1 1  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:** Any number **x** that is reachable from **k** with jumps **d1**
or **d2** will be of the form **x = k + (i * d1) + (j * d2)** where **i** and
**j** are integers.  
Let the GCD of **d1** and **d2** be **gcd**. Since, **gcd** divides both
**d1** and **d2**. Therefore we can write **d1 = m1 * gcd** and **d2 = m2 *
gcd** where **m1** and **m2** are integers  
And **x = k + gcd * (i * m1 + j * m2) = k + M * gcd**.  
So, any number **x** that is reachable from **k** should satisfy **(x – k) %
gcd = 0**.  
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

// Function that returns the vector containing the

// result for the reachability of the required numbers

void reachTheNums(int nums[], int k, int d1, int d2, int
n)

{

 int i, ans[n] = { 0 };

 int gcd = __gcd(d1, d2);

 for (i = 0; i < n; i++) {

 int x = nums[i] - k;

 // If distance x is coverable

 if (x % gcd == 0)

 ans[i] = 1;

 else

 ans[i] = 0;

 }

 for (i = 0; i < n; i++)

 cout << ans[i] << " ";

}

// Driver code

int main()

{

 // Numbers to be checked for reachability

 int nums[] = { 9, 4 };

 int n = sizeof(nums) / sizeof(nums[0]);

 // Starting number K

 int k = 8;

 // Sizes of jumps d1 and d2

 int d1 = 3, d2 = 2;

 reachTheNums(nums, k, d1, d2, n);

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

import java.io.*;

class GFG {

// Recursive function to return gcd of a and b

 static int __gcd(int a, int b)

 {

 // Everything divides 0 

 if (a == 0)

 return b;

 if (b == 0)

 return a;

 

 // base case

 if (a == b)

 return a;

 

 // a is greater

 if (a > b)

 return __gcd(a-b, b);

 return __gcd(a, b-a);

 }

 

// Function that returns the vector containing the

// result for the reachability of the required numbers

static void reachTheNums(int nums[], int k, int d1, int
d2, int n)

{

 int i;

 int ans[] = new int[n];

 int gcd = __gcd(d1, d2);

 for (i = 0; i < n; i++) {

 int x = nums[i] - k;

 // If distance x is coverable

 if (x % gcd == 0)

 ans[i] = 1;

 else

 ans[i] = 0;

 }

 for (i = 0; i < n; i++)

 System.out.print(ans[i] + " ");

}

// Driver code

 public static void main (String[] args) {

 // Numbers to be checked for reachability

 int nums[] = { 9, 4 };

 int n =nums.length;

 // Starting number K

 int k = 8;

 // Sizes of jumps d1 and d2

 int d1 = 3, d2 = 2;

 reachTheNums(nums, k, d1, d2, n);

 }

}

// This code is contributed by inder_verma..  
  
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

import math as mt

# Function that returns the vector

# containing the result for the reachability

# of the required numbers

def reachTheNums(nums, k, d1, d2, n):

 ans = [0 for i in range(n)]

 gcd = mt.gcd(d1, d2)

 for i in range(n):

 x = nums[i] - k

 # If distance x is coverable

 if (x % gcd == 0):

 ans[i] = 1

 else:

 ans[i] = 0

 for i in range(n):

 print(ans[i], end = " ")

# Driver code

# Numbers to be checked for

# reachability

nums = [9, 4]

n = len(nums)

# Starting number K

k = 8

# Sizes of jumps d1 and d2

d1, d2 = 3, 2

reachTheNums(nums, k, d1, d2, n)

# This code is conteibuted

# by mohit kumar 29  
  
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

using System ;

class GFG {

 

 // Recursive function to return gcd of a and b

 static int __gcd(int a, int b)

 {

 // Everything divides 0

 if (a == 0)

 return b;

 if (b == 0)

 return a;

 

 // base case

 if (a == b)

 return a;

 

 // a is greater

 if (a > b)

 return __gcd(a-b, b);

 

 return __gcd(a, b-a);

 }

 

 // Function that returns the vector containing the

 // result for the reachability of the required numbers

 static void reachTheNums(int []nums, int k, int d1, int
d2, int n)

 {

 int i;

 int []ans = new int[n];

 int gcd = __gcd(d1, d2);

 

 for (i = 0; i < n; i++) {

 int x = nums[i] - k;

 

 // If distance x is coverable

 if (x % gcd == 0)

 ans[i] = 1;

 else

 ans[i] = 0;

 }

 

 for (i = 0; i < n; i++)

 Console.Write(ans[i] + " ");

 }

 // Driver code

 public static void Main () {

 // Numbers to be checked for reachability

 int []nums = { 9, 4 };

 int n =nums.Length;

 // Starting number K

 int k = 8;

 // Sizes of jumps d1 and d2

 int d1 = 3, d2 = 2;

 reachTheNums(nums, k, d1, d2, n);

 }

 // This code is contributed by Ryuga

}  
  
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

// gcd function

function GCD($a, $b)

{

 if ($b == 0)

 return $a;

 return GCD($b, $a % $b);

}

// Function that returns the vector

// containing the result for the

// reachability of the required numbers

function reachTheNums($nums, $k, $d1,

 $d2, $n)

{

 $i = 0; $ans = array(0, 0);

 $gcd = GCD($d1, $d2);

 for ($i = 0; $i < $n; $i++)

 {

 $x = $nums[$i] - $k;

 // if distance x is coverable

 if ($x % $gcd == 0)

 $ans[$i] = 1;

 else

 $ans[$i] = 0;

 }

 for ($i = 0; $i < $n; $i++)

 echo $ans[$i] . " ";

}

// Driver Code

// Numbers to be checked for reachability

$nums = array(9, 4);

$n = 2;

// Starting number $K

$k = 8;

// Sizes of jumps $d1 and $d2

$d1 = 3; $d2 = 2;

reachTheNums($nums, $k, $d1, $d2, $n);

 

// This code is contributed by Adesh Singh1

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

// javascript implementation of the approach

 // Recursive function to return gcd of a and b

 function __gcd(a , b)

 {

 

 // Everything divides 0

 if (a == 0)

 return b;

 if (b == 0)

 return a;

 // base case

 if (a == b)

 return a;

 // a is greater

 if (a > b)

 return __gcd(a - b, b);

 return __gcd(a, b - a);

 }

 // Function that returns the vector containing the

 // result for the reachability of the required numbers

 function reachTheNums(nums , k , d1 , d2 , n)

 {

 var i;

 var ans = Array(n).fill(0);

 var gcd = __gcd(d1, d2);

 for (let i = 0; i < n; i++)

 {

 var x = nums[i] - k;

 // If distance x is coverable

 if (x % gcd == 0)

 ans[i] = 1;

 else

 ans[i] = 0;

 }

 for (let i = 0; i < n; i++)

 document.write(ans[i] + " ");

 }

 // Driver code

 

 // Numbers to be checked for reachability

 var nums = [ 9, 4 ];

 var n = nums.length;

 

 // Starting number K

 var k = 8;

 // Sizes of jumps d1 and d2

 var d1 = 3, d2 = 2;

 reachTheNums(nums, k, d1, d2, n);

// This code is contributed by aashish1995.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    1 1

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

