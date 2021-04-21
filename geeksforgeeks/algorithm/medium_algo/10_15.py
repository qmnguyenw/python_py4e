Number of array elements derivable from D after performing certain operations



Given an array of N integers and 3 integers D, A and B. The task is to find
the number of array elements that we can convert D into by performing the
following operations on D:

  * Add A (+A)
  * Subtract A (-A)
  * Add B (+B)
  * Subtract B (-B)

 **Note** : It is allowed to perform any number of operations of any type.

 **Examples:**

    
    
    **Input :** arr = {1, 2, 3}, D = 6, A = 3, B = 2 
    **Output :** 3
    **Explanation:**
    We can derive 1 from D by performing (6 - 3(A) - 2(B))
    We can derive 2 from D by performing (6 - 2(A) - 2(A))
    We can derive 3 from D by performing (6 - 3(A))
    Thus, **All** array elements can be derived from D.
     
    **Input :** arr = {1, 2, 3}, D = 7, A = 4, B = 2 
    **Output :** 2
    **Explanation:**
    We can derive 1 from D by performing (7 - 4(A) - 2(B))
    We can derive 3 from D by performing (7 - 4(A))
    Thus, we can derive **{1, 3}**
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Lets say the we want to check if the element **a i** can be derived from D:

Suppose we perform:

  

  

  * The operation of type1(i.e Add A) P times.
  * The operation of type 2(i.e Subtract A) Q times.
  * The operation of type 3(i.e Add B) R times.
  * The operation of type 4(i.e Subtract B) S times.

> Let the value we get after performing these operations be X, then,  
> -> X = P*A – Q*A + R*B – S*B  
> -> X = (P – Q) * A + (R – S) * B
>
> Suppose we successfully derive Ai from D, i.e X = |Ai – D|,
>
> -> |Ai – D| = (P – Q) * A + (R – S) * B
>
> Let (P – Q) = some constant say, U  
> and similarly let (R – S) be a constant, V
>
> -> |Ai – D| = U * A + V * B
>
> This is in the form of the Linear Diophantine Equation and the solution
> exists only when |Ai – D| is divisible by gcd(A, B).

Thus now we can simply iterate over the array and count all such Ai for which
|Ai – D| is divisible by gcd(a, b).

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to find the number of array elements

// which can be derived by perming (+A, -A, +B, -B)

// operations on D

#include <bits/stdc++.h>

 

using namespace std;

 

// Function to return

// gcd of a and b

int gcd(int a, int b)

{

 if (a == 0)

 return b;

 return gcd(b % a, a);

}

 

/* Function to Return the number of elements

 of arr[] which can be derived from D by 

 performing (+A, -A, +B, -B) */

int findPossibleDerivables(int arr[], int n, int D, 

 int A, int B)

{

 // find the gcd of A and B

 int gcdAB = gcd(A, B);

 

 // counter stores the number of 

 // array elements which

 // can be derived from D

 int counter = 0;

 

 for (int i = 0; i < n; i++) {

 // arr[i] can be derived from D only if

 // |arr[i] - D| is divisible by gcd of A and B

 if ((abs(arr[i] - D) % gcdAB) == 0) {

 counter++;

 }

 }

 

 return counter;

}

 

// Driver Code

int main()

