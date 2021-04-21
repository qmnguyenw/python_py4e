Minimum number of cubes whose sum equals to given number N



Given an integer **n** , the task is to find the minimum number of cubes whose
sum equals to **N**.

 **Examples:**

>  **Input:** N = 496  
>  **Output:** 3  
> 43 \+ 63 \+ 63 = 496  
> Note that 13 \+ 33 \+ 53 \+ 73 = 496 but it requires 4 cubes.
>
>  **Input:** N = 15  
>  **Output:** 8

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** Write a recursive method that will take every perfect
cube less than **N** say **X** as part of the summation and then recur for the
number of cubes required for the remaining sum **N – X**. The time complexity
of this solution is exponential.

  

  

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

#include <iostream>

using namespace std;

 

// Function to return the minimum

// number of cubes whose sum is k

int MinOfCubed(int k)

{

 // If k is less than the 2^3

 if (k < 8)

 return k;

 

 // Initialize with the maximum

 // number of cubes required

 int res = k;

 for (int i = 1; i <= k; i++) {

 if ((i * i * i) > k)

 return res;

 res = min(res, MinOfCubed(k - (i * i * i)) + 1);

 }

 return res;

}

 

// Driver code

int main()

{

 int num = 15;

 cout << MinOfCubed(num);

 

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

// Java implementation of the approach

class GFG {

 

 // Function to return the minimum

 // number of cubes whose sum is k

 static int MinOfCubed(int k)

 {

 // If k is less than the 2^3

 if (k < 8)

 return k;

 

 // Initialize with the maximum

 // number of cubes required

 int res = k;

 for (int i = 1; i <= k; i++) {

 if ((i * i * i) > k)

 return res;

 res = Math.min(res, MinOfCubed(k - (i * i * i)) + 1);

 }

 return res;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int num = 15;

 System.out.println(MinOfCubed(num));

 }

}

 

// This code has been contributed by 29AjayKumar  
  
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

# Python3 implementation of the approach

 

# Function to return the minimum 

# number of cubes whose sum is k 

def MinOfCubed(k):

 

 # If k is less than the 2 ^ 3 

 if (k < 8): 

 return k; 

 

 # Initialize with the maximum 

 # number of cubes required 

 res = k; 

 for i in range(1, k + 1): 

 if ((i * i * i) > k): 

 return res; 

 res = min(res, MinOfCubed(k - (i * i * i)) + 1); 

 return res; 

 

# Driver code 

num = 15; 

print(MinOfCubed(num));

 

# This code contributed by PrinciRaj1992   
  
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

 

 // Function to return the minimum

 // number of cubes whose sum is k

 static int MinOfCubed(int k)

 {

 // If k is less than the 2^3

 if (k < 8)

 return k;

 

 // Initialize with the maximum

 // number of cubes required

 int res = k;

 for (int i = 1; i <= k; i++) {

 if ((i * i * i) > k)

 return res;

 res = Math.Min(res, MinOfCubed(k - (i * i * i)) + 1);

 }

 return res;

 }

 

 // Driver code

 static public void Main()

 {

 int num = 15;

 Console.WriteLine(MinOfCubed(num));

 }

}

 

// This code has been contributed by ajit.  
  
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

 

// Function to return the minimum 

// number of cubes whose sum is k 

function MinOfCubed($k) 

{ 

 // If k is less than the 2^3 

 if ($k < 8) 

 return $k; 

 

 // Initialize with the maximum 

 // number of cubes required 

 $res = $k; 

 for ($i = 1; $i <= $k; $i++)

 { 

 if (($i * $i * $i) > $k) 

 return $res; 

 $res = min($res, MinOfCubed($k - ($i *$i * $i)) +
1); 

 } 

 return $res; 

} 

 

 // Driver code 

 $num = 15; 

 echo MinOfCubed($num); 

 

 // This code is contributed by Ryuga

 

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    8
    

**Efficient approach:** If we draw the complete recursion tree for the above
solution, we can see that many sub-problems are solved again and again, so we
can see that this problem has the overlapping sub-problems property. This
leads us to solve the problem using the Dynamic Programming paradigm.

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

 

// Function to return the minimum

// number of cubes whose sum is k

int MinOfCubedDP(int k)

{

 int *DP = new int[k + 1], j = 1, t = 1;

 DP[0] = 0;

 for (int i = 1; i <= k; i++) {

 DP[i] = INT_MAX;

 

 // While current perfect cube

 // is less than current element

 while (j <= i) {

 

 // If i is a perfect cube

 if (j == i)

 DP[i] = 1;

 

 // i = (i - 1) + 1^3

 else if (DP[i] > DP[i - j])

 DP[i] = DP[i - j] + 1;

 

 // Next perfect cube

 t++;

 j = t * t * t;

 }

 

 // Re-initialization for next element

 t = j = 1;

 }

 return DP[k];

}

 

