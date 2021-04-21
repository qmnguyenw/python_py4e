Minimize the sum of squares of sum of N/2 paired formed by N numbers



Given N numbers(N is an even number). Divide the N numbers into N/2 pairs in
such a way that the sum of squares of the sum of numbers in pairs is minimal.
The task is to print the minimal sum.

 **Examples:**

    
    
    **Input:** a[] = {8, 5, 2, 3}
    **Output:** 164 
    Divide them into two groups of {2, 8} and {3, 5}
    to give (2+8)2 + (3+5)2 = 164   
    
    **Input:** a[] = {1, 1, 1, 2, 2, 2}
    **Output:** 27 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The task is to minimize the sum of squares, hence we divide the
smallest and largest number in the first group and the second smallest and
second largest in the second group and so on till N/2 groups are formed. Add
the numbers and store the sum of squares of them which will be the final
answer.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to minimize the sum

// of squares of sum of numbers

// of N/2 groups of N numbers

 

#include <bits/stdc++.h>

using namespace std;

 

// Function that returns the minimize sum

// of square of sum of numbers of every group

int findMinimal(int a[], int n)

{

 // Sort the array elements

 sort(a, a + n);

 

 int sum = 0;

 

 // Iterate for the first half of array

 for (int i = 0; i < n / 2; i++) 

 sum += (a[i] + a[n - i - 1]) 

 * (a[i] + a[n - i - 1]);

 

 return sum;

}

 

// Driver Code

int main()

{

 int a[] = { 8, 5, 2, 3 };

 int n = sizeof(a) / sizeof(a[0]);

 

 cout << findMinimal(a, n);

 

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

// Java program to minimize the sum

// of squares of sum of numbers 

// of N/2 groups of N numbers 

import java.util.Arrays;

 

class GFG 

{ 

 

 // Function that returns the minimize sum 

 // of square of sum of numbers of every group 

 static int findMinimal(int []a, int n) 

 { 

 // Sort the array elements 

 Arrays.sort(a); 

 

 int sum = 0; 

 

 // Iterate for the first half of array 

 for (int i = 0; i < n / 2; i++) 

 sum += (a[i] + a[n - i - 1]) * 

 (a[i] + a[n - i - 1]); 

 

 return sum; 

 } 

 

 // Driver Code 

 public static void main(String str[]) 

 { 

 int []a = { 8, 5, 2, 3 }; 

 int n = a.length; 

 System.out.println(findMinimal(a, n)); 

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

# Python 3 program to minimize the sum

# of squares of sum of numbers

# of N/2 groups of N numbers

 

# Function that returns the minimize sum

# of square of sum of numbers of every group

def findMinimal(a, n):

 

 # Sort the array elements

 a.sort()

 

 sum = 0

 

 # Iterate for the first half of array

 for i in range( n // 2): 

 sum += ((a[i] + a[n - i - 1]) *

 (a[i] + a[n - i - 1]))

 

 return sum

 

# Driver Code

if __name__ == "__main__":

 

 a = [ 8, 5, 2, 3 ]

 n = len(a)

 

 print(findMinimal(a, n))

 

# This code is contributed by ita_c  
  
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

// C# program to minimize the sum

// of squares of sum of numbers

// of N/2 groups of N numbers

using System;

 

class GFG

{

 

// Function that returns the minimize sum

// of square of sum of numbers of every group

static int findMinimal(int []a, int n)

{

 // Sort the array elements

 Array.Sort(a);

 

 int sum = 0;

 

 // Iterate for the first half of array

 for (int i = 0; i < n / 2; i++) 

 sum += (a[i] + a[n - i - 1]) *

 (a[i] + a[n - i - 1]);

 

 return sum;

}

 

// Driver Code

public static void Main()

{

 int []a = { 8, 5, 2, 3 };

 int n = a.Length;

 

 Console.Write(findMinimal(a, n));

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

// PHP program to minimize the sum

// of squares of sum of numbers

// of N/2 groups of N numbers

 

// Function that returns the minimize sum

// of square of sum of numbers of every group

function findMinimal($a, $n)

{

 // Sort the array elements

 sort($a);

 

 $sum = 0;

 

 // Iterate for the first half of array

 for ($i = 0; $i < $n / 2; $i++) 

 $sum += ($a[$i] + $a[$n - $i - 1]) * 

 ($a[$i] + $a[$n - $i - 1]);

 

 return $sum;

}

 

// Driver Code

$a = array(8, 5, 2, 3 );

$n = sizeof($a);

 

echo findMinimal($a, $n);

 

// This code is contributed by ajit

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    164
    

**Time Complexity:** O(N log N)  
 **Auxiliary Space:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

