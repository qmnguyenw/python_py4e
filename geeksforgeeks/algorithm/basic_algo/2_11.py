Length of the longest alternating subarray



Given an array of N including positive and negative numbers only. The task is
to find the length of the longest alternating (means negative-positive-
negative or positive-negative-positive) subarray present in the array.  
**Examples:**  

    
    
    **Input:** a[] = {-5, -1, -1, 2, -2, -3}
    **Output:** 3 
    The subarray {-1, 2, -2} 
    
    **Input:** a[] = {1, -5, 1, -5}
    **Output:** 4 

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The following steps are followed to solve the problem:  

  * Initially initialize cnt as 1.
  * Iterate among the array elements, check if it has an alternate sign.
  * Increase the cnt by 1 if it has a alternate sign.
  * If it does not has an alternate sign, then re-initialize cnt by 1.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the longest alternating

// subarray in an array of N number

#include <bits/stdc++.h>

using namespace std;

// Function to find the longest subarray

int longestAlternatingSubarray(int a[], int n)

{

 // Length of longest alternating

 int longest = 1;

 int cnt = 1;

 // Iterate in the array

 for (int i = 1; i < n; i++) {

 // Check for alternate

 if (a[i] * a[i - 1] < 0) {

 cnt++;

 longest = max(longest, cnt);

 }

 else

 cnt = 1;

 }

 return longest;

}

/* Driver program to test above functions*/

int main()

{

 int a[] = { -5, -1, -1, 2, -2, -3 };

 int n = sizeof(a) / sizeof(a[0]);

 // Function to find the longest subarray

 cout << longestAlternatingSubarray(a, n);

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

// Java program to find the longest alternating

// subarray in an array of N number

class GFG

{

 // Function to find the longest subarray

 static int longestAlternatingSubarray(int a[], int n)

 {

 // Length of longest alternating

 int longest = 1;

 int cnt = 1;

 

 // Iterate in the array

 for (int i = 1; i < n; i++)

 {

 

 // Check for alternate

 if (a[i] * a[i - 1] < 0)

 {

 cnt++;

 longest = Math.max(longest, cnt);

 }

 else

 cnt = 1;

 }

 return longest;

 }

 

 /* Driver program to test above functions*/

 public static void main (String[] args)

 {

 int a[] = { -5, -1, -1, 2, -2, -3 };

 int n = a.length ;

 

 // Function to find the longest subarray

 System.out.println(longestAlternatingSubarray(a, n));

 }

}

// This code is contributed by Ryuga  
  
---  
  
 __

 __

## Python 3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find the longest alternating

# subarray in an array of N number

# Function to find the longest subarray

def longestAlternatingSubarray(a, n):

 

 # Length of longest alternating

 longest = 1

 cnt = 1

 # Iterate in the array

 i = 1

 while i < n:

 # Check for alternate

 if (a[i] * a[i - 1] < 0):

 cnt = cnt + 1

 longest = max(longest, cnt)

 

 else:

 cnt = 1

 i = i + 1

 

 return longest

# Driver Code

a = [ -5, -1, -1, 2, -2, -3 ]

n = len(a)

# Function to find the longest subarray

print(longestAlternatingSubarray(a, n))

# This code is contributed

# by shashank_sharma  
  
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

// C# program to find the longest alternating

// subarray in an array of N number

using System;

class GFG

{

// Function to find the longest subarray

static int longestAlternatingSubarray(int []a,

 int n)

{

 // Length of longest alternating

 int longest = 1;

 int cnt = 1;

 // Iterate in the array

 for (int i = 1; i < n; i++)

 {

 // Check for alternate

 if (a[i] * a[i - 1] < 0)

 {

 cnt++;

 longest = Math.Max(longest, cnt);

 }

 else

 cnt = 1;

 }

 return longest;

}

// Driver Code

public static void Main()

{

 int []a = { -5, -1, -1, 2, -2, -3 };

 int n = a.Length;

 // Function to find the longest subarray

 Console.Write(longestAlternatingSubarray(a, n));

}

}

// This code is contributed

// by Akanksha Rai  
  
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

// PHP program to find the longest alternating

// subarray in an array of N number

// Function to find the longest subarray

function longestAlternatingSubarray($a, $n)

{

 

 // Length of longest alternating

 $longest = 1;

 $cnt = 1;

 // Iterate in the array

 for ($i = 1; $i < $n; $i++)

 {

 // Check for alternate

 if ($a[$i] * $a[$i - 1] < 0)

 {

 $cnt++;

 $longest = max($longest, $cnt);

 }

 else

 $cnt = 1;

 }

 return $longest;

}

// Driver Code

$a = array(-5, -1, -1, 2, -2, -3 );

$n = sizeof($a);

// Function to find the longest subarray

echo longestAlternatingSubarray($a, $n);

// This code is contributed by akt_mit

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

// JavaScript program to find the longest alternating

// subarray in an array of N number

// Function to find the longest subarray

function longestAlternatingSubarray(a, n)

{

 // Length of longest alternating

 let longest = 1;

 let cnt = 1;

 // Iterate in the array

 for (let i = 1; i < n; i++) {

 // Check for alternate

 if (a[i] * a[i - 1] < 0) {

 cnt++;

 longest = Math.max(longest, cnt);

 }

 else

 cnt = 1;

 }

 return longest;

}

/* Driver program to test above functions*/

 let a = [ -5, -1, -1, 2, -2, -3 ];

 let n = a.length;

 // Function to find the longest subarray

 document.write(longestAlternatingSubarray(a, n));

// This code is contributed by Surbhi Tyagi.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    3

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