{

 int arr[] = { 1, 2, 3, 4, 7, 13 };

 int n = sizeof(arr) / sizeof(arr[0]);

 int D = 5, A = 4, B = 2;

 cout << findPossibleDerivables(arr, n, D, A, B) <<"\n";

 

 int a[] = { 1, 2, 3 };

 n = sizeof(a) / sizeof(a[0]);

 D = 6, A = 3, B = 2;

 cout << findPossibleDerivables(a, n, D, A, B) <<"\n";

 

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

// Java program to find the number of array elements

// which can be derived by perming (+A, -A, +B, -B)

// operations on D

 

import java.io.*;

 

class GFG {

 

 

 

// Function to return

// gcd of a and b

 static int gcd(int a, int b)

{

 if (a == 0)

 return b;

 return gcd(b % a, a);

}

 

/* Function to Return the number of elements

of arr[] which can be derived from D by 

performing (+A, -A, +B, -B) */

static int findPossibleDerivables(int arr[], int n, int D, 

 int A, int B)

{

 // find the gcd of A and B

 int gcdAB = gcd(A, B);

 

 // counter stores the number of 

 // array elements which

 // can be derived from D

 int counter = 0;

 

 for (int i = 0; i < n; i++) {

 // arr[i] can be derived from D only if

 // |arr[i] - D| is divisible by gcd of A and B

 if ((Math.abs(arr[i] - D) % gcdAB) == 0) {

 counter++;

 }

 }

 

 return counter;

}

 

// Driver Code

 

 public static void main (String[] args) {

 int arr[] = { 1, 2, 3, 4, 7, 13 };

 int n = arr.length;

 int D = 5, A = 4, B = 2;

 System.out.println( findPossibleDerivables(arr, n, D, A, B));

 

 int a[] = { 1, 2, 3 };

 n = a.length;

 D = 6;

 A = 3;

 B = 2;

 System.out.println( findPossibleDerivables(a, n, D, A, B));

 }

}

// This code is contributed by anuj_67..  
  
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

# Python3 program to find the number of array

# elements which can be derived by perming 

# (+A, -A, +B, -B) operations on D 

 

# Function to return gcd of a and b 

def gcd(a, b) :

 

 if (a == 0) :

 return b

 

 return gcd(b % a, a); 

 

""" Function to Return the number of elements 

of arr[] which can be derived from D by 

performing (+A, -A, +B, -B) """

def findPossibleDerivables(arr, n, D, A, B) :

 

 # find the gcd of A and B 

 gcdAB = gcd(A, B)

 

 # counter stores the number of 

 # array elements which 

 # can be derived from D 

 counter = 0

 

 for i in range(n) :

 

 # arr[i] can be derived from D only 

 # if |arr[i] - D| is divisible by 

 # gcd of A and B 

 if ((abs(arr[i] - D) % gcdAB) == 0) :

 counter += 1

 

 return counter

 

# Driver Code 

if __name__ == "__main__" : 

 

 arr = [ 1, 2, 3, 4, 7, 13 ] 

 n = len(arr)

 D, A, B = 5, 4, 2

 

 print(findPossibleDerivables(arr, n, D, A, B))

 

 a = [ 1, 2, 3 ]

 n = len(a)

 D, A, B = 6, 3, 2

 

 print(findPossibleDerivables(a, n, D, A, B))

 

# This code is contributed by Ryuga  
  
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

// C# program to find the number of array elements

// which can be derived by perming (+A, -A, +B, -B)

// operations on D 

using System; 

public class GFG {

 

 // Function to return

 // gcd of a and b

 static int gcd(int a, int b)

 {

 if (a == 0)

 return b;

 return gcd(b % a, a);

 }

 

 /* Function to Return the number of elements

 of arr[] which can be derived from D by 

 performing (+A, -A, +B, -B) */

 static int findPossibleDerivables(int []arr, int n, int D,


 int A, int B)

 {

 // find the gcd of A and B

 int gcdAB = gcd(A, B);

 

 // counter stores the number of 

 // array elements which

 // can be derived from D

 int counter = 0;

 

 for (int i = 0; i < n; i++) {

 // arr[i] can be derived from D only if

 // |arr[i] - D| is divisible by gcd of A and B

 if ((Math.Abs(arr[i] - D) % gcdAB) == 0) {

 counter++;

 }

 }

 

 return counter;

 }

 

 // Driver Code

 

 public static void Main () {

 int []arr = { 1, 2, 3, 4, 7, 13 };

 int n = arr.Length;

 int D = 5, A = 4, B = 2;

 Console.WriteLine( findPossibleDerivables(arr, n, D, A, B));

 

 int []a = { 1, 2, 3 };

 n = a.Length;

 D = 6;

 A = 3;

 B = 2;

 Console.WriteLine( findPossibleDerivables(a, n, D, A, B));

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

// PHP program to find the number of 

// array elements which can be derived by

// perming (+A, -A, +B, -B) operations on D

 

// Function to return gcd of a and b

function gcd($a, $b)

{

 if ($a == 0)

 return $b;

 return gcd($b % $a, $a);

}

 

/* Function to Return the number of elements

of arr[] which can be derived from D by 

performing (+A, -A, +B, -B) */

 

function findPossibleDerivables($arr, $n, 

 $D, $A, $B)

{

 // find the gcd of A and B

 $gcdAB = gcd($A, $B);

 

 // counter stores the number of 

 // array elements which

 // can be derived from D

 $counter = 0;

 

 for ($i = 0; $i < $n; $i++) 

 {

 // arr[i] can be derived from D only 

 // if |arr[i] - D| is divisible by 

 // gcd of A and B

 if ((abs($arr[$i] - $D) % $gcdAB) == 0) 

 {

 $counter++;

 }

 }

 

 return $counter;

}

 

// Driver Code

$arr = array( 1, 2, 3, 4, 7, 13 );

$n = sizeof($arr);

$D = 5;

$A = 4;

$B = 2;

echo findPossibleDerivables($arr, $n, 

 $D, $A, $B), "\n";

 

$a = array( 1, 2, 3 );

$n = sizeof($a);

$D = 6;

$A = 3;

$B = 2;

echo findPossibleDerivables($arr, $n, 

 $D, $A, $B), "\n";

 

// This code is contributed by ajit.

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    3
    

**Time Complexity:** O(N), where N is the number of array elements.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

