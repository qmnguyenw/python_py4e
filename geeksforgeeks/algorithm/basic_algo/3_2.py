Smallest power of 2 which is greater than or equal to sum of array elements



Given an array of N numbers where values of the array represent memory sizes.
The memory that is required by the system can only be represented in powers of
2. The task is to return the size of the memory required by the system.  
 **Examples:**  

    
    
    **Input:** a[] = {2, 1, 4, 5}
    **Output:** 16
    The sum of memory required is 12, 
    hence the nearest power of 2 is 16. 
    
    **Input:** a[] = {1, 2, 3, 2}
    **Output:** 8

 **Source:** Microsoft Interview  

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The problem is a combination of summation of array elements and
smallest power of 2 greater than or equal to N. Find the sum of array elements
and then find the smallest power of 2 greater than or equal to N.  
Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

using namespace std;

// Function to find the nearest power of 2

int nextPowerOf2(int n)

{

 // The number

 int p = 1;

 // If already a power of 2

 if (n && !(n & (n - 1)))

 return n;

 // Find the next power of 2

 while (p < n)

 p <<= 1;

 return p;

}

// Function to find the memory used

int memoryUsed(int arr[], int n)

{

 // Sum of array

 int sum = 0;

 // Traverse and find the sum of array

 for (int i = 0; i < n; i++)

 sum += arr[i];

 // Function call to find the nearest power of 2

 int nearest = nextPowerOf2(sum);

 return nearest;

}

// Driver Code

int main()

{

 int arr[] = { 1, 2, 3, 2 };

 int n = sizeof(arr) / sizeof(arr[0]);

 cout << memoryUsed(arr, n);

 // getchar();

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

// Java implementation of the above approach

class GFG

{

 // Function to find the nearest power of 2

 static int nextPowerOf2(int n)

 {

 

 // The number

 int p = 1;

 

 // If already a power of 2

 if(n!=0 && ((n&(n-1)) == 0))

 return n;

 

 // Find the next power of 2

 while (p < n)

 p <<= 1;

 

 return p;

 }

 

 // Function to find the memory used

 static int memoryUsed(int arr[], int n)

 {

 // Sum of array

 int sum = 0;

 

 // Traverse and find the sum of array

 for (int i = 0; i < n; i++)

 sum += arr[i];

 

 // Function call to find the nearest power of 2

 int nearest = nextPowerOf2(sum);

 

 return nearest;

 }

 // Driver Code

 public static void main(String []args)

 {

 int arr[] = { 1, 2, 3, 2 };

 int n = arr.length;

 

 System.out.println(memoryUsed(arr, n));

 

 }

}

// This code is contributed

// by ihritik  
  
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

# Python3 implementation of the above approach

# Function to find the nearest power of 2

def nextPowerOf2(n):

 

 # The number

 p = 1

 

 # If already a power of 2

 if (n and not(n & (n - 1))):

 return n

 

 # Find the next power of 2

 while (p < n):

 p <<= 1

 return p

# Function to find the memory used

def memoryUsed(arr, n):

 

 # Sum of array

 sum = 0

 # Traverse and find the sum of array

 for i in range(n):

 sum += arr[i]

 # Function call to find the nearest

 # power of 2

 nearest = nextPowerOf2(sum)

 return nearest

# Driver Code

arr = [1, 2, 3, 2]

n = len(arr)

print(memoryUsed(arr, n))

# This code is contributed by sahishelangia  
  
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

// C# implementation of the above approach

using System;

class GFG

{

 // Function to find the nearest power of 2

 static int nextPowerOf2(int n)

 {

 

 // The number

 int p = 1;

 

 // If already a power of 2

 if(n!=0 && ((n&(n-1)) == 0))

 return n;

 

 // Find the next power of 2

 while (p < n)

 p <<= 1;

 

 return p;

 }

 

 // Function to find the memory used

 static int memoryUsed(int []arr, int n)

 {

 // Sum of array

 int sum = 0;

 

 // Traverse and find the sum of array

 for (int i = 0; i < n; i++)

 sum += arr[i];

 

 // Function call to find the nearest power of 2

 int nearest = nextPowerOf2(sum);

 

 return nearest;

 }

 // Driver Code

 public static void Main()

 {

 int []arr = { 1, 2, 3, 2 };

 int n = arr.Length;

 

 Console.WriteLine(memoryUsed(arr, n));

 

 }

}

// This code is contributed

// by ihritik  
  
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

// PHP implementation of the above approach

// Function to find the nearest power of 2

function nextPowerOf2($n)

{

 // The number

 $p = 1;

 // If already a power of 2

 if ($n && !($n & ($n - 1)))

 return $n;

 // Find the next power of 2

 while ($p < $n)

 $p <<= 1;

 return $p;

}

// Function to find the memory used

function memoryUsed(&$arr, $n)

{

 // Sum of array

 $sum = 0;

 // Traverse and find the sum of array

 for ($i = 0; $i < $n; $i++)

 $sum += $arr[$i];

 // Function call to find the

 // nearest power of 2

 $nearest = nextPowerOf2($sum);

 return $nearest;

}

// Driver Code

$arr = array(1, 2, 3, 2);

$n = sizeof($arr);

echo(memoryUsed($arr, $n));

// This code is contributed

// by Shivi_Aggarwal

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

// Javascript implementation of the above approach

// Function to find the nearest power of 2

function nextPowerOf2(n)

{

 // The number

 let p = 1;

 // If already a power of 2

 if (n && !(n & (n - 1)))

 return n;

 // Find the next power of 2

 while (p < n)

 p <<= 1;

 return p;

}

// Function to find the memory used

function memoryUsed(arr, n)

{

 // Sum of array

 let sum = 0;

 // Traverse and find the sum of array

 for (let i = 0; i < n; i++)

 sum += arr[i];

 // Function call to find the nearest power of 2

 let nearest = nextPowerOf2(sum);

 return nearest;

}

// Driver Code

let arr = [ 1, 2, 3, 2 ];

let n = arr.length;

document.write(memoryUsed(arr, n));

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    8

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

