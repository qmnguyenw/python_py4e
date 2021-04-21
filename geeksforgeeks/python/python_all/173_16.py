Find number from given list for which value of the function is closest to A



Given a function **F(n) = P – (0.006 * n)** , where P is given. Given a list
of integers and a number, ![A](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e63249dbcb7bc1df2ae6aa725a10a1ad_l3.png). The task is to
find the number from the given list for which the value of the function is
closest to ![A](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e63249dbcb7bc1df2ae6aa725a10a1ad_l3.png).

 **Examples** :

    
    
    **Input** : P = 12, A = 5
            List = {1000, 2000} 
    **Output** : 1
    **Explanation** :
    Given, P=12, A=5
    For 1000, F(1000) is 12 - 1000×0.006 = 6
    For 2000, F(2000) is 12 - 2000×0.006 = 0
    As the nearest value to 5 is 6, 
    so the answer is 1000.
    
    **Input** : P = 21, A = -11
            List = {81234, 94124, 52141}
    **Output** : 3
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Iterate over each value in the given list and find F(n) for
every value. Now, compare the absolute difference of every value of F(n) and A
and the value of ![n](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-ad7ed49d64e4f28446c48c53a0e2718a_l3.png), for which the
absolute difference is minimum is the answer.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find number from

// given list for which value of the

// function is closest to A

#include <bits/stdc++.h>

using namespace std;

 

// Function to find number from

// given list for which value of the

// function is closest to A

int leastValue(int P, int A, int N, int a[])

{

 

 // Stores the final index

 int ans = -1;

 

 // Declaring a variable to store

 // the minimum absolute difference

 float tmp = (float)INFINITY;

 

 for (int i = 0; i < N; i++)

 {

 

 // Finding F(n)

 float t = P - a[i] * 0.006;

 

 // Updating the index of the answer if

 // new absolute difference is less than tmp

 if (abs(t-A) < tmp)

 {

 tmp = abs(t - A);

 ans = i;

 }

 }

 return a[ans];

}

 

// Driver code

int main()

{

 int N = 2, P = 12, A = 2005;

 int a[] = {1000, 2000};

 

 cout << leastValue(P, A, N, a) << endl;

}

 

// This code is contributed by

// sanjeev2552  
  
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

// Java program to find number from

// given list for which value of the

// function is closest to A

import java.util.*;

 

class GFG

{

 

// Function to find number from

// given list for which value of the

// function is closest to A

static int leastValue(int P, int A, 

 int N, int a[])

{

 

 // Stores the final index

 int ans = -1;

 

 // Declaring a variable to store

 // the minimum absolute difference

 float tmp = Float.MAX_VALUE;

 

 for (int i = 0; i < N; i++)

 {

 

 // Finding F(n)

 float t = (float) (P - a[i] * 0.006);

 

 // Updating the index of the answer if

 // new absolute difference is less than tmp

 if (Math.abs(t-A) < tmp)

 {

 tmp = Math.abs(t - A);

 ans = i;

 }

 }

 return a[ans];

}

 

// Driver code

public static void main(String[] args)

{

 int N = 2, P = 12, A = 2005;

 int a[] = {1000, 2000};

 

 System.out.println(leastValue(P, A, N, a));

}

}

 

// This code is contributed by 29AjayKumar  
  
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

# Python program to find number from

# given list for which value of the 

# function is closest to A

 

# Function to find number from 

# given list for which value of the 

# function is closest to A

def leastValue(P, A, N, a):

 # Stores the final index

 ans = -1

 

 # Declaring a variable to store

 # the minimum absolute difference

 tmp = float('inf')

 for i in range(N):

 # Finding F(n)

 t = P - a[i] * 0.006

 

 # Updating the index of the answer if

 # new absolute difference is less than tmp

 if abs(t - A) < tmp:

 tmp = abs(t - A)

 ans = i

 

 return a[ans]

 

# Driver Code

N, P, A = 2, 12, 5

a = [1000, 2000]

 

print(leastValue(P, A, N, a))  
  
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

// C# program to find number from

// given list for which value of the

// function is closest to A

using System;

 

class GFG

{

 

// Function to find number from

// given list for which value of the

// function is closest to A

static int leastValue(int P, int A, 

 int N, int []a)

{

 

 // Stores the final index

 int ans = -1;

 

 // Declaring a variable to store

 // the minimum absolute difference

 float tmp = float.MaxValue;

 

 for (int i = 0; i < N; i++)

 {

 

 // Finding F(n)

 float t = (float) (P - a[i] * 0.006);

 

 // Updating the index of the answer if

 // new absolute difference is less than tmp

 if (Math.Abs(t-A) < tmp)

 {

 tmp = Math.Abs(t - A);

 ans = i;

 }

 }

 return a[ans];

}

 

// Driver code

public static void Main(String[] args)

{

 int N = 2, P = 12, A = 2005;

 int []a = {1000, 2000};

 

 Console.WriteLine(leastValue(P, A, N, a));

}

}

 

// This code is contributed by Rajput-Ji  
  
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

// PHP program to find number from 

// given list for which value of the 

// function is closest to A

 

// Function to find number from 

// given list for which value of the 

// function is closest to A

function leastValue($P, $A, $N, $a)

{

 // Stores the final index

 $ans = -1;

 

 // Declaring a variable to store

 // the minimum absolute difference

 $tmp = PHP_INT_MAX;

 for($i = 0; $i < $N; $i++)

 {

 // Finding F(n)

 $t = $P - $a[$i] * 0.006;

 

 // Updating the index of the 

 // answer if new absolute 

 // difference is less than tmp

 if (abs($t - $A) < $tmp)

 {

 $tmp = abs($t - $A);

 $ans = $i;

 }

 } 

 return $a[$ans];

}

 

// Driver Code

$N = 2;

$P = 12;

$A = 5;

$a = array(1000, 2000);

 

print(leastValue($P, $A, $N, $a));

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    1000
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

