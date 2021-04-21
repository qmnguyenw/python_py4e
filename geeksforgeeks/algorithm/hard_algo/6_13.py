Count of sub-strings that do not contain all the characters from the set {‘a’,
‘b’, ‘c’} at the same time



Given a string **str** consisting only of the characters **‘a’** , **‘b’** and
**‘c’** , find the number of sub-strings that do not contain all the three
characters at the same time.

 **Examples:**

>  **Input:** str = “abc”  
>  **Output:** 5  
> The possible substrings are “a”, “b”, “c”, “ab” and “bc”
>
>  **Input:** str = “babac”  
>  **Output:** 12

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to use three variables **a_index** , **b_index**
and **c_index** to store the latest occurrence of the characters a, b and c
and another variable **ans** to store the number of substrings that don’t have
at least one of a, b or c and initialize its value to the total number of
substrings with length n i.e, **n*(n+1)/2** , where n is the length of the
string.

  

  

Now simply traverse the string from the beginning. At each point update the
value of variables to the latest value whenever encountered.Since we are
indexing with 0, so we are updating the index as **i+1** at each step.

Also at each step, you need to find the index of minimum occurrence of the
remaining of the two characters not encountered in the current step.

Then simply deduct this index from the variable **ans**. This is because once
you found the index of the minimum of the remaining characters you are sure
that any more substrings formed by moving downwards in index will also contain
all the three characters.

Hence the total numbers of all such substrings(ones containing all a, b, and
c) formed at this step is the found index.

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

 

// Function to return the count of valid sub-strings

int CountSubstring(char str[], int n)

{

 

 // Variable ans to store all the possible substrings

 // Initialize its value as total number of substrings

 // that can be formed from the given string

 int ans = (n * (n + 1)) / 2;

 

 // Stores recent index of the characters

 int a_index = 0;

 int b_index = 0;

 int c_index = 0;

 

 for (int i = 0; i < n; i++) {

 

 // If character is a update a's index

 // and the variable ans

 if (str[i] == 'a') {

 a_index = i + 1;

 ans -= min(b_index, c_index);

 }

 

 // If character is b update b's index

 // and the variable ans

 else if (str[i] == 'b') {

 b_index = i + 1;

 ans -= min(a_index, c_index);

 }

 

 // If character is c update c's index

 // and the variable ans

 else {

 c_index = i + 1;

 ans -= min(a_index, b_index);

 }

 }

 

 return ans;

}

 

// Driver code

int main()

{

 char str[] = "babac";

 int n = strlen(str);

 

 cout << CountSubstring(str, n);

 

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

class GFG 

{

 

 // Function to return the count of valid sub-strings

 static int CountSubstring(char str[], int n) 

 {

 

 // Variable ans to store all the possible substrings

 // Initialize its value as total number of substrings

 // that can be formed from the given string

 int ans = (n * (n + 1)) / 2;

 

 // Stores recent index of the characters

 int a_index = 0;

 int b_index = 0;

 int c_index = 0;

 

 for (int i = 0; i < n; i++) 

 {

 

 // If character is a update a's index

 // and the variable ans

 if (str[i] == 'a') 

 {

 a_index = i + 1;

 ans -= Math.min(b_index, c_index);

 } 

 // If character is b update b's index

 // and the variable ans

 else if (str[i] == 'b')

 {

 b_index = i + 1;

 ans -= Math.min(a_index, c_index);

 } 

 // If character is c update c's index

 // and the variable ans

 else

 {

 c_index = i + 1;

 ans -= Math.min(a_index, b_index);

 }

 }

 

 return ans;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 char str[] = "babac".toCharArray();

 int n = str.length;

 

 System.out.println(CountSubstring(str, n));

 }

}

 

// This code contributed by Rajput-Ji  
  
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

 

# Function to return the count of 

# valid sub-Strings

def CountSubString(Str, n):

 

 # Variable ans to store all the possible subStrings

 # Initialize its value as total number of subStrings

 # that can be formed from the given String

 ans = (n * (n + 1)) // 2

 

 # Stores recent index of the characters

 a_index = 0

 b_index = 0

 c_index = 0

 

 for i in range(n):

 

 # If character is a update a's index

 # and the variable ans

 if (Str[i] == 'a'):

 a_index = i + 1

 ans -= min(b_index, c_index)

 

 # If character is b update b's index

 # and the variable ans

 elif (Str[i] == 'b'):

 b_index = i + 1

 ans -= min(a_index, c_index)

 

 # If character is c update c's index

 # and the variable ans

 else:

 c_index = i + 1

 ans -= min(a_index, b_index)

 

 return ans

 

# Driver code

Str = "babac"

n = len(Str)

 

print(CountSubString(Str, n))

 

# This code is contributed by mohit kumar  
  
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

 

// Function to return the count of

// valid sub-strings

static int CountSubstring(char []str, int n) 

{

 

 // Variable ans to store all the possible substrings

 // Initialize its value as total number of substrings

 // that can be formed from the given string

 int ans = (n * (n + 1)) / 2;

 

 // Stores recent index of the characters

 int a_index = 0;

 int b_index = 0;

 int c_index = 0;

 

 for (int i = 0; i < n; i++) 

 {

 

 // If character is a update a's index

 // and the variable ans

 if (str[i] == 'a') 

 {

 a_index = i + 1;

 ans -= Math.Min(b_index, c_index);

 } 

 // If character is b update b's index

 // and the variable ans

 else if (str[i] == 'b')

 {

 b_index = i + 1;

 ans -= Math.Min(a_index, c_index);

 } 

 // If character is c update c's index

 // and the variable ans

 else

 {

 c_index = i + 1;

 ans -= Math.Min(a_index, b_index);

 }

 }

 

 return ans;

}

 

// Driver code

public static void Main()

{

 char []str = "babac".ToCharArray();

 int n = str.Length;

 

 Console.WriteLine(CountSubstring(str, n));

}

}

 

// This code contributed 

// by Akanksha Rai  
  
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

 // PHP implementation of the approach

 // Function to return the count of valid sub-strings

 function CountSubstring($str,$n) 

 

 {

 

 // Variable ans to store all the possible substrings

 // Initialize its value as total number of substrings

 // that can be formed from the given string

 $ans = ($n * ($n + 1)) / 2;

 

 // Stores recent index of the characters

 $a_index = 0;

 $b_index = 0;

 $c_index = 0;

 

 for ($i = 0; $i < $n; $i++) 

 {

 

 

 // If character is a update a's index

 // and the variable ans

 if ($str[$i] == 'a') 

 {

 $a_index = $i + 1;

 $ans -= min($b_index, $c_index);

 } 

 // If character is b update b's index

 // and the variable ans

 else if ($str[$i] == 'b')

 {

 $b_index = $i + 1;

 $ans -= min($a_index, $c_index);

 } 

 // If character is c update c's index

 // and the variable ans

 else

 {

 $c_index = $i + 1;

 $ans -= min($a_index, $b_index);

 }

 }

 

 return $ans;

 }

 

 // Driver code

 {

 $str = str_split("babac");

 $n = sizeof($str);

 

 echo(CountSubstring($str, $n));

 }

 

 

// This code contributed by Code_Mech.  
  
---  
  
 __

 __

 **Output:**

    
    
    12
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

