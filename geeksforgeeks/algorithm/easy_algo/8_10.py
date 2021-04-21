Print numbers 1 to N using Indirect recursion



Given a number N, we need to print numbers from 1 to N with out direct
recursion, loops, labels. Basically we need to insert in above code snippet so
that it can be able to print numbers from 1 to N?

 __

 __  
 __

 __

 __  
 __  
 __

#include<stdio.h>

#define N 20;

int main()

{ 

 // Your code goes Here.

}  
  
---  
  
 __

 __

 **  
Examples :**

    
    
    Input  : 10
    Output : 1 2 3 4 5 6 7 8 9 10
    
    Input  : 5
    Output : 1 2 3 4 5
    

We have already discussed solutions in below posts :  
Print 1 to 100 in C++, without loop and recursion  
How will you print numbers from 1 to 100 without using loop?

## Recommended: Please solve it on “ ** _ _PRACTICE__** ” first, before moving
on to the solution.  

Here’s the code that can print the numbers from 1 to 100 with out direct
recursion, loops and labels. The code uses indirect recursion.

## C

 __

 __  
 __

 __

 __  
 __  
 __

// C program to print from 1 to N using

// indirect recursion/

#include<stdio.h>

 

// We can avoid use of these using references

#define N 20;

int n = 1;

 

// Prints n, increments n and calls fun1()

void fun1()

{

 if (n <= N)

 {

 printf("%d", n);

 n++;

 fun2();

 }

 else

 return;

}

 

// Prints n, increments n and calls fun2()

void fun2()

{

 if (n <= N)

 {

 printf("%d", n);

 n++;

 fun1();

 }

 else

 return;

}

 

// Driver Program

int main(void)

{

 fun1();

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

// Java program to print from 1 to N using

// indirect recursion

class GFG 

{

 // We can avoid use of these using references

 static final int N = 20;

 static int n = 1;

 

 // Prints n, increments n and calls fun1()

 static void fun1() 

 {

 if (n <= N) 

 {

 System.out.printf("%d ", n);

 n++;

 fun2();

 }

 else

 {

 return;

 }

 }

 

 // Prints n, increments n and calls fun2()

 static void fun2() 

 {

 if (n <= N)

 {

 System.out.printf("%d ", n);

 n++;

 fun1();

 } 

 else

 {

 return;

 }

 }

 

 // Driver Program

 public static void main(String[] args) 

 {

 fun1();

 }

}

 

// This code is contributed by Rajput-Ji  
  
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

# Python program to prfrom 1 to N using

# indirect recursion

 

# We can avoid use of these using references

N = 20;

n = 1;

 

# Prints n, increments n and calls fun1()

def fun1():

 global N, n;

 if (n <= N):

 print(n, end = " ");

 n += 1;

 fun2();

 else:

 return;

 

# Prints n, increments n and calls fun2()

def fun2():

 global N, n;

 if (n <= N):

 print(n, end = " ");

 n += 1;

 fun1();

 else:

 return;

 

# Driver Program

if __name__ == '__main__':

 

 fun1();

 

# This code is contributed by 29AjayKumar  
  
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

// C# program to print from 1 to N using

// indirect recursion

using System;

 

class GFG 

{

 // We can avoid use of these using references

 static readonly int N = 20;

 static int n = 1;

 

 // Prints n, increments n and calls fun1()

 static void fun1() 

 {

 if (n <= N) 

 {

 Console.Write("{0} ", n);

 n++;

 fun2();

 }

 else

 {

 return;

 }

 }

 

 // Prints n, increments n and calls fun2()

 static void fun2() 

 {

 if (n <= N)

 {

 Console.Write("{0} ", n);

 n++;

 fun1();

 } 

 else

 {

 return;

 }

 }

 

 // Driver Code

 public static void Main(String[] args) 

 {

 fun1();

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

// PHP program to print 

// from 1 to N using 

// indirect recursion

 

// We can avoid use of

// these using references

$N = 20;

$n = 1;

 

// Prints n, increments 

// n and calls fun1()

function fun1()

{

 global $N;

 global $n;

 

 if ($n <= $N)

 {

 echo $n, " ";

 $n++;

 fun2();

 }

 else

 return;

}

 

// Prints n, increments

// n and calls fun2()

function fun2()

{

 global $N;

 global $n;

 if ($n <= $N)

 {

 echo $n, " ";

 $n++;

 fun1();

 }

 else

 return;

}

 

// Driver Code

fun1();

 

// This code is contributed 

// by m_kit

?>  
  
---  
  
 __

 __

  
 **Output :**

  

  

    
    
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
    

**How This works?:**  
In above Above program, we just used two functions. One calls others and other
one calls previous one, therefore indirect recursion.

 **Exercise :**  
Modify the above program to use N as a parameter instead of making it global.

This article is contributed by **Umamaheswararao Tumma** of **Jntuh college of
Engineering Hyderabad**. If you like GeeksforGeeks and would like to
contribute, you can also write an article using contribute.geeksforgeeks.org
or mail your article to contribute@geeksforgeeks.org. See your article
appearing on the GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

