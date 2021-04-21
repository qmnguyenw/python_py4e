Program to print window pattern



Print the pattern in which there is a hollow square and plus sign inside it.
The pattern will be as per the n i.e. number of rows given as shown in the
example.

**Examples:**

    
    
    **Input :** 6
    **Output :** * * * * * *
             *   * *   * 
             * * * * * * 
             * * * * * * 
             *   * *   * 
             * * * * * *
    
    **Input :** 7
    **Output :** * * * * * * * 
             *     *     * 
             *     *     * 
             * * * * * * * 
             *     *     * 
             *     *     * 
             * * * * * * *

 **Approach:**

  * We will start a for loop up till n and inside this also there is for loop up till n.
  * In this simply we have to check if the row is first or last or column is first or last, then print “*”.
  * Now we have to check for the middle row and column.
  * So when n is odd, we will have a middle row and column and if row or column is in middle then we will print “*”.
  * If n is even, then rows or columns if equal to these values n/2 and (n/2)+1, then we will print “*”.
  * Else everywhere we have to print ” “(space).

Below is the implementation.

## C++14

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to print the pattern

// hollow square with plus inside it

// window pattern

#include <bits/stdc++.h>

using namespace std;

 

// Function to print pattern n means 

// number of rows which we want

void window_pattern (int n)

{

 int c, d;

 

 // If n is odd then we will have

 // only one middle element

 if (n % 2 != 0)

 {

 c = (n / 2) + 1;

 d = 0;

 }

 

 // If n is even then we will have two

 // values

 else

 {

 c = (n / 2) + 1;

 d = n / 2 ;

 }

 

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= n; j++)

 {

 

 // If i,j equals to corner row or

 // column then "*"

 if (i == 1 || j == 1 ||

 i == n || j == n)

 cout << "* ";

 

 else

 {

 

 // If i,j equals to the middle 

 // row or column then "*"

 if (i == c || j == c)

 cout << "* ";

 

 else if (i == d || j == d)

 cout << "* ";

 

 else

 cout << " ";

 }

 }

 cout << '\n';

 }

}

 

// Driver Code

int main()

{

 int n = 7;

 

 window_pattern(n);

 return 0; 

}

 

// This code is contributed by himanshu77  
  
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

// Java program to print the pattern

// hollow square with plus inside it

// window pattern

class GFG

{

 // Function to print pattern n means 

 // number of rows which we want

 static void window_pattern (int n)

 {

 int c, d;

 // If n is odd then we will have

 // only one middle element

 if (n % 2 != 0)

 {

 c = (n / 2) + 1;

 d = 0;

 }

 // If n is even then we will have

 // two values

 else

 {

 c = (n / 2) + 1;

 d = n / 2 ;

 } 

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= n; j++)

 {

 // If i,j equals to corner row

 // or column then "*"

 if (i == 1 || j == 1 ||

 i == n || j == n)

 System.out.print("* "); 

 else

 {

 // If i,j equals to the middle 

 // row or column then "*"

 if (i == c || j == c)

 System.out.print("* ");

 else if (i == d || j == d)

 System.out.print("* ");

 else

 System.out.print(" ");

 }

 }

 System.out.println();

 }

 }

 // Driver code

 public static void main(String[] args)

 {

 int n = 7;

 window_pattern(n);

 }

}

// This code is contributed by divyeshrabadiya07  
  
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

# Python3 program to print the pattern

# hollow square with plus inside it

# window pattern

# function to print pattern n means

# number of rows which we want

def window_pattern(n):

 

 # if n is odd then we will have

 # only one middle element

 if n % 2 != 0:

 c = ( n // 2 ) + 1

 d = 0

 

 # if n is even then we will have two

 # values

 else:

 c = ( n // 2 ) + 1

 d = ( n // 2 )

 for i in range( 1 , n + 1 ):

 for j in range( 1 , n + 1 ):

 

 # if i,j equals to corner row or

 # column then "*"

 if i == 1 or j == 1 or i == n or j ==
n:

 print("*",end=" ")

 

 else:

 

 # if i,j equals to the middle row

 # or column then "*"

 if i == c or j == c:

 print("*",end=" ")

 

 elif i == d or j == d:

 print("*",end=" ")

 

 else:

 print(" ",end=" ")

 

 print()

# Driver Code

if __name__ == "__main__":

 n = 7

 window_pattern(n)  
  
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

// C# program to print the pattern

// hollow square with plus inside it

// window pattern

using System;

class GFG{

// Function to print pattern n means 

// number of rows which we want

static void window_pattern (int n)

{

 int c, d;

 

 // If n is odd then we will have

 // only one middle element

 if (n % 2 != 0)

 {

 c = (n / 2) + 1;

 d = 0;

 }

 

 // If n is even then we will have

 // two values

 else

 {

 c = (n / 2) + 1;

 d = n / 2 ;

 }

 

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= n; j++)

 {

 

 // If i,j equals to corner row

 // or column then "*"

 if (i == 1 || j == 1 ||

 i == n || j == n)

 Console.Write("* ");

 

 else

 {

 

 // If i,j equals to the middle 

 // row or column then "*"

 if (i == c || j == c)

 Console.Write("* ");

 

 else if (i == d || j == d)

 Console.Write("* ");

 

 else

 Console.Write(" ");

 }

 }

 Console.WriteLine();

 }

}

// Driver code

static void Main()

{

 int n = 7;

 

 window_pattern(n);

}

}

// This code is contributed by divyesh072019  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    * * * * * * * 
    *     *     * 
    *     *     * 
    * * * * * * * 
    *     *     * 
    *     *     * 
    * * * * * * *

 **Time complexity:** O(n2)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

