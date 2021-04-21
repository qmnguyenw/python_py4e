Check if an array of 1s and 2s can be divided into 2 parts with equal sum



Given an array containing **N** elements, each element is either 1 or 2. The
task is to find out whether the array can be divided into 2 parts such that
sum of elements in both parts is equal.

 **Examples:**

    
    
    **Input :** N = 3, arr[] = {1, 1, 2}
    **Output :** YES
    
    **Input :** N = 4, arr[] = {1, 2, 2, }
    **Output :** NO
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The idea is to observe that the array can be divided into two parts with equal
sum only if the overall sum of the array is even, i.e. divisible by 2.

Let’s say the overall sum of the array is denoted by **sum**.

Now, there arises two cases:

  

  

  *  **If sum/2 is even** : When the value of sum/2 is also even, it means that sum of each of the two parts is also even and we need not to consider anything special. So, return true for this case.
  *  **If sum/2 is odd** : When the value of sum/2 is ODD, it means that sum of each part is also odd. This is only possible when each of the two parts of the array contains atleast one 1. Consider the cases when sum = 2 or 6 or 10. So, when sum/2 is odd, check if there is atleast one 1 in the array.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above

// approach:

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to check if it is possible to

// split the array in two parts with

// equal sum

bool isSpiltPossible(int n, int a[])

{

 int sum = 0, c1 = 0;

 

 // Calculate sum of elements

 // and count of 1's

 for (int i = 0; i < n; i++) {

 sum += a[i];

 

 if (a[i] == 1) {

 c1++;

 }

 }

 

 // If total sum is odd, return False

 if (sum % 2)

 return false;

 

 // If sum of each part is even,

 // return True

 if ((sum / 2) % 2 == 0)

 return true;

 

 // If sum of each part is even but

 // there is atleast one 1

 if (c1 > 0)

 return true;

 else

 return false;

}

 

// Driver Code

int main()

{

 int n = 3;

 int a[] = { 1, 1, 2 };

 

 if (isSpiltPossible(n, a))

 cout << "YES";

 else

 cout << "NO";

 

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

// Java implementation of the above

// approach:

class GFG

{

 

// Function to check if it is possible 

// to split the array in two parts with

// equal sum

static boolean isSpiltPossible(int n, 

 int a[])

{

 int sum = 0, c1 = 0;

 

 // Calculate sum of elements

 // and count of 1's

 for (int i = 0; i < n; i++) 

 {

 sum += a[i];

 

 if (a[i] == 1) 

 {

 c1++;

 }

 }

 

 // If total sum is odd, return False

 if(sum % 2 != 0)

 return false;

 

 // If sum of each part is even,

 // return True

 if ((sum / 2) % 2 == 0)

 return true;

 

 // If sum of each part is even but

 // there is atleast one 1

 if (c1 > 0)

 return true;

 else

 return false;

}

 

// Driver Code

public static void main(String[] args)

{

 int n = 3;

 int a[] = { 1, 1, 2 };

 

 if (isSpiltPossible(n, a))

 System.out.println("YES");

 else

 System.out.println("NO");

}

}

 

// This code is contributed by 

// Code Mech  
  
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

# Python3 implementation of the above

# approach:

 

# Function to check if it is possible 

# to split the array in two halfs with

# equal Sum

def isSpiltPossible(n, a):

 

 Sum = 0

 c1 = 0

 

 # Calculate Sum of elements

 # and count of 1's

 for i in range(n):

 Sum += a[i]

 

 if (a[i] == 1):

 c1 += 1

 

 # If total Sum is odd, return False

 if (Sum % 2):

 return False

 

 # If Sum of each half is even,

 # return True

 if ((Sum // 2) % 2 == 0):

 return True

 

 # If Sum of each half is even 

 # but there is atleast one 1

 if (c1 > 0):

 return True

 else:

 return False

 

# Driver Code

n = 3

a = [ 1, 1, 2 ]

 

if (isSpiltPossible(n, a)):

 print("YES")

else:

 print("NO")

 

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

// C# implementation of the above

// approach:

using System;

 

class GFG

{

 

// Function to check if it is possible 

// to split the array in two parts with

// equal sum

static bool isSpiltPossible(int n, 

 int[] a)

{

 int sum = 0, c1 = 0;

 

 // Calculate sum of elements

 // and count of 1's

 for (int i = 0; i < n; i++) 

 {

 sum += a[i];

 

 if (a[i] == 1) 

 {

 c1++;

 }

 }

 

 // If total sum is odd, return False

 if(sum % 2 != 0)

 return false;

 

 // If sum of each part is even,

 // return True

 if ((sum / 2) % 2 == 0)

 return true;

 

 // If sum of each part is even but

 // there is atleast one 1

 if (c1 > 0)

 return true;

 else

 return false;

}

 

// Driver Code

public static void Main()

{

 int n = 3;

 int[] a = { 1, 1, 2 };

 

 if (isSpiltPossible(n, a))

 Console.WriteLine("YES");

 else

 Console.WriteLine("NO");

}

}

 

// This code is contributed by 

// Code Mech  
  
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

// PHP implementation of the above

// approach:

 

// Function to check if it is possible 

// to split the array in two parts with

// equal sum

function isSpiltPossible($n, $a)

{

 $sum = 0; $c1 = 0;

 

 // Calculate sum of elements

 // and count of 1's

 for ($i = 0; $i < $n; $i++) 

 {

 $sum += $a[$i];

 

 if ($a[$i] == 1) 

 {

 $c1++;

 }

 }

 

 // If total sum is odd, return False

 if($sum % 2 != 0)

 return false;

 

 // If sum of each part is even,

 // return True

 if (($sum / 2) % 2 == 0)

 return true;

 

 // If sum of each part is even but

 // there is atleast one 1

 if ($c1 > 0)

 return true;

 else

 return false;

}

 

// Driver Code

$n = 3;

$a = array( 1, 1, 2 );

 

if (isSpiltPossible($n, $a))

 echo("YES");

else

 echo("NO");

 

// This code is contributed by 

// Code Mech

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    YES
    

**Time Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

