Sort only non-prime numbers of an array in increasing order



Given an array of **N** integers. The task is to print the sorted array such
that all numbers that are **prime** stay in the same place, sort only the
**non prime** numbers.

 **Examples** :

    
    
    Input : arr[] = {10, 7, 6}
    Output : 6 7 10
    
    Input : arr[] = {100, 11, 500, 2, 17, 1}
    Output : 1 11 100 2 17 500
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  * Traverse the array, take out all non prime numbers and store them in a vector.
  * Now, sort the vector.
  * Then, traverse the array again and check if a number is prime, if yes then print it as it is. Otherwise print a number from the vector.

To check whether a number is prime or not we can use sieve-of-eratosthenes.

  

  

Below is the implementation of above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to sort only non primes

#include <bits/stdc++.h>

using namespace std;

 

// Create a boolean array "prime[0..n]" and initialize

// all entries it as true. A value in prime[i] will

// finally be false if i is Not a prime, else true.

bool prime[100005];

 

void SieveOfEratosthenes(int n)

{

 

 memset(prime, true, sizeof(prime));

 

 prime[1] = false;

 

 for (int p = 2; p * p <= n; p++) {

 // If prime[p] is not changed, then it is a prime

 if (prime[p] == true) {

 // Update all multiples of p

 for (int i = p * 2; i <= n; i += p)

 prime[i] = false;

 }

 }

}

 

// Function to print the array such that

// only non primes are sorted

void sortedArray(int arr[], int n)

{

 SieveOfEratosthenes(100005);

 

 // vector v will store all non

 // prime numbers

 std::vector<int> v;

 

 // If not prime, insert into vector

 for (int i = 0; i < n; ++i) {

 if (prime[arr[i]] == 0)

 v.push_back(arr[i]);

 }

 

 // sorting vector of non primes

 sort(v.begin(), v.end());

 

 int j = 0;

 // print the required array

 for (int i = 0; i < n; ++i) {

 if (prime[arr[i]] == true)

 cout << arr[i] << " ";

 else {

 cout << v[j] << " ";

 j++;

 }

 }

}

 

// Driver Code

int main()

{

 

 int n = 6;

 int arr[] = { 100, 11, 500, 2, 17, 1 };

 

 sortedArray(arr, n);

 

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



// Java program to sort only non primes

import java.util.*;

class solution

{

// Create a boolean array "prime[0..n]" and initialize

// all entries it as true. A value in prime[i] will

// finally be false if i is Not a prime, else true.

static boolean prime[] = new boolean[100006];

 

static void SieveOfEratosthenes(int n)

{

 

 for(int i=1;i<=n;i++)

 prime[i]=true;

 prime[1] = false;

 

 for (int p = 2; p * p <= n; p++) {

 // If prime[p] is not changed, then it is a prime

 if (prime[p] == true) {

 // Update all multiples of p

 for (int i = p * 2; i <= n; i += p)

 prime[i] = false;

 }

 }

}

 

// Function to print the array such that

// only non primes are sorted

static void sortedArray(int arr[], int n)

{

 SieveOfEratosthenes(100005);

 

 // vector v will store all non

 // prime numbers

 Vector<Integer> v = new Vector<Integer>();

 

 // If not prime, insert into vector

 for (int i = 0; i < n; ++i) {

 if (prime[arr[i]]==false)

 v.add(arr[i]);

 }

 

 // sorting vector of non primes

 Collections.sort(v);

 

 int j = 0;

 // print the required array

 for (int i = 0; i < n; ++i) {

 if (prime[arr[i]] == true)

 System.out.print( arr[i] + " ");

 else {

 System.out.print( v.get(j) + " ");

 j++;

 }

 }

}

 

// Driver Code

public static void main(String args[])

{

 

 int n = 6;

 int arr[] = { 100, 11, 500, 2, 17, 1 };

 

 sortedArray(arr, n);

 

}

}

//contributed by Arnab Kundu  
  
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

# Python3 program to sort only

# non primes

 

# from math import sqrt method

from math import sqrt

 

# Create a boolean array "prime[0..n]" 

# and initialize all entries it as true.

# A value in prime[i] will finally be false 

# if i is Not a prime, else true. 

prime = [0] * 100005

 

def SieveOfEratosthenes(n) :

 

 for i in range(len(prime)) :

 prime[i] = True

 

 prime[1] = False

 

 for p in range(2, int(sqrt(n)) + 1) :

 

 # If prime[p] is not changed, 

 # then it is a prime 

 if prime[p] == True :

 

 # Update all multiples of p 

 for i in range(p * 2, n, p) :

 prime[i] = False

 

 

# Function to print the array such that 

# only non primes are sorted 

def sortedArray(arr, n) :

 

 SieveOfEratosthenes(100005)

 

 # list v will store all non 

 # prime numbers 

 v = []

 

 # If not prime, insert into list

 for i in range(n) :

 if prime[arr[i]] == 0 :

 v.append(arr[i])

 

 # sorting list of non primes 

 v.sort()

 

 j = 0

 

 # print the required array

 for i in range(n) :

 

 if prime[arr[i]] == True :

 print(arr[i],end = " ")

 else :

 print(v[j],end = " ")

 j += 1

 

 

# Driver code

if __name__ == "__main__" :

 

 n = 6

 arr = [100, 11, 500, 2, 17, 1]

 

 sortedArray(arr, n)

 

# This code is contributed by 

# ANKITRAI1  
  
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

// C# program to sort only non primes

using System;

using System.Collections.Generic;

 

class GFG

{

 // Create a boolean array "prime[0..n]" 

 // and initialize all entries it as true.

 // A value in prime[i] will finally be

 // false if i is Not a prime, else true.

 static bool []prime = new bool[100006];

 

 static void SieveOfEratosthenes(int n)

 {

 

 for(int i = 1; i <= n; i++)

 prime[i] = true;

 prime[1] = false;

 

 for (int p = 2; p * p <= n; p++) 

 {

 // If prime[p] is not changed, then it is a prime

 if (prime[p] == true)

 {

 // Update all multiples of p

 for (int i = p * 2; i <= n; i += p)

 prime[i] = false;

 }

 }

 }

 

 // Function to print the array such that

 // only non primes are sorted

 static void sortedArray(int []arr, int n)

 {

 SieveOfEratosthenes(100005);

 

 // vector v will store all non

 // prime numbers

 List<int> v = new List<int>();

 

 // If not prime, insert into vector

 for (int i = 0; i < n; ++i)

 {

 if (prime[arr[i]] == false)

 v.Add(arr[i]);

 }

 

 // sorting vector of non primes

 v.Sort();

 

 int j = 0;

 // print the required array

 for (int i = 0; i < n; ++i) 

 {

 if (prime[arr[i]] == true)

 Console.Write( arr[i] + " ");

 else

 {

 Console.Write( v[j] + " ");

 j++;

 }

 }

 }

 

 // Driver Code

 public static void Main()

 {

 

 int n = 6;

 int []arr = { 100, 11, 500, 2, 17, 1 };

 

 sortedArray(arr, n);

 }

}

 

/* This code contributed by PrinciRaj1992 */  
  
---  
  
 __

 __

 **Output:**

    
    
    1 11 100 2 17 500
    

**Time Complexity:** ![O\(Nlog\(N\)\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-9114eb1669acc31c766f05c7d3550ce2_l3.png)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

