Absolute Difference between the Sum of Non-Prime numbers and Prime numbers of
an Array



  
Given an array of positive numbers, the task is to calculate the absolute
difference between sum of non-prime numbers and prime numbers.

 **Note:** 1 is neither prime nor non-prime.

 **Examples:**

    
    
    Input : 1 3 5 10 15 7
    Output : 10
    Explanation: Sum of non-primes = 25
                 Sum of primes = 15
    
    Input : 3 4 6 7 
    Output : 0
    

**Naive Approach:** A simple solution is to traverse the array and keep
checking for every element if it is prime or not. If number is prime, then add
it to sum S2 which represents the sum of primes else check if its not 1 then
add it to sum of non-primes let’s say S1. After traversing the whole array,
take the absolute difference between the two(S1-S2).  
 **Time complexity** : O(Nsqrt(N))

 **Efficient Approach:** Generate all primes up to the maximum element of the
array using the sieve of Eratosthenes and store them in a hash. Now, traverse
the array and check if the number is present in the hash map. Then, add these
numbers to sum S2 else check if it’s not 1, then add it to sum S1.  
After traversing the whole array, display the absolute difference between the
two.  
 **Time Complexity** : O(Nlog(log(N))  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the Absolute Difference

// between the Sum of Non-Prime numbers

// and Prime numbers of an Array

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the difference between

// the sum of non-primes and the

// sum of primes of an array.

int CalculateDifference(int arr[], int n)

{

 // Find maximum value in the array

 int max_val = *max_element(arr, arr + n);

 

 // USE SIEVE TO FIND ALL PRIME NUMBERS LESS

 // THAN OR EQUAL TO max_val

 // Create a boolean array "prime[0..n]". A

 // value in prime[i] will finally be false

 // if i is Not a prime, else true.

 vector<bool> prime(max_val + 1, true);

 

 // Remaining part of SIEVE

 prime[0] = false;

 prime[1] = false;

 for (int p = 2; p * p <= max_val; p++) {

 

 // If prime[p] is not changed, then

 // it is a prime

 if (prime[p] == true) {

 

 // Update all multiples of p

 for (int i = p * 2; i <= max_val; i += p)

 prime[i] = false;

 }

 }

 

 // Store the sum of primes in S1 and

 // the sum of non primes in S2

 int S1 = 0, S2 = 0;

 for (int i = 0; i < n; i++) {

 

 if (prime[arr[i]]) {

 

 // the number is prime

 S1 += arr[i];

 }

 else if (arr[i] != 1) {

 

 // the number is non-prime

 S2 += arr[i];

 }

 }

 

 // Return the absolute difference

 return abs(S2 - S1);

}

 

int main()

{

 

 // Get the array

 int arr[] = { 1, 3, 5, 10, 15, 7 };

 int n = sizeof(arr) / sizeof(arr[0]);

 

 // Find the absolute difference

 cout << CalculateDifference(arr, n);

 

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

// Java program to find the Absolute

// Difference between the Sum of

// Non-Prime numbers and Prime numbers

// of an Array

import java.util.*;

 

class GFG

{

 

// Function to find the difference 

// between the sum of non-primes 

// and the sum of primes of an array.

static int CalculateDifference(int arr[], 

 int n)

{

 // Find maximum value in the array

 int max_val = Integer.MIN_VALUE;

 for(int i = 0; i < n; i++)

 {

 if(arr[i] > max_val)

 max_val = arr[i];

 }

 

 // USE SIEVE TO FIND ALL PRIME NUMBERS 

 // LESS THAN OR EQUAL TO max_val

 // Create a boolean array "prime[0..n]". 

 // A value in prime[i] will finally be 

 // false if i is Not a prime, else true.

 boolean []prime = new boolean[max_val + 1];

 

 for(int i = 0; i <= max_val; i++)

 prime[i] = true;

 

 // Remaining part of SIEVE

 prime[0] = false;

 prime[1] = false;

 for (int p = 2; 

 p * p <= max_val; p++) 

 {

 

 // If prime[p] is not changed,

 // then it is a prime

 if (prime[p] == true) 

 {

 

 // Update all multiples of p

 for (int i = p * 2; 

 i <= max_val; i += p)

 prime[i] = false;

 }

 }

 

 // Store the sum of primes in 

 // S1 and the sum of non 

 // primes in S2

 int S1 = 0, S2 = 0;

 for (int i = 0; i < n; i++) 

 {

 

 if (prime[arr[i]]) 

 {

 

 // the number is prime

 S1 += arr[i];

 }

 else if (arr[i] != 1) 

 {

 

 // the number is non-prime

 S2 += arr[i];

 }

 }

 

 // Return the absolute difference

 return Math.abs(S2 - S1);

}

 

// Driver Code

public static void main(String []args)

{

 

 // Get the array

 int arr[] = { 1, 3, 5, 10, 15, 7 };

 int n = arr.length;

 

 // Find the absolute difference

 System.out.println(CalculateDifference(arr, n));

}

}

 

// This code is contributed

// by ihritik  
  
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

# Python3 program to find the Absolute

# Difference between the Sum of Non-Prime 

# numbers and Prime numbers of an Array

import sys

 

# Function to find the difference 

# between the sum of non-primes 

# and the sum of primes of an array.

def CalculateDifference(arr, n):

 

 # Find maximum value in the array

 max_val = -1

 for i in range(0, n):

 if(arr[i] > max_val):

 max_val = arr[i]

 

 # USE SIEVE TO FIND ALL PRIME NUMBERS

 # LESS THAN OR EQUAL TO max_val

 # Create a boolean array "prime[0..n]". 

 # A value in prime[i] will finally be 

 # false if i is Not a prime, else true.

 prime = [True for i in range(max_val + 1)] 

 

 # Remaining part of SIEVE

 prime[0] = False

 prime[1] = False

 p = 2

 while (p * p <= max_val): 

 

 # If prime[p] is not changed, 

 # then it is a prime 

 if prime[p] == True: 

 

 # Update all multiples of p 

 for i in range(p * 2, 

 max_val + 1, p): 

 prime[i] = False

 p += 1

 

 # Store the sum of primes in 

 # S1 and the sum of non primes 

 # in S2

 S1 = 0

 S2 = 0

 for i in range (0, n):

 

 if prime[arr[i]]: 

 

 # the number is prime

 S1 += arr[i]

 

 elif arr[i] != 1: 

 

 # the number is non-prime

 S2 += arr[i]

 

 # Return the absolute difference

 return abs(S2 - S1)

 

# Driver code

 

# Get the array

arr = [ 1, 3, 5, 10, 15, 7 ]

n = len(arr)

 

# Find the absolute difference

print(CalculateDifference(arr, n))

 

# This code is contributed

# by ihritik  
  
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

// C# program to find the Absolute

// Difference between the Sum of 

// Non-Prime numbers and Prime

// numbers of an Array

using System; 

 

class GFG

{

 

// Function to find the difference

// between the sum of non-primes 

// and the sum of primes of an array.

static int CalculateDifference(int []arr, 

 int n)

{

 // Find maximum value in the array

 int max_val = int.MinValue;

 for(int i = 0; i < n; i++)

 {

 if(arr[i] > max_val)

 max_val = arr[i];

 }

 

 // USE SIEVE TO FIND ALL PRIME NUMBERS

 // LESS THAN OR EQUAL TO max_val

 // Create a boolean array "prime[0..n]". 

 // A value in prime[i] will finally be 

 // false if i is Not a prime, else true.

 bool []prime = new bool[max_val + 1];

 

 for(int i = 0; i <= max_val; i++)

 prime[i] = true;

 

 // Remaining part of SIEVE

 prime[0] = false;

 prime[1] = false;

 for (int p = 2; 

 p * p <= max_val; p++)

 {

 

 // If prime[p] is not changed, 

 // then it is a prime

 if (prime[p] == true)

 {

 

 // Update all multiples of p

 for (int i = p * 2; 

 i <= max_val; i += p)

 prime[i] = false;

 }

 }

 

 // Store the sum of primes in

 // S1 and the sum of non primes 

 // in S2

 int S1 = 0, S2 = 0;

 for (int i = 0; i < n; i++)

 {

 if (prime[arr[i]]) 

 {

 

 // the number is prime

 S1 += arr[i];

 }

 else if (arr[i] != 1) 

 {

 

 // the number is non-prime

 S2 += arr[i];

 }

 }

 

 // Return the absolute difference

 return Math.Abs(S2 - S1);

}

 

// Driver Code

public static void Main(string []args)

{

 

 // Get the array

 int []arr = { 1, 3, 5, 10, 15, 7 };

 int n = arr.Length;

 

 // Find the absolute difference

 Console.WriteLine(CalculateDifference(arr, n));

}

}

 

// This code is contributed

// by ihritik  
  
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

// PHP program to find the Absolute 

// Difference between the Sum of 

// Non-Prime numbers and Prime 

// numbers of an Array

 

// Function to find the difference 

// between the sum of non-primes and 

// the sum of primes of an array.

function CalculateDifference($arr, $n)

{

 // Find maximum value in the array

 $max_val = PHP_INT_MIN;

 for($i = 0; $i < $n; $i++)

 {

 if($arr[$i] > $max_val)

 $max_val = $arr[$i];

 }

 

 // USE SIEVE TO FIND ALL PRIME NUMBERS 

 // LESS THAN OR EQUAL TO max_val

 // Create a boolean array "prime[0..n]". 

 // A value in prime[i] will finally be 

 // false if i is Not a prime, else true.

 $prime = array_fill(0, $max_val + 1, true); 

 

 // Remaining part of SIEVE

 $prime[0] = false;

 $prime[1] = false;

 

 for ($p = 2; $p * $p <= $max_val; $p++) 

 {

 

 // If prime[p] is not changed, 

 // then it is a prime

 if ($prime[$p] == true) 

 {

 

 // Update all multiples of p

 for ($i = $p * 2; 

 $i <= $max_val; $i += $p)

 $prime[$i] = false;

 }

 }

 

 // Store the sum of primes in 

 // S1 and the sum of non 

 // primes in S2

 $S1 = 0;

 $S2 = 0;

 for ($i = 0; $i < $n; $i++) 

 {

 

 if ($prime[$arr[$i]]) 

 {

 

 // the number is prime

 $S1 += $arr[$i];

 }

 else if ($arr[$i] != 1)

 {

 

 // the number is non-prime

 $S2 += $arr[$i];

 }

 }

 

 // Return the absolute difference

 return abs($S2 - $S1);

}

 

// Driver code

 

// Get the array

$arr = array( 1, 3, 5, 10, 15, 7 );

$n = sizeof($arr);

 

// Find the absolute difference

echo CalculateDifference($arr, $n);

 

// This code is contributed

// by ihritik

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    10
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

