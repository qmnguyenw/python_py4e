Program to replace a word with asterisks in a sentence



For the given sentence as input, censor a specific word with asterisks ‘
*****‘.

 **Example :**

>  **Input :** word = “computer”  
> text = “GeeksforGeeks is a computer science portal for geeks. People who
> love computer and computer codes can contribute their valuables/ideas on
> computer codes/structures on here.”  
>  **Output :** GeeksforGeeks is a ******** science portal for geeks. People
> who love ******** and ******** codes can contribute their valuables/ideas on
> ******** codes/structures on here.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The idea is to first split given sentence into different words. Then traverse
the word list. For every word in the word list, check if it matches with given
word. If yes, then replace the word with stars in the list. Finally merge the
words of list and print.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to censor a word

// with asterisks in a sentence 

#include<bits/stdc++.h>

#include <boost/algorithm/string.hpp> 

using namespace std;

 

// Function takes two parameter

string censor(string text, 

 string word) 

{

 

 // Break down sentence by ' ' spaces

 // and store each individual word in

 // a different list

 vector<string> word_list; 

 boost::split(word_list, text, boost::is_any_of("\\ +"));

 

 // A new string to store the result

 string result = "";

 

 // Creating the censor which is an asterisks

 // "*" text of the length of censor word

 string stars = "";

 for (int i = 0; i < word.size(); i++)

 stars += '*';

 

 // Iterating through our list

 // of extracted words

 int index = 0;

 for (string i : word_list) 

 {

 

 if (i.compare(word) == 0)

 {

 

 // changing the censored word to

 // created asterisks censor

 word_list[index] = stars;

 }

 index++;

 }

 

 // join the words

 for (string i : word_list)

 {

 result += i + ' ';

 }

 return result;

}

 

// Driver code

int main() 

{

 string extract = "GeeksforGeeks is a computer science "

 "portal for geeks. I am pursuing my "

 "major in computer science. ";

 string cen = "computer";

 cout << (censor(extract, cen));

}

 

// This code is contributed by Rajput-Ji  
  
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

// Java program to censor a word

// with asterisks in a sentence 

class GFG

{

 

// Function takes two parameter

static String censor(String text, 

 String word) 

{

 

 // Break down sentence by ' ' spaces

 // and store each individual word in

 // a different list

 String[] word_list = text.split("\\s+");

 

 // A new string to store the result

 String result = "";

 

 // Creating the censor which is an asterisks

 // "*" text of the length of censor word

 String stars = "";

 for (int i = 0; i < word.length(); i++)

 stars += '*';

 

 // Iterating through our list

 // of extracted words

 int index = 0;

 for (String i : word_list) 

 {

 if (i.compareTo(word) == 0)

 

 // changing the censored word to

 // created asterisks censor

 word_list[index] = stars;

 index++;

 }

 

 // join the words

 for (String i : word_list)

 result += i + ' ';

 

 return result;

}

 

// Driver code

public static void main(String[] args) 

{

 String extract = "GeeksforGeeks is a computer science "+

 "portal for geeks. I am pursuing my " +

 "major in computer science. ";

 String cen = "computer";

 System.out.println(censor(extract, cen));

}

}

 

// This code is contributed by

// sanjeev2552  
  
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

# Python Program to censor a word

# with asterisks in a sentence

 

 

# Function takes two parameter

def censor(text, word):

 

 # Break down sentence by ' ' spaces

 # and store each individual word in

 # a different list

 word_list = text.split()

 

 # A new string to store the result

 result = ''

 

 # Creating the censor which is an asterisks 

 # "*" text of the length of censor word

 stars = '*' * len(word)

 

 # count variable to 

 # access our word_list

 count = 0

 

 # Iterating through our list

 # of extracted words

 index = 0;

 for i in word_list:

 

 if i == word:

 

 # changing the censored word to 

 # created asterisks censor

 word_list[index] = stars

 index += 1

 

 # join the words

 result =' '.join(word_list)

 

 return result

 

# Driver code

if __name__== '__main__':

 

 extract = "GeeksforGeeks is a computer science portal for
geeks.\

 I am pursuing my major in computer science. " 

 cen = "computer"

 print(censor(extract, cen))  
  
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

// C# program to censor a word

// with asterisks in a sentence 

using System;

using System.Collections.Generic;

 

class GFG

{

 

// Function takes two parameter

static String censor(String text, 

 String word) 

{

 

 // Break down sentence by ' ' spaces

 // and store each individual word in

 // a different list

 String[] word_list = text.Split(' ');

 

 // A new string to store the result

 String result = "";

 

 // Creating the censor which is an asterisks

 // "*" text of the length of censor word

 String stars = "";

 for (int i = 0; i < word.Length; i++)

 stars += '*';

 

 // Iterating through our list

 // of extracted words

 int index = 0;

 foreach (String i in word_list) 

 {

 if (i.CompareTo(word) == 0)

 

 // changing the censored word to

 // created asterisks censor

 word_list[index] = stars;

 index++;

 }

 

 // join the words

 foreach (String i in word_list)

 result += i + " ";

 

 return result;

}

 

// Driver code

public static void Main(String[] args) 

{

 String extract = "GeeksforGeeks is a computer science "+

 "portal for geeks. I am pursuing my " +

 "major in computer science. ";

 String cen = "computer";

 Console.WriteLine(censor(extract, cen));

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

// PHP Program to censor a word

// with asterisks in a sentence

 

// Function takes two parameter

function censor($text, $word)

{

 

 // Break down sentence by ' ' spaces

 // and store each individual word in

 // a different list

 $word_list = explode(" ", $text); 

 

 // A new string to store the result

 $result = '';

 

 // Creating the censor which is an 

 // asterisks "*" text of the length 

 // of censor word

 $stars = "";

 for($i = 0; $i < strlen($word); $i++)

 $stars .= "*";

 

 // count variable to access 

 // our word_list

 $count = 0;

 

 // Iterating through our list of 

 // extracted words

 $index = 0;

 for($i = 0; $i < sizeof($word_list); $i++)

 {

 if($word_list[$i] == $word)

 

 // changing the censored word to 

 // created asterisks censor

 $word_list[$index] = $stars;

 $index += 1;

 }

 

 // join the words

 return implode(' ', $word_list);

}

 

// Driver code

$extract = "GeeksforGeeks is a computer science ".

 "portal for geeks.\nI am pursuing my ".

 "major in computer science. "; 

$cen = "computer";

echo censor($extract, $cen);

 

// This code is contributed

// by Aman ojha

?>  
  
---  
  
 __

 __

  
 **Output :**

    
    
    GeeksforGeeks is a ******** science portal for geeks.
    I am pursuing my major in ******** science.
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

