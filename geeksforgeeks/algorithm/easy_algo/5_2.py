Sum of (maximum element – minimum element) for all the subsets of an array.



Given an array **arr[]** , the task is to compute the **sum of (max{A} –
min{A}) for every non-empty subset A** of the array arr[].

 **Examples:**

>  **Input:** arr[] = { 4, 7 }  
>  **Output:** 3
>
> There are three non-empty subsets: { 4 }, { 7 } and { 4, 7 }.  
> max({4}) – min({4}) = 0  
> max({7}) – min({7}) = 0  
> max({4, 7}) – min({4, 7}) = 7 – 4 = 3.
>
> Sum = 0 + 0 + 3 = 3
>
>  
>
>
>  
>
>
>  **Input:** arr[] = { 4, 3, 1 }  
>  **Output:** 9

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **naive solution** is to generate all subsets and traverse every subset to
find the maximum and minimum element and add their difference to the current
sum. The time complexity of this solution is **O(n * 2 n)**.

An **efficient solution** is based on a simple observation stated below.

> For example, A = { 4, 3, 1 }  
> Let value to be added in the sum for every subset be V.
>
> Subsets with max, min and V values:  
> { 4 }, max = 4, min = 4 (V = 4 – 4)  
> { 3 }, max = 3, min = 3 (V = 3 – 3)  
> { 1 }, max = 1, min = 1 (V = 1 – 1)  
> { 4, 3 }, max = 4, min = 3 (V = 4 – 3)  
> { 4, 1 }, max = 4, min = 1 (V = 4 – 1)  
> { 3, 1 }, max = 3, min = 1 (V = 3 – 1)  
> { 4, 3, 1 }, max = 4, min = 1 (V = 4 – 1)
>
> Sum of all V values  
> = (4 – 4) + (3 – 3) + (1 – 1) + (4 – 3) + (4 – 1) + (3 – 1) + (4 – 1)  
> = 0 + 0 + 0 + (4 – 3) + (4 – 1) + (3 – 1) + (4 – 1)  
> = (4 – 3) + (4 – 1) + (3 – 1) + (4 – 1)
>
> First 3 ‘V’ values can be ignored since they evaluate to 0  
> (because they result from 1-sized subsets).
>
> Rearranging the sum, we get:
>
>  
>
>
>  
>
>
> = (4 – 3) + (4 – 1) + (3 – 1) + (4 – 1)  
> = (1 * 0 – 1 * 3) + (3 * 1 – 3 * 1) + (4 * 3 – 4 * 0)  
> = (1 * A – 1 * B) + (3 * C – 3 * D) + (4 * E – 4 * F)
>
> where A = 0, B = 3, C = 1, D = 1, E = 3 and F = 0
>
> If we closely look at the expression, instead of analyzing every subset,
> here we analyze every element of how many times it occurs as a minimum or a
> maximum element.
>
> A = 0 implies that 1 doesn’t occur as a maximum element in any of the
> subsets.  
> B = 3 implies that 1 occurs as a minimum element in 3 subsets.  
> C = 1 implies that 3 occurs as a maximum element in 1 subset.  
> D = 1 implies that 3 occurs as a minimum element in 1 subset.  
> E = 3 implies that 4 occurs as a maximum element in 3 subsets.  
> F = 0 implies that 4 doesn’t occur as a minimum element in any of the
> subsets.

If we somehow know the count of subsets for every element in which it occurs
as a maximum element and a minimum element then we can solve the problem in
**linear** time, since the computation above is linear in nature.

Let A = { 6, 3, 89, 21, 4, 2, 7, 9 }  
sorted(A) = { 2, 3, 4, **6** , 7, 9, 21, 89 }

For example, we analyze _element with value 6 (marked in bold)_. 3 elements
are smaller than 6 and 4 elements are larger than 6. Therefore, if we think of
all subsets in which 6 occurs with the 3 smaller elements, then in all those
subsets 6 will be the maximum element. No of those subsets will be 23. Similar
argument holds for 6 being the minimum element when it occurs with the 4
elements greater than 6.

> Hence,  
> No of occurrences for an element as the maximum in all subsets = **2 pos –
> 1**  
> No of occurrences for an element as the minimum in all subsets = **2 n – 1 –
> pos – 1**
>
> where **pos** is the index of the element in the sorted array.

Below is the implementation of the above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

 

#define ll long long

 

using namespace std;

 

const int mod = 1000000007;

 

// Function to return a^n % mod

ll power(ll a, ll n)

{

 if (n == 0)

 return 1;

 

 ll p = power(a, n / 2) % mod;

 p = (p * p) % mod;

 if (n & 1) {

 p = (p * a) % mod;

 }

 return p;

}

 

// Compute sum of max(A) - min(A) for all subsets

ll computeSum(int* arr, int n)

{

 

 // Sort the array.

 sort(arr, arr + n);

 

 ll sum = 0;

 for (int i = 0; i < n; i++) {

 

 // Maxs = 2^i - 1

 ll maxs = (power(2, i) - 1 + mod) % mod;

 maxs = (maxs * arr[i]) % mod;

 

 // Mins = 2^(n-1-i) - 1

 ll mins = (power(2, n - 1 - i) - 1 + mod) % mod;

 mins = (mins * arr[i]) % mod;

 

 ll V = (maxs - mins + mod) % mod;

 sum = (sum + V) % mod;

 }

 return sum;

}

 

// Driver code

