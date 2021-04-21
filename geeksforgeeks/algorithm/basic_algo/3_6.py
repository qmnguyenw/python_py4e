Sum of elements from an array having even parity



Given an array **arr[]** , the task is to calculate the sum of the elements
from the given array which has **even parity** i.e. the number of set bits is
**even** using **bitwise operator**.

 **Examples:**

> **Input:** arr[] = {2, 4, 3, 5, 9}  
> **Output:** 17  
> Only 3(0011), 5(0101) and 9(1001) have even parity  
> So 3 + 5 + 9 = 17
>
>  **Input:** arr[] = {1, 5, 4, 16, 10}  
> **Output:** 15  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:** Initialize a variable **sum = 0** and traverse the array from
**0** to **n – 1** while counting the number of set bits in **arr[i]** using
Brian Kernighan’s Algorithm. If the **count** is **even** then update **sum =
sum + arr[i]**. Print the **sum** in the end.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the sum of the elements

// from an array which have even parity

#include <bits/stdc++.h>

using namespace std;

// Function that returns true if x has even parity

bool checkEvenParity(int x)

{

 // We basically count set bits

 // https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

 int parity = 0;

 while (x != 0) {

 x = x & (x - 1);

 parity++;

 }

 if (parity % 2 == 0)

 return true;

 else

 return false;

}

// Function to return the sum of the elements

// from an array which have even parity

long sumlist(int a[], int n)

{

 long sum = 0;

 for (int i = 0; i < n; i++) {

 // If a[i] has even parity

 if (checkEvenParity(a[i]))

 sum += a[i];

 }

 return sum;

}

// Driver code

int main()

{

 int arr[] = { 2, 4, 3, 5, 9 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << sumlist(arr, n);

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

// Java program to find the sum of the elements

// from an array which have even parity

import java.io.*;

class GFG {

// Function that returns true if x has even parity

static boolean checkEvenParity(int x)

{

 // We basically count set bits

 // https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

 int parity = 0;

 while (x != 0) {

 x = x & (x - 1);

 parity++;

 }

 if (parity % 2 == 0)

 return true;

 else

 return false;

}

// Function to return the sum of the elements

// from an array which have even parity

static long sumlist(int a[], int n)

{

 long sum = 0;

 for (int i = 0; i < n; i++) {

 // If a[i] has even parity

 if (checkEvenParity(a[i]))

 sum += a[i];

 }

 return sum;

}

// Driver code

 public static void main (String[] args) {

 int arr[] = { 2, 4, 3, 5, 9 };

 int n =arr.length;

 System.out.println(sumlist(arr, n));

 }

}

// This code is contributed by inder_verma..  
  
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

# Python3 program to find the sum of the elements

# from an array which have even parity

# Function that returns true if x

# has even parity

def checkEvenParity(x):

 

 # We basically count set bits

 # https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

 parity = 0

 while (x != 0):

 x = x & (x - 1)

 parity += 1

 if (parity % 2 == 0):

 return True

 else:

 return False

# Function to return the sum of the elements

# from an array which have even parity

def sumlist(a, n):

 sum = 0

 for i in range(n):

 

 # If a[i] has even parity

 if (checkEvenParity(a[i])):

 sum += a[i]

 return sum

# Driver code

if __name__ == '__main__':

 arr = [ 2, 4, 3, 5, 9 ]

 n = len(arr)

 print(sumlist(arr, n))

# This code is contributed by 29AjayKumar.  
  
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

// C# program to find the sum of the elements

// from an array which have even parity

using System ;

class GFG {

// Function that returns true if x has even parity

static bool checkEvenParity(int x)

{

 // We basically count set bits

 // https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

 int parity = 0;

 while (x != 0) {

 x = x & (x - 1);

 parity++;

 }

 if (parity % 2 == 0)

 return true;

 else

 return false;

}

// Function to return the sum of the elements

// from an array which have even parity

static long sumlist(int []a, int n)

{

 long sum = 0;

 for (int i = 0; i < n; i++) {

 // If a[i] has even parity

 if (checkEvenParity(a[i]))

 sum += a[i];

 }

 return sum;

}

// Driver code

 public static void Main () {

 int []arr = { 2, 4, 3, 5, 9 };

 int n =arr.Length;

 Console.WriteLine(sumlist(arr, n));

 }

 // This code is contributed by Ryuga

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

// PHP program to find the sum of the

// elements from an array which have

// even parity

// Function that returns true

// if x has even parity

function checkEvenParity($x)

{

 // We basically count set bits

 // https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

 $parity = 0;

 while ($x != 0)

 {

 $x = ($x & ($x - 1));

 $parity++;

 }

 if ($parity % 2 == 0)

 return true;

 else

 return false;

}

// Function to return the sum of the elements

// from an array which have even parity

function sumlist($a, $n)

{

 $sum = 0;

 for ($i = 0; $i < $n; $i++)

 {

 // If a[i] has even parity

 if (checkEvenParity($a[$i]))

 $sum += $a[$i];

 }

 return $sum;

}

// Driver code

$arr = array( 2, 4, 3, 5, 9 );

$n = sizeof($arr);

echo sumlist($arr, $n);

 

// This code is contributed by ajit.

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

// Javascript program to find the sum of the elements

// from an array which have even parity

// Function that returns true if x has even parity

function checkEvenParity(x)

{

 

 // We basically count set bits

 // https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

 let parity = 0;

 while (x != 0)

 {

 x = x & (x - 1);

 parity++;

 }

 

 if (parity % 2 == 0)

 return true;

 else

 return false;

}

// Function to return the sum of the elements

// from an array which have even parity

function sumlist(a, n)

{

 let sum = 0;

 for(let i = 0; i < n; i++)

 {

 

 // If a[i] has even parity

 if (checkEvenParity(a[i]))

 sum += a[i];

 }

 return sum;

}

// Driver code

let arr = [ 2, 4, 3, 5, 9 ];

let n = arr.length;

document.write(sumlist(arr, n));

// This code is contributed by unknown2108

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    17

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

