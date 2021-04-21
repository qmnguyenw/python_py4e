Find minimum positive integer x such that a(x^2) + b(x) + c >= k



Given four integers **a** , **b** , **c** and **k**. The task is to find the
minimum positive value of **x** such that **ax 2 \+ bx + c ≥ k**.

 **Examples:**

>  **Input:** a = 3, b = 4, c = 5, k = 6  
>  **Output:** 1  
> For x = 0, a * 0 + b * 0 + c = 5 < 6  
> For x = 1, a * 1 + b * 1 + c = 3 + 4 + 5 = 12 > 6
>
>  **Input:** a = 2, b = 7, c = 6, k = 3  
>  **Output:** 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use binary search. The lower limit for our
search will be **0** since **x** has to be minimum positive integer.

  

  

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

 

// Function to return the minimum positive

// integer satisfying the given equation

int MinimumX(int a, int b, int c, int k)

{

 int x = INT_MAX;

 

 if (k <= c)

 return 0;

 

 int h = k - c;

 int l = 0;

 

 // Binary search to find the value of x

 while (l <= h) {

 int m = (l + h) / 2;

 if ((a * m * m) + (b * m) > (k - c)) {

 x = min(x, m);

 h = m - 1;

 }

 else if ((a * m * m) + (b * m) < (k - c))

 l = m + 1;

 else

 return m;

 }

 

 // Return the answer

 return x;

}

 

// Driver code

int main()

{

 int a = 3, b = 2, c = 4, k = 15;

 cout << MinimumX(a, b, c, k);

 

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

class GFG

{

 

// Function to return the minimum positive

// integer satisfying the given equation

static int MinimumX(int a, int b, int c, int k)

{

 int x = Integer.MAX_VALUE;

 

 if (k <= c)

 return 0;

 

 int h = k - c;

 int l = 0;

 

 // Binary search to find the value of x

 while (l <= h) 

 {

 int m = (l + h) / 2;

 if ((a * m * m) + (b * m) > (k - c)) 

 {

 x = Math.min(x, m);

 h = m - 1;

 }

 else if ((a * m * m) + (b * m) < (k - c))

 l = m + 1;

 else

 return m;

 }

 

 // Return the answer

 return x;

}

 

// Driver code

public static void main(String[] args)

{

 int a = 3, b = 2, c = 4, k = 15;

 System.out.println(MinimumX(a, b, c, k));

}

}

 

// This code is contributed by Code_Mech.   
  
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

 

# Function to return the minimum positive

# integer satisfying the given equation

def MinimumX(a, b, c, k):

 

 x = 10**9

 

 if (k <= c):

 return 0

 

 h = k - c

 l = 0

 

 # Binary search to find the value of x

 while (l <= h):

 m = (l + h) // 2

 if ((a * m * m) + (b * m) > (k - c)):

 x = min(x, m)

 h = m - 1

 

 elif ((a * m * m) + (b * m) < (k - c)):

 l = m + 1

 else:

 return m

 

 # Return the answer

 return x

 

# Driver code

a, b, c, k = 3, 2, 4, 15

print(MinimumX(a, b, c, k))

 

# This code is contributed by mohit kumar  
  
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

 

class GFG

{

 

// Function to return the minimum positive

// integer satisfying the given equation

static int MinimumX(int a, int b, int c, int k)

{

 int x = int.MaxValue;

 

 if (k <= c)

 return 0;

 

 int h = k - c;

 int l = 0;

 

 // Binary search to find the value of x

 while (l <= h) 

 {

 int m = (l + h) / 2;

 if ((a * m * m) + (b * m) > (k - c)) 

 {

 x = Math.Min(x, m);

 h = m - 1;

 }

 else if ((a * m * m) + (b * m) < (k - c))

 l = m + 1;

 else

 return m;

 }

 

 // Return the answer

 return x;

}

 

// Driver code

public static void Main()

{

 int a = 3, b = 2, c = 4, k = 15;

 Console.Write(MinimumX(a, b, c, k));

}

}

 

// This code is contributed by Akanksha Rai  
  
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

 

// Function to return the minimum positive 

// integer satisfying the given equation 

function MinimumX($a, $b, $c, $k) 

{ 

 $x = PHP_INT_MAX; 

 

 if ($k <= $c) 

 return 0; 

 

 $h = $k - $c; 

 $l = 0; 

 

 // Binary search to find the value of x 

 while ($l <= $h) 

 { 

 $m = floor(($l + $h) / 2); 

 if (($a * $m * $m) + 

 ($b * $m) > ($k - $c))

 { 

 $x = min($x, $m); 

 $h = $m - 1; 

 } 

 else if (($a * $m * $m) + 

 ($b * $m) < ($k - $c)) 

 $l = $m + 1; 

 else

 return $m; 

 } 

 

 // Return the answer 

 return $x; 

} 

 

// Driver code 

$a = 3; $b = 2; $c = 4; $k = 15; 

 

echo MinimumX($a, $b, $c, $k);

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

