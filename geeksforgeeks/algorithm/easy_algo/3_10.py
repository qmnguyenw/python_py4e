Check if the sum of digits of N is palindrome



Given an integer **N** , the task is to check whether the sum of digits of
**N** is palindrome or not.

 **Example:**

>  **Input:** N = 56  
>  **Output:** Yes  
> Digit sum is (5 + 6) = 11  
> which is a palindrome.
>
>  **Input:** N = 51241  
>  **Output:** No  
> (5 + 1 + 2 + 4 + 1) = 13

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Find the sum of digits of **N** and store it in a variable
**sum**. Now check whether **sum** is palindrome or not using the approach
discussed in this article.

  

  

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the

// sum of digits of n

int digitSum(int n)

{

 int sum = 0;

 while (n > 0) {

 sum += (n % 10);

 n /= 10;

 }

 return sum;

}

 

// Function that returns true

// if n is palindrome

bool isPalindrome(int n)

{

 // Find the appropriate divisor

 // to extract the leading digit

 int divisor = 1;

 while (n / divisor >= 10)

 divisor *= 10;

 

 while (n != 0) {

 int leading = n / divisor;

 int trailing = n % 10;

 

 // If first and last digit

 // not same return false

 if (leading != trailing)

 return false;

 

 // Removing the leading and trailing

 // digit from number

 n = (n % divisor) / 10;

 

 // Reducing divisor by a factor

 // of 2 as 2 digits are dropped

 divisor = divisor / 100;

 }

 return true;

}

 

// Function that returns true if

// the digit sum of n is palindrome

bool isDigitSumPalindrome(int n)

{

 

 // Sum of the digits of n

 int sum = digitSum(n);

 

 // If the digit sum is palindrome

 if (isPalindrome(sum))

 return true;

 return false;

}

 

// Driver code

int main()

{

 int n = 56;

 

 if (isDigitSumPalindrome(n))

 cout << "Yes";

 else

 cout << "No";

 

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

// Java implementation of the approach

import java.util.*;

 

class GFG

{

 

// Function to return the

// sum of digits of n

static int digitSum(int n)

{

 int sum = 0;

 while (n > 0)

 {

 sum += (n % 10);

 n /= 10;

 }

 return sum;

}

 

// Function that returns true

// if n is palindrome

static boolean isPalindrome(int n)

{

 // Find the appropriate divisor

 // to extract the leading digit

 int divisor = 1;

 while (n / divisor >= 10)

 divisor *= 10;

 

 while (n != 0)

 {

 int leading = n / divisor;

 int trailing = n % 10;

 

 // If first and last digit

 // not same return false

 if (leading != trailing)

 return false;

 

 // Removing the leading and trailing

 // digit from number

 n = (n % divisor) / 10;

 

 // Reducing divisor by a factor

 // of 2 as 2 digits are dropped

 divisor = divisor / 100;

 }

 return true;

}

 

// Function that returns true if

// the digit sum of n is palindrome

static boolean isDigitSumPalindrome(int n)

{

 

 // Sum of the digits of n

 int sum = digitSum(n);

 

 // If the digit sum is palindrome

 if (isPalindrome(sum))

 return true;

 return false;

}

 

// Driver code

public static void main(String []args)

{

 int n = 56;

 

 if (isDigitSumPalindrome(n))

 System.out.println("Yes");

 else

 System.out.println("No");

}

}

 

// This code is contributed by Surendra_Gangwar  
  
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

# Python3 implementation of the approach

 

# Function to return the 

# sum of digits of n 

def digitSum(n) :

 

 sum = 0; 

 while (n > 0) :

 sum += (n % 10); 

 n //= 10; 

 

 return sum; 

 

# Function that returns true 

# if n is palindrome 

def isPalindrome(n) : 

 

 # Find the appropriate divisor 

 # to extract the leading digit 

 divisor = 1; 

 while (n // divisor >= 10) :

 divisor *= 10; 

 

 while (n != 0) :

 leading = n // divisor; 

 trailing = n % 10; 

 

 # If first and last digit 

 # not same return false 

 if (leading != trailing) :

 return False; 

 

 # Removing the leading and trailing 

 # digit from number 

 n = (n % divisor) // 10; 

 

 # Reducing divisor by a factor 

 # of 2 as 2 digits are dropped 

 divisor = divisor // 100; 

 

 return True; 

 

# Function that returns true if 

# the digit sum of n is palindrome 

def isDigitSumPalindrome(n) : 

 

 # Sum of the digits of n 

 sum = digitSum(n); 

 

 # If the digit sum is palindrome 

 if (isPalindrome(sum)) :

 return True; 

 return False; 

 

# Driver code 

if __name__ == "__main__" : 

 

 n = 56; 

 

 if (isDigitSumPalindrome(n)) :

 print("Yes"); 

 else :

 print("No"); 

 

# This code is contributed by AnkitRai01  
  
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

// C# implementation of the approach

using System;

 

class GFG

{

 

// Function to return the

// sum of digits of n

static int digitSum(int n)

{ 

 int sum = 0;

 while (n > 0)

 {

 sum += (n % 10);

 n /= 10;

 }

 return sum;

}

 

// Function that returns true

// if n is palindrome

static bool isPalindrome(int n)

{

 // Find the appropriate divisor

 // to extract the leading digit

 int divisor = 1;

 while (n / divisor >= 10)

 divisor *= 10;

 

 while (n != 0)

 {

 int leading = n / divisor;

 int trailing = n % 10;

 

 // If first and last digit

 // not same return false

 if (leading != trailing)

 return false;

 

 // Removing the leading and trailing

 // digit from number

 n = (n % divisor) / 10;

 

 // Reducing divisor by a factor

 // of 2 as 2 digits are dropped

 divisor = divisor / 100;

 }

 return true;

}

 

// Function that returns true if

// the digit sum of n is palindrome

static bool isDigitSumPalindrome(int n)

{

 

 // Sum of the digits of n

 int sum = digitSum(n);

 

 // If the digit sum is palindrome

 if (isPalindrome(sum))

 return true;

 return false;

}

 

// Driver code

static public void Main ()

{

 int n = 56;

 

 if (isDigitSumPalindrome(n))

 Console.Write("Yes");

 else

 Console.Write("No");

}

}

 

// This code is contributed by ajit  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

