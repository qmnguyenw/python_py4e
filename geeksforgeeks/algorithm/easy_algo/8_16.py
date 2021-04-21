Number of flips to make binary string alternate | Set 1



Given a binary string, that is it contains only 0s and 1s. We need to make
this string a sequence of alternate characters by flipping some of the bits,
our goal is to minimize the number of bits to be flipped.  
**Examples :**  

    
    
    Input : str = “001”
    Output : 1
    Minimum number of flips required = 1
    We can flip 1st bit from 0 to 1 
    
    Input : str = “0001010111”
    Output : 2
    Minimum number of flips required = 2
    We can flip 2nd bit from 0 to 1 and 9th 
    bit from 1 to 0 to make alternate 
    string “0101010101”.

Expected time complexity : O(n) where n is length of input string.  

Recommended: Please solve it on “ _ ** _PRACTICE_**_ ” first, before moving on
to the solution.

We can solve this problem by considering all possible results, As we are
supposed to get alternate string, there are only 2 possibilities, alternate
string starting with 0 and alternate string starting with 1. We will try both
cases and choose the string which will require minimum number of flips as our
final answer.  
Trying a case requires O(n) time in which we will loop over all characters of
given string, if current character is expected character according to
alternation then we will do nothing otherwise we will increase flip count by
1. After trying strings starting with 0 and starting with 1, we will choose
the string with minimum flip count.  
Total time complexity of solution will be O(n)  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C/C++ program to find minimum number of

// flip to make binary string alternate

#include <bits/stdc++.h>

using namespace std;

// Utility method to flip a character

char flip(char ch)

{

 return (ch == '0') ? '1' : '0';

}

// Utility method to get minimum flips when

// alternate string starts with expected char

int getFlipWithStartingCharcter(string str,

 char expected)

{

 int flipCount = 0;

 for (int i = 0; i < str.length(); i++)

 {

 // if current character is not expected,

 // increase flip count

 if (str[i] != expected)

 flipCount++;

 // flip expected character each time

 expected = flip(expected);

 }

 return flipCount;

}

// method return minimum flip to make binary

// string alternate

int minFlipToMakeStringAlternate(string str)

{

 // return minimum of following two

 // 1) flips when alternate strign starts with 0

 // 2) flips when alternate strign starts with 1

 return min(getFlipWithStartingCharcter(str, '0'),

 getFlipWithStartingCharcter(str, '1'));

}

// Driver code to test above method

int main()

