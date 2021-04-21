Minimum removals in a number to be divisible by 10 power raised to K



Given two positive integers **N** and **K**. Find the minimum number of digits
that can be removed from the number N such that after removals the number is
divisible by **10 K** or print -1 if it is impossible.

 **Examples:**

    
    
    **Input :** N = 10904025, K = 2
    **Output :** 3
    **Explanation :** We can remove the digits 4, 2 and 5 such that the number 
    becomes 10900 which is divisible by 102.
    
    **Input :** N = 1000, K = 5
    **Output :** 3
    **Explanation :** We can remove the digits 1 and any two zeroes such that the
    number becomes 0 which is divisible by 105
    
    **Input :** N = 23985, K = 2
    **Output :** -1
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach :** The idea is to start traversing the number from the last digit
while keeping a counter. If the current digit is not zero, increment the
counter variable, otherwise decrement variable K. When K becomes zero, return
counter as answer. After traversing the whole number, check if the current
value of K is zero or not. If it is zero, return counter as answer, otherwise
return answer as number of digits in N – 1, since we need to reduce the whole
number to a single zero which is divisible by any number. Also, if the given
number does not contain any zero, return -1 as answer.

Below is the implementation of above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP Program to count the number

// of digits that can be removed such

// that number is divisible by 10^K

#include <bits/stdc++.h>

using namespace std;

 

// function to return the required

// number of digits to be removed

int countDigitsToBeRemoved(int N, int K)

{

 // Converting the given number

 // into string

 string s = to_string(N);

 

 // variable to store number of

 // digits to be removed

 int res = 0;

 

 // variable to denote if atleast

 // one zero has been found

 int f_zero = 0;

 for (int i = s.size() - 1; i >= 0; i--) {

 if (K == 0)

 return res;

 if (s[i] == '0') {

 

 // zero found

 f_zero = 1;

 K--;

 }

 else

 res++;

 }

 

 // return size - 1 if K is not zero and

 // atleast one zero is present, otherwise

 // result

 if (!K)

 return res;

 else if (f_zero)

 return s.size() - 1;

 return -1;

}

 

// Driver Code to test above function

int main()

