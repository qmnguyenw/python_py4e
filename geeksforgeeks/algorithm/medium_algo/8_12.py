Count pairs in array whose sum is divisible by K



Given an array **A[]** and positive integer **K** , the task is to count total
number of pairs in the array whose sum is divisible by **K**.  
Note : This question is generalised version of this  
**Examples:**

    
    
    **Input :** A[] = {2, 2, 1, 7, 5, 3}, K = 4
    **Output :** 5
    **Explanation :**
    There are five pairs possible whose sum
    is divisible by '4' i.e., (2, 2), 
    (1, 7), (7, 5), (1, 3) and (5, 3)
    
    **Input :** A[] = {5, 9, 36, 74, 52, 31, 42}, K = 3
    **Output :** 7

Recommended: Please solve it on _**_PRACTICE_**_ first, before moving on to
the solution.

 **Naive Approach** : The simplest approach is to iterate through every pair
of the array but using two nested for loops and count those pairs whose sum is
divisible by ‘K’. Time complexity of this approach is O(N2).  
 **Efficient Approach** : An efficient approach is to use Hashing technique.
We will separate elements into buckets depending on their (value mod K). When
a number is divided by K then the remainder may be 0, 1, 2, upto (k-1). So
take an array say **freq[]** of size K (initialized with Zero) and increase
the value of freq[A[i]%K] so that we can calculate the number of values giving
remainder j on division with K.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program to count pairs

// whose sum divisible by 'K'

#include <bits/stdc++.h>

using namespace std;

// Program to count pairs whose sum divisible

// by 'K'

int countKdivPairs(int A[], int n, int K)

{

 // Create a frequency array to count

 // occurrences of all remainders when

 // divided by K

 int freq[K] = { 0 };

 // Count occurrences of all remainders

 for (int i = 0; i < n; i++)

 ++freq[A[i] % K];

 // If both pairs are divisible by 'K'

 int sum = freq[0] * (freq[0] - 1) / 2;

 // count for all i and (k-i)

 // freq pairs

 for (int i = 1; i <= K / 2 && i != (K - i); i++)

 sum += freq[i] * freq[K - i];

 // If K is even

 if (K % 2 == 0)

 sum += (freq[K / 2] * (freq[K / 2] - 1) / 2);

 return sum;

}

// Driver code

int main()

{

 int A[] = { 2, 2, 1, 7, 5, 3 };

 int n = sizeof(A) / sizeof(A[0]);

 int K = 4;

 cout << countKdivPairs(A, n, K);

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

// Java program to count pairs

// whose sum divisible by 'K'

import java.util.*;

class Count {

 public static int countKdivPairs(int A[], int n, int K)

 {

 // Create a frequency array to count

 // occurrences of all remainders when

 // divided by K

 int freq[] = new int[K];

 // Count occurrences of all remainders

 for (int i = 0; i < n; i++)

 ++freq[A[i] % K];

 // If both pairs are divisible by 'K'

 int sum = freq[0] * (freq[0] - 1) / 2;

 // count for all i and (k-i)

 // freq pairs

 for (int i = 1; i <= K / 2 && i != (K - i); i++)

 sum += freq[i] * freq[K - i];

 // If K is even

 if (K % 2 == 0)

 sum += (freq[K / 2] * (freq[K / 2] - 1) / 2);

 return sum;

 }

 public static void main(String[] args)

 {

 int A[] = { 2, 2, 1, 7, 5, 3 };

 int n = 6;

 int K = 4;

 System.out.print(countKdivPairs(A, n, K));

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

# Python3 code to count pairs whose

# sum is divisible by 'K'

# Function to count pairs whose

# sum is divisible by 'K'

def countKdivPairs(A, n, K):

 

 # Create a frequency array to count

 # occurrences of all remainders when

 # divided by K

 freq = [0] * K

 

 # Count occurrences of all remainders

 for i in range(n):

 freq[A[i] % K]+= 1

 

 # If both pairs are divisible by 'K'

 sum = freq[0] * (freq[0] - 1) / 2;

 

 # count for all i and (k-i)

 # freq pairs

 i = 1

 while(i <= K//2 and i != (K - i) ):

 sum += freq[i] * freq[K-i]

 i+= 1

 # If K is even

 if( K % 2 == 0 ):

 sum += (freq[K//2] *
(freq[K//2]-1)/2);

 

 return int(sum)

# Driver code

A = [2, 2, 1, 7, 5, 3]

n = len(A)

K = 4

print(countKdivPairs(A, n, K))  
  
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

// C# program to count pairs

// whose sum divisible by 'K'

using System;

class Count

{

 public static int countKdivPairs(int []A, int n, int K)

 {

 // Create a frequency array to count

 // occurrences of all remainders when

 // divided by K

 int []freq = new int[K];

 // Count occurrences of all remainders

 for (int i = 0; i < n; i++)

 ++freq[A[i] % K];

 // If both pairs are divisible by 'K'

 int sum = freq[0] * (freq[0] - 1) / 2;

 // count for all i and (k-i)

 // freq pairs

 for (int i = 1; i <= K / 2 && i != (K - i); i++)

 sum += freq[i] * freq[K - i];

 

 // If K is even

 if (K % 2 == 0)

 sum += (freq[K / 2] * (freq[K / 2] - 1) / 2);

 return sum;

 }

 

 // Driver code

 static public void Main ()

 {

 int []A = { 2, 2, 1, 7, 5, 3 };

 int n = 6;

 int K = 4;

 Console.WriteLine(countKdivPairs(A, n, K));

 }

}

// This code is contributed by akt_mit.  
  
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

// PHP Program to count pairs

// whose sum divisible by 'K'

// Program to count pairs whose sum

// divisible by 'K'

function countKdivPairs($A, $n, $K)

{

 

 // Create a frequency array to count

 // occurrences of all remainders when

 // divided by K

 $freq = array_fill(0, $K, 0);

 // Count occurrences of all remainders

 for ($i = 0; $i < $n; $i++)

 ++$freq[$A[$i] % $K];

 // If both pairs are divisible by 'K'

 $sum = (int)($freq[0] * ($freq[0] - 1) / 2);

 // count for all i and (k-i)

 // freq pairs

 for ($i = 1; $i <= $K / 2 &&

 $i != ($K - $i); $i++)

 $sum += $freq[$i] * $freq[$K - $i];

 

 // If K is even

 if ($K % 2 == 0)

 $sum += (int)($freq[(int)($K / 2)] *

 ($freq[(int)($K / 2)] - 1) / 2);

 return $sum;

}

// Driver code

$A = array( 2, 2, 1, 7, 5, 3 );

$n = count($A);

$K = 4;

echo countKdivPairs($A, $n, $K);

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output :**

    
    
     5

 **Time complexity:** O(N)  
**Auxiliary space:** O(K)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

