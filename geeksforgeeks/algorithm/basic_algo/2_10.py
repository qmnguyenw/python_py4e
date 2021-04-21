Check whether two strings are equivalent or not according to given condition



Given two strings **A** and **B** of equal size. Two strings are equivalent
either of the following conditions hold true:  
1) They both are equal. Or,  
2) If we divide the string A into two contiguous substrings of same size A1
and A2 and string B into two contiguous substrings of same size B1 and B2,
then one of the following should be correct:

  * A1 is recursively equivalent to B1 and A2 is recursively equivalent to B2
  * A1 is recursively equivalent to B2 and A2 is recursively equivalent to B1

Check whether given strings are equivalent or not. Print YES or NO.

 **Examples:**

>  **Input :** A = “aaba”, B = “abaa”  
>  **Output :** YES  
>  **Explanation :** Since condition 1 doesn’t hold true, we can divide string
> A into “aaba” = “aa” + “ba” and string B into “abaa” = “ab” + “aa”. Here,
> 2nd subcondition holds true where A1 is equal to B2 and A2 is recursively
> equal to B1
>
>  **Input :** A = “aabb”, B = “abab”  
>  **Output :** NO
>
>  
>
>
>  
>

 **Naive Solution :** A simple solution is to consider all possible scenarios.
Check first if the both strings are equal return “YES”, otherwise divide the
strings and check if **A 1 = B1** and **A 2 = B2** or **A 1 = B2** and **A 2 =
B1** by using four recursive calls. Complexity of this solution would be
O(n2), where n is the size of the string.

 **Efficient Solution :** Let’s define following operation on string S. We can
divide it into two halves and if we want we can swap them. And also, we can
recursively apply this operation to both of its halves. By careful
observation, we can see that if after applying the operation on some string A,
we can obtain B, then after applying the operation on B we can obtain A. And
for the given two strings, we can recursively find the least lexicographically
string that can be obtained from them. Those obtained strings if are equal,
answer is YES, otherwise NO. For example, least lexicographically string for
“aaba” is “aaab”. And least lexicographically string for “abaa” is also
“aaab”. Hence both of these are equivalent.

Below is the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP Program to find whether two strings

// are equivalent or not according to given

// condition

#include <bits/stdc++.h>

using namespace std;

 

// This function returns the least lexicogr

// aphical string obtained from its two halves

string leastLexiString(string s)

{

 // Base Case - If string size is 1

 if (s.size() & 1)

 return s;

 

 // Divide the string into its two halves

 string x = leastLexiString(s.substr(0,

 s.size() / 2));

 string y = leastLexiString(s.substr(s.size() / 2));

 

 // Form least lexicographical string

 return min(x + y, y + x);

}

 

bool areEquivalent(string a, string b)

{

 return (leastLexiString(a) == leastLexiString(b));

} 

 

// Driver Code

int main()

