Select numbers in such way to maximize the amount of money



Given two arrays A1 and A2 of N numbers. There are two people A and B who
select numbers out of N. If A selects i-th number, then he will be paid A1[i]
amount of money and if B selects i-th number then he will be paid A2[i] amount
of money but A cannot select more than **X** numbers and B cannot select more
than **Y** numbers. The task is to select N numbers in such a way that the
amount of total money is maximized at the end.

 **Note:** X + Y >= N

    
    
    **Examples:**
    **Input** : N = 5, X = 3, Y = 3 
           A1[] = {1, 2, 3, 4, 5}, 
           A2= {5, 4, 3, 2, 1}
    **Output:** 21 
    B will take the first 3 orders and A 
    will take the last two orders. 
    
    **Input** : N = 2, X = 1, Y = 1 
           A1[] = {10, 10}, A2= {20, 20}
    **Output:** 30 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Let us create a new array C such that **C[i] = A2[i] – A1[i]**.
Now we will sort the array **C** in decreasing order. Note that the condition
**X + Y >= N** guarantees that we will be able to assign the number to any one
of the persons. Assume that for some i, A1[i] > A2[i] and you assigned an
order to B, loss encountered due to this assignment is C[i]. Similarly, for
some i, A2[i] > A1[i] and you assigned a number to A, loss encountered due to
this assignment is C[i]. As we want to minimize the loss encountered, it is
better to process the numbers having high possible losses, because we can try
to reduce the loss in the starting part. There is no point of selecting a
number with high loss after assigning a number with less loss. Hence we
initially assign all numbers to A initially, then subtract the loss from them
greedily. Once the assigned order number is under X, then we store the maximal
of that.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to maximize profit

 

#include <bits/stdc++.h>

using namespace std;

 

// Function that maximizes the sum

int maximize(int A1[], int A2[], int n,

 int x, int y)

{

 // Array to store the loss

 int c[n];

 

 // Initial sum

 int sum = 0;

 

 // Generate the array C

 for (int i = 0; i < n; i++) {

 c[i] = A2[i] - A1[i];

 sum += A1[i];

 }

 

 // Sort the array elements

 // in descending order

 sort(c, c + n, greater<int>());

 

 // Variable to store the answer

 int maxi = -1;

 

 // Iterate in the array, C

 for (int i = 0; i < n; i++) {

 

 // Subtract the loss

 sum += c[i];

 

 // Check if X orders are going

 // to be used

 if (i + 1 >= (n - x))

 maxi = max(sum, maxi);

 }

 

 return maxi;

}

 

// Driver Code

int main()

