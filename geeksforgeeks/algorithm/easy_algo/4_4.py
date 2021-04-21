Rearrange characters in a string such that no two adjacent are same using
hashing



Given a string **str** with repeated characters, the task is to rearrange the
characters in a string such that no two adjacent characters are same. If it is
possible then print **Yes** else print **No**.  
 **Examples:**

> **Input:** str = “geeksforgeeks”  
> **Output:** Yes  
> “egeksforegeks” is one such arrangement.
>
>  **Input:** str = “bbbbb”  
> **Output:** No

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to store the frequency of each character in an
unordered_map and compare maximum frequency of character with the difference
of string length and maximum frequency number. If the maximum frequency is
less than the difference then it can be arranged otherwise not.

  1. Let we start putting all the character having maximum frequency alternatively. Then at minimum, we need (max_freq-1) spaces between them to solve the question so that they are not adjacent to each other. 
  2. But we have (length of the string – max_freq) spaces left. So, (length of the string – max_freq) should be at least (max_freq-1) to arrange such that no two char are the same.
  3. So, it goes this way: (max_freq+1) <= (length of the string – max_freq)   

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

#include <time.h>

using namespace std;

// Function that returns true if it is possible

// to rearrange the characters of the string

// such that no two consecutive characters are same

int isPossible(string str)

{

 // To store the frequency of

 // each of the character

 unordered_map<char, int> freq;

 // To store the maximum frequency so far

 int max_freq = 0;

 for (int j = 0; j < (str.length()); j++) {

 freq[str[j]]++;

 if (freq[str[j]] > max_freq)

 max_freq = freq[str[j]];

 }

 // If possible

 if (max_freq <= (str.length() - max_freq + 1))

 return true;

 return false;

}

// Driver code

int main()

{

 string str = "geeksforgeeks";

 if (isPossible(str))

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

class GFG {

 // Function that returns true if it is possible

 // to rearrange the characters of the string

 // such that no two consecutive characters are same

 static boolean isPossible(char[] str)

 {

 // To store the frequency of

 // each of the character

 Map<Character, Integer> freq = new HashMap<>();

 // To store the maximum frequency so far

 int max_freq = 0;

 for (int j = 0; j < (str.length); j++) {

 if (freq.containsKey(str[j])) {

 freq.put(str[j], freq.get(str[j]) + 1);

 if (freq.get(str[j]) > max_freq)

 max_freq = freq.get(str[j]);

 }

 else {

 freq.put(str[j], 1);

 if (freq.get(str[j]) > max_freq)

 max_freq = freq.get(str[j]);

 }

 }

 // If possible

 if (max_freq <= (str.length - max_freq + 1))

 return true;

 return false;

 }

 // Driver code

 public static void main(String[] args)

 {

 String str = "geeksforgeeks";

 if (isPossible(str.toCharArray()))

 System.out.println("Yes");

 else

 System.out.println("No");

 }

}

// This code is contributed by Rajput-Ji  
  
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

# Function that returns true if it is possible

# to rearrange the characters of the String

# such that no two consecutive characters are same

def isPossible(Str):

 # To store the frequency of

 # each of the character

 freq = dict()

 # To store the maximum frequency so far

 max_freq = 0

 for j in range(len(Str)):

 freq[Str[j]] = freq.get(Str[j], 0) + 1

 if (freq[Str[j]] > max_freq):

 max_freq = freq[Str[j]]

 # If possible

 if (max_freq <= (len(Str) - max_freq + 1)):

 return True

 return False

# Driver code

Str = "geeksforgeeks"

if (isPossible(Str)):

 print("Yes")

else:

 print("No")

# This code is contributed by Mohit Kumar  
  
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

using System.Collections.Generic;

class GFG {

 // Function that returns true if it is possible

 // to rearrange the characters of the string

 // such that no two consecutive characters are same

 static Boolean isPossible(char[] str)

 {

 // To store the frequency of

 // each of the character

 Dictionary<char, int> freq = new Dictionary<char,
int>();

 // To store the maximum frequency so far

 int max_freq = 0;

 for (int j = 0; j < (str.Length); j++) {

 if (freq.ContainsKey(str[j])) {

 var v = freq[str[j]] + 1;

 freq.Remove(str[j]);

 freq.Add(str[j], v);

 if (freq[str[j]] > max_freq)

 max_freq = freq[str[j]];

 }

 else {

 freq.Add(str[j], 1);

 if (freq[str[j]] > max_freq)

 max_freq = freq[str[j]];

 }

 }

 // If possible

 if (max_freq <= (str.Length - max_freq + 1))

 return true;

 return false;

 }

 // Driver code

 public static void Main(String[] args)

 {

 String str = "geeksforgeeks";

 if (isPossible(str.ToCharArray()))

 Console.WriteLine("Yes");

 else

 Console.WriteLine("No");

 }

}

// This code is contributed by Princi Singh  
  
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

