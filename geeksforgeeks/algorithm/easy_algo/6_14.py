Count Numbers with N digits which consists of even number of 0’s



Given a number **N**. The task is to find the count of numbers which have N
digits and even number of zeroes.

 **Note:** The number can have preceding 0’s.

 **Examples** :

    
    
    **Input** : N = 2
    **Output** : Count = 81 
    Total 2 digit numbers are 99 considering 1 as 01.
    2 digit numbers are 01, 02, 03, 04, 05.... 99
    Numbers with odd 0's are 01, 02, 03, 04, 05, 06, 07, 08, 09
    10, 20, 30, 40, 50, 70, 80, 90 i.e. 18
    The rest of the numbers between 01 and 99 will 
    do not have any zeroes and zero is also an even number.
    So, numbers with even 0's are 99 - 18 = 81.
    
    **Input** : N = 3
    **Output** : Count = 755
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to find the Count Numbers with N digits which
consists of odd number of 0’s and subtract it from the total number with N
digits to get the number with even 0’s.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count numbers with N digits

// which consists of odd number of 0's

#include <bits/stdc++.h>

using namespace std;

 

// Function to count Numbers with N digits

// which consists of odd number of 0's

int countNumbers(int N)

{

 return (pow(10, N) - 1) - (pow(10, N) - pow(8, N)) / 2;

}

 

// Driver code

int main()

{

 int n = 2;

 

 cout << countNumbers(n) << endl;

 

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

// Java program to count numbers

// with N digits which consists 

// of odd number of 0's 

import java.lang.*;

import java.util.*;

 

class GFG

{

 

// Function to count Numbers with 

// N digits which consists of odd 

// number of 0's 

static double countNumbers(int N) 

{ 

 return (Math.pow(10, N) - 1) - 

 (Math.pow(10, N) - 

 Math.pow(8, N)) / 2; 

} 

 

// Driver code 

static public void main (String args[])

{

 int n = 2; 

 System.out.println(countNumbers(n)); 

}

}

 

// This code si contributed 

// by Akanksha Rai  
  
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

# Python3 program to count numbers with N digits

# which consists of odd number of 0's

 

# Function to count Numbers with N digits

# which consists of odd number of 0's

def countNumber(n):

 

 return (pow(10,n)-1)-
(pow(10,n)-pow(8,n))//2

 

 

# Driver code

n = 2

print(countNumber(n))

 

# This code is contributed by Shrikant13  
  
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

// C# program to count numbers

// with N digits which consists 

// of odd number of 0's 

using System;

 

class GFG

{

 

// Function to count Numbers with 

// N digits which consists of odd 

// number of 0's 

static double countNumbers(int N) 

{ 

 return (Math.Pow(10, N) - 1) - 

 (Math.Pow(10, N) - 

 Math.Pow(8, N)) / 2; 

} 

 

// Driver code 

static public void Main ()

{

 int n = 2; 

 Console.WriteLine(countNumbers(n)); 

}

}

 

// This code si contributed by ajit   
  
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

// PHP program to count numbers with N digits 

// which consists of odd number of 0's 

 

// Function to count Numbers with N digits 

// which consists of odd number of 0's 

function countNumbers($N) 

{ 

 return (pow(10, $N) - 1) - 

 (pow(10, $N) - pow(8, $N)) / 2; 

} 

 

// Driver code 

$n = 2; 

echo countNumbers($n),"\n"; 

 

// This code is contributed by akt_mit

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    81
    

**Note** : Answer can be very large, so for N greater than 9, use modular
exponentiation.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