// Driver code

int main()

{

 int num = 15;

 cout << MinOfCubedDP(num);

 

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

// Java implementation of the approach

class GFG {

 

 // Function to return the minimum

 // number of cubes whose sum is k

 static int MinOfCubedDP(int k)

 {

 int[] DP = new int[k + 1];

 int j = 1, t = 1;

 DP[0] = 0;

 for (int i = 1; i <= k; i++) {

 DP[i] = Integer.MAX_VALUE;

 

 // While current perfect cube

 // is less than current element

 while (j <= i) {

 

 // If i is a perfect cube

 if (j == i)

 DP[i] = 1;

 

 // i = (i - 1) + 1^3

 else if (DP[i] > DP[i - j])

 DP[i] = DP[i - j] + 1;

 

 // Next perfect cube

 t++;

 j = t * t * t;

 }

 

 // Re-initialization for next element

 t = j = 1;

 }

 return DP[k];

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int num = 15;

 System.out.println(MinOfCubedDP(num));

 }

}

 

/* This code contributed by PrinciRaj1992 */  
  
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

# Python implementation of the approach

import sys

 

# Function to return the minimum

# number of cubes whose sum is k

def MinOfCubedDP(k):

 DP = [0] * (k + 1);

 j = 1;

 t = 1;

 DP[0] = 0;

 for i in range(1, k + 1):

 DP[i] = sys.maxsize;

 

 # While current perfect cube

 # is less than current element

 while (j <= i):

 

 # If i is a perfect cube

 if (j == i):

 DP[i] = 1;

 

 # i = (i - 1) + 1^3

 elif (DP[i] > DP[i - j]):

 DP[i] = DP[i - j] + 1;

 

 # Next perfect cube

 t += 1;

 j = t * t * t;

 

 # Re-initialization for next element

 t = j = 1;

 return DP[k];

 

 

# Driver code

num = 15;

print(MinOfCubedDP(num));

 

# This code contributed by Rajput-Ji  
  
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

 

 // Function to return the minimum

 // number of cubes whose sum is k

 static int MinOfCubedDP(int k)

 {

 int[] DP = new int[k + 1];

 int j = 1, t = 1;

 DP[0] = 0;

 for (int i = 1; i <= k; i++) {

 DP[i] = int.MaxValue;

 

 // While current perfect cube

 // is less than current element

 while (j <= i) {

 

 // If i is a perfect cube

 if (j == i)

 DP[i] = 1;

 

 // i = (i - 1) + 1^3

 else if (DP[i] > DP[i - j])

 DP[i] = DP[i - j] + 1;

 

 // Next perfect cube

 t++;

 j = t * t * t;

 }

 

 // Re-initialization for next element

 t = j = 1;

 }

 return DP[k];

 }

 

 // Driver code

 public static void Main()

 {

 int num = 15;

 Console.WriteLine(MinOfCubedDP(num));

 }

}

 

/* This code contributed by Code_Mech */  
  
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

 

// Function to return the minimum

// number of cubes whose sum is k

function MinOfCubedDP($k)

{

 $DP = array($k + 1);

 $j = 1; $t = 1;

 $DP[0] = 0;

 for ($i = 1; $i <= $k; $i++) 

 {

 $DP[$i] = PHP_INT_MAX;

 

 // While current perfect cube

 // is less than current element

 while ($j <= $i) 

 {

 

 // If i is a perfect cube

 if ($j == $i)

 $DP[$i] = 1;

 

 // i = (i - 1) + 1^3

 else if ($DP[$i] > $DP[$i - $j])

 $DP[$i] = $DP[$i - $j] + 1;

 

 // Next perfect cube

 $t++;

 $j = $t * $t * $t;

 }

 

 // Re-initialization for next element

 $t = $j = 1;

 }

 return $DP[$k];

}

 

// Driver code

$num = 15;

echo(MinOfCubedDP($num));

 

// This code contributed by Code_Mech 

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    8
    

On the first glance, it seems that the algorithm works in polynomial time
because we have two nested loops, the outer loop takes O(n), and the inner
loop takes O(n^(1/3)). So the overall algorithm takes O(n*n^(1/3)). But what
is the complexity as a function of input length? To represent a number in a
size of n we need m=log(n) – (log of base 2) bits. In this case n=2^m. If we
set 2^m as n in the formula O(n*n^(1/3)), we see that the time complexity is
still exponential. This algorithm is called Pseudo-polynomial.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

