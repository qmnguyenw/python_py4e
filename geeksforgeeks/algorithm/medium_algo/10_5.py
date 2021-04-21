Count distinct substrings that contain some characters at most k times



Given a integer **k** and a sting **str** , the task is to count the number of
**distinct** sub-strings such that each sub-string does not contain some
specific characters more than **k** times. The specific characters are given
as another string.

 **Examples:**

>  **Input:** str = “ababab”, anotherStr = “bcd”, k = 1  
>  **Output:** 5  
> All valid sub-strings are “a”, “b”, “ab”, “ba” and “aba”
>
>  **Input:** str = “acbacbacaa”, anotherStr = “ycb”, k = 2  
>  **Output:** 8

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

  * Store characters of anotherStr in a boolean array of size 256 for quick lookip
  * Traverse through all substrings of given string. For every substring, keep the count of **illegal** characters in **anotherStr**.
  * If the **count** of these characters exceeds the value of **k** then break out of the inner loop.
  * Else, store this sub-string in an hash table to keep distinct substrings.

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

 

const int MAX_CHAR = 256;

 

// Function to return the count of valid sub-strings

int countSubStrings(string s, string anotherStr, int k)

{

 // Store all characters of anotherStr in a 

 // direct index table for quick lookup.

 bool illegal[MAX_CHAR] = { false };

 for (int i = 0; i < anotherStr.size(); i++)

 illegal[anotherStr[i]] = true;

 

 // To store distinct output substrings

 unordered_set<string> us;

 

 // Traverse through the given string and

 // one by one generate substrings beginning

 // from s[i].

 for (int i = 0; i < s.size(); ++i) {

 

 // One by one generate substrings ending

 // with s[j]

 string ss = "";

 int count = 0;

 for (int j = i; j < s.size(); ++j) {

 

 // If character is illegal

 if (illegal[s[j]])

 ++count;

 ss = ss + s[j];

 

 // If current substring is valid

 if (count <= k) {

 us.insert(ss);

 }

 

 // If current substring is invalid,

 // adding more characters would not

 // help.

 else

 break;

 }

 }

 

 // Return the count of distinct sub-strings

 return us.size();

}

 

// Driver code

int main()

{

 string str = "acbacbacaa";

 string anotherStr = "abcdefghijklmnopqrstuvwxyz";

 int k = 2;

 cout << countSubStrings(str, anotherStr, k);

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

 

 static int MAX_CHAR = 256;

 

 // Function to return the count of valid sub-strings

 static int countSubStrings(String s, String anotherStr, int k) 

 {

 // Store all characters of anotherStr in a 

 // direct index table for quick lookup.

 boolean illegal[] = new boolean[MAX_CHAR];

 for (int i = 0; i < anotherStr.length(); i++) 

 {

 illegal[anotherStr.charAt(i)] = true;

 }

 

 // To store distinct output substrings

 HashSet<String> us = new HashSet<String>();

 

 // Traverse through the given string and

 // one by one generate substrings beginning

 // from s[i].

 for (int i = 0; i < s.length(); ++i) 

 {

 

 // One by one generate substrings ending

 // with s[j]

 String ss = "";

 int count = 0;

 for (int j = i; j < s.length(); ++j) 

 {

 

 // If character is illegal

 if (illegal[s.charAt(j)])

 {

 ++count;

 }

 ss = ss + s.charAt(j);

 

 // If current substring is valid

 if (count <= k) 

 {

 us.add(ss);

 } 

 

 // If current substring is invalid,

 // adding more characters would not

 // help.

 else

 {

 break;

 }

 }

 }

 

 // Return the count of distinct sub-strings

 return us.size();

 }

 

 // Driver code

 public static void main(String[] args) 

 {

 String str = "acbacbacaa";

 String anotherStr = "abcdefghijklmnopqrstuvwxyz";

 int k = 2;

 System.out.println(countSubStrings(str, anotherStr, k));

 }

}

 

// This code is contributed by PrinciRaj1992  
  
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

 

MAX_CHAR = 256

 

# Function to return the count

# of valid sub-strings 

def countSubStrings(s, anotherStr, k) :

 

 # Store all characters of anotherStr in

 # a direct index table for quick lookup. 

 illegal = [False] * MAX_CHAR

 

 for i in range(len(anotherStr)) :

 illegal[ord(anotherStr[i])] = True

 

 # To store distinct output substrings 

 us = set() 

 

 # Traverse through the given string 

 # and one by one generate substrings 

 # beginning from s[i]. 

 for i in range(len(s)) :

 

 # One by one generate substrings 

 # ending with s[j] 

 ss = "" 

 

 count = 0

 for j in range(i, len(s)) :

 

 # If character is illegal

 if (illegal[ord(s[j])]) :

 count += 1

 ss = ss + s[j]

 

 # If current substring is valid

 if (count <= k) :

 us.add(ss)

 

 # If current substring is invalid,

 # adding more characters would not

 # help.

 else :

 break

 

 # Return the count of distinct

 # sub-strings 

 return len(us)

 

# Driver code 

if __name__ == "__main__" : 

 

 string = "acbacbacaa"

 anotherStr = "abcdefghijklmnopqrstuvwxyz"

 k = 2

 print(countSubStrings(string, 

 anotherStr, k))

 

# This code is contributed by Ryuga  
  
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

 

class GFG

{

 static int MAX_CHAR = 256;

 

 // Function to return the count 

 // of valid sub-strings

 static int countSubStrings(String s, 

 String anotherStr, int k) 

 {

 

 // Store all characters of anotherStr in a 

 // direct index table for quick lookup.

 bool []illegal = new bool[MAX_CHAR];

 for (int i = 0; i < anotherStr.Length; i++) 

 {

 illegal[anotherStr[i]] = true;

 }

 

 // To store distinct output substrings

 HashSet<String> us = new HashSet<String>();

 

 // Traverse through the given 

 // string and one by one generate 

 // substrings beginning from s[i].

 for (int i = 0; i < s.Length; ++i) 

 {

 

 // One by one generate substrings 

 // ending with s[j]

 String ss = "";

 int count = 0;

 for (int j = i; j < s.Length; ++j) 

 {

 

 // If character is illegal

 if (illegal[s[j]])

 {

 ++count;

 }

 ss = ss + s[j];

 

 // If current substring is valid

 if (count <= k) 

 {

 us.Add(ss);

 } 

 

 // If current substring is invalid,

 // adding more characters would not

 // help.

 else

 {

 break;

 }

 }

 }

 

 // Return the count of distinct sub-strings

 return us.Count;

 }

 

 // Driver code

 public static void Main() 

 {

 String str = "acbacbacaa";

 String anotherStr = "abcdefghijklmnopqrstuvwxyz";

 int k = 2;

 Console.WriteLine(countSubStrings(str, anotherStr, k));

 }

}

 

//This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    8
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