{

 int N = 10904025, K = 2;

 cout << countDigitsToBeRemoved(N, K) << endl;

 

 N = 1000, K = 5;

 cout << countDigitsToBeRemoved(N, K) << endl;

 

 N = 23985, K = 2;

 cout << countDigitsToBeRemoved(N, K) << endl;

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

// Java Program to count the number

// of digits that can be removed such 

// that number is divisible by 10^K 

 

public class GFG{

 

 // function to return the required 

 // number of digits to be removed 

 static int countDigitsToBeRemoved(int N, int K) 

 { 

 // Converting the given number 

 // into string 

 String s = Integer.toString(N); 

 

 // variable to store number of 

 // digits to be removed 

 int res = 0; 

 

 // variable to denote if atleast 

 // one zero has been found 

 int f_zero = 0; 

 for (int i = s.length() - 1; i >= 0; i--) { 

 if (K == 0) 

 return res; 

 if (s.charAt(i) == '0') { 

 

 // zero found 

 f_zero = 1; 

 K--; 

 } 

 else

 res++; 

 } 

 

 // return size - 1 if K is not zero and 

 // atleast one zero is present, otherwise 

 // result 

 if (K == 0) 

 return res; 

 else if (f_zero == 1) 

 return s.length() - 1; 

 return -1; 

 } 

 

 // Driver Code to test above function 

 public static void main(String []args)

 { 

 int N = 10904025;

 int K = 2; 

 System.out.println(countDigitsToBeRemoved(N, K)) ; 

 

 N = 1000 ;

 K = 5; 

 System.out.println(countDigitsToBeRemoved(N, K)) ;

 

 N = 23985;

 K = 2; 

 System.out.println(countDigitsToBeRemoved(N, K)) ; 

 } 

 

 // This code is contributed by Ryuga

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

# Python3 Program to count the number

# of digits that can be removed such

# that number is divisible by 10^K

 

# function to return the required

# number of digits to be removed

def countDigitsToBeRemoved(N, K):

 

 # Converting the given number

 # into string

 s = str(N);

 

 # variable to store number of

 # digits to be removed

 res = 0;

 

 # variable to denote if atleast

 # one zero has been found

 f_zero = 0;

 for i in range(len(s) - 1, -1, -1):

 if (K == 0):

 return res;

 if (s[i] == '0'):

 

 # zero found

 f_zero = 1;

 K -= 1;

 else:

 res += 1;

 

 # return size - 1 if K is not zero and

 # atleast one zero is present, otherwise

 # result

 if (K == 0):

 return res;

 elif (f_zero > 0):

 return len(s) - 1;

 return -1;

 

# Driver Code

N = 10904025;

K = 2;

print(countDigitsToBeRemoved(N, K));

 

N = 1000;

K = 5;

print(countDigitsToBeRemoved(N, K));

 

N = 23985;

K = 2;

print(countDigitsToBeRemoved(N, K));

 

# This code is contributed by mits  
  
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

// C# Program to count the number

// of digits that can be removed such 

// that number is divisible by 10^K 

 

using System;

public class GFG{

 

 // function to return the required 

 // number of digits to be removed 

 static int countDigitsToBeRemoved(int N, int K) 

 { 

 // Converting the given number 

 // into string 

 string s = Convert.ToString(N); 

 

 // variable to store number of 

 // digits to be removed 

 int res = 0; 

 

 // variable to denote if atleast 

 // one zero has been found 

 int f_zero = 0; 

 for (int i = s.Length - 1; i >= 0; i--) { 

 if (K == 0) 

 return res; 

 if (s[i] == '0') { 

 

 // zero found 

 f_zero = 1; 

 K--; 

 } 

 else

 res++; 

 } 

 

 // return size - 1 if K is not zero and 

 // atleast one zero is present, otherwise 

 // result 

 if (K == 0) 

 return res; 

 else if (f_zero == 1) 

 return s.Length - 1; 

 return -1; 

 } 

 

 // Driver Code to test above function 

 public static void Main()

 { 

 int N = 10904025;

 int K = 2; 

 Console.Write(countDigitsToBeRemoved(N, K)+"\n") ; 

 

 N = 1000 ;

 K = 5; 

 Console.Write(countDigitsToBeRemoved(N, K)+"\n") ;

 

 N = 23985;

 K = 2; 

 Console.Write(countDigitsToBeRemoved(N, K)+"\n") ; 

 } 

 

 

 }  
  
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

// PHP Program to count the number

// of digits that can be removed such

// that number is divisible by 10^K

 

// function to return the required

// number of digits to be removed

function countDigitsToBeRemoved($N, $K)

{

 // Converting the given number

 // into string

 $s = strval($N);

 

 // variable to store number of

 // digits to be removed

 $res = 0;

 

 // variable to denote if atleast

 // one zero has been found

 $f_zero = 0;

 for ($i = strlen($s)-1; $i >= 0; $i--) {

 if ($K == 0)

 return $res;

 if ($s[$i] == '0') {

 

 // zero found

 $f_zero = 1;

 $K--;

 }

 else

 $res++;

 }

 

 // return size - 1 if K is not zero and

 // atleast one zero is present, otherwise

 // result

 if (!$K)

 return $res;

 else if ($f_zero)

 return strlen($s) - 1;

 return -1;

}

 

// Driver Code to test above function

 

 $N = 10904025;

 $K = 2;

 echo countDigitsToBeRemoved($N, $K)."\n";

 

 $N = 1000;

 $K = 5;

 echo countDigitsToBeRemoved($N, $K)."\n";

 

 $N = 23985;

 $K = 2;

 echo countDigitsToBeRemoved($N, $K);

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    3
    -1
    

**Time Complexity :** Number of digits in the given number.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

