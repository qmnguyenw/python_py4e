Check if N can be expressed as product of 3 distinct numbers



  
Given a number **N**. Print three distinct numbers **( >=1)** whose product is
equal to N. print -1 if it is not possible to find three numbers.

 **Examples:**

>  **Input:** 64  
>  **Output:** 2 4 8  
>  **Explanation:**  
>  (2*4*8 = 64)
>
>  **Input:** 24  
>  **Output:** 2 3 4  
>  **Explanation:**  
>  (2*3*4 = 24)
>
>  **Input:** 12  
>  **Output:** -1  
>  **Explanation:**  
>  No such triplet exists
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  1. Make an array which stores all the divisors of the given number using the approach discussed in this article
  2. Let the three number be a, b, c initialize to 1
  3. Traverse the divisors array and check the following condition:
    * value of a = value at 1st index of divisor array.
    * value of b = product of value at 2nd and 3rd index of divisor array. If divisor array has only one or two element then no such triplets exists
    * After finding a & b, value of c = product of all the rest elements in divisor array.
  4. Check the final condition such that value of a, b, c must be distinct and not equal to 1.

Below is the implementation code:  

## CPP

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the

// three numbers

#include "bits/stdc++.h"

using namespace std;

 

// function to find 3 distinct number

// with given product

void getnumbers(int n)

{

 // Declare a vector to store

 // divisors

 vector<int> divisor;

 

 // store all divisors of number

 // in array

 for (int i = 2; i * i <= n; i++) {

 

 // store all the occurence of

 // divisors

 while (n % i == 0) {

 divisor.push_back(i);

 n /= i;

 }

 }

 

 // check if n is not equals to -1

 // then n is also a prime factor

 if (n != 1) {

 divisor.push_back(n);

 }

 

 // Initialize the variables with 1

 int a, b, c, size;

 a = b = c = 1;

 size = divisor.size();

 

 for (int i = 0; i < size; i++) {

 

 // check for first number a

 if (a == 1) {

 a = a * divisor[i];

 }

 

 // check for second number b

 else if (b == 1 || b == a) {

 b = b * divisor[i];

 }

 

 // check for third number c

 else {

 c = c * divisor[i];

 }

 }

 

 // check for all unwanted codition

 if (a == 1 || b == 1 || c == 1

 || a == b || b == c || a == c) {

 cout << "-1" << endl;

 }

 else {

 cout << a << ' ' << b

 << ' ' << c << endl;

 }

}

 

// Driver function

int main()

{

 int n = 64;

 getnumbers(n);

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

// Java program to find the

// three numbers

import java.util.*;

 

class GFG{

 

// function to find 3 distinct number

// with given product

static void getnumbers(int n)

{

 // Declare a vector to store

 // divisors

 Vector<Integer> divisor = new Vector<Integer>();

 

 // store all divisors of number

 // in array

 for (int i = 2; i * i <= n; i++) {

 

 // store all the occurence of

 // divisors

 while (n % i == 0) {

 divisor.add(i);

 n /= i;

 }

 }

 

 // check if n is not equals to -1

 // then n is also a prime factor

 if (n != 1) {

 divisor.add(n);

 }

 

 // Initialize the variables with 1

 int a, b, c, size;

 a = b = c = 1;

 size = divisor.size();

 

 for (int i = 0; i < size; i++) {

 

 // check for first number a

 if (a == 1) {

 a = a * divisor.get(i);

 }

 

 // check for second number b

 else if (b == 1 || b == a) {

 b = b * divisor.get(i);

 }

 

 // check for third number c

 else {

 c = c * divisor.get(i);

 }

 }

 

 // check for all unwanted codition

 if (a == 1 || b == 1 || c == 1

 || a == b || b == c || a == c) {

 System.out.print("-1" +"\n");

 }

 else {

 System.out.print(a +" "+ b

 +" "+ c +"\n");

 }

}

 

// Driver function

public static void main(String[] args)

{

 int n = 64;

 getnumbers(n);

}

}

 

// This code is contributed by sapnasingh4991  
  
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

# Python3 program to find the

# three numbers

 

# function to find 3 distinct number

# with given product

def getnumbers(n):

 

 # Declare a vector to store

 # divisors

 divisor = []

 

 # store all divisors of number

 # in array

 for i in range(2, n + 1):

 

 # store all the occurence of

 # divisors

 while (n % i == 0):

 divisor.append(i)

 n //= i

 

 # check if n is not equals to -1

 # then n is also a prime factor

 if (n != 1):

 divisor.append(n)

 

 # Initialize the variables with 1

 a, b, c, size = 0, 0, 0, 0

 a = b = c = 1

 size = len(divisor)

 

 for i in range(size):

 

 # check for first number a

 if (a == 1):

 a = a * divisor[i]

 

 # check for second number b

 elif (b == 1 or b == a):

 b = b * divisor[i]

 

 # check for third number c

 else:

 c = c * divisor[i]

 

 # check for all unwanted codition

 if (a == 1 or b == 1 or c == 1

 or a == b or b == c or a == c):

 print("-1")

 else:

 print(a, b, c)

 

# Driver function

 

n = 64

getnumbers(n)

 

# This code is contributed by mohit kumar 29  
  
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

// C# program to find the

// three numbers

using System;

using System.Collections.Generic;

 

class GFG{

 

// function to find 3 distinct number

// with given product

static void getnumbers(int n)

{

 // Declare a vector to store

 // divisors

 List<int> divisor = new List<int>();

 

 // store all divisors of number

 // in array

 for (int i = 2; i * i <= n; i++) {

 

 // store all the occurence of

 // divisors

 while (n % i == 0) {

 divisor.Add(i);

 n /= i;

 }

 }

 

 // check if n is not equals to -1

 // then n is also a prime factor

 if (n != 1) {

 divisor.Add(n);

 }

 

 // Initialize the variables with 1

 int a, b, c, size;

 a = b = c = 1;

 size = divisor.Count;

 

 for (int i = 0; i < size; i++) {

 

 // check for first number a

 if (a == 1) {

 a = a * divisor[i];

 }

 

 // check for second number b

 else if (b == 1 || b == a) {

 b = b * divisor[i];

 }

 

 // check for third number c

 else {

 c = c * divisor[i];

 }

 }

 

 // check for all unwanted codition

 if (a == 1 || b == 1 || c == 1

 || a == b || b == c || a == c) {

 Console.Write("-1" +"\n");

 }

 else {

 Console.Write(a +" "+ b

 +" "+ c +"\n");

 }

}

 

// Driver function

public static void Main(String[] args)

{

 int n = 64;

 getnumbers(n);

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    2 4 8
    

**Time Complexity:** O( **(log N)*sqrt(N)** )

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

