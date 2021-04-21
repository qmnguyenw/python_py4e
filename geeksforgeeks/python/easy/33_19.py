Swap two variables in one line



We have discussed different approaches to swap two integers without the
temporary variable. How to swap in a single line without using library
function?  
 **Python:** In Python, there is a simple and syntactically neat construct to
swap variables, we just need to write “x, y = y, x”.  
 **C/C++:** Below is one generally provided classical solution

    
    
    // Swap using bitwise XOR (Wrong Solution in C/C++)
    x ^= y ^= x ^= y; 

The above solution is wrong in C/C++ as it causes undefined behaviour
(compiler is free to behave in any way). The reason is, modifying a variable
more than once in an expression causes undefined behaviour if there is no
sequence point between the modifications.  
However, we can use a comma to introduce sequence points. So the modified
solution is

    
    
    // Swap using bitwise XOR (Correct Solution in C/C++)
    // sequence point introduced using comma.
    (x ^= y), (y ^= x), (x ^= y);

 **Java:** In Java, rules for subexpression evaluations are clearly defined.
The left hand operand is always evaluated before right hand operand (See this
for more details). In Java, the expression “x ^= y ^= x ^= y;” doesn’t produce
the correct result according to Java rules. It makes x = 0. However, we can
use “x = x ^ y ^ (y = x);” Note the expressions are evaluated from left to
right. If x = 5 and y = 10 initially, the expression is equivalent to “x = 5 ^
10 ^ (y = 5);”. Note that we can’t use this in C/C++ as in C/C++, it is not
defined whether left operand or right operand is executed for any operator
(See this for more details)  

## C

 __

 __  
 __

 __

 __  
 __  
 __

// C program to swap two variables in single line

#include <stdio.h>

int main()

{

 int x = 5, y = 10;

 (x ^= y), (y ^= x), (x ^= y);

 printf("After Swapping values of x and y are %d %d", x,

 y);

 return 0;

}  
  
---  
  
 __

 __

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code to swap using XOR

#include <bits/stdc++.h>

using namespace std;

int main()

{

 int x = 5, y = 10;

 // Code to swap 'x' and 'y'

 // to swap two numbers in one

 // line

 x = x ^ y, y = x ^ y, x = x ^ y;

 // printing the swapped variables

 cout << "After Swapping: x = "

 << x << ", y= " << y;

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

// Java program to swap two variables in a single line

class GFG {

 public static void main(String[] args)

 {

 int x = 5, y = 10;

 x = x ^ y ^ (y = x);

 System.out.println(

 "After Swapping values"

 +" of x and y are " + x

 + " " + y);

 }

}  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to swap two variables in a single line

x = 5

y = 10

x, y = y, x

print("After Swapping values of x and y are", x, y)  
  
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

// C# program to swap two

// variables in single line

using System;

class GFG {

 static public void Main()

 {

 int x = 5, y = 10;

 x = x ^ y ^ (y = x);

 Console.WriteLine("After Swapping values "

 + "of x and y are " + x + " "

 + y);

 }

}

// This code is contributed by aj_36  
  
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

// PHP program to swap two

// variables in single line

 // Driver Code

 $x = 5;

 $y = 10;

 ($x ^= $y);

 ($y ^= $x);

 ($x ^= $y);

 echo "After Swapping values of x and y are "

 ,$x," ", $y;

// This code is contributed by Vishal Tripathi

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

// javascript program to swap two variables in single line

 let x = 5, y = 10;

 (x ^= y), (y ^= x), (x ^= y);

 document.write("After Swapping values of x and y are ", x + " ",

 y);

 

// This code is contributed by Surbhi Tyagi

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    After Swapping values of x and y are 10 5

 **Alternate Solutions :**

  * C++ also provides a library function swap()
  * b = (a + b) – (a = b); [Thanks to Rajat Mishra for this]
  * a += b – (b = a); [Thanks to Zoran Davidovi? for this]
  * a = a * b / (b = a)[Thanks to kongasricharan for this]
  * a = a ^ b ^ (b = a)

This article is contributed by **Harshit Gupta.** If you like GeeksforGeeks
and would like to contribute, you can also write an article and mail your
article to contribute@geeksforgeeks.org. See your article appearing on the
GeeksforGeeks main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Want to learn from the best curated videos and practice problems, check out
the **C++ Foundation Course **for Basic to Advanced C++ and **C++ STL Course**
for foundation plus STL. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

