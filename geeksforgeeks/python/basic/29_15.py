Count words in a given string



Given a string, count number of words in it. The words are separated by
following characters: space (‘ ‘) or new line (‘\n’) or tab (‘\t’) or a
combination of these.  

Recommended: Please solve it on “ _ ** _PRACTICE_**_ ” first, before moving on
to the solution.  

There can be many solutions to this problem. Following is a simple and
interesting solution.  
The idea is to maintain two states: IN and OUT. The state OUT indicates that a
separator is seen. State IN indicates that a word character is seen. We
increment word count when previous state is OUT and next character is a word
character.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

/* C++ program to count no of words

from given input string. */

#include <bits/stdc++.h>

using namespace std;

#define OUT 0

#define IN 1

// returns number of words in str

unsigned countWords(char *str)

{

 int state = OUT;

 unsigned wc = 0; // word count

 // Scan all characters one by one

 while (*str)

 {

 // If next character is a separator, set the

 // state as OUT

 if (*str == ' ' || *str == '\n' || *str == '\t')

 state = OUT;

 // If next character is not a word separator and

 // state is OUT, then set the state as IN and

 // increment word count

 else if (state == OUT)

 {

 state = IN;

 ++wc;

 }

 // Move to next character

 ++str;

 }

 return wc;

}

// Driver code

int main(void)

{

 char str[] = "One two three\n four\tfive ";

 cout<<"No of words : "<<countWords(str);

 return 0;

}

// This is code is contributed by rathbhupendra  
  
---  
  
 __

 __

## C

 __

 __  
 __

 __

 __  
 __  
 __

/* C program to count no of words from given input string. */

#include <stdio.h>

#define OUT 0

#define IN 1

// returns number of words in str

unsigned countWords(char *str)

{

 int state = OUT;

 unsigned wc = 0; // word count

 // Scan all characters one by one

 while (*str)

 {

 // If next character is a separator, set the

 // state as OUT

 if (*str == ' ' || *str == '\n' || *str == '\t')

 state = OUT;

 // If next character is not a word separator and

 // state is OUT, then set the state as IN and

 // increment word count

 else if (state == OUT)

 {

 state = IN;

 ++wc;

 }

 // Move to next character

 ++str;

 }

 return wc;

}

// Driver program to tes above functions

int main(void)

