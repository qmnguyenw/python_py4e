Print all safe primes below N



Given an integer **N** , the task is to print all safe primes below **N** safe
primes. A **safe prime** is a prime number of the form **(2 * p) + 1** where
**p** is also a **prime**.

> The first few safe primes are 5, 7, 11, 23, 47, …

 **Examples:**

> **Input:** N = 13  
> **Output:** 5 7 11  
> 5 = 2 * 2 + 1  
> 7 = 2 * 3 + 1  
> 11 = 2 * 5 + 1
>
>  **Input:** N = 6  
> **Output:** 5 7  
>
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:** First pre-compute all the primes till **N** using Sieve of
Eratosthenes and then starting from **2** check whether the current prime is
also a safe prime. If **yes** then print it else skip to the next prime.

Below is the implementation of above approach:

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

// Function to print first n safe primes

void printSafePrimes(int n)

{

 int prime[n + 1];

 // Initialize all entries of integer array

 // as 1. A value in prime[i] will finally

 // be 0 if i is Not a prime, else 1

 for (int i = 2; i <= n; i++)

 prime[i] = 1;

 // 0 and 1 are not primes

 prime[0] = prime[1] = 0;

 for (int p = 2; p * p <= n; p++) {

 // If prime[p] is not changed, then

 // it is a prime

 if (prime[p] == 1) {

 // Update all multiples of p

 for (int i = p * 2; i <= n; i += p)

 prime[i] = 0;

 }

 }

 for (int i = 2; i <= n; i++) {

 // If i is prime

 if (prime[i] != 0) {

 // 2p + 1

 int temp = (2 * i) + 1;

 // If 2p + 1 is also a prime

 // then set prime[2p + 1] = 2

 if (temp <= n && prime[temp] != 0)

 prime[temp] = 2;

 }

 }

 for (int i = 5; i <= n; i++)

 // i is a safe prime

 if (prime[i] == 2)

 cout << i << " ";

}

// Driver code

int main()

