G-Fact 19 (Logical and Bitwise Not Operators on Boolean)



Most of the languages including C, C++, Java and Python provide the boolean
type that can be either set to **False** or **True**.

Consider below programs that use **Logical Not (or !)** operator on boolean.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program that uses Logical Not or ! on boolean

a = not True

b = not False

print a

print b

# Output: False

# True  
  
---  
  
 __

 __

## C/C++

 __

 __  
 __

 __

 __  
 __  
 __

// A C/C++ program that uses Logical Not or ! on boolean

#include <stdio.h>

#include <stdbool.h>

 

int main()

{

 bool a = 1, b = 0;

 a = !a;

 b = !b;

 printf("%d\n%d", a, b);

 return 0;

}

// Output: 0

// 1  
  
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

// A Java program that uses Logical Not or ! on boolean

import java.io.*;

 

class GFG

{

 public static void main (String[] args)

 {

 boolean a = true, b = false;

 System.out.println(!a);

 System.out.println(!b);

 }

}

// Output: False

// True  
  
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

// C# program that uses Logical

// Not or ! on boolean 

using System;

 

class GFG

{

 public static void Main ()

 { 

 bool a = true, b = false; 

 Console.WriteLine(!a); 

 Console.WriteLine(!b); 

 } 

} 

// Output: False 

// True 

 

// This code is contributed 

// by Rajput-Ji  
  
---  
  
 __

 __

The outputs of above programs are as expected, but the outputs following
programs may not be as expected if we have not used **Bitwise Not (or ~)**
operator before.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program that uses Bitwise Not or ~ on boolean

a = True

b = False

print ~a

print ~b  
  
---  
  
 __

 __

## C/C++

 __

 __  
 __

 __

 __  
 __  
 __

// C/C++ program that uses Bitwise Not or ~ on boolean

#include <bits/stdc++.h>

using namespace std;

int main()

{

 bool a = true, b = false;

 cout << ~a << endl << ~b;

 return 0;

}  
  
---  
  
 __

 __

  
Output:

    
    
    -2
    -1

 **Reason:** The bitwise not operator ~ returns the complement of a number
i.e., it switches each 1 to 0 and each 0 to 1. Booleans True and False have
values 1 and 0 respectively.

  

  

˜being the bitwise not operator,

  * The expression “˜True” returns bitwise inverse of 1.
  * The expression “˜False” returns bitwise inverse of 0.

**Java** doesn’t allow ~ operator to be applied on boolean values. For
example, the below program produces compiler error.

 __

 __  
 __

 __

 __  
 __  
 __

// A Java program that uses Bitwise Not or ~ on boolean

import java.io.*;

 

class GFG

{

 public static void main (String[] args)

 {

 boolean a = true, b = false;

 System.out.println(~a);

 System.out.println(~b);

 }

}  
  
---  
  
 __

 __

Output:

    
    
    6: error: bad operand type boolean for unary operator '~'
            System.out.println(~a);
                               ^
    7: error: bad operand type boolean for unary operator '~'
            System.out.println(~b);
                               ^
    2 errors

 **Conclusion:**  
“Logical not or !” is meant for boolean values and “bitwise not or ~” is for
integers. Languages like C/C++ and python do auto promotion of boolean to
integer type when an integer operator is applied. But Java doesn’t do it.

This article is contributed by **Arpit Agarwal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article and mail your
article to contribute@geeksforgeeks.org. See your article appearing on the
GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

