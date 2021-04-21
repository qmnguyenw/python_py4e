Integers from the range that are composed of a single distinct digit



Given two integer **L** and **R** representing a range **[L, R]** , the task
is to find the count of integers from the range that are composed of a single
distinct digit.

 **Examples:**

    
    
    **Input :** L = 9, R = 11
    **Output :** 2
    Only 9 and 11 have single distinct digit
    
    **Input :** L = 10, R = 50
    **Output :** 4
    11, 22, 33 and 44 are the only valid numbers
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** Iterate through all the numbers and check if the number
is composed of a single distinct digit only.

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

 

// Boolean function to check

// distinct digits of a number

bool checkDistinct(int x)

{

 // Take last digit

 int last = x % 10;

 

 // Check if all other digits

 // are same as last digit

 while (x) {

 if (x % 10 != last)

 return false;

 

 // Remove last digit

 x = x / 10;

 }

 

 return true;

}

 

// Function to return the count of integers that

// are composed of a single distinct digit only

int findCount(int L, int R)

{

 int count = 0;

 

 for (int i = L; i <= R; i++) {

 

 // If i has single distinct digit

 if (checkDistinct(i))

 count += 1;

 }

 

 return count;

}

 

// Driver code

int main()

{

 int L = 10, R = 50;

 

 cout << findCount(L, R);

 

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

//Java implementation of the approach

 

import java.io.*;

 

class GFG {

 

// Boolean function to check

// distinct digits of a number

static boolean checkDistinct(int x)

{

 // Take last digit

 int last = x % 10;

 

 // Check if all other digits

 // are same as last digit

 while (x >0) {

 if (x % 10 != last)

 return false;

 

 // Remove last digit

 x = x / 10;

 }

 

 return true;

}

 

// Function to return the count of integers that

// are composed of a single distinct digit only

static int findCount(int L, int R)

{

 int count = 0;

 

 for (int i = L; i <= R; i++) {

 

 // If i has single distinct digit

 if (checkDistinct(i))

 count += 1;

 }

 

 return count;

}

 

// Driver code

 public static void main (String[] args) {

 

 

 int L = 10, R = 50;

 System.out.println (findCount(L, R));

 }

//This code is contributed by ajit. 

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

# Python3 implementation of above approach

 

# Boolean function to check 

# distinct digits of a number 

def checkDistinct(x): 

 

 # Take last digit 

 last = x % 10

 

 # Check if all other digits 

 # are same as last digit 

 while (x):

 

 if (x % 10 != last):

 return False

 

 # Remove last digit 

 x = x // 10

 

 return True

 

# Function to return the count of 

# integers that are composed of a 

# single distinct digit only 

def findCount(L, R):

 

 count = 0

 

 for i in range(L, R + 1): 

 

 # If i has single distinct digit 

 if (checkDistinct(i)):

 count += 1

 

 return count

 

# Driver code 

L = 10

R = 50

 

print(findCount(L, R)) 

 

# This code is contributed

# by saurabh_shukla  
  
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

 

class GFG {

 

// Boolean function to check

// distinct digits of a number

static Boolean checkDistinct(int x)

{

 // Take last digit

 int last = x % 10;

 

 // Check if all other digits

 // are same as last digit

 while (x >0) {

 if (x % 10 != last)

 return false;

 

 // Remove last digit

 x = x / 10;

 }

 

 return true;

}

 

// Function to return the count of integers that

// are composed of a single distinct digit only

static int findCount(int L, int R)

{

 int count = 0;

 

 for (int i = L; i <= R; i++) {

 

 // If i has single distinct digit

 if (checkDistinct(i))

 count += 1;

 }

 

 return count;

}

 

// Driver code

 static public void Main (String []args) {

 

 

 int L = 10, R = 50;

 Console.WriteLine (findCount(L, R));

 } 

}

//This code is contributed by Arnab Kundu.  
  
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

 

// Boolean function to check distinct

// digits of a number 

function checkDistinct($x) 

{

 // Take last digit 

 $last = $x % 10; 

 

 // Check if all other digits 

 // are same as last digit 

 while ($x) 

 { 

 if ($x % 10 != $last) 

 return false; 

 

 // Remove last digit 

 $x = floor($x / 10); 

 } 

 

 return true; 

} 

 

// Function to return the count of integers that 

// are composed of a single distinct digit only 

function findCount($L, $R) 

{ 

 $count = 0; 

 

 for ($i = $L; $i <= $R; $i++) 

 { 

 

 // If i has single distinct digit 

 if (checkDistinct($i)) 

 $count += 1; 

 } 

 

 return $count; 

} 

 

// Driver code 

$L = 10;

$R = 50; 

 

echo findCount($L, $R);

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    4
    