{

 int A1[] = { 1, 2, 3, 4, 5 };

 int A2[] = { 5, 4, 3, 2, 1 };

 

 int n = 5;

 int x = 3, y = 3;

 

 cout << maximize(A1, A2, n, x, y);

 

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

// Java program to maximize profit

import java.util.*;

 

class GFG

{

 

// Function that maximizes the sum

static int maximize(int A1[], int A2[], int n,

 int x, int y)

{

 // Array to store the loss

 int[] c = new int[n];

 

 // Initial sum

 int sum = 0;

 

 // Generate the array C

 for (int i = 0; i < n; i++) 

 {

 c[i] = A2[i] - A1[i];

 sum += A1[i];

 }

 

 // Sort the array elements

 // in descending order

int temp;

for(int i = 0; i < n - 1; i++)

{

 if(c[i] < c[i+1])

 {

 temp = c[i];

 c[i] = c[i + 1];

 c[i + 1] = temp;

 }

}

 

 // Variable to store the answer

 int maxi = -1;

 

 // Iterate in the array, C

 for (int i = 0; i < n; i++) 

 {

 

 // Subtract the loss

 sum += c[i];

 

 // Check if X orders are going

 // to be used

 if (i + 1 >= (n - x))

 maxi = Math.max(sum, maxi);

 }

 

 return maxi;

}

 

// Driver Code

public static void main(String args[])

{

 int A1[] = { 1, 2, 3, 4, 5 };

 int A2[] = { 5, 4, 3, 2, 1 };

 

 int n = 5;

 int x = 3, y = 3;

 

 System.out.println(maximize(A1, A2, n, x, y));

}

}

 

// This code is contributed by

// Surendra_Gangwar  
  
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

# Python3 program to maximize profit

 

# Function that maximizes the Sum

def maximize(A1, A2, n, x, y):

 

 # Array to store the loss

 c = [0 for i in range(n)]

 

 # Initial Sum

 Sum = 0

 

 # Generate the array C

 for i in range(n):

 c[i] = A2[i] - A1[i]

 Sum += A1[i]

 

 # Sort the array elements

 # in descending order

 c.sort()

 c = c[::-1]

 

 # Variable to store the answer

 maxi = -1

 

 # Iterate in the array, C

 for i in range(n):

 

 # Subtract the loss

 Sum += c[i]

 

 # Check if X orders are going

 # to be used

 if (i + 1 >= (n - x)):

 maxi = max(Sum, maxi)

 

 return maxi

 

# Driver Code

A1 = [ 1, 2, 3, 4, 5 ]

A2 = [ 5, 4, 3, 2, 1 ]

 

n = 5

x, y = 3, 3

 

print(maximize(A1, A2, n, x, y))

 

# This code is contributed

# by Mohit Kumar  
  
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

// C# program to maximize profit

using System;

 

class GFG

{

 

 // Function that maximizes the sum

 static int maximize(int [] A1, int [] A2, int n,

 int x, int y)

 {

 // Array to store the loss

 int [] c = new int[n];

 

 // Initial sum

 int sum = 0;

 

 // Generate the array C

 for (int i = 0; i < n; i++) 

 {

 c[i] = A2[i] - A1[i];

 sum += A1[i];

 }

 

 // Sort the array elements

 // in descending order

 int temp;

 for(int i = 0; i < n - 1; i++)

 {

 if(c[i] < c[i+1])

 {

 temp = c[i];

 c[i] = c[i + 1];

 c[i + 1] = temp;

 }

 }

 

 // Variable to store the answer

 int maxi = -1;

 

 // Iterate in the array, C

 for (int i = 0; i < n; i++) 

 {

 

 // Subtract the loss

 sum += c[i];

 

 // Check if X orders are going

 // to be used

 if (i + 1 >= (n - x))

 maxi = Math.Max(sum, maxi);

 }

 

 return maxi;

 }

 

 // Driver Code

 public static void Main()

 {

 int [] A1 = { 1, 2, 3, 4, 5 };

 int [] A2 = { 5, 4, 3, 2, 1 };

 

 int n = 5;

 int x = 3, y = 3;

 

 Console.WriteLine(maximize(A1, A2, n, x, y));

 }

}

 

// This code is contributed by ihritik  
  
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

// PHP program to maximize profit 

 

// Function that maximizes the sum 

function maximize($A1, $A2, $n, $x, $y) 

{ 

 # Array to store the loss 

 $c = array();

 

 # Initial sum 

 $sum = 0; 

 

 // Generate the array C 

 for ($i = 0; $i < $n; $i++) 

 { 

 $c[$i] = $A2[$i] - $A1[$i]; 

 $sum += $A1[$i]; 

 } 

 

 // Sort the array elements 

 // in descending order 

 rsort($c); 

 

 // Variable to store the answer 

 $maxi = -1; 

 

 // Iterate in the array, C 

 for ($i = 0; $i < $n; $i++) 

 { 

 

 // Subtract the loss 

 $sum += $c[$i]; 

 

 // Check if X orders are going 

 // to be used 

 if ($i + 1 >= ($n - $x)) 

 $maxi = max($sum, $maxi); 

 } 

 

 return $maxi; 

} 

 

# Driver Code 

$A1 = array( 1, 2, 3, 4, 5 ); 

$A2 = array( 5, 4, 3, 2, 1 ); 

 

$n = 5; 

$x = 3;

$y = 3; 

 

echo maximize($A1, $A2, $n, $x, $y); 

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    21
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

