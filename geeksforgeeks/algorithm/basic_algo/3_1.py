Occurrences of a pattern in binary representation of a number



Given a string **pat** and an integer **N** , the task is to find the number
of occurrences of the pattern **pat** in binary representation of **N**.

 **Examples:**

>  **Input:** N = 2, pat = “101”  
>  **Output:** 0  
> Pattern “101” doesn’t occur in the binary representation of 2 (10).
>
>  **Input:** N = 10, pat = “101”  
>  **Output:** 1  
> Binary representation of 10 is 1010 and the given pattern occurs only once.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** Convert the number into its binary string representation
and then use a pattern matching algorithm to check the number of times the
pattern has occurred in the binary representation.

  

  

 **Efficient Approach:**

  1. Convert the binary pattern into it’s decimal representation.
  2. Take an integer **all_ones** , whose binary representation consists of all set bits (equal to the number of bits in the pattern).
  3. Performing **N & all_ones** now will leave only the last **k** bits unchanged (others will be 0) where **k** is the number of bits in the pattern.
  4. Now if **N = pattern** , it means that **N** contained the pattern in the end in its binary representation. So update **count = count + 1**.
  5. Right shift **N** by 1 and repeat the previous two steps until **N ≥ pattern & N > 0**.
  6. Print the **count** in the end.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the number of times

// pattern p occurred in binary representation

// on n.

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the count of occurrence

// of pat in binary representation of n

int countPattern(int n, string pat)

{

 // To store decimal value of the pattern

 int pattern_int = 0;

 

 int power_two = 1;

 

 // To store a number that has all ones in

 // its binary representation and length

 // of ones equal to length of the pattern

 int all_ones = 0;

 

 // Find values of pattern_int and all_ones

 for (int i = pat.length() - 1; i >= 0; i--) {

 int current_bit = pat[i] - '0';

 pattern_int += (power_two * current_bit);

 all_ones = all_ones + power_two;

 power_two = power_two * 2;

 }

 

 int count = 0;

 while (n && n >= pattern_int) {

 

 // If the pattern occurs in the last

 // digits of n

 if ((n & all_ones) == pattern_int) {

 count++;

 }

 

 // Right shift n by 1 bit

 n = n >> 1;

 }

 return count;

}

 

// Driver code

int main()

{

 int n = 500;

 string pat = "10";

 cout << countPattern(n, pat);

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

// Java program to find the number of times

// pattern p occurred in binary representation

// on n.

import java.util.*;

 

class solution

{

 

// Function to return the count of occurrence

// of pat in binary representation of n

static int countPattern(int n, String pat)

{

 // To store decimal value of the pattern

 int pattern_int = 0;

 

 int power_two = 1;

 

 // To store a number that has all ones in

 // its binary representation and length

 // of ones equal to length of the pattern

 int all_ones = 0;

 

 // Find values of pattern_int and all_ones

 for (int i = pat.length() - 1; i >= 0; i--) {

 int current_bit = pat.charAt(i) - '0';

 pattern_int += (power_two * current_bit);

 all_ones = all_ones + power_two;

 power_two = power_two * 2;

 }

 

 int count = 0;

 while (n!=0 && n >= pattern_int) {

 

 // If the pattern occurs in the last

 // digits of n

 if ((n & all_ones) == pattern_int) {

 count++;

 }

 

 // Right shift n by 1 bit

 n = n >> 1;

 }

 return count;

}

 

// Driver code

public static void main(String args[])

{

 int n = 500;

 String pat = "10";

 System.out.println(countPattern(n, pat));

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

# Python 3 program to find the number of times

# pattern p occurred in binary representation

# on n.

 

# Function to return the count of occurrence

# of pat in binary representation of n

def countPattern(n, pat):

 

 # To store decimal value of the pattern

 pattern_int = 0

 

 power_two = 1

 

 # To store a number that has all ones in

 # its binary representation and length

 # of ones equal to length of the pattern

 all_ones = 0

 

 # Find values of pattern_int and all_ones

 i = len(pat) - 1

 while(i >= 0):

 current_bit = ord(pat[i]) - ord('0')

 pattern_int += (power_two * current_bit)

 all_ones = all_ones + power_two

 power_two = power_two * 2

 i -= 1

 

 count = 0

 while (n != 0 and n >= pattern_int):

 

 # If the pattern occurs in the last

 # digits of n

 if ((n & all_ones) == pattern_int):

 count += 1

 

 # Right shift n by 1 bit

 n = n >> 1

 

 return count

 

# Driver code

if __name__ == '__main__':

 n = 500

 pat = "10"

 print(countPattern(n, pat))

 

# This code is contributed by

# Surendra_Gangwar  
  
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

// C# program to find the number of times

// pattern p occurred in binary representation 

// on n. 

using System ;

 

class GFG 

{ 

 

// Function to return the count of occurrence 

// of pat in binary representation of n 

static int countPattern(int n, string pat) 

{ 

 // To store decimal value of the pattern 

 int pattern_int = 0; 

 

 int power_two = 1; 

 

 // To store a number that has all ones in 

 // its binary representation and length 

 // of ones equal to length of the pattern 

 int all_ones = 0; 

 

 // Find values of pattern_int and all_ones 

 for (int i = pat.Length - 1; i >= 0; i--) 

 { 

 int current_bit = pat[i] - '0'; 

 pattern_int += (power_two * current_bit); 

 all_ones = all_ones + power_two; 

 power_two = power_two * 2; 

 } 

 

 int count = 0; 

 while (n != 0 && n >= pattern_int) 

 { 

 

 // If the pattern occurs in the last 

 // digits of n 

 if ((n & all_ones) == pattern_int) 

 { 

 count++; 

 } 

 

 // Right shift n by 1 bit 

 n = n >> 1; 

 } 

 return count; 

} 

 

// Driver code 

public static void Main() 

{ 

 int n = 500; 

 string pat = "10"; 

 Console.WriteLine(countPattern(n, pat)); 

} 

} 

 

// This code is contributed by Ryuga  
  
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

// PHP program to find the number of times

// pattern pat occurred in binary representation

// of n.

 

// Function to return the count of occurrence

// of pat in binary representation of n

function countPattern($n, $pat)

{

 // To store decimal value of the pattern

 $pattern_int = 0;

 

 $power_two = 1;

 

 // To store a number that has all ones in

 // its binary representation and length

 // of ones equal to length of the pattern

 $all_ones = 0;

 

 // Find values of $pattern_int and $all_ones

 for ($i = strlen($pat) - 1; $i >= 0; $i--) 

 {

 $current_bit = $pat[$i] - '0';

 $pattern_int += ($power_two * $current_bit);

 $all_ones = $all_ones + $power_two;

 $power_two = $power_two * 2;

 }

 

 $count = 0;

 while ($n && $n >= $pattern_int)

 {

 

 // If the pattern occurs in the last

 // digits of $n

 if (($n & $all_ones) == $pattern_int) 

 {

 $count++;

 }

 

 // Right shift $n by 1 bit

 $n = $n >> 1;

 }

 return $count;

}

 

// Driver code

$n = 500;

$pat = "10";

echo countPattern($n, $pat);

 

// This code is contributed by ihritik

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

