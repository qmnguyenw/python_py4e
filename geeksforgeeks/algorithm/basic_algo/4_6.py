Make n using 1s and 2s with minimum number of terms multiple of k



Given two positive integer **n** and **k**. n can be represented as the sum of
1s and 2s in many ways, using multiple numbers of terms. The task is to find
the minimum number of terms of 1s and 2s use to make the sum n and also number
of terms must be multiple of k. Print “-1”, if no such number of terms exists.  
**Examples :**  

    
    
    Input : n = 10, k = 2
    Output : 6
    10 can be represented as 2 + 2 + 2 + 2 + 1 + 1.
    Number of terms used are 6 which is multiple of 2.
    
    Input : n = 11, k = 4
    Output : 8
    10 can be represented as 2 + 2 + 2 + 1 + 1 + 1 + 1 + 1
    Number of terms used are 8 which is multiple of 4.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

Observe, the maximum number of terms used to represent n as the sum of 1s and
2s is n, when 1 are added n number of times. Also, the minimum number of terms
will be n/2 times of 2s and n%2 times 1s are added. So, iterate from minimum
number of terms to maximum number of terms and check if there is any multiple
of k.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find minimum multiple of k

// terms used to make sum n using 1s and 2s.

#include<bits/stdc++.h>

using namespace std;

// Return minimum multiple of k terms used to

// make sum n using 1s and 2s.

int minMultipleK(int n, int k)

{

 // Minimum number of terms required to make

 // sum n using 1s and 2s.

 int min = (n / 2) + (n % 2);

 // Iterate from Minimum to maximum to find

 // multiple of k. Maximum number of terns is

 // n (Sum of all 1s)

 for (int i = min; i <= n; i++)

 if (i % k == 0)

 return i;

 return -1;

}

// Driven Program

int main()

{

 int n = 10, k = 2;

 cout << minMultipleK(n, k) << endl;

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

// Java program to find minimum

// multiple of k terms used to

// make sum n using 1s and 2s.

import java.io.*;

class GFG

{

 

// Return minimum multiple of

// k terms used to make sum n

// using 1s and 2s.

static int minMultipleK(int n,

 int k)

{

 // Minimum number of terms

 // required to make sum n

 // using 1s and 2s.

 int min = (n / 2) + (n % 2);

 // Iterate from Minimum to

 // maximum to findmultiple of k.

 // Maximum number of terms is

 // n (Sum of all 1s)

 for (int i = min; i <= n; i++)

 if (i % k == 0)

 return i;

 return -1;

}

// Driver Code

public static void main (String[] args)

{

 int n = 10, k = 2;

 System.out.println( minMultipleK(n, k));

}

}

// This code is contributed by anuj_67.  
  
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

# Python3 program to find minimum multiple of k

# terms used to make sum n using 1s and 2s.

# Return minimum multiple of k terms

# used to make sum n using 1s and 2s.

def minMultipleK( n, k):

 # Minimum number of terms required

 # to make sum n using 1s and 2s.

 min = (n // 2) + (n % 2)

 # Iterate from Minimum to maximum to find

 #multiple of k. Maximum number of terns is

 # n (Sum of all 1s)

 for i in range(min, n + 1):

 if (i % k == 0):

 return i

 return -1

# Driver Code

if __name__=="__main__":

 n = 10

 k = 2

 print (minMultipleK(n, k))

 

# This code is contributed

# by ChitraNayal  
  
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

// C# program to find minimum

// multiple of k terms used to

// make sum n using 1s and 2s.

using System;

class GFG

{

 

// Return minimum multiple of

// k terms used to make sum n

// using 1s and 2s.

static int minMultipleK(int n,

 int k)

{

 // Minimum number of terms

 // required to make sum n

 // using 1s and 2s.

 int min = (n / 2) + (n % 2);

 // Iterate from Minimum to

 // maximum to findmultiple of k.

 // Maximum number of terms is

 // n (Sum of all 1s)

 for (int i = min; i <= n; i++)

 if (i % k == 0)

 return i;

 return -1;

}

// Driver Code

public static void Main ()

{

 int n = 10, k = 2;

 Console.WriteLine( minMultipleK(n, k));

}

}

// This code is contributed by anuj_67.  
  
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

// PHP program to find minimum multiple of

// k terms used to make sum n using 1s and 2s.

// Return minimum multiple of k terms used

// to make sum n using 1s and 2s.

function minMultipleK($n, $k)

 

{

 // Minimum number of terms required

 // to make sum n using 1s and 2s.

 $min = ($n / 2) + ($n % 2);

 // Iterate from Minimum to maximum to

 // findmultiple of k. Maximum number

 // of terms is n (Sum of all 1s)

 for ($i = $min; $i <= $n; $i++)

 if ($i % $k == 0)

 return $i;

 return -1;

}

// Driver Code

$n = 10; $k = 2;

echo(minMultipleK($n, $k));

// This code is contributed

// by Mukul singh.  
  
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

// JavaScript program for the above approach

 

// Return minimum multiple of

// k terms used to make sum n

// using 1s and 2s.

function minMultipleK(n, k)

{

 // Minimum number of terms 

 // required to make sum n 

 // using 1s and 2s.

 let min = (n / 2) + (n % 2);

 

 // Iterate from Minimum to 

 // maximum to findmultiple of k. 

 // Maximum number of terms is

 // n (Sum of all 1s)

 for (let i = min; i <= n; i++)

 if (i % k == 0)

 return i;

 

 return -1;

}

// Driver Code

 

 let n = 10, k = 2;

 document.write( minMultipleK(n, k));

 

 // This code is contributed by splevel62.

</script>  
  
---  
  
 __

 __

 **Output :**  

    
    
    6

This article is contributed by **Anuj Chauhan**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

