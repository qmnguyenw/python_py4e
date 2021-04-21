Product of 2 numbers using recursion | Set 2



Given two numbers N and M. The task is to find the product of the 2 numbers
using recursion.

 **Note** : The numbers can be both positive or negative.

 **Examples** :

    
    
    Input : N = 5 ,  M = 3
    Output : 15
    
    Input : N = 5  ,  M = -3
    Output : -15
    
    Input : N = -5  ,  M = 3
    Output : -15
    
    Input : N = -5  ,  M = -3
    Output:15
    

A recursive solution to the above problem for only positive numbers is already
discussed in the previous article. In this post, a recursive solution for
finding the product for both positive and negative numbers is discussed.

Below is the step by step approach:

  

  

  1. Check if one or both of the numbers are negative.
  2. If the number passed in the second parameter is negative swap the parameters and call the function again.
  3. If both of the parameters are negative call the function again and pass the absolute values of the numbers as parameters.
  4. If n>m call the function with swapped parameters for less execution time of the function.
  5. As long as m is not 0 keep on calling the function with subcase n, m-1 and return n + multrecur(n, m-1).

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program to find product of two numbers

// using recursion

#include <iostream>

using namespace std;

 

// Recursive function to calculate the product 

// of 2 integers

int multrecur(int n, int m)

{

 // case 1 : n<0 and m>0

 // swap the position of n and m to keep second

 // parameter positive

 if (n > 0 && m < 0) {

 return multrecur(m, n);

 }

 // case 2 : both n and m are less than 0

 // return the product of their absolute values

 else if (n < 0 && m < 0) {

 return multrecur((-1 * n), (-1 * m));

 }

 

 // if n>m , swap n and m so that recursion

 // takes less time

 if (n > m) {

 return multrecur(m, n);

 }

 

 // as long as m is not 0 recursively call multrecur for 

 // n and m-1 return sum of n and the product of n times m-1

 else if (m != 0) {

 return n + multrecur(n, m - 1);

 }

 

 // m=0 then return 0

 else {

 return 0;

 }

}

// Driver code

int main()

