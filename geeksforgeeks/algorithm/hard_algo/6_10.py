Length of the smallest number which is divisible by K and formed by using 1’s
only



Given an integer **K** , the task is to find the length of the smallest no.
**N** which is divisible by **K** and formed by using 1 as its digits only. If
no such number exists then print **-1**  
 **Examples:**  

> **Input:** K = 3  
> **Output:** 3  
> 111 is the smallest number formed by using 1 only  
> which is divisible by 3.  
>  **Input:** K = 7  
> **Output:** 6  
> 111111 is the required number.  
>  **Input:** K = 12  
> **Output:** -1  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive approach:**  

  1. First we have to check if **K** is a multiple of either **2** or **5** then the answer will be **-1** because there is no number formed by using only **1’s** as its digits which is divisible by **2** or **5**.
  2. Now iterate for every possible no. formed by using **1’s** at most **K** times and check for its divisibility with **K**.

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

// Function to return length

// of the resulatant number

int numLen(int K)

{

 // If K is a multiple of 2 or 5

 if (K % 2 == 0 || K % 5 == 0)

 return -1;

 int number = 0;

 int len = 1;

 for (len = 1; len <= K; len++) {

 // Generate all possible numbers

 // 1, 11, 111, 111, ..., K 1's

 number = number * 10 + 1;

 // If number is divisible by k

 // then return the length

 if ((number % K == 0))

 return len;

 }

 return -1;

}

// Driver code

int main()

{

 int K = 7;

 cout << numLen(K);

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

class GFG

{

 // Function to return length

 // of the resulatant number

 static int numLen(int K)

 {

 // If K is a multiple of 2 or 5

 if (K % 2 == 0 || K % 5 == 0)

 {

 return -1;

 }

 int number = 0;

 int len = 1;

 for (len = 1; len <= K; len++)

 {

 // Generate all possible numbers

 // 1, 11, 111, 111, ..., K 1's

 number = number * 10 + 1;

 // If number is divisible by k

 // then return the length

 if ((number % K == 0))

 {

 return len;

 }

 }

 return -1;

 }

 // Driver code

 public static void main(String[] args)

 {

 int K = 7;

 System.out.println(numLen(K));

 }

}

/* This code contributed by PrinciRaj1992 */  
  
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

# Python implementation of the approach

# Function to return length

# of the resulatant number

def numLen(K):

 # If K is a multiple of 2 or 5

 if (K % 2 == 0 or K % 5 == 0):

 return -1;

 number = 0;

 len = 1;

 for len in range(1,K+1):

 # Generate all possible numbers

 # 1, 11, 111, 111, ..., K 1's

 number = number * 10 + 1;

 # If number is divisible by k

 # then return the length

 if ((number % K == 0)):

 return len;

 return -1;

# Driver code

K = 7;

print(numLen(K));

# This code contributed by Rajput-Ji  
  
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

 

// Function to return length

// of the resulatant number

static int numLen(int K)

{

 // If K is a multiple of 2 or 5

 if (K % 2 == 0 || K % 5 == 0)

 return -1;

 int number = 0;

 int len = 1;

 for (len = 1; len <= K; len++)

 {

 // Generate all possible numbers

 // 1, 11, 111, 111, ..., K 1's

 number = number * 10 + 1;

 // If number is divisible by k

 // then return the length

 if ((number % K == 0))

 return len;

 }

 return -1;

}

// Driver code

static void Main()

{

 int K = 7;

 Console.WriteLine(numLen(K));

}

}

// This code is contributed by mits  
  
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

// Function to return length

// of the resulatant number

function numLen($K)

{

 // If K is a multiple of 2 or 5

 if ($K % 2 == 0 || $K % 5 == 0)

 return -1;

 $number = 0;

 $len = 1;

 for ($len = 1; $len <= $K; $len++)

 {

 // Generate all possible numbers

 // 1, 11, 111, 111, ..., K 1's

 $number = $number * 10 + 1;

 // If number is divisible by k

 // then return the length

 if (($number % $K == 0))

 return $len;

 }

 return -1;

}

// Driver code

$K = 7;

echo numLen($K);

// This code is contributed by Akanksha Rai

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

// javascript implementation of the approach 

// Function to return length

 // of the resulatant number

 function numLen(K) {

 // If K is a multiple of 2 or 5

 if (K % 2 == 0 || K % 5 == 0) {

 return -1;

 }

 var number = 0;

 var len = 1;

 for (len = 1; len <= K; len++)

 {

 // Generate all possible numbers

 // 1, 11, 111, 111, ..., K 1's

 number = number * 10 + 1;

 // If number is divisible by k

 // then return the length

 if ((number % K == 0)) {

 return len;

 }

 }

 return -1;

 }

 // Driver code 

 var K = 7;

 document.write(numLen(K));

// This code is contributed by Princi Singh

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    6

