Find elements of array using XOR of consecutive elements



Given an array **arr[]** in which XOR of every 2 consecutive elements of the
original array is given i.e if the total number of elements in the original
array is ![n  ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-3ebe7b3d5f19356fe8152deb8e32c84d_l3.png)then the size of
this XOR array would be n-1. The first element in the original array is also
given. The task is to find out the rest of **n-1** elements of the original
array.

  * Let **a, b, c, d, e, f** are the original elements and the xor of every 2 consecutive elements is given, i.e **a^b = k1** , **b ^ c = k2** , **c ^ d = k3** , **d ^ e = k4** , **e ^ f = k5** (where k1, k2, k3, k4, k5 are the elements that are given as along with the first element **a** ), and we have to find the value of **b, c, d, e, f**.

 **Examples:**

    
    
    **Input :** arr[] = {13, 2, 6, 1}, a = 5
    **Output :** 5 8 10 12 13
    5^8=13, 8^10=2, 10^12=6, 12^13=1
    
    **Input :** arr[] = {12, 5, 26, 7}, a = 6
    **Output :** 6 10 15 21 18 

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** We can find all the elements one by one with the help of ![a
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-6c0e21ff348eb9786a2ca7b7c269cba7_l3.png)(first elements),
and to find the next element i.e ![b  ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-e4160a950ae7e84eff9044a49e7e95d6_l3.png)we
have to xor a by arr[0], similarly for ![c
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-5061d0ff5ded305f41403a874a0c738d_l3.png)xor arr[1] with b
and so on.

This works by following the properties of XOR as stated below:

  * XOR of a number to itself is zero.
  * XOR of a number with zero given the number itself.

So, as arr[0] contains **a^b**. Therefore,

  

  

    
    
    a ^ arr[0] = a ^ a ^ b
               = 0 ^ b
               = b

Similarly as arr[i] contains XOR of ai and ai+1. Therefore,

    
    
    ai ^ arr[i] = ai ^ ai ^ ai+1
                = 0 ^ ai+1
                = ai+1

Below is the implementation of above approach

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the array elements

// using XOR of consecutive elements

#include <bits/stdc++.h>

using namespace std;

// Function to find the array elements

// using XOR of consecutive elements

void getElements(int a, int arr[], int n)

{

 // array to store the orginal

 // elements

 int elements[n + 1];

 // first element a i.e elements[0]=a

 elements[0] = a;

 for (int i = 0; i < n; i++) {

 /* To get the next elements we have to calculate

 xor of previous elements with given xor of 2

 consecutive elements.

 e.g. if a^b=k1 so to get b xor a both side.

 b = k1^a

 */

 elements[i + 1] = arr[i] ^ elements[i];

 }

 // Printing the original array elements

 for (int i = 0; i < n + 1; i++)

 cout << elements[i] << " ";

}

// Driver Code

int main()

