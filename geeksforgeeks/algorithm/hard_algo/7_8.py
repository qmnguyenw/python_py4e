Sub-strings of a string that are prefix of the same string



Given a string **str** , the task is to count all possible sub-strings of the
given string that are prefix of the same string.  
 **Examples:**

> **Input:** str = “ababc”  
> **Output:** 7  
> All possible sub-string are “a”, “ab”, “aba”, “abab”, “ababc”, “a” and “ab”  
>  **Input:** str = “abdabc”  
> **Output:** 8

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:** Traverse the string character by character, if the current
character is equal to the first character of the string then count all
possible sub-strings starting from here that are also the prefixes of **str**
and add it to **count**. After the complete string has been traversed, print
the **count**.  
Below is the implementation of the above approach:

## C++14

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <iostream>

#include <string>

using namespace std;

 

// Function to return the 

// count of sub-strings starting

// from startIndex that are 

// also the prefixes of str

int subStringsStartingHere(string str, int n,

 int startIndex)

{

 int count = 0, i = 1;

 while (i <= n)

 {

 if (str.substr(0,i) == 

 str.substr(startIndex, i))

 {

 count++;

 }

 else

 break;

 i++;

 }

 

 return count;

}

 

 

// Function to return the 

// count of all possible sub-strings

// of str that are also the prefixes of str

int countSubStrings(string str, int n)

{

 int count = 0;

 for (int i = 0; i < n; i++)

 {

 

 // If current character is equal to 

 // the starting character of str

 if (str[i] == str[0])

 count += subStringsStartingHere(str, 

 n, i);

 }

 return count;

}

 

// Driver code

int main() 

{

 string str = "abcda";

 int n = str.length();

 

 // Function Call

 cout << (countSubStrings(str, n));

}

 

// This code is contributed by harshvijeta0  
  
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

public class GFG 

{

 

 // Function to return 

 // the count of sub-strings starting

 // from startIndex that 

 // are also the prefixes of str

 public static int subStringsStartingHere(

 String str, int n,

 int startIndex)

 {

 int count = 0, i = startIndex + 1;

 while (i <= n) 

 {

 if (str.startsWith(str.substring(

 startIndex, i))) 

 {

 count++;

 }

 else

 break;

 i++;

 }

 return count;

 }

 

 // Function to return the 

 // count of all possible sub-strings

 // of str that are also the prefixes of str

 public static int countSubStrings(String str, 

 int n)

 {

 int count = 0;

 

 for (int i = 0; i < n; i++) 

 {

 

 // If current character is equal to 

 // the starting character of str

 if (str.charAt(i) == str.charAt(0))

 count += subStringsStartingHere(str, n, i);

 }

 

 return count;

 }

 

 // Driver code

 public static void main(String[] args)

 {

 String str = "ababc";

 int n = str.length();

 System.out.println(countSubStrings(str, n));

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

 

# Function to return the 

# count of sub-strings starting 

# from startIndex that are 

# also the prefixes of string 

def subStringsStartingHere(string, n, 

 startIndex):

 count = 0

 i = startIndex + 1

 

 while(i <= n) :

 if string.startswith(

 string[startIndex : i]):

 count += 1

 else :

 break

 

 i += 1

 

 return count

 

# Function to return the 

# count of all possible sub-strings 

# of string that are also 

# the prefixes of string 

def countSubStrings(string, n) :

 count = 0

 

 for i in range(n) :

 

 # If current character is equal to 

 # the starting character of str 

 if string[i] == string[0] :

 count += subStringsStartingHere(

 string, n, i)

 

 return count

 

 

# Driver Code

if __name__ == "__main__" :

 

 string = "ababc"

 n = len(string)

 print(countSubStrings(string, n))

 

# this code is contributed by Ryuga  
  
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

 // count of sub-strings starting

 // from startIndex that 

 // are also the prefixes of str

 static int subStringsStartingHere(

 String str, int n,

 int startIndex)

 {

 int count = 0, i = startIndex + 1;

 while (i <= n) {

 if (str.StartsWith(str.Substring(

 startIndex, i-startIndex))) 

 {

 count++;

 }

 else

 break;

 i++;

 }

 

 return count;

 }

 

 // Function to return the 

 // count of all possible sub-strings

 // of str that are also the prefixes of str

 static int countSubStrings(String str, int n)

 {

 int count = 0;

 

 for (int i = 0; i < n; i++) {

 

 // If current character is equal to 

 // the starting character of str

 if (str[i] == str[0])

 count += subStringsStartingHere(

 str, n, i);

 }

 

 return count;

 }

 

 // Driver code

 static public void Main(String []args)

 {

 String str = "ababc";

 int n = str.Length;

 Console.WriteLine(countSubStrings(str, n));

 }

}

//contributed by Arnab Kundu  
  
---  
  
 __

 __

 **Output**

    
    
    6

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

