Count occurrences of a word in string



You are given a string and a word your task is that count the number of the
occurrence of the given word in the string and print the number of occurrence
of the word.  
**Examples:**

    
    
    **Input :** string = "GeeksforGeeks A computer science portal for geeks"
    word = "portal"
    **Output :** Occurrences of Word = 1 Time
    
    **Input :** string = "GeeksforGeeks A computer science portal for geeks"
    word = "technical" 
    **Output :** Occurrences of Word = 0 Time

 **Approach:**

  * First, we split the string by spaces in a
  * Then, take a variable count = 0 and in every true condition we increment the count by 1
  * Now run a loop at 0 to length of string and check if our string is equal to the word
  * if condition true then we increment the value of count by 1 and in the end we print the value of count.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

Below is the implementation of the above approach :

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to count the number

// of occurrence of a word in

// the given string given string

#include <bits/stdc++.h>

using namespace std;

int countOccurences(char *str,

 string word)

{

 char *p;

 // split the string by spaces in a

 vector<string> a;

 p = strtok(str, " ");

 while (p != NULL)

 {

 a.push_back(p);

 p = strtok(NULL, " ");

 }

 // search for pattern in a

 int c = 0;

 for (int i = 0; i < a.size(); i++)

 // if match found increase count

 if (word == a[i])

 c++;

 return c;

}

// Driver code

int main()

{

 char str[] = "GeeksforGeeks A computer science portal for geeks ";

 string word = "portal";

 cout << countOccurences(str, word);

 return 0;

}

// This code is contributed by

// sanjeev2552  
  
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

// Java program to count the number

// of occurrence of a word in

// the given string given string

import java.io.*;

class GFG {

static int countOccurences(String str, String word)

{

 // split the string by spaces in a

 String a[] = str.split(" ");

 // search for pattern in a

 int count = 0;

 for (int i = 0; i < a.length; i++)

 {

 // if match found increase count

 if (word.equals(a[i]))

 count++;

 }

 return count;

}

// Driver code

public static void main(String args[])

{

 String str = "GeeksforGeeks A computer science portal for geeks ";

 String word = "portal";

 System.out.println(countOccurences(str, word));

}

}

/*This code is contributed by Nikita Tiwari.*/  
  
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

# Python program to count the number of occurrence

# of a word in the given string given string

def countOccurences(str, word):

 

 # split the string by spaces in a

 a = str.split(" ")

 # search for pattern in a

 count = 0

 for i in range(0, len(a)):

 

 # if match found increase count

 if (word == a[i]):

 count = count + 1

 

 return count 

# Driver code

str ="GeeksforGeeks A computer science portal for geeks "

word ="portal"

print(countOccurences(str, word))  
  
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

// C# program to count the number

// of occurrence of a word in

// the given string given string

using System;

class GFG

{

static int countOccurences(string str,

 string word)

{

 // split the string by spaces

 string[] a = str.Split(' ');

 // search for pattern in string

 int count = 0;

 for (int i = 0; i < a.Length; i++)

 {

 

 // if match found increase count

 if (word.Equals(a[i]))

 count++;

 }

 return count;

}

// Driver code

public static void Main()

{

 string str = "GeeksforGeeks A computer science portal for geeks ";

 string word = "portal";

 Console.Write(countOccurences(str, word));

}

}

// This code is contributed

// by ChitraNayal  
  
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

// PHP program to count the number

// of occurrence of a word in

// the given string given string

function countOccurences($str, $word)

{

 // split the string by spaces

 $a = explode(" ", $str);

 // search for pattern in string

 $count = 0;

 for ($i = 0; $i < sizeof($a); $i++)

 {

 

 // if match found increase count

 if ($word == $a[$i])

 $count++;

 }

 return $count;

}

// Driver code

$str = "GeeksforGeeks A computer science portal for geeks ";

$word = "portal";

echo (countOccurences($str, $word));

// This code is contributed

// by ChitraNayal

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    1

#### Method #2: Using **Count()** function in python:

  * First, we split the string by spaces and store in list.
  * We use count() to find count of that word in list.

Below is the implementation:

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count the number of occurrence

# of a word in the given string given string

def countOccurences(str, word):

 wordslist = list(str.split())

 return wordslist.count(word)

# Driver code

str = "GeeksforGeeks A computer science portal for geeks "

word = "portal"

print(countOccurences(str, word))

# This code is contributed by vikkycirus  
  
---  
  
 __

 __

 **Output:**

    
    
    1

Reference : split function python

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

