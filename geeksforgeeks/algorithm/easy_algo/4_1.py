Find the number of pairs (a, b) such that a % b = K



Given two integers **N** and **K** where **N, K > 0**, the task is to find the
total number of pairs **(a, b)** where **1 ≤ a, b ≤ N** such that **a % b =
K**.

 **Examples:**

>  **Input:** N = 4, K = 2  
>  **Output:** 2  
> Only valid pairs are (2, 3) and (2, 4).
>
>  **Input:** N = 11, K = 5  
>  **Output:** 7

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** Run two loop from **1** to **n** and count all the pairs
**(i, j)** where **i % j = K**. The time complexity of this approach will be
**O(n 2)**.

  

  

 **Efficient approach:** Initially total **count = N – K** because all the
numbers from the range which are **> K** will give **K** as the remainder
after dividing it. After that, for all **i > K** there are exactly **(N – K) /
i** numbers which will give remainder as **K** after getting divided by **i**.

Below is the implementataion of the above approach:

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

 

// Function to return the count

// of required pairs

int CountAllPairs(int N, int K)

{

 

 int count = 0;

 

 if (N > K) {

 

 // Initial count

 count = N - K;

 for (int i = K + 1; i <= N; i++)

 count = count + ((N - K) / i);

 }

 

 return count;

}

 

// Driver code

int main()

{

 int N = 11, K = 5;

 

 cout << CountAllPairs(N, K);

 

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

 

 // Function to return the count

 // of required pairs

 static int CountAllPairs(int N, int K)

 {

 

 int count = 0;

 

 if (N > K) {

 

 // Initial count

 count = N - K;

 for (int i = K + 1; i <= N; i++)

 count = count + ((N - K) / i);

 }

 

 return count;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int N = 11, K = 5;

 System.out.println(CountAllPairs(N, K));

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

 

# Function to return the count 

# of required pairs

def CountAllPairs(N, K):

 count = 0

 if( N > K):

 

 # Initial count

 count = N - K

 for i in range(K + 1, N + 1):

 count = count + ((N - K) // i)

 

 return count

 

# Driver code

N = 11

K = 5

print(CountAllPairs(N, K))  
  
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

class GFG {

 

 // Function to return the count

 // of required pairs

 static int CountAllPairs(int N, int K)

 {

 

 int count = 0;

 

 if (N > K) {

 

 // Initial count

 count = N - K;

 for (int i = K + 1; i <= N; i++)

 count = count + ((N - K) / i);

 }

 

 return count;

 }

 

 // Driver code

 public static void Main()

 {

 int N = 11, K = 5;

 Console.WriteLine(CountAllPairs(N, K));

 }

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

 

// Function to return the count 

// of required pairs

function CountAllPairs($N, $K)

{

 $count = 0;

 

 if( $N > $K){

 

 // Initial count

 $count = $N - $K;

 for($i = $K+1; $i <= $N ; $i++)

 {

 $x = ((($N - $K) / $i));

 $count = $count + (int)($x);

 }

 }

 

 return $count;

}

 

 // Driver code

 $N = 11; 

 $K = 5;

 echo(CountAllPairs($N, $K));

 

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    7
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

