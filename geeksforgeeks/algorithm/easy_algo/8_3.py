Number of ways an array can be filled with 0s and 1s such that no consecutive
elements are 1



Given a number N, find the number of ways to construct an array of size N such
that it contains only 1s and 0s but no two consecutive indexes have value 1 in
them.

Examples:

    
    
    Input  : 2
    Output : 3
    **Explanation:**
    For n=2, the possible arrays are:
    {0, 1} {1, 0} {0, 0}
    
    Input  : 3
    Output : 5
    **Explanation:**
    For n=3, the possible arrays are:
    {0, 0, 0} {1, 0, 0} {0, 1, 0} {0, 0, 1} {1, 0, 1} 

**Naive Approach:**  
The basic brute force approach would be to construct all the possible ways
that the array can be filled with 1s and 0s, and then checking if there are
any two consecutive 1s in the array if there are, do not count those arrays.

Since each element has 2 possible values, 1 and 0, and there are n total
elements, the total number of arrays without any restriction will be of
exponential order i.e 2n.

 **Efficient Approach:**  
If we observe a bit closely, we can notice that there is a pattern forming in
the input and output.

  

  

For **n = 1** , number of ways is **2** i.e. {0}, {1}  
for **n = 2** , number of ways is **3**  
Similarly,

for **n = 3** number of ways is **5**  
for **n = 4** number of ways is **8**

and so on…  
Let T() be the function which gives the number of ways the array of size n can
be filled, then we get the following recurrence relation

> T(n) = T(n-1) + T(n-2)

And this is the recurrence relation of **Fibonacci series<**.  
Hence, the output for any n is equal to the **(n+2) th term** of the Fibonacci
series starting from 1.  
i.e. 1 1 2 3 5 8 11…

So now we just need to compute the Fibonacci sequence up to the (n+2)th
elements and that will be the answer.  
 **Time complexity is O(n)**  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the

// above approach

#include <iostream>

using namespace std;

 

 // The total number of ways 

 // is equal to the (n+2)th 

 // Fibonacci term, hence we 

 // only need to find that.

 int nth_term(int n)

 {

 int a = 1, b = 1, c = 1;

 

 // Construct fibonacci upto 

 // (n+2)th term the first

 // two terms being 1 and 1

 for (int i = 0; i < n; i++) 

 {

 c = a + b;

 a = b;

 b = c;

 }

 

 return c;

 }

 

 // Driver Code

 int main()

 {

 

 // Take input n

 int n = 10;

 int c = nth_term(n);

 

 // printing output

 cout << c;

 }

 

// This code is contributed by Sumit Sudhakar.  
  
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

// Java implementation of the

// above approach

class Main 

{

 

 // The total number of ways 

 // is equal to the (n+2)th 

 // Fibonacci term, hence we 

 // only need to find that.

 public static int nth_term(int n)

 {

 int a = 1, b = 1, c = 1;

 

 // Construct fibonacci upto 

 // (n+2)th term the first

 // two terms being 1 and 1

 for (int i = 0; i < n; i++) 

 {

 c = a + b;

 a = b;

 b = c;

 }

 

 return c;

 }

 

 // Driver program

 public static void main(String[] args)

 {

 // Take input n

 int n = 10;

 int c = nth_term(n);

 

 // printing output

 System.out.println(c);

 }

}  
  
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

# Python3 implementation of

# the above approach

 

# The total number of ways 

# is equal to the (n+2)th 

# Fibonacci term, hence we 

# only need to find that.

def nth_term(n) :

 

 a = 1

 b = 1

 c = 1

 

 # Construct fibonacci upto 

 # (n+2)th term the first

 # two terms being 1 and 1

 for i in range(0, n) :

 c = a + b

 a = b

 b = c

 return c

 

# Driver Code

 

# Take input n

n = 10

c = nth_term(n)

 

# printing output

print (c)

# This code is contributed by 

# Manish Shaw (manishshaw1)  
  
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

// C# implementation of the

// above approach

using System;

 

class GFG {

 

 // The total number of ways 

 // is equal to the (n+2)th 

 // Fibonacci term, hence we 

 // only need to find that.

 static int nth_term(int n)

 {

 int a = 1, b = 1, c = 1;

 

 // Construct fibonacci upto 

 // (n+2)th term the first

 // two terms being 1 and 1

 for (int i = 0; i < n; i++) 

 {

 c = a + b;

 a = b;

 b = c;

 }

 

 return c;

 }

 

 // Driver Code

 public static void Main()

 {

 

 // Take input n

 int n = 10;

 int c = nth_term(n);

 

 // printing output

 Console.WriteLine(c);

 

 }

}

 

// This code is contributed by Sam007

 

 

   
  
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

// PHP implementation of the 

// above approach

 

 // The total number of ways 

 // is equal to the (n+2)th 

 // Fibonacci term, hence we 

 // only need to find that.

 function nth_term($n)

 {

 $a = 1; $b = 1; $c = 1;

 

 // Construct fibonacci upto 

 // (n+2)th term the first

 // two terms being 1 and 1

 for ($i = 0; $i < $n; $i++) 

 {

 $c = $a + $b;

 $a = $b;

 $b = $c;

 }

 

 return $c;

 }

 

 // Driver Code

 

 // Take input n

 $n = 10;

 $c = nth_term($n);

 

 // printing output

 echo $c;

 

// This code is contributed by nitin mittal

?>  
  
---  
  
 __

 __

  
 **Output:**

    
    
    144
    

We can further optimize above solution to work in O(Log n) using matrix
exponentiation solution for finding n-th Fibonacci number (Please see methods
4, 5 and 6 of Program for Fibonacci numbers ).

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

