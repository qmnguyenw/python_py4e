Find minimum x such that (x % k) * (x / k) == n



Given two positive integers n and k. Find minimum positive integer x such that
the (x % k) * (x / k) == n, where % is the modulus operator and / is the
integer division operator.  
 **Examples:**  

    
    
    **Input :** n = 4, k = 6
    **Output :** 10
    **Explanation :** (10 % 6) * (10 / 6) = (4) * (1) = 4 which is equal to n
    
    **Input :** n = 5, k = 5
    **Output :** 26

 **Naive Solution :** A simple approach is to run a while loop until we find a
solution which satisfies the given equation, but this would be very slow.  
**Efficient Solution :** The key idea here is to notice that the value of (x %
k) lies in the range [1, k – 1]. (0 is not included, since we can’t divide n
by (x % k) when it is zero). Now, we need to find the largest possible number
in the range that divides n and hence the given equation becomes x = (n * k) /
(x % k) + (x % k).  
**Note :** (x % k) is added to the answer since for the current value of
modulus (x % k), it must not be contradicting that on one hand x is such that
the remainder upon dividing by k is (x % k) and on the other x is (n * k) / (x
% k) whose remainder is simply zero when we divide this value by k.  
Below is the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP Program to find the minimum

// positive X such that the given

// equation holds true

#include <bits/stdc++.h>

using namespace std;

// This function gives the required

// answer

int minimumX(int n, int k)

{

 int ans = INT_MAX;

 // Iterate over all possible

 // remainders

 for (int rem = k - 1; rem > 0; rem--) {

 // it must divide n

 if (n % rem == 0)

 ans = min(ans, rem + (n / rem) * k);

 }

 return ans;

}

// Driver Code to test above function

int main()

{

 int n = 4, k = 6;

 cout << minimumX(n, k) << endl;

 n = 5, k = 5;

 cout << minimumX(n, k) << endl;

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

// Java Program to find the minimum

// positive X such that the given

// equation holds true

class Solution

{

// This function gives the required

// answer

static int minimumX(int n, int k)

{

 int ans =Integer.MAX_VALUE;

 

 // Iterate over all possible

 // remainders

 for (int rem = k - 1; rem > 0; rem--) {

 

 // it must divide n

 if (n % rem == 0)

 ans = Math.min(ans, rem + (n / rem) * k);

 }

 return ans;

}

 

// Driver Code to test above function

public static void main(String args[])

{

 int n = 4, k = 6;

 System.out.println( minimumX(n, k));

 

 n = 5; k = 5;

 System.out.println(minimumX(n, k));

 

}

}

//contributed by Arnab Kundu  
  
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

# Python 3 program to find the minimum positive

# x such that the given equation holds true

# This function gives the required answer

def minimumX(n, k):

 

 

 ans = 10 ** 18

 

 # Iterate over all possible remainders

 for i in range(k - 1, 0, -1):

 if n % i == 0:

 ans = min(ans, i + (n / i) * k)

 return ans

# Driver Code

n, k = 4, 6

print(minimumX(n, k))

n, k = 5, 5

print(minimumX(n, k))

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

// C# Program to find the minimum

// positive X such that the given

// equation holds true

using System;

public class GFG{

 // This function gives the required

// answer

static int minimumX(int n, int k)

{

 int ans =int.MaxValue;

 // Iterate over all possible

 // remainders

 for (int rem = k - 1; rem > 0; rem--) {

 // it must divide n

 if (n % rem == 0)

 ans = Math.Min(ans, rem + (n / rem) * k);

 }

 return ans;

}

// Driver Code to test above function

 static public void Main (){

 int n = 4, k = 6;

 Console.WriteLine( minimumX(n, k));

 n = 5; k = 5;

 Console.WriteLine(minimumX(n, k));

 

}

}

//This code is contributed by Sachin.  
  
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

// PHP Program to find the minimum

// positive X such that the given

// equation holds true

// This function gives the required

// answer

function minimumX($n, $k)

{

 $ans = PHP_INT_MAX;

 // Iterate over all possible

 // remainders

 for ($rem = $k - 1; $rem > 0; $rem--)

 {

 // it must divide n

 if ($n % $rem == 0)

 $ans = min($ans, $rem +

 ($n / $rem) * $k);

 }

 return $ans;

}

// Driver Code

$n = 4 ;

$k = 6 ;

echo minimumX($n, $k), "\n" ;

$n = 5 ;

$k = 5 ;

echo minimumX($n, $k) ;

// This code is contributed by Ryuga

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

 // Javascript Program to find the minimum

 // positive X such that the given

 // equation holds true

 

 // This function gives the required

 // answer

 function minimumX(n, k)

 {

 let ans = Number.MAX_VALUE;

 

 // Iterate over all possible

 // remainders

 for (let rem = k - 1; rem > 0; rem--) {

 

 // it must divide n

 if (n % rem == 0)

 ans = Math.min(ans, rem + (n / rem) * k);

 }

 return ans;

 }

 

// Driver code to test above function 

 let n = 4, k = 6;

 document.write(minimumX(n, k) + "</br>");

 

 n = 5, k = 5;

 document.write(minimumX(n, k));

 

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    10
    26

**Time Complexity :** O(k), where k is the given positive integer.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