{

 int n = 20;

 printSafePrimes(n);

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

class GFG{

 

 // Function to print first n safe primes

 static void printSafePrimes(int n)

 {

 int prime[] = new int [n + 1];

 

 // Initialize all entries of integer array

 // as 1. A value in prime[i] will finally

 // be 0 if i is Not a prime, else 1

 for (int i = 2; i <= n; i++)

 prime[i] = 1;

 

 // 0 and 1 are not primes

 prime[0] = prime[1] = 0;

 

 for (int p = 2; p * p <= n; p++)

 {

 

 // If prime[p] is not changed, then

 // it is a prime

 if (prime[p] == 1)

 {

 

 // Update all multiples of p

 for (int i = p * 2; i <= n; i += p)

 prime[i] = 0;

 }

 }

 

 for (int i = 2; i <= n; i++)

 {

 

 // If i is prime

 if (prime[i] != 0)

 {

 

 // 2p + 1

 int temp = (2 * i) + 1;

 

 // If 2p + 1 is also a prime

 // then set prime[2p + 1] = 2

 if (temp <= n && prime[temp] != 0)

 prime[temp] = 2;

 }

 }

 

 for (int i = 5; i <= n; i++)

 

 // i is a safe prime

 if (prime[i] == 2)

 System.out.print(i + " ");

 }

 

 // Driver code

 public static void main(String []args)

 {

 int n = 20;

 printSafePrimes(n);

 }

}

// This code is contributed by Ryuga  
  
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

# Python 3 implementation of the approach

from math import sqrt

# Function to print first n safe primes

def printSafePrimes(n):

 prime = [0 for i in range(n + 1)]

 # Initialize all entries of integer

 # array as 1. A value in prime[i]

 # will finally be 0 if i is Not a

 # prime, else 1

 for i in range(2, n + 1):

 prime[i] = 1

 # 0 and 1 are not primes

 prime[0] = prime[1] = 0

 for p in range(2, int(sqrt(n)) + 1, 1):

 

 # If prime[p] is not changed,

 # then it is a prime

 if (prime[p] == 1):

 

 # Update all multiples of p

 for i in range(p * 2, n + 1, p):

 prime[i] = 0

 

 for i in range(2, n + 1, 1):

 

 # If i is prime

 if (prime[i] != 0):

 

 # 2p + 1

 temp = (2 * i) + 1

 # If 2p + 1 is also a prime

 # then set prime[2p + 1] = 2

 if (temp <= n and prime[temp] != 0):

 prime[temp] = 2

 for i in range(5, n + 1):

 

 # i is a safe prime

 if (prime[i] == 2):

 print(i, end = " ")

# Driver code

if __name__ == '__main__':

 n = 20

 printSafePrimes(n)

 

# This code is contributed by

# Sanjit_Prasad  
  
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

class GFG{

 

 // Function to print first n safe primes

 static void printSafePrimes(int n)

 {

 int[] prime = new int [n + 1];

 

 // Initialize all entries of integer array

 // as 1. A value in prime[i] will finally

 // be 0 if i is Not a prime, else 1

 for (int i = 2; i <= n; i++)

 prime[i] = 1;

 

 // 0 and 1 are not primes

 prime[0] = prime[1] = 0;

 

 for (int p = 2; p * p <= n; p++)

 {

 

 // If prime[p] is not changed, then

 // it is a prime

 if (prime[p] == 1)

 {

 

 // Update all multiples of p

 for (int i = p * 2; i <= n; i += p)

 prime[i] = 0;

 }

 }

 

 for (int i = 2; i <= n; i++)

 {

 

 // If i is prime

 if (prime[i] != 0)

 {

 

 // 2p + 1

 int temp = (2 * i) + 1;

 

 // If 2p + 1 is also a prime

 // then set prime[2p + 1] = 2

 if (temp <= n && prime[temp] != 0)

 prime[temp] = 2;

 }

 }

 

 for (int i = 5; i <= n; i++)

 

 // i is a safe prime

 if (prime[i] == 2)

 Console.Write(i + " ");

 }

 

 // Driver code

 public static void Main()

 {

 int n = 20;

 printSafePrimes(n);

 }

}

// This code is contributed by Ita_c.  
  
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

// Function to print first n safe primes

function printSafePrimes($n)

{

 $prime = array();

 // Initialize all entries of integer array

 // as 1. A value in prime[i] will finally

 // be 0 if i is Not a prime, else 1

 for ($i = 2; $i <= $n; $i++)

 $prime[$i] = 1;

 // 0 and 1 are not primes

 $prime[0] = $prime[1] = 0;

 for ($p = 2; $p * $p <= $n; $p++)

 {

 // If prime[p] is not changed,

 // then it is a prime

 if ($prime[$p] == 1)

 {

 // Update all multiples of p

 for ($i = $p * 2;

 $i <= $n; $i += $p)

 $prime[$i] = 0;

 }

 }

 for ($i = 2; $i <= $n; $i++)

 {

 // If i is prime

 if ($prime[$i] != 0)

 {

 // 2p + 1

 $temp = (2 * $i) + 1;

 // If 2p + 1 is also a prime

 // then set prime[2p + 1] = 2

 if ($temp <= $n &&

 $prime[$temp] != 0)

 $prime[$temp] = 2;

 }

 }

 for ($i = 5; $i <= $n; $i++)

 // i is a safe prime

 if ($prime[$i] == 2)

 echo $i, " ";

}

// Driver code

$n = 20;

printSafePrimes($n);

// This code is contributed

// by aishwarya.27

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

// Function to print first n safe primes

function printSafePrimes(n)

{

 let prime = new Array(n + 1);

 

 // Initialize all entries of integer array

 // as 1. A value in prime[i] will finally

 // be 0 if i is Not a prime, else 1

 for(let i = 2; i <= n; i++)

 prime[i] = 1;

 

 // 0 and 1 are not primes

 prime[0] = prime[1] = 0;

 

 for(let p = 2; p * p <= n; p++)

 {

 

 // If prime[p] is not changed, then

 // it is a prime

 if (prime[p] == 1)

 {

 

 // Update all multiples of p

 for(let i = p * 2; i <= n; i += p)

 prime[i] = 0;

 }

 }

 

 for(let i = 2; i <= n; i++)

 {

 

 // If i is prime

 if (prime[i] != 0)

 {

 

 // 2p + 1

 let temp = (2 * i) + 1;

 

 // If 2p + 1 is also a prime

 // then set prime[2p + 1] = 2

 if (temp <= n && prime[temp] != 0)

 prime[temp] = 2;

 }

 }

 

 for(let i = 5; i <= n; i++)

 

 // i is a safe prime

 if (prime[i] == 2)

 document.write(i + " ");

}

// Driver code

let n = 20;

printSafePrimes(n);

// This code is contributed by unknown2108

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    5 7 11

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

