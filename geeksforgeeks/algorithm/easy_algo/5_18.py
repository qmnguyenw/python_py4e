Count pairs in an array such that at least one element is prime



Given an array **arr[]** of distinct elements, the task is to count the total
number of distinct pairs in which at least one element is prime.

 **Examples:**

    
    
    **Input:** arr[] = {1, 3, 10, 7, 8}
    **Output:** 7
    Pairs with at least one prime are (1, 3), (1, 7), 
    (3, 1), (3, 7), (3, 8), (10, 7), (7, 8).
    
    **Input:** arr[]={4, 6, 8, 2, 9};
    **Output:** 4
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** First precompute all the prime till the Maximum element of
array using **Sieve **. Traverse each and every possible pair and check if any
of the element in the pair is prime. If yes, then increment the count.

Below is the implementation of above approach:  

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

 

// Function to find primes

void sieve(int maxm, int prime[])

{

 prime[0] = prime[1] = 1;

 

 for (int i = 2; i * i <= maxm; i++)

 if (!prime[i])

 for (int j = 2 * i; j <= maxm; j += i)

 prime[j] = 1;

}

 

// Function to count the pair

int countPair(int a[], int n)

{

 // Find the maximum element of the array

 int maxm = *max_element(a, a + n);

 int prime[maxm + 1];

 memset(prime, 0, sizeof(prime));

 

 // Find primes upto maximum

 sieve(maxm, prime);

 

 // Count pairs with at least prime

 int count = 0;

 for (int i = 0; i < n; i++)

 for (int j = i + 1; j < n; j++)

 if (prime[a[i]] == 0 || prime[a[j]] == 0)

 count++;

 

 return count;

}

 

// Driver code

int main()

{

 int arr[] = { 2, 3, 5, 4, 7 };

 int n = 5;

 

 cout << countPair(arr, n);

 

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

 

class GFG

{

 // Function to find primes

 static void sieve(int maxm, int prime[])

 {

 prime[0] = prime[1] = 1;

 

 for (int i = 2; i * i <= maxm; i++)

 if (prime[i] == 0)

 for (int j = 2 * i; j <= maxm; j += i)

 prime[j] = 1;

 }

 

 // Function to count the pair

 static int countPair(int a[], int n)

 {

 // Find the maximum element of the array

 int maxm = a[0];

 

 for(int i = 1; i < n; i++)

 if(a[i] > maxm)

 maxm = a[i];

 

 int [] prime = new int[maxm + 1];

 

 for(int i = 0; i < maxm + 1; i++)

 prime[i] = 0;

 

 // Find primes upto maximum

 sieve(maxm, prime);

 

 // Count pairs with at least prime

 int count = 0;

 for (int i = 0; i < n; i++)

 for (int j = i + 1; j < n; j++)

 if (prime[a[i]] == 0 || prime[a[j]] == 0)

 count++;

 

 return count;

 }

 

 // Driver code

 public static void main(String []args)

 {

 int arr[] = { 2, 3, 5, 4, 7 };

 int n = arr.length;

 System.out.println(countPair(arr, n));

 }

}

 

// This code is contributed by ihritik  
  
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

# Python 3 implementation of the above approach

from math import sqrt

 

# Function to count the pair

def countPair(a, n):

 

 # Find the maximum element of the array

 maxm = a[0]

 for i in range(len(a)):

 if(a[i] > maxm):

 maxm = a[i]

 prime = [0 for i in range(maxm + 1)]

 

 # Find primes upto maximum

 prime[0] = prime[1] = 1;

 

 for i in range(2, int(sqrt(maxm)) + 1, 1):

 if (prime[i] == 0):

 for j in range(2 * i, maxm + 1, i):

 prime[j] = 1

 

 # Count pairs with at least prime

 count = 0

 for i in range(n):

 for j in range(i + 1, n, 1):

 if (prime[a[i]] == 0 or

 prime[a[j]] == 0):

 count += 1

 

 return count

 

# Driver code

if __name__ == '__main__':

 arr = [2, 3, 5, 4, 7]

 n = 5

 

 print(countPair(arr, n))

 

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

// C# implementation of the above approach

using System;

 

class GFG

{

 // Function to find primes

 static void sieve(int maxm, int []prime)

 {

 prime[0] = prime[1] = 1;

 

 for (int i = 2; i * i <= maxm; i++)

 if (prime[i] == 0)

 for (int j = 2 * i; j <= maxm; j += i)

 prime[j] = 1;

 }

 

 // Function to count the pair

 static int countPair(int []a, int n)

 {

 // Find the maximum element of the array

 int maxm = a[0];

 

 for(int i = 1; i < n; i++)

 if(a[i] > maxm)

 maxm = a[i];

 

 int [] prime = new int[maxm + 1];

 

 for(int i = 0; i < maxm + 1; i++)

 prime[i] = 0;

 

 // Find primes upto maximum

 sieve(maxm, prime);

 

 // Count pairs with at least prime

 int count = 0;

 for (int i = 0; i < n; i++)

 for (int j = i + 1; j < n; j++)

 if (prime[a[i]] == 0 || prime[a[j]] == 0)

 count++;

 

 return count;

 }

 

 // Driver code

 public static void Main()

 {

 int []arr = { 2, 3, 5, 4, 7 };

 int n = arr.Length;

 Console.WriteLine(countPair(arr, n));

 }

}

 

// This code is contributed by ihritik  
  
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

 

// Function to find primes 

function sieve($maxm, $prime) 

{ 

 $prime[0] = $prime[1] = 1; 

 

 for ($i = 2; $i * $i <= $maxm; $i++) 

 if (!$prime[$i]) 

 for ($j = 2 * $i; 

 $j <= $maxm; $j += $i) 

 $prime[$j] = 1; 

} 

 

// Function to count the pair 

function countPair($a, $n) 

{ 

 // Find the maximum element of the array 

 $maxm = max($a); 

 $prime = array(); 

 

 $prime = array_fill(0, $maxm + 1, 0);

 

 // Find primes upto maximum 

 sieve($maxm, $prime); 

 

 // Count pairs with at least prime 

 $count = 0; 

 for ($i = 0; $i < $n; $i++) 

 for ($j = $i + 1; $j < $n; $j++) 

 if ($prime[$a[$i]] == 0 || 

 $prime[$a[$j]] == 0) 

 $count++; 

 

 return $count; 

} 

 

// Driver code 

$arr = array( 2, 3, 5, 4, 7 ); 

$n = 5; 

 

echo countPair($arr, $n); 

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    10
    