{

 int arr[] = { 13, 2, 6, 1 };

 int n = sizeof(arr) / sizeof(arr[0]);

 int a = 5;

 getElements(a, arr, n);

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

// Java program to find the array elements

// using XOR of consecutive elements

import java.io.*;

class GFG {

 

// Function to find the array elements

// using XOR of consecutive elements

static void getElements(int a, int arr[], int n)

{

 // array to store the orginal

 // elements

 int elements[] = new int[n + 1];

 // first element a i.e elements[0]=a

 elements[0] = a;

 for (int i = 0; i < n; i++) {

 /* To get the next elements we have to calculate

 xor of previous elements with given xor of 2

 consecutive elements.

 e.g. if a^b=k1 so to get b xor a both side.

 b = k1^a

 */

 elements[i + 1] = arr[i] ^ elements[i];

 }

 // Printing the original array elements

 for (int i = 0; i < n + 1; i++)

 System.out.print( elements[i] + " ");

}

// Driver Code

 public static void main (String[] args) {

 int arr[] = { 13, 2, 6, 1 };

 int n = arr.length;

 int a = 5;

 getElements(a, arr, n);

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

# Python3 program to find the array

# elements using xor of consecutive elements

# Function to find the array elements

# using XOR of consecutive elements

def getElements(a, arr, n):

 

 # array to store the original elements

 elements = [1 for i in range(n + 1)]

 

 # first elements a i.e elements[0]=a

 elements[0] = a

 

 for i in range(n):

 

 # To get the next elements we have to

 # calculate xor of previous elements

 # with given xor of 2 consecutive elements.

 # e.g. if a^b=k1 so to get b xor a both side.

 # b = k1^a

 elements[i + 1] = arr[i] ^ elements[i]

 

 # Printing the original array elements

 for i in range(n + 1):

 print(elements[i], end = " ")

# Driver code

arr = [13, 2, 6, 1]

n = len(arr)

a = 5

getElements(a, arr, n)

# This code is contributed by Mohit Kumar  
  
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

// C# program to find the array elements

// using XOR of consecutive elements

using System;

class GFG {

 // Function to find the array elements

 // using XOR of consecutive elements

 static void getElements(int a, int []arr, int n)

 {

 // array to store the orginal

 // elements

 int []elements = new int[n + 1];

 

 // first element a i.e elements[0]=a

 elements[0] = a;

 

 for (int i = 0; i < n; i++) {

 

 /* To get the next elements we have to calculate

 xor of previous elements with given xor of 2

 consecutive elements.

 e.g. if a^b=k1 so to get b xor a both side.

 b = k1^a

 */

 elements[i + 1] = arr[i] ^ elements[i];

 }

 

 // Printing the original array elements

 for (int i = 0; i < n + 1; i++)

 Console.Write( elements[i] + " ");

 }

 // Driver Code

 public static void Main () {

 int []arr = { 13, 2, 6, 1 };

 int n = arr.Length;

 int a = 5;

 getElements(a, arr, n);

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

// PHP program to find the array elements

// using XOR of consecutive elements

// Function to find the array elements

// using XOR of consecutive elements

function getElements($a, &$arr, &$n)

{

 // array to store the orginal

 // elements

 

 // first element a i.e elements[0]=a

 $elements[0] = $a;

 for ($i = 0; $i < $n; $i++)

 {

 /* To get the next elements we have to

 calculate xor of previous elements

 with given xor of 2 consecutive elements.

 e.g. if a^b=k1 so to get b xor a both side.

 b = k1^a

 */

 $elements[$i + 1] = $arr[$i] ^ $elements[$i];

 }

 // Printing the original array elements

 for ($i = 0; $i < $n + 1; $i++)

 {

 echo($elements[$i] . " ");

 }

}

// Driver Code

$arr = array(13, 2, 6, 1);

$n = sizeof($arr);

$a = 5;

getElements($a, $arr, $n);

// This code is contributed by Shivi_Aggarwal

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

// Javascript program to find the array elements

// using XOR of consecutive elements

 

// Function to find the array elements

// using XOR of consecutive elements

function getElements(a, arr, n)

{

 

 // Array to store the orginal

 // elements

 let elements = new Array(n + 1);

 for(let i = 0; i < n + 1; i++)

 {

 elements[i] = 0;

 }

 

 // first element a i.e elements[0]=a

 elements[0] = a;

 

 for(let i = 0; i < n; i++)

 {

 

 /* To get the next elements we have to calculate

 xor of previous elements with given xor of 2

 consecutive elements.

 e.g. if a^b=k1 so to get b xor a both side.

 b = k1^a

 */

 elements[i + 1] = arr[i] ^ elements[i];

 }

 

 // Printing the original array elements

 for(let i = 0; i < n + 1; i++)

 document.write( elements[i] + " ");

}

// Driver Code

let arr = [ 13, 2, 6, 1 ];

let n = arr.length;

let a = 5;

getElements(a, arr, n);

// This code is contributed by unknown2108

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    5 8 10 12 13

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

