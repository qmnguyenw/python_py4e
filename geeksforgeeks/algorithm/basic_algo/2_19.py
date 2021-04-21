Ternary Search



 **Ternary search** is a divide and conquer algorithm that can be used to find
an element in an array. It is similar to binary search where we divide the
array into two parts but in this algorithm, we divide the given array into
three parts and determine which has the key (searched element). We can divide
the array into three parts by taking mid1 and mid2 which can be calculated as
shown below. Initially, l and r will be equal to 0 and n-1 respectively, where
n is the length of the array.

> mid1 = l + (r-l)/3  
> mid2 = r – (r-l)/3

**Note:** Array needs to be sorted to perform ternary search on it.

 **Steps to perform Ternary Search:**

  1. First, we compare the key with the element at mid1. If found equal, we return mid1.
  2. If not, then we compare the key with the element at mid2. If found equal, we return mid2.
  3. If not, then we check whether the key is less than the element at mid1. If yes, then recur to the first part.
  4. If not, then we check whether the key is greater than the element at mid2. If yes, then recur to the third part.
  5. If not, then we recur to the second (middle) part.

 **Example:**

  

  

![](https://media.geeksforgeeks.org/wp-content/uploads/ternaryS-3.png)

 **Recursive Implementation of Ternary Search**

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to illustrate

// recursive approach to ternary search

#include <bits/stdc++.h>

using namespace std;

// Function to perform Ternary Search

int ternarySearch(int l, int r, int key, int ar[])

{

 if (r >= l) {

 // Find the mid1 and mid2

 int mid1 = l + (r - l) / 3;

 int mid2 = r - (r - l) / 3;

 // Check if key is present at any mid

 if (ar[mid1] == key) {

 return mid1;

 }

 if (ar[mid2] == key) {

 return mid2;

 }

 // Since key is not present at mid,

 // check in which region it is present

 // then repeat the Search operation

 // in that region

 if (key < ar[mid1]) {

 // The key lies in between l and mid1

 return ternarySearch(l, mid1 - 1, key, ar);

 }

 else if (key > ar[mid2]) {

 // The key lies in between mid2 and r

 return ternarySearch(mid2 + 1, r, key, ar);

 }

 else {

 // The key lies in between mid1 and mid2

 return ternarySearch(mid1 + 1, mid2 - 1, key, ar);

 }

 }

 // Key not found

 return -1;

}

// Driver code

int main()

{

 int l, r, p, key;

 // Get the array

 // Sort the array if not sorted

 int ar[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

 // Starting index

 l = 0;

 // length of array

 r = 9;

 // Checking for 5

 // Key to be searched in the array

 key = 5;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 cout << "Index of " << key

 << " is " << p << endl;

 // Checking for 50

 // Key to be searched in the array

 key = 50;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 cout << "Index of " << key

 << " is " << p << endl;

}

// This code is contributed

// by Akanksha_Rai  
  
---  
  
 __

 __

## C

 __

 __  
 __

 __

 __  
 __  
 __

// C program to illustrate

// recursive approach to ternary search

#include <stdio.h>

// Function to perform Ternary Search

int ternarySearch(int l, int r, int key, int ar[])

{

 if (r >= l) {

 // Find the mid1 and mid2

 int mid1 = l + (r - l) / 3;

 int mid2 = r - (r - l) / 3;

 // Check if key is present at any mid

 if (ar[mid1] == key) {

 return mid1;

 }

 if (ar[mid2] == key) {

 return mid2;

 }

 // Since key is not present at mid,

 // check in which region it is present

 // then repeat the Search operation

 // in that region

 if (key < ar[mid1]) {

 // The key lies in between l and mid1

 return ternarySearch(l, mid1 - 1, key, ar);

 }

 else if (key > ar[mid2]) {

 // The key lies in between mid2 and r

 return ternarySearch(mid2 + 1, r, key, ar);

 }

 else {

 // The key lies in between mid1 and mid2

 return ternarySearch(mid1 + 1, mid2 - 1, key, ar);

 }

 }

 // Key not found

 return -1;

}

// Driver code

int main()

{

 int l, r, p, key;

 // Get the array

 // Sort the array if not sorted

 int ar[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

 // Starting index

 l = 0;

 // length of array

 r = 9;

 // Checking for 5

 // Key to be searched in the array

 key = 5;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 printf("Index of %d is %d\n", key, p);

 // Checking for 50

 // Key to be searched in the array

 key = 50;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 printf("Index of %d is %d", key, p);

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

// Java program to illustrate

// recursive approach to ternary search

class GFG {

 // Function to perform Ternary Search

 static int ternarySearch(int l, int r, int key, int
ar[])

 {

 if (r >= l) {

 // Find the mid1 and mid2

 int mid1 = l + (r - l) / 3;

 int mid2 = r - (r - l) / 3;

 // Check if key is present at any mid

 if (ar[mid1] == key) {

 return mid1;

 }

 if (ar[mid2] == key) {

 return mid2;

 }

 // Since key is not present at mid,

 // check in which region it is present

 // then repeat the Search operation

 // in that region

 if (key < ar[mid1]) {

 // The key lies in between l and mid1

 return ternarySearch(l, mid1 - 1, key, ar);

 }

 else if (key > ar[mid2]) {

 // The key lies in between mid2 and r

 return ternarySearch(mid2 + 1, r, key, ar);

 }

 else {

 // The key lies in between mid1 and mid2

 return ternarySearch(mid1 + 1, mid2 - 1, key, ar);

 }

 }

 // Key not found

 return -1;

 }

 // Driver code

 public static void main(String args[])

 {

 int l, r, p, key;

 // Get the array

 // Sort the array if not sorted

 int ar[] = { 1, 2, 3, 4, 5, 6, 7, 8,
9, 10 };

 // Starting index

 l = 0;

 // length of array

 r = 9;

 // Checking for 5

 // Key to be searched in the array

 key = 5;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 System.out.println("Index of " + key + " is " + p);

 // Checking for 50

 // Key to be searched in the array

 key = 50;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 System.out.println("Index of " + key + " is " + p);

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

# Python3 program to illustrate

# recursive approach to ternary search

import math as mt

# Function to perform Ternary Search

def ternarySearch(l, r, key, ar):

 if (r >= l):

 # Find the mid1 and mid2

 mid1 = l + (r - l) //3

 mid2 = r - (r - l) //3

 # Check if key is present at any mid

 if (ar[mid1] == key):

 return mid1

 

 if (ar[mid2] == key):

 return mid2

 

 # Since key is not present at mid,

 # check in which region it is present

 # then repeat the Search operation

 # in that region

 if (key < ar[mid1]):

 # The key lies in between l and mid1

 return ternarySearch(l, mid1 - 1, key, ar)

 

 elif (key > ar[mid2]):

 # The key lies in between mid2 and r

 return ternarySearch(mid2 + 1, r, key, ar)

 

 else:

 # The key lies in between mid1 and mid2

 return ternarySearch(mid1 + 1,

 mid2 - 1, key, ar)

 

 # Key not found

 return -1

# Driver code

l, r, p = 0, 9, 5

# Get the array

# Sort the array if not sorted

ar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,
10 ]

# Starting index

l = 0

# length of array

r = 9

# Checking for 5

# Key to be searched in the array

key = 5

# Search the key using ternarySearch

p = ternarySearch(l, r, key, ar)

# Print the result

print("Index of", key, "is", p)

# Checking for 50

# Key to be searched in the array

key = 50

# Search the key using ternarySearch

p = ternarySearch(l, r, key, ar)

# Print the result

print("Index of", key, "is", p)

# This code is contributed by

# Mohit kumar 29  
  
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

// CSharp program to illustrate

// recursive approach to ternary search

using System;

class GFG {

 // Function to perform Ternary Search

 static int ternarySearch(int l, int r, int key, int[]
ar)

 {

 if (r >= l) {

 // Find the mid1 and mid2

 int mid1 = l + (r - l) / 3;

 int mid2 = r - (r - l) / 3;

 // Check if key is present at any mid

 if (ar[mid1] == key) {

 return mid1;

 }

 if (ar[mid2] == key) {

 return mid2;

 }

 // Since key is not present at mid,

 // check in which region it is present

 // then repeat the Search operation

 // in that region

 if (key < ar[mid1]) {

 // The key lies in between l and mid1

 return ternarySearch(l, mid1 - 1, key, ar);

 }

 else if (key > ar[mid2]) {

 // The key lies in between mid2 and r

 return ternarySearch(mid2 + 1, r, key, ar);

 }

 else {

 // The key lies in between mid1 and mid2

 return ternarySearch(mid1 + 1, mid2 - 1, key, ar);

 }

 }

 // Key not found

 return -1;

 }

 // Driver code

 public static void Main()

 {

 int l, r, p, key;

 // Get the array

 // Sort the array if not sorted

 int[] ar = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

 // Starting index

 l = 0;

 // length of array

 r = 9;

 // Checking for 5

 // Key to be searched in the array

 key = 5;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 Console.WriteLine("Index of " + key + " is " + p);

 // Checking for 50

 // Key to be searched in the array

 key = 50;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 Console.WriteLine("Index of " + key + " is " + p);

 }

}

// This code is contributed by Ryuga  
  
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

// PHP program to illustrate

// recursive approach to ternary search

// Function to perform Ternary Search

function ternarySearch($l, $r, $key, $ar)

{

 if ($r >= $l)

 {

 // Find the mid1 and mid2

 $mid1 = (int)($l + ($r - $l) / 3);

 $mid2 = (int)($r - ($r - $l) / 3);

 // Check if key is present at any mid

 if ($ar[$mid1] == $key)

 {

 return $mid1;

 }

 if ($ar[$mid2] == $key)

 {

 return $mid2;

 }

 // Since key is not present at mid,

 // check in which region it is present

 // then repeat the Search operation

 // in that region

 if ($key < $ar[$mid1])

 {

 // The key lies in between l and mid1

 return ternarySearch($l, $mid1 - 1,

 $key, $ar);

 }

 else if ($key > $ar[$mid2])

 {

 // The key lies in between mid2 and r

 return ternarySearch($mid2 + 1, $r, 

 $key, $ar);

 }

 else

 {

 // The key lies in between mid1 and mid2

 return ternarySearch($mid1 + 1, $mid2 - 1,

 $key, $ar);

 }

 }

 // Key not found

 return -1;

}

// Driver code

// Get the array

// Sort the array if not sorted

$ar = array( 1, 2, 3, 4, 5,

 6, 7, 8, 9, 10 );

// Starting index

$l = 0;

// length of array

$r = 9;

// Checking for 5

// Key to be searched in the array

$key = 5;

// Search the key using ternarySearch

$p = ternarySearch($l, $r, $key, $ar);

// Print the result

echo "Index of ", $key,

 " is ", (int)$p, "\n";

// Checking for 50

// Key to be searched in the array

$key = 50;

// Search the key using ternarySearch

$p = ternarySearch($l, $r, $key, $ar);

// Print the result

echo "Index of ", $key,

 " is ", (int)$p, "\n";

// This code is contributed by Arnab Kundu

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    Index of 5 is 4
    Index of 50 is -1
    
    
    
    

**Iterative Approach of Ternary Search**

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to illustrate

// iterative approach to ternary search

#include <iostream>

using namespace std;

// Function to perform Ternary Search

int ternarySearch(int l, int r, int key, int ar[])

{

 while (r >= l) {

 // Find the mid1 and mid2

 int mid1 = l + (r - l) / 3;

 int mid2 = r - (r - l) / 3;

 // Check if key is present at any mid

 if (ar[mid1] == key) {

 return mid1;

 }

 if (ar[mid2] == key) {

 return mid2;

 }

 // Since key is not present at mid,

 // check in which region it is present

 // then repeat the Search operation

 // in that region

 if (key < ar[mid1]) {

 // The key lies in between l and mid1

 r = mid1 - 1;

 }

 else if (key > ar[mid2]) {

 // The key lies in between mid2 and r

 l = mid2 + 1;

 }

 else {

 // The key lies in between mid1 and mid2

 l = mid1 + 1;

 r = mid2 - 1;

 }

 }

 // Key not found

 return -1;

}

// Driver code

int main()

{

 int l, r, p, key;

 // Get the array

 // Sort the array if not sorted

 int ar[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

 // Starting index

 l = 0;

 // length of array

 r = 9;

 // Checking for 5

 // Key to be searched in the array

 key = 5;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 cout << "Index of "<<key<<" is " << p << endl;

 // Checking for 50

 // Key to be searched in the array

 key = 50;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 cout << "Index of "<<key<<" is " << p;

}  
  
---  
  
 __

 __

## C

 __

 __  
 __

 __

 __  
 __  
 __

// C program to illustrate

// iterative approach to ternary search

#include <stdio.h>

// Function to perform Ternary Search

int ternarySearch(int l, int r, int key, int ar[])

{

 while (r >= l) {

 // Find the mid1 and mid2

 int mid1 = l + (r - l) / 3;

 int mid2 = r - (r - l) / 3;

 // Check if key is present at any mid

 if (ar[mid1] == key) {

 return mid1;

 }

 if (ar[mid2] == key) {

 return mid2;

 }

 // Since key is not present at mid,

 // check in which region it is present

 // then repeat the Search operation

 // in that region

 if (key < ar[mid1]) {

 // The key lies in between l and mid1

 r = mid1 - 1;

 }

 else if (key > ar[mid2]) {

 // The key lies in between mid2 and r

 l = mid2 + 1;

 }

 else {

 // The key lies in between mid1 and mid2

 l = mid1 + 1;

 r = mid2 - 1;

 }

 }

 // Key not found

 return -1;

}

// Driver code

int main()

{

 int l, r, p, key;

 // Get the array

 // Sort the array if not sorted

 int ar[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

 // Starting index

 l = 0;

 // length of array

 r = 9;

 // Checking for 5

 // Key to be searched in the array

 key = 5;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 printf("Index of %d is %d\n", key, p);

 // Checking for 50

 // Key to be searched in the array

 key = 50;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 printf("Index of %d is %d", key, p);

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

// Java program to illustrate

// the iterative approach to ternary search

class GFG {

 // Function to perform Ternary Search

 static int ternarySearch(int l, int r, int key, int
ar[])

 {

 while (r >= l) {

 // Find the mid1 mid2

 int mid1 = l + (r - l) / 3;

 int mid2 = r - (r - l) / 3;

 // Check if key is present at any mid

 if (ar[mid1] == key) {

 return mid1;

 }

 if (ar[mid2] == key) {

 return mid2;

 }

 // Since key is not present at mid,

 // check in which region it is present

 // then repeat the Search operation

 // in that region

 if (key < ar[mid1]) {

 // The key lies in between l and mid1

 r = mid1 - 1;

 }

 else if (key > ar[mid2]) {

 // The key lies in between mid2 and r

 l = mid2 + 1;

 }

 else {

 // The key lies in between mid1 and mid2

 l = mid1 + 1;

 r = mid2 - 1;

 }

 }

 // Key not found

 return -1;

 }

 // Driver code

 public static void main(String args[])

 {

 int l, r, p, key;

 // Get the array

 // Sort the array if not sorted

 int ar[] = { 1, 2, 3, 4, 5, 6, 7, 8,
9, 10 };

 // Starting index

 l = 0;

 // length of array

 r = 9;

 // Checking for 5

 // Key to be searched in the array

 key = 5;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 System.out.println("Index of " + key + " is " + p);

 // Checking for 50

 // Key to be searched in the array

 key = 50;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 System.out.println("Index of " + key + " is " + p);

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

# Python 3 program to illustrate iterative

# approach to ternary search

# Function to perform Ternary Search

def ternarySearch(l, r, key, ar):

 while r >= l:

 

 # Find mid1 and mid2

 mid1 = l + (r-l) // 3

 mid2 = r - (r-l) // 3

 # Check if key is at any mid

 if key == ar[mid1]:

 return mid1

 if key == mid2:

 return mid2

 # Since key is not present at mid,

 # Check in which region it is present

 # Then repeat the search operation in that region

 if key < ar[mid1]:

 # key lies between l and mid1

 r = mid1 - 1

 elif key > ar[mid2]:

 # key lies between mid2 and r

 l = mid2 + 1

 else:

 # key lies between mid1 and mid2

 l = mid1 + 1

 r = mid2 - 1

 # key not found

 return -1

# Driver code

# Get the list

# Sort the list if not sorted

ar = [1, 2, 3, 4, 5, 6, 7, 8, 9,
10]

# Starting index

l = 0

# Length of list

r = 9

# Checking for 5

# Key to be searched in the list

key = 5

# Search the key using ternary search

p = ternarySearch(l, r, key, ar)

# Print the result

print("Index of", key, "is", p)

# Checking for 50

# Key to be searched in the list

key = 50

# Search the key using ternary search

p = ternarySearch(l, r, key, ar)

# Print the result

print("Index of", key, "is", p)

# This code has been contributed by Sujal Motagi  
  
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

// C# program to illustrate the iterative

// approach to ternary search

using System;

public class GFG {

 // Function to perform Ternary Search

 static int ternarySearch(int l, int r,

 int key, int[] ar)

 {

 while (r >= l) {

 // Find the mid1 and mid2

 int mid1 = l + (r - l) / 3;

 int mid2 = r - (r - l) / 3;

 // Check if key is present at any mid

 if (ar[mid1] == key) {

 return mid1;

 }

 if (ar[mid2] == key) {

 return mid2;

 }

 // Since key is not present at mid,

 // check in which region it is present

 // then repeat the Search operation

 // in that region

 if (key < ar[mid1]) {

 // The key lies in between l and mid1

 r = mid1 - 1;

 }

 else if (key > ar[mid2]) {

 // The key lies in between mid2 and r

 l = mid2 + 1;

 }

 else {

 // The key lies in between mid1 and mid2

 l = mid1 + 1;

 r = mid2 - 1;

 }

 }

 // Key not found

 return -1;

 }

 // Driver code

 public static void Main(String[] args)

 {

 int l, r, p, key;

 // Get the array

 // Sort the array if not sorted

 int[] ar = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

 // Starting index

 l = 0;

 // length of array

 r = 9;

 // Checking for 5

 // Key to be searched in the array

 key = 5;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 Console.WriteLine("Index of " + key + " is " + p);

 // Checking for 50

 // Key to be searched in the array

 key = 50;

 // Search the key using ternarySearch

 p = ternarySearch(l, r, key, ar);

 // Print the result

 Console.WriteLine("Index of " + key + " is " + p);

 }

}

// This code has been contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    Index of 5 is 4
    Index of 50 is -1
    
    
    
    

**Time Complexity:**

![O\(\\log _{3} n\)   ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-df538f6bb6b63ecf50eb01e47959aa93_l3.png)

, where n is the size of the array.

 **Uses:** In finding the maximum or minimum of a unimodal function.  
Hackerearth Problems on Ternary search  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

