Find the count of sub-strings whose characters can be rearranged to form the
given word



Given a string **str** , the task is to find the count of all the sub-strings
of length four whose characters can be rearranged to form the word **“clap”**.

 **Examples:**

>  **Input:** str = “clapc”  
>  **Output:** 2  
> “clap” and “lapc” are the required sub-strings
>
>  **Input:** str = “abcd”  
>  **Output:** 0

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** For every sub-string of length four, count the occurrences of
the characters from the word **“clap”**. If every character has the occurrence
exactly one in the sub-string then increment the **count**. Print the
**count** in the end.

  

  

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP implementation of the approach

#include<bits/stdc++.h>

using namespace std;

 

// Function to return the count of

// required occurrence

int countOcc(string s)

{

 

 // To store the count of occurrences

 int cnt = 0;

 

 // Check first four characters from ith position

 for (int i = 0; i < s.length() - 3; i++) 

 {

 

 // Variables for counting the required characters

 int c = 0, l = 0, a = 0, p = 0;

 

 // Check the four contiguous characters which

 // can be reordered to form 'clap'

 for (int j = i; j < i + 4; j++) 

 {

 switch (s[j]) 

 {

 case 'c':

 c++;

 break;

 case 'l':

 l++;

 break;

 case 'a':

 a++;

 break;

 case 'p':

 p++;

 break;

 }

 }

 

 // If all four contiguous characters are present

 // then increment cnt variable

 if (c == 1 && l == 1 && a == 1 && p == 1)

 cnt++;

 }

 

 return cnt;

}

 

// Driver code

int main()

{

 string s = "clapc";

 transform(s.begin(), s.end(), s.begin(), ::tolower);

 cout << (countOcc(s));

}

 

// This code is contributed by

// Surendra_Gangwar  
  
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

class GFG {

 

 // Function to return the count of

 // required occurrence

 static int countOcc(String s)

 {

 

 // To store the count of occurrences

 int cnt = 0;

 

 // Check first four characters from ith position

 for (int i = 0; i < s.length() - 3; i++) {

 

 // Variables for counting the required characters

 int c = 0, l = 0, a = 0, p = 0;

 

 // Check the four contiguous characters which

 // can be reordered to form 'clap'

 for (int j = i; j < i + 4; j++) {

 switch (s.charAt(j)) {

 case 'c':

 c++;

 break;

 case 'l':

 l++;

 break;

 case 'a':

 a++;

 break;

 case 'p':

 p++;

 break;

 }

 }

 

 // If all four contiguous characters are present

 // then increment cnt variable

 if (c == 1 && l == 1 && a == 1 && p == 1)

 cnt++;

 }

 

 return cnt;

 }

 

 // Driver code

 public static void main(String args[])

 {

 String s = "clapc";

 System.out.print(countOcc(s.toLowerCase()));

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

# Python3 implementation of the approach

 

# Function to return the count of

# required occurrence

def countOcc(s):

 

 # To store the count of occurrences

 cnt = 0

 

 # Check first four characters from ith position

 for i in range(0, len(s) - 3): 

 

 # Variables for counting the required characters

 c, l, a, p = 0, 0, 0, 0

 

 # Check the four contiguous characters

 # which can be reordered to form 'clap'

 for j in range(i, i + 4): 

 

 if s[j] == 'c':

 c += 1

 

 elif s[j] == 'l':

 l += 1

 

 elif s[j] == 'a':

 a += 1

 

 elif s[j] == 'p':

 p += 1

 

 # If all four contiguous characters are

 # present then increment cnt variable

 if c == 1 and l == 1 and a == 1 and p
== 1:

 cnt += 1

 

 return cnt

 

# Driver code

if __name__ == "__main__":

 

 s = "clapc"

 print(countOcc(s.lower()))

 

# This code is contributed by Rituraj Jain  
  
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

// required occurrence

static int countOcc(string s)

{

 

 // To store the count of occurrences

 int cnt = 0;

 

 // Check first four characters 

 // from ith position

 for (int i = 0; i < s.Length - 3; i++) 

 {

 

 // Variables for counting the 

 // required characters

 int c = 0, l = 0, a = 0, p = 0;

 

 // Check the four contiguous characters 

 // which can be reordered to form 'clap'

 for (int j = i; j < i + 4; j++) 

 {

 switch (s[j]) 

 {

 case 'c':

 c++;

 break;

 case 'l':

 l++;

 break;

 case 'a':

 a++;

 break;

 case 'p':

 p++;

 break;

 }

 }

 

 // If all four contiguous characters are

 // present then increment cnt variable

 if (c == 1 && l == 1 && a == 1 && p == 1)

 cnt++;

 }

 

 return cnt;

}

 

// Driver code

public static void Main()

{

 string s = "clapc";

 Console.Write(countOcc(s.ToLower()));

}

}

 

// This code is contributed by Akanksha Rai  
  
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

 

// Function to return the count of 

// required occurrence 

function countOcc($s) 

{ 

 

 // To store the count of occurrences 

 $cnt = 0; 

 

 // Check first four characters 

 // from ith position 

 for ($i = 0; $i < strlen($s) - 3; $i++) 

 { 

 

 // Variables for counting the 

 // required characters 

 $c = 0; $l = 0; $a = 0; $p = 0; 

 

 // Check the four contiguous characters 

 // which can be reordered to form 'clap' 

 for ($j = $i; $j < $i + 4; $j++) 

 { 

 switch ($s[$j]) 

 { 

 case 'c': 

 $c++; 

 break; 

 case 'l': 

 $l++; 

 break; 

 case 'a': 

 $a++; 

 break; 

 case 'p': 

 $p++; 

 break; 

 } 

 } 

 

 // If all four contiguous characters are present 

 // then increment cnt variable 

 if ($c == 1 && $l == 1 && 

 $a == 1 && $p == 1) 

 $cnt++; 

 } 

 

 return $cnt; 

} 

 

// Driver code 

$s = "clapc"; 

 

echo countOcc(strtolower($s)); 

 

// This code is contributed by Ryuga

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

