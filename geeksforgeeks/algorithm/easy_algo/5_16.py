Print prime numbers with prime sum of digits in an array



Given an array **arr[]** and the task is to print the additive primes in an
array.  
 **Additive primes:** Primes such that the sum of their digits is also a
prime, such as **2, 3, 7, 11, 23** are additive primes but not **13, 19, 31**
etc.

 **Examples:**

    
    
    **Input:** arr[] = {2, 4, 6, 11, 12, 18, 7}
    **Output:** 2, 11, 7 
    
    **Input:** arr[] = {2, 3, 19, 13, 25, 7}
    **Output:** 2, 3, 7
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **simple approach** is to traverse through all array elements. For every
element check if it is Additive prime or not.

This above approach is fine when array is small or when array values are
large. For large sized arrays having relatively small values, we use **Sieve**
to store primes up to maximum element of the array. Then check if the current
element is prime or not. If yes then check the sum of its digit is also prime
or not. If yes then print that number.

Below is the implementation of the above approach:  

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

using namespace std;

 

// Function to store the primes

void sieve(int maxEle, int prime[])

{

 prime[0] = prime[1] = 1;

 

 for (int i = 2; i * i <= maxEle; i++) {

 if (!prime[i]) {

 for (int j = 2 * i; j <= maxEle; j += i)

 prime[j] = 1;

 }

 }

}

 

// Function to return the sum of digits

int digitSum(int n)

{

 int sum = 0;

 while (n) {

 sum += n % 10;

 n = n / 10;

 }

 return sum;

}

 

// Function to print additive primes

void printAdditivePrime(int arr[], int n)

{

 

 int maxEle = *max_element(arr, arr + n);

 

 int prime[maxEle + 1];

 memset(prime, 0, sizeof(prime));

 sieve(maxEle, prime);

 

 for (int i = 0; i < n; i++) {

 

 // If the number is prime

 if (prime[arr[i]] == 0) {

 int sum = digitSum(arr[i]);

 

 // Check if it's digit sum is prime

 if (prime[sum] == 0)

 cout << arr[i] << " ";

 }

 }

}

 

// Driver code

int main()

{

 

 int a[] = { 2, 4, 6, 11, 12, 18, 7 };

 int n = sizeof(a) / sizeof(a[0]);

 

 printAdditivePrime(a, n);

 

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

import java.util.Arrays;

 

class GFG

{

 

// Function to store the primes

static void sieve(int maxEle, int prime[])

{

 prime[0] = prime[1] = 1;

 

 for (int i = 2; i * i <= maxEle; i++) 

 {

 if (prime[i]==0)

 {

 for (int j = 2 * i; j <= maxEle; j += i)

 prime[j] = 1;

 }

 }

}

 

// Function to return the sum of digits

static int digitSum(int n)

{

 int sum = 0;

 while (n > 0) 

 {

 sum += n % 10;

 n = n / 10;

 }

 return sum;

}

 

// Function to print additive primes

static void printAdditivePrime(int arr[], int n)

{

 

 int maxEle = Arrays.stream(arr).max().getAsInt();

 

 int prime[] = new int[maxEle + 1];

 sieve(maxEle, prime);

 

 for (int i = 0; i < n; i++) 

 {

 

 // If the number is prime

 if (prime[arr[i]] == 0) 

 {

 int sum = digitSum(arr[i]);

 

 // Check if it's digit sum is prime

 if (prime[sum] == 0)

 System.out.print(arr[i]+" ");

 }

 }

}

 

// Driver code

public static void main(String[] args)

{

 

 int a[] = { 2, 4, 6, 11, 12, 18, 7 };

 int n =a.length;

 printAdditivePrime(a, n);

}

}

 

// This code is contributed by chandan_jnu  
  
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

 

# from math lib import sqrt

from math import sqrt

 

# Function to store the primes 

def sieve(maxEle, prime) :

 

 prime[0], prime[1] = 1 , 1

 

 for i in range(2, int(sqrt(maxEle)) + 1) :

 if (not prime[i]) :

 for j in range(2 * i , maxEle + 1, i) :

 prime[j] = 1

 

# Function to return the sum of digits 

def digitSum(n) : 

 sum = 0

 while (n) :

 

 sum += n % 10

 n = n // 10

 return sum

 

# Function to print additive primes

def printAdditivePrime(arr, n):

 maxEle = max(arr)

 prime = [0] * (maxEle + 1)

 sieve(maxEle, prime)

 for i in range(n) :

 

 # If the number is prime

 if (prime[arr[i]] == 0):

 sum = digitSum(arr[i])

 

 # Check if it's digit sum is prime

 if (prime[sum] == 0) :

 print(arr[i], end = " ") 

 

# Driver code 

if __name__ == "__main__" :

 a = [ 2, 4, 6, 11, 12, 18, 7 ]

 n = len(a)

 printAdditivePrime(a, n) 

 

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

// C# implementation of the above approach

using System.Linq;

using System;

 

class GFG

{

 

// Function to store the primes

static void sieve(int maxEle, int[] prime)

{

 prime[0] = prime[1] = 1;

 

 for (int i = 2; i * i <= maxEle; i++) 

 {

 if (prime[i] == 0)

 {

 for (int j = 2 * i; j <= maxEle; j += i)

 prime[j] = 1;

 }

 }

}

 

// Function to return the sum of digits

static int digitSum(int n)

{

 int sum = 0;

 while (n > 0) 

 {

 sum += n % 10;

 n = n / 10;

 }

 return sum;

}

 

// Function to print additive primes

static void printAdditivePrime(int []arr, int n)

{

 

 int maxEle = arr.Max();

 

 int[] prime = new int[maxEle + 1];

 sieve(maxEle, prime);

 

 for (int i = 0; i < n; i++) 

 {

 

 // If the number is prime

 if (prime[arr[i]] == 0) 

 {

 int sum = digitSum(arr[i]);

 

 // Check if it's digit sum is prime

 if (prime[sum] == 0)

 Console.Write(arr[i] + " ");

 }

 }

}

 

// Driver code

static void Main()

{

 int[] a = { 2, 4, 6, 11, 12, 18, 7 };

 int n = a.Length;

 printAdditivePrime(a, n);

}

}

 

// This code is contributed by chandan_jnu  
  
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

 

// Function to store the primes

function sieve($maxEle, &$prime)

{

 $prime[0] = $prime[1] = 1;

 

 for ($i = 2; $i * $i <= $maxEle; $i++)

 {

 if (!$prime[$i]) 

 {

 for ($j = 2 * $i; 

 $j <= $maxEle; $j += $i)

 $prime[$j] = 1;

 }

 }

}

 

// Function to return the sum of digits

function digitSum($n)

{

 $sum = 0;

 while ($n) 

 {

 $sum += $n % 10;

 $n = $n / 10;

 }

 return $sum;

}

 

// Function to print additive primes

function printAdditivePrime($arr, $n)

{

 

 $maxEle = max($arr);

 

 $prime = array_fill(0, $maxEle + 1, 0);

 sieve($maxEle, $prime);

 

 for ($i = 0; $i < $n; $i++)

 {

 

 // If the number is prime

 if ($prime[$arr[$i]] == 0)

 {

 $sum = digitSum($arr[$i]);

 

 // Check if it's digit sum is prime

 if ($prime[$sum] == 0)

 print($arr[$i] . " ");

 }

 }

}

 

// Driver code

$a = array(2, 4, 6, 11, 12, 18, 7);

$n = count($a);

 

printAdditivePrime($a, $n);

 

// This code is contributed by chandan_jnu

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    2 11 7
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

