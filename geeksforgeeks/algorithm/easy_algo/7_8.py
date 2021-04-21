Numbers less than N which are product of exactly two distinct prime numbers



Given a number ![N  ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-565caf8fc5ee54b6e74c09db3181dafb_l3.png). The task is to
find all such numbers less than N and are a product of exactly two distinct
prime numbers.  
For Example, 33 is the product of two distinct primes i.e 11 * 3, whereas
numbers like 60 which has three distinct prime factors i.e 2 * 2 * 3 * 5.  
 **Note** : These numbers cannot be a perfect square.  
 **Examples:**  

> **Input** : N = 30  
> **Output** : 6, 10, 14, 15, 21, 22, 26  
>  **Input** : N = 50  
> **Output** : 6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Algorithm** :  

  1. Traverse till N and check whether each number has exactly two prime factors or not.
  2. Now to avoid the situation like 49 having 7 * 7 product of two prime numbers, check whether the number is a perfect square or not to ensure that it has two distinct prime.
  3. If Step 1 and Step 2 satisfies then add the number in the vector list.
  4. Traverse the vector and print all the elements in it.

Below is the implementation of the above approach:  

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find numbers that are product

// of exactly two distinct prime numbers

#include <bits/stdc++.h>

using namespace std;

// Function to check whether a number

// is a PerfectSquare or not

bool isPerfectSquare(long double x)

{

 long double sr = sqrt(x);

 return ((sr - floor(sr)) == 0);

}

// Function to check if a number is a

// product of exactly two distinct primes

bool isProduct(int num)

{

 int cnt = 0;

 for (int i = 2; cnt < 2 && i * i <= num; ++i) {

 while (num % i == 0) {

 num /= i;

 ++cnt;

 }

 }

 if (num > 1)

 ++cnt;

 return cnt == 2;

}

// Function to find numbers that are product

// of exactly two distinct prime numbers.

void findNumbers(int N)

{

 // Vector to store such numbers

 vector<int> vec;

 for (int i = 1; i <= N; i++) {

 if (isProduct(i) && !isPerfectSquare(i)) {

 // insert in the vector

 vec.push_back(i);

 }

 }

 // Print all numers till n from the vector

 for (int i = 0; i < vec.size(); i++) {

 cout << vec[i] << " ";

 }

}

// Driver function

int main()

