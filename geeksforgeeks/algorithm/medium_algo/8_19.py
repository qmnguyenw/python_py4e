Find Nth positive number whose digital root is X



Given a number X ( 1<= X <= 9) and a positive number N, find the Nth positive
number whose **digital root** is X.  
 **Digital Root** : The digital root of a positive number is obtained by
iteratively summing up the digits of a number. On each iteration the number is
replaced by the sum of its digit and the iteration stops when the number is
reduced to a single digit number. This single digit number is known as the
digital root. For example, the digital root of 65 is 2, because 6 + 5 = 11 and
1 + 1 = 2.

 **Examples:**

> **Input** : X = 3, N = 100  
> **Output** : 894  
> The N-th Number whose digit root is X is 894
>
>  **Input** : X = 7, N = 43  
> **Output** : 385

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Simple Method** : The simple method is to start from 1 and calculate the
_digital root_ of every number, whenever we come across a number whose
_digital root_ is equal to X, we increase our counter by 1. We will stop our
search when our counter is equal to N.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the N-th number whose

// digital root is X

#include <bits/stdc++.h>

using namespace std;

// Function to find the digital root of

// a number

int findDigitalRoot(int num)

{

 int sum = INT_MAX, tempNum = num;

 while (sum >= 10) {

 sum = 0;

 while (tempNum > 0) {

 sum += tempNum % 10;

 tempNum /= 10;

 }

 tempNum = sum;

 }

 return sum;

}

// Function to find the Nth number with

// digital root as X

void findAnswer(int X, int N)

{

 // Counter variable to keep the

 // count of valid numbers

 int counter = 0;

 for (int i = 1; counter < N; ++i) {

 // Find digital root

 int digitalRoot = findDigitalRoot(i);

 // Check if is required answer or not

 if (digitalRoot == X) {

 ++counter;

 }

 // Print the answer if you have found it

 // and breakout of the loop

 if (counter == N) {

 cout << i;

 break;

 }

 }

}

// Driver Code

int main()