{

 string a = "aaba";

 string b = "abaa";

 if (areEquivalent(a, b))

 cout << "YES" << endl;

 else

 cout << "NO" << endl;

 

 a = "aabb";

 b = "abab";

 if (areEquivalent(a, b))

 cout << "YES" << endl;

 else

 cout << "NO" << endl;

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

// Java Program to find whether two strings

// are equivalent or not according to given

// condition

class GfG 

{

 

// This function returns the least lexicogr

// aphical String obtained from its two halves

static String leastLexiString(String s)

{

 // Base Case - If String size is 1

 if (s.length() == 1)

 return s;

 

 // Divide the String into its two halves

 String x = leastLexiString(s.substring(0,

 s.length() / 2));

 String y = leastLexiString(s.substring(s.length() / 2));

 

 // Form least lexicographical String

 return String.valueOf((x + y).compareTo(y + x));

}

 

static boolean areEquivalent(String a, String b)

{

 return !(leastLexiString(a).equals(leastLexiString(b)));

} 

 

// Driver Code

public static void main(String[] args) 

{

 String a = "aaba";

 String b = "abaa";

 if (areEquivalent(a, b))

 System.out.println("Yes");

 else

 System.out.println("No");

 

 a = "aabb";

 b = "abab";

 if (areEquivalent(a, b))

 System.out.println("Yes");

 else

 System.out.println("No");

 }

}

 

/* This code contributed by PrinciRaj1992 */  
  
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

# Python 3 Program to find whether two strings

# are equivalent or not according to given

# condition

 

# This function returns the least lexicogr

# aphical string obtained from its two halves

def leastLexiString(s):

 

 # Base Case - If string size is 1

 if (len(s) & 1 != 0):

 return s

 

 # Divide the string into its two halves

 x = leastLexiString(s[0:int(len(s) / 2)])

 y = leastLexiString(s[int(len(s) / 2):len(s)])

 

 # Form least lexicographical string

 return min(x + y, y + x)

 

def areEquivalent(a,b):

 return (leastLexiString(a) == leastLexiString(b))

 

# Driver Code

if __name__ == '__main__':

 a = "aaba"

 b = "abaa"

 if (areEquivalent(a, b)):

 print("YES")

 else:

 print("NO")

 

 a = "aabb"

 b = "abab"

 if (areEquivalent(a, b)):

 print("YES")

 else:

 print("NO")

 

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

// C# Program to find whether two strings

// are equivalent or not according to given 

// condition 

using System;

class GFG 

{ 

 

// This function returns the least lexicogr- 

// aphical String obtained from its two halves 

static String leastLexiString(String s) 

{ 

 // Base Case - If String size is 1 

 if (s.Length == 1) 

 return s; 

 

 // Divide the String into its two halves 

 String x = leastLexiString(s.Substring(0, 

 s.Length / 2)); 

 String y = leastLexiString(s.Substring(

 s.Length / 2)); 

 

 // Form least lexicographical String 

 return ((x + y).CompareTo(y + x).ToString()); 

} 

 

static Boolean areEquivalent(String a, String b) 

{ 

 return !(leastLexiString(a).Equals(

 leastLexiString(b))); 

} 

 

// Driver Code 

public static void Main(String[] args) 

{ 

 String a = "aaba"; 

 String b = "abaa"; 

 if (areEquivalent(a, b)) 

 Console.WriteLine("YES"); 

 else

 Console.WriteLine("NO"); 

 

 a = "aabb"; 

 b = "abab"; 

 if (areEquivalent(a, b)) 

 Console.WriteLine("YES"); 

 else

 Console.WriteLine("NO"); 

} 

} 

 

// This code is contributed by PrinciRaj1992   
  
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

// PHP Program to find whether two strings 

// are equivalent or not according to given 

// condition 

 

// This function returns the least lexicogr 

// aphical string obtained from its two halves 

function leastLexiString($s) 

{ 

 // Base Case - If string size is 1 

 if (strlen($s) & 1) 

 return $s; 

 

 // Divide the string into its two halves 

 $x = leastLexiString(substr($s, 0,floor(strlen($s) /
2))); 

 $y = leastLexiString(substr($s,floor(strlen($s) /
2),strlen($s))); 

 

 // Form least lexicographical string 

 return min($x.$y, $y.$x); 

} 

 

function areEquivalent($a, $b) 

{ 

 return (leastLexiString($a) == leastLexiString($b)); 

} 

 

 // Driver Code 

 $a = "aaba"; 

 $b = "abaa"; 

 if (areEquivalent($a, $b)) 

 echo "YES", "\n"; 

 else

 echo "NO", "\n"; 

 

 $a = "aabb"; 

 $b = "abab"; 

 if (areEquivalent($a, $b)) 

 echo "YES", "\n"; 

 else

 echo "NO","\n"; 

 

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    YES
    NO
    

**Time Complexity :** O(n), where n is the size of the string.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

