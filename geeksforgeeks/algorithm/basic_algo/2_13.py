Find frequency of smallest value in an array



Given an array **A** of **N** elements. Find the frequency of the smallest
value in the array.

 **Examples:**

    
    
    **Input :** N = 5, arr[] = {3, 2, 3, 4, 4} 
    **Output :** 1
    The smallest element in the array is 2 
    and it occurs only once.
    
    **Input :** N = 6, arr[] = {4, 3, 5, 3, 3, 6}
    **Output :** 3
    The smallest element in the array is 3 
    and it occurs 3 times.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Simple Approach** : A simple method is to first find the minimum element in
the array in first traversal. Then traverse the array again and find the
number of occurrences of the minimum element.

 **Efficient Approach** : The efficient approach is to do this in a single
traversal.  
Let us assume the first element to be the current minimum, so the frequency of
the current minimum would be 1. Now let’s iterate through the array (1 to N),
we come across 2 cases:

  * Current element is smaller than our current minimum: We change the current minimum to be equal to current element and since this is the first time we are coming across this element, we make it’s frequency 1.
  * Current element is equal to the current minimum: We increment the frequency of current minimum.

Below is the implementation of the above approach:

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the frequency of

// minimum element in the array

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the frequency of the

// smallest value in the array

int frequencyOfSmallest(int n, int arr[])

{

 int mn = arr[0], freq = 1;

 

 for (int i = 1; i < n; i++) {

 

 // If current element is smaller

 // than minimum

 if (arr[i] < mn) {

 mn = arr[i];

 freq = 1;

 }

 // If current element is equal

 // to smallest

 else if (arr[i] == mn)

 freq++;

 }

 

 return freq;

}

 

// Driver Code

int main()

{

 int N = 5;

 int arr[] = { 3, 2, 3, 4, 4 };

 

 cout << frequencyOfSmallest(N, arr);

 

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

// Java program to find the frequency of

// minimum element in the array

import java.io.*;

 

class GFG 

{

 

// Function to find the frequency of the

// smallest value in the array

static int frequencyOfSmallest(int n, int arr[])

{

 int mn = arr[0], freq = 1;

 

 for (int i = 1; i < n; i++) 

 {

 

 // If current element is smaller

 // than minimum

 if (arr[i] < mn)

 {

 mn = arr[i];

 freq = 1;

 }

 

 // If current element is equal

 // to smallest

 else if (arr[i] == mn)

 freq++;

 }

 return freq;

}

 

 // Driver Code

 public static void main (String[] args) 

 {

 int N = 5;

 int arr[] = { 3, 2, 3, 4, 4 };

 System.out.println (frequencyOfSmallest(N, arr));

 }

}

 

// This code is contributed by Tushil.  
  
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

# Python 3 program to find the frequency of

# minimum element in the array

 

 

# Function to find the frequency of the

# smallest value in the array

def frequencyOfSmallest(n,arr):

 mn = arr[0]

 freq = 1

 

 for i in range(1,n):

 # If current element is smaller

 # than minimum

 if (arr[i] < mn):

 mn = arr[i]

 freq = 1

 

 # If current element is equal

 # to smallest

 elif(arr[i] == mn):

 freq += 1

 

 return freq

 

# Driver Code

if __name__ == '__main__':

 N = 5

 arr = [3, 2, 3, 4, 4]

 

 print(frequencyOfSmallest(N, arr))

 

# This code is contributed by

# Surendra_Gangwar  
  
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

// C# program to find the frequency of

// minimum element in the array 

using System;

 

class GFG 

{ 

 

 // Function to find the frequency of the 

 // smallest value in the array 

 static int frequencyOfSmallest(int n, int []arr) 

 { 

 int mn = arr[0], freq = 1; 

 

 for (int i = 1; i < n; i++) 

 { 

 

 // If current element is smaller 

 // than minimum 

 if (arr[i] < mn) 

 { 

 mn = arr[i]; 

 freq = 1; 

 } 

 

 // If current element is equal 

 // to smallest 

 else if (arr[i] == mn) 

 freq++; 

 } 

 return freq; 

 } 

 

 // Driver Code 

 public static void Main() 

 { 

 int N = 5; 

 int []arr = { 3, 2, 3, 4, 4 }; 

 

 Console.WriteLine(frequencyOfSmallest(N, arr)); 

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

// PHP program to find the frequency of

// minimum element in the array

 

// Function to find the frequency of the

// smallest value in the array

function frequencyOfSmallest($n, $arr)

{

 $mn = $arr[0];

 $freq = 1;

 

 for ($i = 1; $i < $n; $i++)

 {

 

 // If current element is smaller

 // than minimum

 if ($arr[$i] < $mn) 

 {

 $mn = $arr[$i];

 $freq = 1;

 }

 // If current element is equal

 // to smallest

 else if ($arr[$i] == $mn)

 $freq++;

 }

 

 return $freq;

}

 

// Driver Code

$N = 5;

$arr = array( 3, 2, 3, 4, 4 );

 

print(frequencyOfSmallest($N, $arr));

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    

**Time Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