{

 int X = 1, N = 3;

 findAnswer(X, N);

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

// Java program to find the N-th number whose

// digital root is X

class GFG

{

// Function to find the digital root of

// a number

static int findDigitalRoot(int num)

{

 int sum = Integer.MAX_VALUE, tempNum = num;

 while (sum >= 10)

 {

 sum = 0;

 while (tempNum > 0)

 {

 sum += tempNum % 10;

 tempNum /= 10;

 }

 tempNum = sum;

 }

 return sum;

}

// Function to find the Nth number with

// digital root as X

static void findAnswer(int X, int N)

{

 // Counter variable to keep the

 // count of valid numbers

 int counter = 0;

 for (int i = 1; counter < N; ++i)

 {

 // Find digital root

 int digitalRoot = findDigitalRoot(i);

 // Check if is required answer or not

 if (digitalRoot == X)

 {

 ++counter;

 }

 // Print the answer if you have found it

 // and breakout of the loop

 if (counter == N)

 {

 System.out.print( i);

 break;

 }

 }

}

// Driver Code

public static void main(String args[])

{

 int X = 1, N = 3;

 findAnswer(X, N);

}

}

// This code is contributed by Arnab Kundu  
  
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

# Python3 program to find the N-th number whose

# digital root is X

import sys

# Function to find the digital root of

# a number

def findDigitalRoot(num):

 sum = sys.maxsize;

 tempNum = num;

 while (sum >= 10):

 sum = 0;

 while (tempNum > 0):

 sum += tempNum % 10;

 tempNum //= 10;

 tempNum = sum;

 return sum;

# Function to find the Nth number with

# digital root as X

def findAnswer(X, N):

 

 # Counter variable to keep the

 # count of valid numbers

 counter = 0;

 i = 0;

 while (counter < N):

 i += 1;

 

 # Find digital root

 digitalRoot = findDigitalRoot(i);

 

 # Check if is required answer or not

 if (digitalRoot == X):

 counter += 1;

 

 # Print the answer if you have found it

 # and breakout of the loop

 if (counter == N):

 print(i);

 break;

# Driver Code

if __name__ == '__main__':

 X = 1;

 N = 3;

 findAnswer(X, N);

# This code is contributed by 29AjayKumar  
  
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

// C# program to find the N-th number whose

// digital root is X

using System;

class GFG

{

// Function to find the digital root of

// a number

static int findDigitalRoot(int num)

{

 int sum = int.MaxValue, tempNum = num;

 while (sum >= 10)

 {

 sum = 0;

 while (tempNum > 0)

 {

 sum += tempNum % 10;

 tempNum /= 10;

 }

 tempNum = sum;

 }

 return sum;

}

// Function to find the Nth number with

// digital root as X

static void findAnswer(int X, int N)

{

 // Counter variable to keep the

 // count of valid numbers

 int counter = 0;

 for (int i = 1; counter < N; ++i)

 {

 // Find digital root

 int digitalRoot = findDigitalRoot(i);

 // Check if is required answer or not

 if (digitalRoot == X)

 {

 ++counter;

 }

 // Print the answer if you have found it

 // and breakout of the loop

 if (counter == N)

 {

 Console.Write( i);

 break;

 }

 }

}

// Driver Code

public static void Main(String []args)

{

 int X = 1, N = 3;

 findAnswer(X, N);

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

// PHP program to find the N-th number

// whose digital root is X

// Function to find the digital root

// of a number

function findDigitalRoot($num)

{

 $sum = PHP_INT_MAX;

 $tempNum = $num;

 while ($sum >= 10)

 {

 $sum = 0;

 while ($tempNum > 0)

 {

 $sum += $tempNum % 10;

 $tempNum /= 10;

 }

 $tempNum = $sum;

 }

 return $sum;

}

// Function to find the Nth number 

// with digital root as X

function findAnswer($X, $N)

{

 

 // Counter variable to keep the

 // count of valid numbers

 $counter = 0;

 for ($i = 1; $counter < $N; ++$i)

 {

 // Find digital root

 $digitalRoot = findDigitalRoot($i);

 // Check if is required answer or not

 if ($digitalRoot == $X)

 {

 ++$counter;

 }

 // Print the answer if you have found

 // it and breakout of the loop

 if ($counter == $N)

 {

 echo( $i);

 break;

 }

 }

}

// Driver Code

$X = 1; $N = 3;

findAnswer($X, $N);

// This code is contributed by Code_Mech.  
  
---  
  
 __

 __

 **Output:**

    
    
    19

**Efficient Approach:** We can find _digital root_ of a number K directly
using the formula:

    
    
    digitalRoot(k) = (k - 1)mod 9 +1

From this we can find the N-th number whose _digital_ root is K as,

    
    
    Nth number = (N - 1)*9 + K

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the N-th number with

// digital root as X

#include <bits/stdc++.h>

using namespace std;

// Function to find the N-th number with

// digital root as X

int findAnswer(int X, int N)

{

 return (N - 1) * 9 + X;

}

// Driver Code

int main()

{

 int X = 7, N = 43;

 cout << findAnswer(X, N);

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

// Java program to find the N-th number with

// digital root as X

class GfG

{

 // Function to find the N-th number with

 // digital root as X

 static int findAnswer(int X, int N)

 {

 return (N - 1) * 9 + X;

 }

 // Driver Code

 public static void main(String[] args)

 {

 int X = 7, N = 43;

 System.out.println(findAnswer(X, N));

 }

}

// This code contributed by Rajput-Ji  
  
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

# Python3 program to find the N-th

# number with digital root as X

# Function to find the N-th number

# with digital root as X

def findAnswer(X, N):

 return (N - 1) * 9 + X;

# Driver Code

X = 7;

N = 43;

print(findAnswer(X, N));

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

// C# program to find the N-th number

// with digital root as X

using System;

class GFG

{

// Function to find the N-th

// number with digital root as X

static int findAnswer(int X, int N)

{

 return (N - 1) * 9 + X;

}

// Driver Code

public static void Main()

{

 int X = 7, N = 43;

 Console.WriteLine(findAnswer(X, N));

}

}

// This code contributed by Ryuga  
  
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

// PHP program to find the N-th number

// with digital root as X

// Function to find the N-th number

// with digital root as X

function findAnswer($X, $N)

{

 return ($N - 1) * 9 + $X;

}

// Driver Code

$X = 7; $N = 43;

echo(findAnswer($X, $N));

// This code contributed

// by Code_Mech

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

// Javascript program to find the N-th number

// with digital root as X

// Function to find the N-th number

// with digital root as X

function findAnswer(X, N)

{

 return (N - 1) * 9 + X;

}

// Driver Code

let X = 7;

let N = 43;

document.write(findAnswer(X, N));

// This code is contributed by mohan1240760

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    385

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

