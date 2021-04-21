Program to print the diamond shape



Given a number n, write a program to print a diamond shape with 2n rows.  
 **Examples :**  

![diamond](https://media.geeksforgeeks.org/wp-content/cdn-uploads/diamond.png)

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to print diamond shape

// with 2n rows

#include <bits/stdc++.h>

using namespace std;

// Prints diamond pattern with 2n rows

void printDiamond(int n)

{

 int space = n - 1;

 // run loop (parent loop)

 // till number of rows

 for (int i = 0; i < n; i++)

 {

 // loop for initially space,

 // before star printing

 for (int j = 0;j < space; j++)

 cout << " ";

 // Print i+1 stars

 for (int j = 0; j <= i; j++)

 cout << "* ";

 cout << endl;

 space--;

 }

 // Repeat again in reverse order

 space = 0;

 // run loop (parent loop)

 // till number of rows

 for (int i = n; i > 0; i--)

 {

 // loop for initially space,

 // before star printing

 for (int j = 0; j < space; j++)

 cout << " ";

 // Print i stars

 for (int j = 0;j < i;j++)

 cout << "* ";

 cout << endl;

 space++;

 }

}

// Driver code

int main()

{

 printDiamond(5);

 return 0;

}

// This is code is contributed

// by rathbhupendra  
  
---  
  
 __

 __

## C

 __

 __  
 __

 __

 __  
 __  
 __

// C program to print

// diamond shape with

// 2n rows

#include<stdio.h>

// Prints diamond

// pattern with 2n rows

void printDiamond(int n)

{

 int space = n - 1;

 // run loop (parent loop)

 // till number of rows

 for (int i = 0; i < n; i++)

 {

 // loop for initially space,

 // before star printing

 for (int j = 0;j < space; j++)

 printf(" ");

 // Print i+1 stars

 for (int j = 0;j <= i; j++)

 printf("* ");

 printf("\n");

 space--;

 }

 // Repeat again in

 // reverse order

 space = 0;

 // run loop (parent loop)

 // till number of rows

 for (int i = n; i > 0; i--)

 {

 // loop for initially space,

 // before star printing

 for (int j = 0; j < space; j++)

 printf(" ");

 // Print i stars

 for (int j = 0;j < i;j++)

 printf("* ");

 printf("\n");

 space++;

 }

}

// Driver code

int main()

{

 printDiamond(5);

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

// JAVA Code to print

// the diamond shape

import java.util.*;

class GFG

{

 

 // Prints diamond pattern

 // with 2n rows

 static void printDiamond(int n)

 {

 int space = n - 1;

 

 // run loop (parent loop)

 // till number of rows

 for (int i = 0; i < n; i++)

 {

 // loop for initially space,

 // before star printing

 for (int j = 0; j < space; j++)

 System.out.print(" ");

 

 // Print i+1 stars

 for (int j = 0; j <= i; j++)

 System.out.print("* ");

 

 System.out.print("\n");

 space--;

 }

 

 // Repeat again in

 // reverse order

 space = 0;

 

 // run loop (parent loop)

 // till number of rows

 for (int i = n; i > 0; i--)

 {

 // loop for initially space,

 // before star printing

 for (int j = 0; j < space; j++)

 System.out.print(" ");

 

 // Print i stars

 for (int j = 0; j < i; j++)

 System.out.print("* ");

 

 System.out.print("\n");

 space++;

 }

 }

 

 // Driver Code

 public static void main(String[] args)

 {

 printDiamond(5);

 

 }

}

// This code is contributed

// by Arnav Kr. Mandal.  
  
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

# Python program to

# print Diamond shape

# Function to print

# Diamond shape

def Diamond(rows):

 n = 0

 for i in range(1, rows + 1):

 # loop to print spaces

 for j in range (1, (rows - i) + 1):

 print(end = " ")

 

 # loop to print star

 while n != (2 * i - 1):

 print("*", end = "")

 n = n + 1

 n = 0

 

 # line break

 print()

 k = 1

 n = 1

 for i in range(1, rows):

 # loop to print spaces

 for j in range (1, k + 1):

 print(end = " ")

 k = k + 1

 

 # loop to print star

 while n <= (2 * (rows - i) - 1):

 print("*", end = "")

 n = n + 1

 n = 1

 print()

# Driver Code

# number of rows input

rows = 5

Diamond(rows)  
  
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

// C# Code to print

// the diamond shape

using System;

class GFG

{

 

 // Prints diamond pattern

 // with 2n rows

 static void printDiamond(int n)

 {

 int space = n - 1;

 

 // run loop (parent loop)

 // till number of rows

 for (int i = 0; i < n; i++)

 {

 // loop for initially space,

 // before star printing

 for (int j = 0; j < space; j++)

 Console.Write(" ");

 

 // Print i+1 stars

 for (int j = 0; j <= i; j++)

 Console.Write("* ");

 

 Console.Write("\n");

 space--;

 }

 

 // Repeat again in

 // reverse order

 space = 0;

 

 // run loop (parent loop)

 // till number of rows

 for (int i = n; i > 0; i--)

 {

 // loop for initially space,

 // before star printing

 for (int j = 0; j < space; j++)

 Console.Write(" ");

 

 // Print i stars

 for (int j = 0; j < i; j++)

 Console.Write("* ");

 

 Console.Write("\n");

 space++;

 }

 }

 

 // Driver Code

 public static void Main()

 {

 printDiamond(5);

 

 }

}

// This code is contributed

// by Smitha Semwal.  
  
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

// diamond shape with

// 2n rows

// Prints diamond $

// pattern with 2n rows

function printDiamond($n)

{

 $space = $n - 1;

 // run loop (parent loop)

 // till number of rows

 for ($i = 0; $i < $n; $i++)

 {

 

 // loop for initially space,

 // before star printing

 for ($j = 0;$j < $space; $j++)

 printf(" ");

 // Print i+1 stars

 for ($j = 0;$j <= $i; $j++)

 printf("* ");

 printf("\n");

 $space--;

 }

 // Repeat again in

 // reverse order

 $space = 0;

 // run loop (parent loop)

 // till number of rows

 for ($i = $n; $i > 0; $i--)

 {

 

 // loop for initially space,

 // before star printing

 for ($j = 0; $j < $space; $j++)

 printf(" ");

 // Pr$i stars

 for ($j = 0;$j < $i;$j++)

 printf("* ");

 printf("\n");

 $space++;

 }

}

 // Driver code

 printDiamond(5);

// This code is contributed by Anuj_67

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

 // JavaScript program to print diamond shape

 // with 2n rows

 // Prints diamond pattern with 2n rows

 function printDiamond(n) {

 var space = n - 1;

 // run loop (parent loop)

 // till number of rows

 for (var i = 0; i < n; i++) {

 // loop for initially space,

 // before star printing

 for (var j = 0; j < space; j++) document.write(" ");

 // Print i+1 stars

 for (var j = 0; j <= i; j++) document.write("*" + " ");

 document.write("<br>");

 space--;

 }

 // Repeat again in reverse order

 space = 0;

 // run loop (parent loop)

 // till number of rows

 for (var i = n; i > 0; i--)

 {

 

 // loop for initially space,

 // before star printing

 for (var j = 0; j < space; j++) document.write(" ");

 // Print i stars

 for (var j = 0; j < i; j++) document.write("*" + " ");

 document.write("<br>");

 space++;

 }

 }

 // Driver code

 printDiamond(5);

 

 // This code is contributed by rdtank.

 </script>  
  
---  
  
 __

 __

 **Output :**  

    
    
            *
           * *
          * * *
         * * * *
        * * * * *
        * * * * *
         * * * *
          * * *
           * *
            *

This article is contributed by **Rahul Singh(Nit KKR)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

Want to learn from the best curated videos and practice problems, check out
the **C Foundation Course **for Basic to Advanced C.

  
  

  

My Personal Notes _arrow_drop_up_

Save