**Efficient Approach:** As we see in the above approach we generate all
possible numbers like **1, 11, 1111, 11111, …, K times** but if the value of
**K** is very large then the no. will be out of range of data type so we can
make use of the modular properties.  
Instead of doing **number = number * 10 + 1** , we can do better as **number =
(number * 10 + 1) % K**  
**Explanation:** We start with **number = 1** and repeatedly do **number =
number * 10 + 1** then in each iteration we’ll get a new term of the above
sequence.  

> 1*10 + 1 = 11  
> 11*10 + 1 = 111  
> 111*10 + 1 = 1111  
> 1111*10 + 1 = 11111  
> 11111*10 + 1 = 111111  
>

Since we are repeatedly taking the remainders of the number at each step, at
each step we have, **newNum = oldNum * 10 + 1** .By the rules of modular
arithmetic **(a * b + c) % m** is same as **((a * b) % m + c % m) % m**. So,
it doesn’t matter whether **oldNum** is the remainder or the original number,
the answer would be correct.  
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

// Function to return length

// of the resulatant number

int numLen(int K)

{

 // If K is a multiple of 2 or 5

 if (K % 2 == 0 || K % 5 == 0)

 return -1;

 int number = 0;

 int len = 1;

 for (len = 1; len <= K; len++) {

 // Instead of generating all possible numbers

 // 1, 11, 111, 111, ..., K 1's

 // Take remainder with K

 number = (number * 10 + 1) % K;

 // If number is divisible by k

 // then remainder will be 0

 if (number == 0)

 return len;

 }

 return -1;

}

// Driver code

int main()

{

 int K = 7;

 cout << numLen(K);

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

class GFG {

 // Function to return length

 // of the resulatant number

 public static int numLen(int K)

 {

 // If K is a multiple of 2 or 5

 if (K % 2 == 0 || K % 5 == 0)

 return -1;

 int number = 0;

 int len = 1;

 for (len = 1; len <= K; len++) {

 // Instead of generating all possible numbers

 // 1, 11, 111, 111, ..., K 1's

 // Take remainder with K

 number = (number * 10 + 1) % K;

 // If number is divisible by k

 // then remainder will be 0

 if (number == 0)

 return len;

 }

 return -1;

 }

 // Driver code

 public static void main(String[] args)

 {

 int K = 7;

 System.out.print(numLen(K));

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

# Function to return length

# of the resulatant number

def numLen(K):

 

 # If K is a multiple of 2 or 5

 if(K % 2 == 0 or K % 5 == 0):

 return -1

 number = 0

 len = 1

 for len in range (1, K + 1):

 

 # Instead of generating all possible numbers

 # 1, 11, 111, 111, ..., K 1's

 # Take remainder with K

 number = ( number * 10 + 1 ) % K

 

 # If number is divisible by k

 # then remainder will be 0

 if number == 0:

 return len

 return -1

# Driver code

K = 7

print(numLen(K))  
  
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

// Function to return length

// of the resulatant number

public static int numLen(int K)

{

 // If K is a multiple of 2 or 5

 if (K % 2 == 0 || K % 5 == 0)

 return -1;

 int number = 0;

 int len = 1;

 for (len = 1; len <= K; len++)

 {

 // Instead of generating all possible numbers

 // 1, 11, 111, 111, ..., K 1's

 // Take remainder with K

 number = (number * 10 + 1) % K;

 // If number is divisible by k

 // then remainder will be 0

 if (number == 0)

 return len;

 }

 return -1;

}

// Driver code

public static void Main()

{

 int K = 7;

 Console.WriteLine(numLen(K));

}

}

// This code is contirbuted by Ryuga  
  
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

// Function to return length

// of the resulatant number

function numLen($K)

{

 // If K is a multiple of 2 or 5

 if ($K % 2 == 0 || $K % 5 == 0)

 return -1;

 $number = 0;

 $len = 1;

 for ($len = 1; $len <= $K; $len++)

 {

 // Instead of generating all possible numbers

 // 1, 11, 111, 111, ..., K 1's

 // Take remainder with K

 $number = ($number * 10 + 1) % $K;

 // If number is divisible by k

 // then remainder will be 0

 if ($number == 0)

 return $len;

 }

 return -1;

}

// Driver code

$K = 7;

echo numLen($K);

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

// javascript implementation of the approach 

// Function to return length

// of the resulatant number

function numLen(K)

{

 // If K is a multiple of 2 or 5

 if (K % 2 == 0 || K % 5 == 0)

 return -1;

 var number = 0;

 var len = 1;

 for (len = 1; len <= K; len++) {

 // Instead of generating all possible numbers

 // 1, 11, 111, 111, ..., K 1's

 // Take remainder with K

 number = (number * 10 + 1) % K;

 // If number is divisible by k

 // then remainder will be 0

 if (number == 0)

 return len;

 }

 return -1;

}

// Driver code

var K = 7;

document.write(numLen(K));

// This code contributed by shikhasingrajput

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    6

**Time Complexity:** O(K)  
**Auxiliary Space:** O(1)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

