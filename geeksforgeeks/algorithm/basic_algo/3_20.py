Finding the Parity of a number Efficiently



Given an integer N. The task is to write a program to find the parity of the
given number.  
**Note** : Parity of a number is used to define if the total number of set-
bits(1-bit in binary representation) in a number is even or odd. If the total
number of set-bits in the binary representation of a number is even then the
number is said to have even parity, otherwise, it will have odd parity.

 **Examples** :

> **Input** : N = 13  
> **Output** : Odd Parity  
>  **Explanation:**  
>  Binary representation of 13 is (1101)
>
>  **Input** : N = 9 (1001)  
>  **Output** : Even Parity

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

The parity of a number represented by 32-bits can be efficiently calculated by
performing the following operations.  
Let the given number be x, then perform the below operations:

  

  

  * y = x^(x>>1)
  * y = y^(y>>2)
  * y = y^(y>>4)
  * y = y^(y>>8)
  * y = y^(y>>16)

Now, the rightmost bit in y will represent the parity of x. If the rightmost
bit is 1, then x will have odd parity and if it is 0 then x will have even
parity.  
So, in order to extract the last bit of y, perform bit-wise AND operation of y
with 1.

**Why does this work?**

> Consider that we want to find the parity of n = 150 = 1001 0110 (in binary).
>
> 1\. Let’s divide this number into two parts and xor them and assign it to n:
> n = n ^ (n >> 4) = 1001 ^ 0110 = 1111.
>
> Dissimilar bits result in a 1 bit in the result while similar bits result in
> a 0. We have basically considered all 8 bits to arrive at this intermediate
> result. So, effectively we have nullified even parities within the number.
>
> Now repeat step 1 again until you end up with a single bit.  
> n = n ^ (n >> 2) = 11 ^ 11 = 00  
> n = n ^ (n >> 1) = 0 ^ 0 = 0  
> Final result = n & 1 = 0
>
>  **Another example:**
>
> n = 1000 0101  
> n = n ^ (n >> 4) = 1000 ^ 0101 = 1101  
> n = n ^ (n >> 2) = 11 ^ 01 = 10  
> n = n ^ (n >> 1) = 1 ^ 0 = 1  
> Final result = n & 1 = 1
    
    
    if(y&1==1)
        odd Parity
    else
        even Parity

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// Program to find the parity of a given number

#include <bits/stdc++.h>

using namespace std;

// Function to find the parity

bool findParity(int x)

{

 int y = x ^ (x >> 1);

 y = y ^ (y >> 2);

 y = y ^ (y >> 4);

 y = y ^ (y >> 8);

 y = y ^ (y >> 16);

 // Rightmost bit of y holds the parity value

 // if (y&1) is 1 then parity is odd else even

 if (y & 1)

 return 1;

 return 0;

}

// Driver code

int main()

{

 (findParity(9)==0)?cout<<"Even Parity\n":

 cout<<"Odd Parity\n";

 

 (findParity(13)==0)?cout<<"Even Parity\n":

 cout<<"Odd Parity\n";

 

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

// Program to find the

// parity of a given number

import java.io.*;

class GFG

{

// Function to find the parity

static boolean findParity(int x)

{

 int y = x ^ (x >> 1);

 y = y ^ (y >> 2);

 y = y ^ (y >> 4);

 y = y ^ (y >> 8);

 y = y ^ (y >> 16);

 // Rightmost bit of y holds

 // the parity value

 // if (y&1) is 1 then parity

 // is odd else even

 if ((y & 1) > 0)

 return true;

 return false;

}

// Driver code

public static void main (String[] args)

{

 if((findParity(9) == false))

 System.out.println("Even Parity");

 else

 System.out.println("Odd Parity");

 

 if(findParity(13) == false)

 System.out.println("Even Parity");

 else

 System.out.println("Odd Parity");

}

}

// This Code is Contributed by chandan_jnu.  
  
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

# Program to find the

# parity of a given number

# Function to find the parity

def findParity(x):

 y = x ^ (x >> 1);

 y = y ^ (y >> 2);

 y = y ^ (y >> 4);

 y = y ^ (y >> 8);

 y = y ^ (y >> 16);

 # Rightmost bit of y holds

 # the parity value if (y&1)

 # is 1 then parity is odd

 # else even

 if (y & 1):

 return 1;

 return 0;

# Driver code

if(findParity(9) == 0):

 print("Even Parity");

else:

 print("Odd Parity\n");

if(findParity(13) == 0):

 print("Even Parity");

else:

 print("Odd Parity");

 

# This code is contributed by mits  
  
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

// Program to find the

// parity of a given number

using System;

class GFG

{

// Function to find the parity

static bool findParity(int x)

{

 int y = x ^ (x >> 1);

 y = y ^ (y >> 2);

 y = y ^ (y >> 4);

 y = y ^ (y >> 8);

 y = y ^ (y >> 16);

 // Rightmost bit of y holds

 // the parity value

 // if (y&1) is 1 then parity

 // is odd else even

 if ((y & 1) > 0)

 return true;

 return false;

}

// Driver code

public static void Main ()

{

 if((findParity(9) == false))

 Console.WriteLine("Even Parity");

 else

 Console.WriteLine("Odd Parity");

 

 if(findParity(13) == false)

 Console.WriteLine("Even Parity");

 else

 Console.WriteLine("Odd Parity");

}

}

// This Code is Contributed

// by chandan_jnu  
  
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

// Program to find the

// parity of a given number

// Function to find the parity

function findParity($x)

{

 $y = $x ^ ($x >> 1);

 $y = $y ^ ($y >> 2);

 $y = $y ^ ($y >> 4);

 $y = $y ^ ($y >> 8);

 $y = $y ^ ($y >> 16);

 // Rightmost bit of y holds

 // the parity value if (y&1)

 // is 1 then parity is odd

 // else even

 if ($y & 1)

 return 1;

 return 0;

}

// Driver code

(findParity(9) == 0) ?

 print("Even Parity\n"):

 print("Odd Parity\n");

(findParity(13) == 0) ?

print("Even Parity\n"):

print("Odd Parity\n");

 

// This Code is Contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    Even Parity
    Odd Parity

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