{

 cout << "5 * 3 = " << multrecur(5, 3) << endl;

 cout << "5 * (-3) = " << multrecur(5, -3) << endl;

 cout << "(-5) * 3 = " << multrecur(-5, 3) << endl;

 cout << "(-5) * (-3) = " << multrecur(-5, -3) << endl;

 

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

//Java program to find product of two numbers

//using recursion

public class GFG {

 

 //Recursive function to calculate the product 

 //of 2 integers

 static int multrecur(int n, int m)

 {

 // case 1 : n<0 and m>0

 // swap the position of n and m to keep second

 // parameter positive

 if (n > 0 && m < 0) {

 return multrecur(m, n);

 }

 // case 2 : both n and m are less than 0

 // return the product of their absolute values

 else if (n < 0 && m < 0) {

 return multrecur((-1 * n), (-1 * m));

 }

 

 // if n>m , swap n and m so that recursion

 // takes less time

 if (n > m) {

 return multrecur(m, n);

 }

 

 // as long as m is not 0 recursively call multrecur for 

 // n and m-1 return sum of n and the product of n times m-1

 else if (m != 0) {

 return n + multrecur(n, m - 1);

 }

 

 // m=0 then return 0

 else {

 return 0;

 }

 }

 

 //Driver code

 public static void main(String[] args) {

 

 System.out.println("5 * 3 = " + multrecur(5, 3));

 System.out.println("5 * (-3) = " + multrecur(5, -3));

 System.out.println("(-5) * 3 = " + multrecur(-5, 3));

 System.out.println("(-5) * (-3) = " +multrecur(-5, -3));

 }

}  
  
---  
  
 __

 __

## Python 3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to find product of two numbers

# using recursion 

 

# Recursive function to calculate the product 

# of 2 integers 

def multrecur(n, m) :

 

 # case 1 : n<0 and m>0 

 # swap the position of n and m to keep second 

 # parameter positive

 if n > 0 and m < 0 :

 return multrecur(m,n)

 

 # case 2 : both n and m are less than 0 

 # return the product of their absolute values

 elif n < 0 and m < 0 :

 return multrecur((-1 * n),(-1 * m))

 

 # if n>m , swap n and m so that recursion 

 # takes less time

 if n > m :

 return multrecur(m, n)

 

 # as long as m is not 0 recursively call multrecur for 

 # n and m-1 return sum of n and the product of n times m-1

 elif m != 0 :

 return n + multrecur(n, m-1)

 

 # m=0 then return 0 

 else :

 return 0

 

 

# Driver Code

if __name__ == "__main__" :

 

 print("5 * 3 =",multrecur(5, 3))

 print("5 * (-3) =",multrecur(5, -3))

 print("(-5) * 3 =",multrecur(-5, 3))

 print("(-5) * (-3) =",multrecur(-5, -3))

 

 

# This code is contributed by ANKITRAI1  
  
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

// C# program to find product of

// two numbers using recursion

using System;

class GFG 

{

 

// Recursive function to calculate 

// the product of 2 integers

static int multrecur(int n, int m)

{

// case 1 : n<0 and m>0

// swap the position of n and m

// to keep second parameter positive

if (n > 0 && m < 0) 

{

 return multrecur(m, n);

}

 

// case 2 : both n and m are less than 0

// return the product of their absolute values

else if (n < 0 && m < 0) 

{

 return multrecur((-1 * n), (-1 * m));

}

 

// if n>m , swap n and m so that 

// recursion takes less time

if (n > m) 

{

 return multrecur(m, n);

}

 

// as long as m is not 0 recursively 

// call multrecur for n and m-1 return 

// sum of n and the product of n times m-1

else if (m != 0)

{

 return n + multrecur(n, m - 1);

}

 

// m=0 then return 0

else

{

 return 0;

}

}

 

// Driver code

public static void Main() 

{

 Console.WriteLine("5 * 3 = " + 

 multrecur(5, 3));

 Console.WriteLine("5 * (-3) = " + 

 multrecur(5, -3));

 Console.WriteLine("(-5) * 3 = " + 

 multrecur(-5, 3));

 Console.WriteLine("(-5) * (-3) = " + 

 multrecur(-5, -3));

}

}

 

// This code is contributed by anuj_67  
  
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

// PHP program to find product of 

// two numbers using recursion

 

// Recursive function to calculate 

// the product of 2 integers

function multrecur($n, $m)

{

 // case 1 : n<0 and m>0

 // swap the position of n and m to keep second

 // parameter positive

 if ($n > 0 && $m < 0) 

 {

 return multrecur($m, $n);

 }

 

 // case 2 : both n and m are less than 0

 // return the product of their absolute values

 else if ($n < 0 && $m < 0) 

 {

 return multrecur((-1 * $n),

 (-1 * $m));

 }

 

 // if n>m , swap n and m so that 

 // recursion takes less time

 if ($n > $m) 

 {

 return multrecur($m, $n);

 }

 

 // as long as m is not 0 recursively call multrecur for 

 // n and m-1 return sum of n and the product of n times m-1

 else if ($m != 0) 

 {

 return $n + multrecur($n, $m - 1);

 }

 

 // m=0 then return 0

 else

 {

 return 0;

 }

}

 

// Driver code

echo "5 * 3 = " . multrecur(5, 3) . "\n";

echo "5 * (-3) = " . multrecur(5, -3) . "\n";

echo "(-5) * 3 = " . multrecur(-5, 3) . "\n";

echo "(-5) * (-3) = " . multrecur(-5, -3) . "\n";

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    5 * 3 = 15
    5 * (-3) = -15
    (-5) * 3 = -15
    (-5) * (-3) = 15
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