{

 char str[] = "One two three\n four\tfive ";

 printf("No of words : %u", countWords(str));

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

/* Java program to count no of words

from given input string. */

public class GFG {

 

 static final int OUT = 0;

 static final int IN = 1;

 

 // returns number of words in str

 static int countWords(String str)

 {

 int state = OUT;

 int wc = 0; // word count

 int i = 0;

 

 // Scan all characters one by one

 while (i < str.length())

 {

 // If next character is a separator, set the

 // state as OUT

 if (str.charAt(i) == ' ' || str.charAt(i) == '\n'

 || str.charAt(i) == '\t')

 state = OUT;

 

 

 // If next character is not a word separator

 // and state is OUT, then set the state as IN

 // and increment word count

 else if (state == OUT)

 {

 state = IN;

 ++wc;

 }

 

 // Move to next character

 ++i;

 }

 return wc;

 }

 

 // Driver program to test above functions

 public static void main(String args[])

 {

 String str = "One two three\n four\tfive ";

 System.out.println("No of words : " + countWords(str));

 }

}

// This code is contributed by Sumit Ghosh  
  
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

# Python3 program to count words

# in a given string

OUT = 0

IN = 1

# Returns number of words in string

def countWords(string):

 state = OUT

 wc = 0

 # Scan all characters one by one

 for i in range(len(string)):

 # If next character is a separator,

 # set the state as OUT

 if (string[i] == ' ' or string[i] == '\n' or

 string[i] == '\t'):

 state = OUT

 # If next character is not a word

 # separator and state is OUT, then

 # set the state as IN and increment

 # word count

 elif state == OUT:

 state = IN

 wc += 1

 # Return the number of words

 return wc

# Driver Code

string = "One two three\n four\tfive "

print("No. of words : " + str(countWords(string)))

# This code is contributed by BHAVYA JAIN  
  
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

// C# program to count no of words

// from given input string.

using System;

class GFG {

 

 static int OUT = 0;

 static int IN = 1;

 

 // returns number of words in str

 static int countWords(String str)

 {

 int state = OUT;

 int wc = 0; // word count

 int i = 0;

 

 // Scan all characters one

 // by one

 while (i < str.Length)

 {

 // If next character is a separator,

 // set the state as OUT

 if (str[i] == ' ' || str[i] == '\n'||

 str[i] == '\t')

 state = OUT;

 

 

 // If next character is not a word

 // separator and state is OUT, then

 // set the state as IN and increment

 // word count

 else if (state == OUT)

 {

 state = IN;

 ++wc;

 }

 

 // Move to next character

 ++i;

 }

 

 return wc;

 }

 

 // Driver program to test above functions

 public static void Main()

 {

 String str = "One two three\n four\tfive ";

 Console.WriteLine("No of words : "

 + countWords(str));

 }

}

// This code is contributed by Sam007.  
  
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

// PHP program to count no of

// words from given input string

$OUT = 0;

$IN = 1;

// returns number of words in str

function countWords($str)

{

 global $OUT, $IN;

 $state = $OUT;

 $wc = 0; // word count

 $i = 0;

 

 // Scan all characters one by one

 while ($i < strlen($str))

 {

 // If next character is

 // a separator, set the

 // state as OUT

 if ($str[$i] == " " ||

 $str[$i] == "\n" ||

 $str[$i] == "\t")

 $state = $OUT;

 // If next character is not a

 // word separator and state is

 // OUT, then set the state as

 // IN and increment word count

 else if ($state == $OUT)

 {

 $state = $IN;

 ++$wc;

 }

 // Move to next character

 ++$i;

 }

 return $wc;

}

// Driver Code

$str = "One two three\n four\tfive ";

echo "No of words : " . countWords($str);

// This code is contributed

// by ChitraNayal

?>  
  
---  
  
 __

 __

 **Output**

    
    
    No of words : 5

 **Time complexity:** O(n)  
This article is compiled by **Narendra Kangralkar**. Please write comments if
you find anything incorrect, or you want to share more information about the
topic discussed above.  

**Method 2: using** **String.split()** **method**

  

  

  1. Get the string to count the total number of words.
  2. Check if the string is empty or null then return 0.
  3. Use split() method of String class to split the string on whitespaces.
  4. The split() method breaks the given string around matches of the given regular expression and returns an array of string.
  5. The length of the array is the number of words in the given string.
  6. Now, print the result.

Below is the implementation of the above approach:

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java program to count total

// number of words in the string

class GFG

{

 

 // Function to count total number

 // of words in the string

 public static int

 countWords(String str)

 {

 

 // Check if the string is null

 // or empty then return zero

 if (str == null || str.isEmpty())

 return 0;

 

 // Splitting the string around

 // matches of the given regular

 // expression

 String[] words = str.split("\\s+");

 

 // Return number of words

 // in the given string

 return words.length;

 }

 

 // Driver Code

 public static void main(String args[])

 {

 

 // Given String str

 String str =

 "One two three\n four\tfive ";

 

 // Print the result

 System.out.println("No of words : " +

 countWords(str));

 }

}

// This code is contributed by Prashant Srivastava  
  
---  
  
 __

 __

  

**Output**

    
    
    No of words : 5

**Time Complexity:** O(N)

**Method 3: using** **StringTokenizer.countTokens()** **method**

  

  

  1. Get the string to count the total number of words.
  2. Check if the string is empty or null then return 0.
  3. Create a StringTokenizer with the given string passed as a parameter.
  4. Count the total number of words in the given string using the countTokens() method.
  5. Now, print the result.

Below is the implementation of the above approach:

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java program to count total

// number of words in the string

import java.util.StringTokenizer;

class GFG

{

 

 // Function to count total number

 // of words in the string

 public static int

 countWords(String str)

 {

 

 // Check if the string is null

 // or empty then return zero

 if (str == null || str.isEmpty())

 return 0;

 

 // Create a StringTokenizer with the

 // given string passed as a parameter

 StringTokenizer tokens = new

 StringTokenizer(str);

 

 // Return the number of words

 // in the given string using

 // countTokens() method

 return tokens.countTokens();

 }

 

 // Driver Code

 public static void main(String args[])

 {

 

 // Given String str

 String str =

 "One two three\n four\tfive ";

 

 // Print the result

 System.out.println("No of words: " +

 countWords(str));

 }

}

// This code is contributed by Prashant Srivastava  
  
---  
  
 __

 __

  

**Output**

    
    
    No of words: 5

**Time Complexity:** O(N)

**Method 4: using Character.isLetter() method**

  1. Get the string to count the total number of words.
  2. Check if the string is empty or null then return 0.
  3. Converting the given string into a character array.
  4. Check if the character is a letter and index of the character array doesn’t equal to the end of the line that means, it is a word and set _isWord_ by true.
  5. Check if the character is not a letter that means there is a space, then we increment the _wordCount_ by one and set the _isWord_ by false.
  6. Check for the last word of the sentence and increment the _wordCount_ by one.
  7. Now, print the result.

Below is the implementation of the above approach:

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java program to count total

// number of words in the string

class GFG

{

 

 // Function to count total number

 // of words in the string

 public static int

 countWords(String str)

 {

 

 // Check if the string is null

 // or empty then return zero

 if(str == null || str.isEmpty())

 return 0;

 

 int wordCount = 0;

 

 boolean isWord = false;

 int endOfLine = str.length() - 1;

 

 // Converting the given string

 // into a character array

 char[] ch = str.toCharArray();

 

 for (int i = 0; i < ch.length; i++) {

 

 // Check if the character is a letter

 // and index of character array doesn't

 // equal to end of line that means, it is

 // a word and set isWord by true

 if (Character.isLetter(ch[i])

 && i != endOfLine)

 

 isWord = true;

 

 // Check if the character is not a letter

 // that means there is a space, then we

 // increment the wordCount by one and set

 // the isWord by false

 else if (!Character.isLetter(ch[i])

 && isWord) {

 

 wordCount++;

 isWord = false;

 }

 

 // Check for the last word of the

 // sentence and increment the wordCount

 // by one

 else if (Character.isLetter(ch[i])

 && i == endOfLine)

 wordCount++;

 }

 

 // Return the total number of

 // words in the string

 return wordCount;

 

 }

 

 // Driver Code

 public static void main(String args[])

 {

 

 // Given String str

 String str =

 "One two three\n four\tfive ";

 

 // Print the result

 System.out.println("No of words : " +

 countWords(str));

 }

}

// This code is contributed by Prashant Srivastava  
  
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

# Python program to count total

# number of words in the string

# Function to count total number

# of words in the string

def countWords(Str):

 

 # Check if the string is null

 # or empty then return zero

 if(Str == None or len(Str) == 0):

 return 0

 

 wordCount = 0

 isWord = False

 endOfLine = len(Str) - 1

 

 # Converting the given string

 # into a character array

 ch = list(Str)

 for i in range(len(ch)):

 

 # Check if the character is a letter

 # and index of character array doesn't

 # equal to end of line that means, it is

 # a word and set isWord by true

 if(ch[i].isalpha() and i != endOfLine):

 isWord = True

 

 # Check if the character is not a letter

 # that means there is a space, then we

 # increment the wordCount by one and set

 # the isWord by false

 elif(not ch[i].isalpha() and isWord):

 wordCount += 1

 isWord = False

 

 # Check for the last word of the

 # sentence and increment the wordCount

 # by one

 elif(ch[i].isalpha() and i == endOfLine):

 wordCount += 1

 

 # Return the total number of

 # words in the string

 return wordCount

# Driver Code

# Given String str

Str = "One two three\n four\tfive "

# Print the result

print("No of words :", countWords(Str))

# This code is contributed by rag2127  
  
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

// C# program to count total

// number of words in the string

using System;

public class GFG

{

 // Function to count total number

 // of words in the string

 static int countWords(String str)

 {

 // Check if the string is null

 // or empty then return zero

 if(str == null)

 {

 return 0;

 }

 int wordCount = 0;

 bool isWord = false;

 int endOfLine = str.Length - 1;

 // Converting the given string 

 // into a character array

 char[] ch = str.ToCharArray();

 for (int i = 0; i < ch.Length; i++)

 {

 // Check if the character is a letter

 // and index of character array doesn't

 // equal to end of line that means, it is

 // a word and set isWord by true

 if (Char.IsLetter(ch[i]) 

 && i != endOfLine)

 {

 isWord = true;

 }

 // Check if the character is not a letter

 // that means there is a space, then we

 // increment the wordCount by one and set

 // the isWord by false

 else if (!Char.IsLetter(ch[i]) 

 && isWord)

 {

 wordCount++;

 isWord = false;

 }

 // Check for the last word of the 

 // sentence and increment the wordCount 

 // by one

 else if (Char.IsLetter(ch[i])

 && i == endOfLine)

 {

 wordCount++;

 }

 }

 // Return the total number of 

 // words in the string

 return wordCount;

 }

 // Driver Code

 static public void Main ()

 {

 // Given String str

 string str = "One two three\n four\tfive ";

 // Print the result

 Console.WriteLine("No of words : " + countWords(str));

 }

}

// This code is contributed by avanitrachhadiya2155  
  
---  
  
 __

 __

  

**Output**

    
    
    No of words : 5

**Time Complexity:** O(N)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