{

 string str = "0001010111";

 cout << minFlipToMakeStringAlternate(str);

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

// Java program to find minimum number of

// flip to make binary string alternate

class GFG

{

 // Utility method to flip a character

 public static char flip(char ch)

 {

 return (ch == '0') ? '1' : '0';

 }

 

 // Utility method to get minimum flips when

 // alternate string starts with expected char

 public static int getFlipWithStartingCharcter(String str,

 char expected)

 {

 int flipCount = 0;

 for (int i = 0; i < str.length(); i++)

 {

 // if current character is not expected,

 // increase flip count

 if (str.charAt(i) != expected)

 flipCount++;

 

 // flip expected character each time

 expected = flip(expected);

 }

 return flipCount;

 }

 

 // method return minimum flip to make binary

 // string alternate

 public static int minFlipToMakeStringAlternate(String str)

 {

 // return minimum of following two

 // 1) flips when alternate string starts with 0

 // 2) flips when alternate string starts with 1

 return Math.min(getFlipWithStartingCharcter(str, '0'),

 getFlipWithStartingCharcter(str, '1'));

 }

 

 // Driver code to test above method

 public static void main(String args[])

 {

 String str = "0001010111";

 System.out.println(minFlipToMakeStringAlternate(str));

 }

}

// This code is contributed by Sumit Ghosh  
  
---  
  
 __

 __

## Python 3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 program to find minimum number of

# flip to make binary string alternate

# Utility method to flip a character

def flip( ch):

 return '1' if (ch == '0') else '0'

# Utility method to get minimum flips when

# alternate string starts with expected char

def getFlipWithStartingCharcter(str, expected):

 flipCount = 0

 for i in range(len( str)):

 

 # if current character is not expected,

 # increase flip count

 if (str[i] != expected):

 flipCount += 1

 # flip expected character each time

 expected = flip(expected)

 return flipCount

# method return minimum flip to make binary

# string alternate

def minFlipToMakeStringAlternate(str):

 # return minimum of following two

 # 1) flips when alternate strign starts with 0

 # 2) flips when alternate strign starts with 1

 return min(getFlipWithStartingCharcter(str, '0'),

 getFlipWithStartingCharcter(str, '1'))

# Driver code to test above method

if __name__ == "__main__":

 

 str = "0001010111"

 print(minFlipToMakeStringAlternate(str))  
  
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

// C# program to find minimum number of

// flip to make binary string alternate

using System;

class GFG

{

 // Utility method to

 // flip a character

 public static char flip(char ch)

 {

 return (ch == '0') ? '1' : '0';

 }

 

 // Utility method to get minimum flips

 // when alternate string starts with

 // expected char

 public static int getFlipWithStartingCharcter(String str,

 char expected)

 {

 int flipCount = 0;

 for (int i = 0; i < str.Length; i++)

 {

 // if current character is not

 // expected, increase flip count

 if (str[i] != expected)

 flipCount++;

 

 // flip expected character each time

 expected = flip(expected);

 }

 return flipCount;

 }

 

 // method return minimum flip to

 // make binary string alternate

 public static int minFlipToMakeStringAlternate(string str)

 {

 // return minimum of following two

 // 1) flips when alternate string starts with 0

 // 2) flips when alternate string starts with 1

 return Math.Min(getFlipWithStartingCharcter(str, '0'),

 getFlipWithStartingCharcter(str, '1'));

 }

 

 // Driver Code

 public static void Main()

 {

 string str = "0001010111";

 Console.Write(minFlipToMakeStringAlternate(str));

 }

}

// This code is contributed by nitin mittal.  
  
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

// PHP program to find minimum number of

// flip to make binary string alternate

// Utility method to flip a character

function flip( $ch)

{

 return ($ch == '0') ? '1' : '0';

}

// Utility method to get minimum flips when

// alternate string starts with expected char

function getFlipWithStartingCharcter($str,

 $expected)

{

 

 $flipCount = 0;

 for ($i = 0; $i < strlen($str); $i++)

 {

 

 // if current character is not expected,

 // increase flip count

 if ($str[$i] != $expected)

 $flipCount++;

 // flip expected character each time

 $expected = flip($expected);

 }

 return $flipCount;

}

// method return minimum flip to make binary

// string alternate

function minFlipToMakeStringAlternate( $str)

{

 

 // return minimum of following two

 // 1) flips when alternate strign starts with 0

 // 2) flips when alternate strign starts with 1

 return min(getFlipWithStartingCharcter($str, '0'),

 getFlipWithStartingCharcter($str, '1'));

}

// Driver code to test above method

$str = "0001010111";

echo minFlipToMakeStringAlternate($str);

// This code is contributed by anuj_67.

?>  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// Javascript program to find minimum number of

// flip to make binary string alternate

 

 // Utility method to flip a character

 function flip(ch)

 {

 return (ch == '0') ? '1' : '0';

 }

 

 // Utility method to get minimum flips when

 // alternate string starts with expected char

 function getFlipWithStartingCharcter(str,expected)

 {

 let flipCount = 0;

 for (let i = 0; i < str.length; i++)

 {

 // if current character is not expected,

 // increase flip count

 if (str.charAt(i) != expected)

 flipCount++;

 

 // flip expected character each time

 expected = flip(expected);

 }

 return flipCount;

 }

 

 // method return minimum flip to make binary

 // string alternate

 function minFlipToMakeStringAlternate(str)

 {

 // return minimum of following two

 // 1) flips when alternate string starts with 0

 // 2) flips when alternate string starts with 1

 return Math.min(getFlipWithStartingCharcter(str, '0'),

 getFlipWithStartingCharcter(str, '1'));

 }

 

 // Driver code to test above method

 let str = "0001010111";

 document.write(minFlipToMakeStringAlternate(str));

 

 // This code is contributed by avanitrachhadiya2155

 

</script>  
  
---  
  
 __

 __

 **Output :**

    
    
    2

 **Minimum number of replacements to make the binary string alternating | Set
2**  

  

  

This article is contributed by **Utkarsh Trivedi**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.  
Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

