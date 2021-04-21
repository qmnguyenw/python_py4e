Check whether a number has consecutive 0’s in the given base or not



Given a decimal number N, the task is to check if a number has consecutive
zeroes or not after converting the number to its K-based notation.

 **Examples:**

> Input: N = 4, K = 2  
> Output: No  
> 4 in base 2 is 100, As there are consecutive 2 thus the answer is No.
>
> Input: N = 15, K = 8  
> Output: Yes  
> 15 in base 8 is 17, As there are no consecutive 0 so the answer is Yes.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach** : First convert the number N into base K and then simply check
if the number has consecutive zeroes or not.

  

  

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

#include<bits/stdc++.h>

using namespace std;

// Function to convert N into base K

int toK(int N, int K)

{

// Weight of each digit

 int w = 1;

 int s = 0;

 while (N != 0)

 {

 int r = N % K;

 N = N/K;

 s = r * w + s;

 w *= 10;

 }

 return s;

}

// Function to check for consecutive 0

bool check(int N)

{

// Flag to check if there are consecutive

 // zero or not

 bool fl = false;

 while (N != 0)

 {

 int r = N % 10;

 N = N/10;

 // If there are two consecutive zero

 // then returning False

 if (fl == true and r == 0)

 return false;

 if (r > 0)

 {

 fl = false;

 continue;

 }

 fl = true;

 }

 return true;

 

}

// We first convert to given base, then

// check if the converted number has two

// consecutive 0s or not

void hasConsecutiveZeroes(int N, int K)

{

 int z = toK(N, K);

 if (check(z))

 cout<<"Yes"<<endl;

 else

 cout<<"No"<<endl;

}

 

// Driver code

int main()

{

int N = 15;

int K = 8;

hasConsecutiveZeroes(N, K);

}

// This code is contributed by

// Surendra_Gangwar  
  
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

// Function to convert N into base K

static int toK(int N, int K)

{

 // Weight of each digit

 int w = 1;

 int s = 0;

 while (N != 0)

 {

 int r = N % K;

 N = N / K;

 s = r * w + s;

 w *= 10;

 }

 return s;

}

// Function to check for consecutive 0

static boolean check(int N)

{

 // Flag to check if there are consecutive

 // zero or not

 boolean fl = false;

 while (N != 0)

 {

 int r = N % 10;

 N = N / 10;

 // If there are two consecutive zero

 // then returning False

 if (fl == true && r == 0)

 return false;

 if (r > 0)

 {

 fl = false;

 continue;

 }

 fl = true;

 }

 return true;

}

// We first convert to given base, then

// check if the converted number has two

// consecutive 0s or not

static void hasConsecutiveZeroes(int N, int K)

{

 int z = toK(N, K);

 if (check(z))

 System.out.println("Yes");

 else

 System.out.println("No");

}

// Driver code

public static void main(String[] args)

{

 int N = 15;

 int K = 8;

 hasConsecutiveZeroes(N, K);

}

}

// This code is contributed by Princi Singh  
  
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

# Python implementation of the above approach

# We first convert to given base, then

# check if the converted number has two

# consecutive 0s or not

def hasConsecutiveZeroes(N, K):

 z = toK(N, K)

 if (check(z)):

 print("Yes")

 else:

 print("No")

# Function to convert N into base K

def toK(N, K):

 # Weight of each digit

 w = 1

 s = 0

 while (N != 0):

 r = N % K

 N = N//K

 s = r * w + s

 w* = 10

 return s

# Function to check for consecutive 0

def check(N):

 # Flag to check if there are consecutive

 # zero or not

 fl = False

 while (N != 0):

 r = N % 10

 N = N//10

 # If there are two consecutive zero

 # then returning False

 if (fl == True and r == 0):

 return False

 if (r > 0):

 fl = False

 continue

 fl = True

 return True

# Driver code

N, K = 15, 8

hasConsecutiveZeroes(N, K)  
  
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

// Function to convert N into base K

static int toK(int N, int K)

{

 // Weight of each digit

 int w = 1;

 int s = 0;

 while (N != 0)

 {

 int r = N % K;

 N = N / K;

 s = r * w + s;

 w *= 10;

 }

 return s;

}

// Function to check for consecutive 0

static Boolean check(int N)

{

 // Flag to check if there are consecutive

 // zero or not

 Boolean fl = false;

 while (N != 0)

 {

 int r = N % 10;

 N = N / 10;

 // If there are two consecutive zero

 // then returning False

 if (fl == true && r == 0)

 return false;

 if (r > 0)

 {

 fl = false;

 continue;

 }

 fl = true;

 }

 return true;

}

// We first convert to given base, then

// check if the converted number has two

// consecutive 0s or not

static void hasConsecutiveZeroes(int N, int K)

{

 int z = toK(N, K);

 if (check(z))

 Console.WriteLine("Yes");

 else

 Console.WriteLine("No");

}

// Driver code

public static void Main(String[] args)

{

 int N = 15;

 int K = 8;

 hasConsecutiveZeroes(N, K);

}

}

// This code is contributed by 29AjayKumar  
  
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

// We first convert to given base,

// then check if the converted number

// has two consecutive 0s or not

function hasConsecutiveZeroes($N, $K)

{

 $z = toK($N, $K);

 if (check($z))

 print("Yes");

 else

 print("No");

}

// Function to convert N into base K

function toK($N, $K)

{

 // Weight of each digit

 $w = 1;

 $s = 0;

 while ($N != 0)

 {

 $r = $N % $K;

 $N = (int)($N / $K);

 $s = $r * $w + $s;

 $w *= 10;

 }

 return $s;

}

// Function to check for consecutive 0

function check($N)

{

 // Flag to check if there are

 // consecutive zero or not

 $fl = false;

 while ($N != 0)

 {

 $r = $N % 10;

 $N = (int)($N / 10);

 // If there are two consecutive

 // zero then returning false

 if ($fl == true and $r == 0)

 return false;

 if ($r > 0)

 {

 $fl = false;

 continue;

 }

 $fl = true;

 }

 return true;

}

// Driver code

$N = 15;

$K = 8;

hasConsecutiveZeroes($N, $K);

// This code is contributed by mits

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

// Javascript implementation of the above approach

// Function to convert N into base K

function toK(N, K)

{

 

 // Weight of each digit

 let w = 1;

 let s = 0;

 

 while (N != 0)

 {

 let r = N % K;

 N = parseInt(N / K);

 s = r * w + s;

 w *= 10;

 }

 return s;

}

// Function to check for consecutive 0

function check(N)

{

 

 // Flag to check if there are consecutive

 // zero or not

 let fl = false;

 

 while (N != 0)

 {

 let r = N % 10;

 N = parseInt(N/10);

 // If there are two consecutive zero

 // then returning False

 if (fl == true && r == 0)

 return false;

 if (r > 0)

 {

 fl = false;

 continue;

 }

 fl = true;

 }

 return true;

}

// We first convert to given base, then

// check if the converted number has two

// consecutive 0s or not

function hasConsecutiveZeroes(N, K)

{

 let z = toK(N, K);

 if (check(z))

 document.write("Yes");

 else

 document.write("No");

}

// Driver code

let N = 15;

let K = 8;

hasConsecutiveZeroes(N, K);

// This code is contributed by souravmahato348

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