int main()

{

 int arr[] = { 4, 3, 1 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 cout << computeSum(arr, n);

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

// Java implementation of the above approach

import java.util.*;

 

class GFG 

{

 

static int mod = 1000000007;

 

 // Function to return a^n % mod

 static long power(long a, long n) 

 {

 if (n == 0) 

 {

 return 1;

 }

 

 long p = power(a, n / 2) % mod;

 p = (p * p) % mod;

 if (n == 1) 

 {

 p = (p * a) % mod;

 }

 return p;

 }

 

 // Compute sum of max(A) - min(A) for all subsets

 static long computeSum(int[] arr, int n) 

 {

 

 // Sort the array.

 Arrays.sort(arr);

 

 long sum = 0;

 for (int i = 0; i < n; i++) 

 {

 

 // Maxs = 2^i - 1

 long maxs = (power(2, i) - 1 + mod) % mod;

 maxs = (maxs * arr[i]) % mod;

 

 // Mins = 2^(n-1-i) - 1

 long mins = (power(2, n - 1 - i) - 1 + mod) % mod;

 mins = (mins * arr[i]) % mod;

 

 long V = (maxs - mins + mod) % mod;

 sum = (sum + V) % mod;

 }

 return sum;

 }

 

 // Driver code

 public static void main(String[] args) 

 {

 int arr[] = {4, 3, 1};

 int n = arr.length;

 System.out.println(computeSum(arr, n));

 }

}

 

// This code has been contributed by 29AjayKumar  
  
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

# Python3 implementation of the

# above approach 

 

# Function to return a^n % mod 

def power(a, n): 

 

 if n == 0:

 return 1

 

 p = power(a, n // 2) % mod 

 p = (p * p) % mod 

 if n & 1 == 1: 

 p = (p * a) % mod 

 

 return p 

 

# Compute sum of max(A) - min(A) 

# for all subsets 

def computeSum(arr, n): 

 

 # Sort the array. 

 arr.sort()

 

 Sum = 0

 for i in range(0, n): 

 

 # Maxs = 2^i - 1 

 maxs = (power(2, i) - 1 + mod) % mod 

 maxs = (maxs * arr[i]) % mod 

 

 # Mins = 2^(n-1-i) - 1 

 mins = (power(2, n - 1 - i) -

 1 + mod) % mod 

 mins = (mins * arr[i]) % mod 

 

 V = (maxs - mins + mod) % mod 

 Sum = (Sum + V) % mod 

 

 return Sum

 

# Driver code 

if __name__ =="__main__":

 

 mod = 1000000007

 arr = [4, 3, 1] 

 n = len(arr) 

 

 print(computeSum(arr, n)) 

 

# This code is contributed

# by Rituraj Jain  
  
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

using System.Collections;

 

class GFG 

{

 

static int mod = 1000000007;

 

 // Function to return a^n % mod

 static long power(long a, long n) 

 {

 if (n == 0) 

 {

 return 1;

 }

 

 long p = power(a, n / 2) % mod;

 p = (p * p) % mod;

 if (n == 1) 

 {

 p = (p * a) % mod;

 }

 return p;

 }

 

 // Compute sum of max(A) - min(A) for all subsets

 static long computeSum(int []arr, int n) 

 {

 

 // Sort the array.

 Array.Sort(arr);

 

 long sum = 0;

 for (int i = 0; i < n; i++) 

 {

 

 // Maxs = 2^i - 1

 long maxs = (power(2, i) - 1 + mod) % mod;

 maxs = (maxs * arr[i]) % mod;

 

 // Mins = 2^(n-1-i) - 1

 long mins = (power(2, n - 1 - i) - 1 + mod) % mod;

 mins = (mins * arr[i]) % mod;

 

 long V = (maxs - mins + mod) % mod;

 sum = (sum + V) % mod;

 }

 return sum;

 }

 

 // Driver code

 public static void Main() 

 {

 int []arr = {4, 3, 1};

 int n = arr.Length;

 Console.WriteLine(computeSum(arr, n));

 }

}

 

// This code has been contributed by mits  
  
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

// PHP implementation of the above approach

$mod = 1000000007;

 

// Function to return a^n % mod

function power($a, $n)

{

 global $mod;

 if ($n == 0)

 return 1;

 

 $p = power($a, $n / 2) % $mod;

 $p = ($p * $p) % $mod;

 if ($n & 1) 

 {

 $p = ($p * $a) % $mod;

 }

 return $p;

}

 

// Compute sum of max(A) - min(A)

// for all subsets

function computeSum(&$arr, $n)

{

 global $mod;

 

 // Sort the array.

 sort($arr);

 

 $sum = 0;

 for ($i = 0; $i < $n; $i++) 

 {

 

 // Maxs = 2^i - 1

 $maxs = (power(2, $i) - 1 + $mod) % $mod;

 $maxs = ($maxs * $arr[$i]) % $mod;

 

 // Mins = 2^(n-1-i) - 1

 $mins = (power(2, $n - 1 - $i) - 1 + $mod) % $mod;

 $mins = ($mins * $arr[$i]) % $mod;

 

 $V = ($maxs - $mins + $mod) % $mod;

 $sum = ($sum + $V) % $mod;

 }

 return $sum;

}

 

// Driver code

$arr = array( 4, 3, 1 );

$n = sizeof($arr);

 

echo computeSum($arr, $n);

 

// This code is contributed by ita_c

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    9
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

