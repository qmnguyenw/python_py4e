Pairs from an array that satisfy the given condition



Given an array **arr[]** , the task is to count all the valid pairs from the
array. A pair **(arr[i], arr[j])** is said to be valid if **func( arr[i] ) +
func( arr[j] ) = func( XOR(arr[i], arr[j]) )** where **func(x)** returns the
number of **set bits** in **x**.

 **Examples:**

> **Input:** arr[] = {2, 3, 4, 5, 6}  
> **Output:** 3  
> (2, 4), (2, 5) and (3, 4) are the only valid pairs.
>
>  **Input:** arr[] = {12, 13, 34, 25, 6}  
> **Output:** 4  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:** Iterating every possible pair and check whether the pair
satisfies the given condition. If the condition is satisfied then update
**count = count + 1**. Print the **count** in the end.

  

  

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

#include <bits/stdc++.h>

using namespace std;

// Function to return the number

// of set bits in n

int setBits(int n)

{

 int count = 0;

 while (n) {

 n = n & (n - 1);

 count++;

 }

 return count;

}

// Function to return the count of required pairs

int countPairs(int a[], int n)

{

 int count = 0;

 for (int i = 0; i < n - 1; i++) {

 // Set bits for first element of the pair

 int setbits_x = setBits(a[i]);

 for (int j = i + 1; j < n; j++) {

 // Set bits for second element of the pair

 int setbits_y = setBits(a[j]);

 // Set bits of the resultant number which is

 // the XOR of both the elements of the pair

 int setbits_xor_xy = setBits(a[i] ^ a[j]);

 // If the condition is satisfied

 if (setbits_x + setbits_y == setbits_xor_xy)

 // Increment the count

 count++;

 }

 }

 // Return the total count

 return count;

}

// Driver code

int main()

{

 int a[] = { 2, 3, 4, 5, 6 };

 int n = sizeof(a) / sizeof(a[0]);

 cout << countPairs(a, n);

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

class GFG

{

 

// Function to return the number

// of set bits in n

static int setBits(int n)

{

 int count = 0;

 while (n > 0)

 {

 n = n & (n - 1);

 count++;

 }

 return count;

}

// Function to return the count of

// required pairs

static int countPairs(int a[], int n)

{

 int count = 0;

 for (int i = 0; i < n - 1; i++)

 {

 // Set bits for first element

 // of the pair

 int setbits_x = setBits(a[i]);

 for (int j = i + 1; j < n; j++)

 {

 // Set bits for second element

 // of the pair

 int setbits_y = setBits(a[j]);

 // Set bits of the resultant number which is

 // the XOR of both the elements of the pair

 int setbits_xor_xy = setBits(a[i] ^ a[j]);

 // If the condition is satisfied

 if (setbits_x + setbits_y == setbits_xor_xy)

 // Increment the count

 count++;

 }

 }

 // Return the total count

 return count;

}

 // Driver code

 public static void main (String[] args)

 {

 int []a = { 2, 3, 4, 5, 6 };

 int n = a.length;

 System.out.println(countPairs(a, n));

 }

}

// This code is contributed by ajit.  
  
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

# Function to return the number

# of set bits in n

def setBits(n):

 count = 0

 while (n):

 n = n & (n - 1)

 count += 1

 return count

# Function to return the count

# of required pairs

def countPairs(a, n):

 count = 0

 for i in range(0, n - 1, 1):

 

 # Set bits for first element

 # of the pair

 setbits_x = setBits(a[i])

 for j in range(i + 1, n, 1):

 

 # Set bits for second element

 # of the pair

 setbits_y = setBits(a[j])

 # Set bits of the resultant number

 # which is the XOR of both the

 # elements of the pair

 setbits_xor_xy = setBits(a[i] ^ a[j]);

 # If the condition is satisfied

 if (setbits_x +

 setbits_y == setbits_xor_xy):

 

 # Increment the count

 count += 1

 # Return the total count

 return count

# Driver code

if __name__ == '__main__':

 a = [2, 3, 4, 5, 6]

 n = len(a)

 print(countPairs(a, n))

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

class GFG

{

// Function to return the number

// of set bits in n

static int setBits(int n)

{

 int count = 0;

 while (n > 0)

 {

 n = n & (n - 1);

 count++;

 }

 return count;

}

// Function to return the count of

// required pairs

static int countPairs(int []a, int n)

{

 int count = 0;

 for (int i = 0; i < n - 1; i++)

 {

 // Set bits for first element

 // of the pair

 int setbits_x = setBits(a[i]);

 for (int j = i + 1; j < n; j++)

 {

 // Set bits for second element

 // of the pair

 int setbits_y = setBits(a[j]);

 // Set bits of the resultant number which is

 // the XOR of both the elements of the pair

 int setbits_xor_xy = setBits(a[i] ^ a[j]);

 // If the condition is satisfied

 if (setbits_x + setbits_y == setbits_xor_xy)

 // Increment the count

 count++;

 }

 }

 // Return the total count

 return count;

}

// Driver code

public static void Main()

{

 int []a = { 2, 3, 4, 5, 6 };

 int n = a.Length;

 Console.Write(countPairs(a, n));

}

}

// This code is contributed

// by Akanksha Rai  
  
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

// Function to return the number

// of set bits in n

function setBits($n)

{

 $count = 0;

 while ($n)

 {

 $n = $n & ($n - 1);

 $count++;

 }

 return $count;

}

// Function to return the count of

// required pairs

function countPairs(&$a, $n)

{

 $count = 0;

 for ($i = 0; $i < $n - 1; $i++)

 {

 // Set bits for first element

 // of the pair

 $setbits_x = setBits($a[$i]);

 for ($j = $i + 1; $j < $n; $j++)

 {

 // Set bits for second element of the pair

 $setbits_y = setBits($a[$j]);

 // Set bits of the resultant number which is

 // the XOR of both the elements of the pair

 $setbits_xor_xy = setBits($a[$i] ^ $a[$j]);

 // If the condition is satisfied

 if ($setbits_x +

 $setbits_y == $setbits_xor_xy)

 // Increment the count

 $count++;

 }

 }

 // Return the total count

 return $count;

}

// Driver code

$a = array(2, 3, 4, 5, 6 );

$n = sizeof($a) / sizeof($a[0]);

echo countPairs($a, $n);

// This code is contributed by ita_c

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

 

// Function to return the number

// of set bits in n

function setBits(n)

{

 let count = 0;

 

 while (n > 0)

 {

 n = n & (n - 1);

 count++;

 }

 return count;

}

// Function to return the count of

// required pairs

function countPairs(a, n)

{

 let count = 0;

 

 for(let i = 0; i < n - 1; i++)

 {

 

 // Set bits for first element

 // of the pair

 let setbits_x = setBits(a[i]);

 

 for(let j = i + 1; j < n; j++)

 {

 

 // Set bits for second element

 // of the pair

 let setbits_y = setBits(a[j]);

 

 // Set bits of the resultant number which is

 // the XOR of both the elements of the pair

 let setbits_xor_xy = setBits(a[i] ^ a[j]);

 

 // If the condition is satisfied

 if (setbits_x + setbits_y == setbits_xor_xy)

 

 // Increment the count

 count++;

 }

 }

 

 // Return the total count

 return count;

}

// Driver code

let a = [ 2, 3, 4, 5, 6 ];

let n = a.length;

document.write(countPairs(a, n));

// This code is contributed by unknown2108

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    3

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