{

 int N = 30;

 findNumbers(N);

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

// Java program to find numbers that are product

// of exactly two distinct prime numbers

import java.util.*; 

class GFG{

// Function to check whether a number

// is a PerfectSquare or not

static boolean isPerfectSquare(double x)

{

 double sr = Math.sqrt(x);

 return ((sr - Math.floor(sr)) == 0);

}

// Function to check if a number is a

// product of exactly two distinct primes

static boolean isProduct(int num)

{

 int cnt = 0;

 for (int i = 2; cnt < 2 && i * i <= num; ++i) {

 while (num % i == 0) {

 num /= i;

 ++cnt;

 }

 }

 if (num > 1)

 ++cnt;

 return cnt == 2;

}

// Function to find numbers that are product

// of exactly two distinct prime numbers.

static void findNumbers(int N)

{

 // Vector to store such numbers

 Vector<Integer> vec = new Vector<Integer>();

 for (int i = 1; i <= N; i++) {

 if (isProduct(i) && !isPerfectSquare(i)) {

 // insert in the vector

 vec.add(i);

 }

 }

 // Print all numers till n from the vector

 Iterator<Integer> itr = vec.iterator(); 

 while(itr.hasNext()){ 

 System.out.print(itr.next()+" "); 

 } 

}

// Driver function

public static void main(String[] args)

{

 int N = 30;

 findNumbers(N);

}

}

// This Code is Contributed by mits  
  
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

# Python 3 program to find numbers that are product

# of exactly two distinct prime numbers

import math

# Function to check whether a number

# is a PerfectSquare or not

def isPerfectSquare(x):

 

 sr = math.sqrt(x)

 

 return ((sr - math.floor(sr)) == 0)

# Function to check if a number is a

# product of exactly two distinct primes

def isProduct( num):

 cnt = 0

 

 i = 2

 while cnt < 2 and i * i <= num:

 while (num % i == 0) :

 num //= i

 cnt += 1

 i += 1

 

 if (num > 1):

 cnt += 1

 

 return cnt == 2

 

# Function to find numbers that are product

# of exactly two distinct prime numbers.

def findNumbers(N):

 # Vector to store such numbers

 vec = []

 

 for i in range(1,N+1) :

 if (isProduct(i) and not isPerfectSquare(i)) :

 

 # insert in the vector

 vec.append(i)

 

 # Print all numers till n from the vector

 for i in range(len( vec)):

 print(vec[i] ,end= " ")

 

# Driver function

if __name__=="__main__":

 

 N = 30

 findNumbers(N)  
  
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

// C# program to find numbers that are product

// of exactly two distinct prime numbers

using System;

using System.Collections.Generic;

class GFG

{

 // Function to check whether a number

 // is a PerfectSquare or not

 static bool isPerfectSquare(double x)

 {

 double sr = Math.Sqrt(x);

 return ((sr - Math.Floor(sr)) == 0);

 }

 // Function to check if a number is a

 // product of exactly two distinct primes

 static bool isProduct(int num)

 {

 int cnt = 0;

 for (int i = 2; cnt < 2 && i * i <= num; ++i)

 {

 while (num % i == 0)

 {

 num /= i;

 ++cnt;

 }

 }

 if (num > 1)

 ++cnt;

 return cnt == 2;

 }

 // Function to find numbers that are product

 // of exactly two distinct prime numbers.

 static void findNumbers(int N)

 {

 // Vector to store such numbers

 List<int> vec = new List<int>();

 for (int i = 1; i <= N; i++)

 {

 if (isProduct(i) && !isPerfectSquare(i))

 {

 // insert in the vector

 vec.Add(i);

 }

 }

 // Print all numers till n from the vector

 foreach(var a in vec)

 Console.Write(a + " ");

 }

 // Driver code

 public static void Main(String[] args)

 {

 int N = 30;

 findNumbers(N);

 }

}

// This code has been contributed by 29AjayKumar  
  
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

// PHP program to find numbers that are product

// of exactly two distinct prime numbers

// Function to check whether a number

// is a PerfectSquare or not

function isPerfectSquare($x)

{

 $sr = sqrt($x);

 return (($sr - floor($sr)) == 0);

}

// Function to check if a number is a

// product of exactly two distinct primes

function isProduct($num)

{

 $cnt = 0;

 for ($i = 2; $cnt < 2 &&

 $i * $i <= $num; ++$i)

 {

 while ($num % $i == 0)

 {

 $num /= $i;

 ++$cnt;

 }

 }

 if ($num > 1)

 ++$cnt;

 return $cnt == 2;

}

// Function to find numbers that are product

// of exactly two distinct prime numbers.

function findNumbers($N)

{

 // Vector to store such numbers

 $vec = array();

 for ($i = 1; $i <= $N; $i++)

 {

 if (isProduct($i) &&

 !isPerfectSquare($i))

 {

 // insert in the vector

 array_push($vec, $i);

 }

 }

 // Print all numers till n from the vector

 for ($i = 0; $i < sizeof($vec); $i++)

 {

 echo $vec[$i] . " ";

 }

}

// Driver Code

$N = 30;

findNumbers($N);

// This code is contributed by ita_c  
  
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

// Javascript program to find numbers that are product

// of exactly two distinct prime numbers

// Function to check whether a number

// is a PerfectSquare or not

function isPerfectSquare(x)

{

 sr = Math.sqrt(x);

 return ((sr - Math.floor(sr)) == 0);

}

// Function to check if a number is a

// product of exactly two distinct primes

function isProduct(num)

{

 var cnt = 0;

 for(var i = 2; cnt < 2 && (i * i) <= num; ++i)

 {

 while (num % i == 0)

 {

 num = parseInt(num / i);

 ++cnt;

 }

 }

 if (num > 1)

 ++cnt;

 return cnt == 2;

}

// Function to find numbers that are product

// of exactly two distinct prime numbers.

function findNumbers( N)

{

 // Vector to store such numbers

 vec = [];

 for (var i = 1; i <= N; i++)

 {

 if (isProduct(i) && !isPerfectSquare(i))

 {

 // insert in the vector

 vec.push(i);

 }

 }

 // Print all numers till n from the vector

 for (var i = 0; i < vec.length; i++) {

 document.write(vec[i] + " ");

 }

}

// Driver function

var N = 30;

findNumbers(N);

// This code is contributed by noob2000.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    6 10 14 15 21 22 26

**Time Complexity:** O(![n  ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-3ebe7b3d5f19356fe8152deb8e32c84d_l3.png)*![$\\sqrt{n}$
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d9c873ac0baf7ca08365d58f0472305d_l3.png))  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

