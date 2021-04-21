Multiples of 3 and 5 without using % operator



Write a short program that prints each number from 1 to n on a new line.  

  1. For each multiple of 3, print “Multiple of 3” instead of the number.
  2. For each multiple of 5, print “Multiple of 5” instead of the number.
  3. For numbers which are multiples of both 3 and 5, print “Multiple of 3. Multiple of 5.” instead of the number.

 **Examples:**  

    
    
    Input  : 15 
    Output : 1
             2
             Multiple of 3.
             4
             Multiple of 5.
             Multiple of 3.
             7
             8
             Multiple of 3.
             Multiple of 5.
             11
             Multiple of 3.
             13
             14
             Multiple of 3. Multiple of 5.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

The idea is iterate from 1 to n and keep track of multiples of 3 and 5 by
adding 3 and 5 to current multiple. If current number matches with a multiple,
we update our output accordingly.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to print multiples

// of 3 and 5 without using % operator.

#include <iostream>

using namespace std;

void findMultiples(int n)

{

 int a = 3; // To keep track of multiples of 3

 int b = 5; // To keep track of multiples of 5

 for (int i = 1; i <= n; i++)

 {

 string s = "";

 // Found multiple of 3

 if (i == a)

 {

 a = a + 3; // Update next multiple of 3

 s = s + "Multiple of 3. ";

 }

 // Found multiple of 5

 if (i == b)

 {

 b = b + 5; // Update next multiple of 5

 s = s + "Multiple of 5.";

 }

 if (s == "")

 cout << (i) << endl;

 else

 cout << (s) << endl;

 }

}

// Driver Code

int main()

{

 findMultiples(20);

 return 0;

}

// This code is contributed

// by Sach_Code  
  
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

// Java program to print multiples of 3 and

// 5 without using % operator.

import java.io.*;

class GFG

{

 static void findMultiples(int n)

 {

 int a = 3; // To keep track of multiples of 3

 int b = 5; // To keep track of multiples of 5

 for (int i=1; i<=n; i++)

 {

 String s = "";

 // Found multiple of 3

 if (i==a)

 {

 a = a + 3; // Update next multiple of 3

 s = s + "Multiple of 3. ";

 }

 // Found multiple of 5

 if (i==b)

 {

 b = b+5; // Update next multiple of 5

 s = s + "Multiple of 5.";

 }

 if (s == "")

 System.out.println(i);

 else System.out.println(s);

 }

 }

 public static void main (String[] args)

 {

 findMultiples(20);

 }

}  
  
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

// C# program to print multiples of 3 and

// 5 without using % operator.

using System;

public class GFG {

 

 static void findMultiples(int n)

 {

 

 // To keep track of multiples of 3

 int a = 3;

 

 // To keep track of multiples of 5

 int b = 5;

 for (int i = 1; i <= n; i++)

 {

 String s = "";

 // Found multiple of 3

 if (i == a)

 {

 

 // Update next multiple of 3

 a = a + 3;

 s = s + "Multiple of 3. ";

 }

 // Found multiple of 5

 if (i == b)

 {

 

 // Update next multiple of 5

 b = b + 5;

 s = s + "Multiple of 5.";

 }

 if (s == "")

 Console.WriteLine(i);

 else

 Console.WriteLine(s);

 }

 }

 // Driver code

 public static void Main ()

 {

 findMultiples(20);

 }

}

// This code is contributed by Sam007.  
  
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

// PHP program to print multiples

// of 3 and 5 without using % operator.

function findMultiples($n)

{

 $a = 3; // To keep track of multiples of 3

 $b = 5; // To keep track of multiples of 5

 for ($i = 1; $i <= $n; $i++)

 {

 $s = "";

 // Found multiple of 3

 if ($i == $a)

 {

 $a = $a + 3; // Update next multiple of 3

 $s = $s . "Multiple of 3. ";

 }

 // Found multiple of 5

 if ($i == $b)

 {

 $b = $b + 5; // Update next multiple of 5

 $s = $s . "Multiple of 5.";

 }

 if ($s == "")

 echo ($i). "\n";

 else

 echo ($s). "\n";

 }

}

// Driver Code

findMultiples(20);

// This code is contributed

// by Akanksha Rai(Abby_akku)  
  
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

 function findMultiples(n)

 {

 let a = 3; // To keep track of multiples of 3

 let b = 5; // To keep track of multiples of 5

 for (let i=1; i<=n; i++)

 {

 let s = "";

 // Found multiple of 3

 if (i==a)

 {

 a = a + 3; // Update next multiple of 3

 s = s + "Multiple of 3. ";

 }

 // Found multiple of 5

 if (i==b)

 {

 b = b+5; // Update next multiple of 5

 s = s + "Multiple of 5.";

 }

 if (s == "") {

 document.write(i);

 document.write("<br />");

 }

 else {

 document.write(s);

 document.write("<br />");

 }

 }

 }

// Driver Code

 findMultiples(20);

 

 // This code is contributed by susmitakundugoaldanga.

</script>  
  
---  
  
 __

 __

 **Output:**  

    
    
    1
    2
    Multiple of 3. 
    4
    Multiple of 5.
    Multiple of 3. 
    7
    8
    Multiple of 3. 
    Multiple of 5.
    11
    Multiple of 3. 
    13
    14
    Multiple of 3. Multiple of 5.
    16
    17
    Multiple of 3. 
    19
    Multiple of 5.

This article is contributed by **Nimish Jain**. If you like GeeksforGeeks and
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

