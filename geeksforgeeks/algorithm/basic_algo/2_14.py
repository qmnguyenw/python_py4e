Maximize the value of A by replacing some of its digits with digits of B



Given two string **A** and **B** which represents two integers, the task is to
print the maximized value of **A** after replacing 0 or more digits of **A**
with any digit of **B**.

 **Note** : A digit in **B** can only be used once.

 **Examples:**

>  **Input:** A = “1234”, B = “4321”  
>  **Output:** 4334  
> 1 can be replaced with 4 and 2 can be replaced with 3.
>
>  **Input:** A = “1002”, B = “100”  
>  **Output:** 1102  
> The first 0 can be replaced with a 1.
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Since the value of **A** has to maximized, any digit will be
replaced by only digits of greater value. The digits on the left have more
significance in contributing to the value, so they should be replaced with as
large values as possible. Sort **B** and iterate from left to right in **A**
and try replacing the current digit with the maximum of available options if
possible.

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

 

// Function to return the maximized value of A

string maxValue(string a, string b)

{

 // Sort digits in ascending order

 sort(b.begin(), b.end());

 int n = a.length();

 int m = b.length();

 

 // j points to largest digit in B

 int j = m - 1;

 for (int i = 0; i < n; i++) {

 

 // If all the digits of b have been used

 if (j < 0)

 break;

 

 if (b[j] > a[i]) {

 a[i] = b[j];

 

 // Current digit has been used

 j--;

 }

 }

 

 // Return the maximized value

 return a;

}

 

// Driver code

int main()

{

 string a = "1234";

 string b = "4321";

 

 cout << maxValue(a, b);

 

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

 

import java.util.*;

 

class GFG{ 

 

// Function to return the maximized value of A 

static String maxValue(char []a, char []b) 

{ 

 // Sort digits in ascending order 

 Arrays.sort(b); 

 int n = a.length; 

 int m = b.length; 

 

 // j points to largest digit in B 

 int j = m - 1; 

 for (int i = 0; i < n; i++) { 

 

 // If all the digits of b have been used 

 if (j < 0) 

 break; 

 

 if (b[j] > a[i]) { 

 a[i] = b[j]; 

 

 // Current digit has been used 

 j--; 

 } 

 } 

 

 // Return the maximized value 

 return String.valueOf(a); 

} 

 

// Driver code 

public static void main(String[] args) 

{ 

 String a = "1234"; 

 String b = "4321"; 

 

 System.out.print(maxValue(a.toCharArray(), b.toCharArray())); 

}

} 

 

// This code is contributed by PrinciRaj1992  
  
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

 

# Function to return the maximized

# value of A

def maxValue(a, b):

 

 # Sort digits in ascending order

 b = sorted(b)

 bi = [i for i in b]

 ai = [i for i in a]

 

 n = len(a)

 m = len(b)

 

 # j points to largest digit in B

 j = m - 1

 for i in range(n):

 

 # If all the digits of b 

 # have been used

 if (j < 0):

 break

 

 if (bi[j] > ai[i]):

 ai[i] = bi[j]

 

 # Current digit has been used

 j -= 1

 

 # Return the maximized value

 x = "" . join(ai)

 return x

 

# Driver code

a = "1234"

b = "4321"

 

print(maxValue(a, b))

 

# This code is contributed 

# by mohit kumar  
  
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

 

// Function to return the maximized value of A 

static String maxValue(char []a, char []b) 

{ 

 // Sort digits in ascending order 

 Array.Sort(b); 

 int n = a.Length; 

 int m = b.Length; 

 

 // j points to largest digit in B 

 int j = m - 1; 

 for (int i = 0; i < n; i++)

 { 

 

 // If all the digits of b have been used 

 if (j < 0) 

 break; 

 

 if (b[j] > a[i]) 

 { 

 a[i] = b[j]; 

 

 // Current digit has been used 

 j--; 

 } 

 } 

 

 // Return the maximized value 

 return String.Join("",a); 

} 

 

// Driver code 

public static void Main(String[] args) 

{ 

 String a = "1234"; 

 String b = "4321"; 

 

 Console.Write(maxValue(a.ToCharArray(), b.ToCharArray())); 

}

} 

 

// This code is contributed by PrinciRaj1992  
  
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

 

// Function to return the maximized value of A 

function maxValue($a, $b) 

{ 

 // Sort digits in ascending order 

 sort($b); 

 $n = sizeof($a); 

 $m = sizeof($b); 

 

 // j points to largest digit in B 

 $j = $m - 1; 

 for ($i = 0; $i < $n; $i++)

 { 

 

 // If all the digits of b have been used 

 if ($j < 0) 

 break; 

 

 if ($b[$j] > $a[$i])

 { 

 $a[$i] = $b[$j]; 

 

 // Current digit has been used 

 $j--; 

 } 

 } 

 

 // Convert array into string

 $a = implode("",$a);

 

 // Return the maximized value 

 return $a ;

} 

 

 // Driver code 

 # convert string into array

 $a = str_split("1234"); 

 $b = str_split("4321"); 

 

 echo maxValue($a, $b); 

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    4334
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

