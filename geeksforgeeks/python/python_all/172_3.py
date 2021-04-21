Minimum Distance Between Words of a String



Given a string **s** and two words **w1** and **w2** that are present in S.
The task is to find the minimum distance between **w1** and **w2**. Here
distance is the number of steps or words between the first and the second
word.  
**Examples:**  

> **Input :** s = “geeks for geeks contribute practice”, w1 = “geeks”, w2 =
> “practice”  
> **Output : 1**  
> There is only one word between closest occurrences of w1 and w2.  
>  **Input :** s = “the quick the brown quick brown the frog”, w1 = “quick”,
> w2 = “frog”  
> **Output :** 2

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

A **simple approach** is to consider every occurrence of w1. For every
occurrence of w1, find the closest w2 and keep track of minimum distance.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find Minimum Distance

// Between Words of a String

#include <bits/stdc++.h>

#include <sstream>

using namespace std;

// Function to implement split function

void split(const string &s;, char delimeter,

 vector<string> &words;)

{

 string token;

 stringstream tokenStream(s);

 while (getline(tokenStream, token, delimeter))

 words.push_back(token);

}

// Function to calculate the minimum

// distance between w1 and w2 in s

int distance(string s, string w1, string w2)

{

 if (w1 == w2)

 return 0;

 // get individual words in a list

 vector<string> words;

 split(s, ' ', words);

 // assume total length of the string

 // as minimum distance

 int min_dist = words.size() + 1;

 // traverse through the entire string

 for (int index = 0; index < words.size(); index++)

 {

 if (words[index] == w1)

 {

 for (int search = 0;

 search < words.size(); search++)

 {

 if (words[search] == w2)

 {

 // the distance between the words is

 // the index of the first word - the

 // current word index

 int curr = abs(index - search) - 1;

 // comparing current distance with

 // the previously assumed distance

 if (curr < min_dist)

 min_dist = curr;

 }

 }

 }

 }

 // w1 and w2 are same and adjacent

 return min_dist;

}

// Driver Code

int main(int argc, char const *argv[])

{

 string s = "geeks for geeks contribute practice";

 string w1 = "geeks";

 string w2 = "practice";

 cout << distance(s, w1, w2) << endl;

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

// Java program to find Minimum Distance

// Between Words of a String

 class solution

 {

// Function to calculate the minimum

// distance between w1 and w2 in s

static int distance(String s,String w1,String w2)

{

 

 if (w1 .equals( w2) )

 return 0 ;

 

 // get individual words in a list

 String words[] = s.split(" ");

 

 // assume total length of the string

 // as minimum distance

 int min_dist = (words.length) + 1;

 

 // traverse through the entire string

 for (int index = 0;

 index < words.length ; index ++)

 {

 

 if (words[index] .equals( w1))

 {

 for (int search = 0;

 search < words.length; search ++)

 {

 if (words[search] .equals(w2))

 {

 // the distance between the words is

 // the index of the first word - the

 // current word index

 int curr = Math.abs(index - search) - 1;

 

 // comparing current distance with

 // the previously assumed distance

 if (curr < min_dist)

 {

 min_dist = curr ;

 }

 }

 }

 }

 }

 

 // w1 and w2 are same and adjacent

 return min_dist;

}

 

// Driver code

public static void main(String args[])

{

 

String s = "geeks for geeks contribute practice";

String w1 = "geeks" ;

String w2 = "practice" ;

 

System.out.print( distance(s, w1, w2) );

 

}

}

//contributed by Arnab Kundu  
  
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

# function to calculate the minimum

# distance between w1 and w2 in s

 

def distance(s, w1, w2):

 

 if w1 == w2 :

 return 0

 # get individual words in a list

 words = s.split(" ")

 # assume total length of the string as

 # minimum distance

 min_dist = len(words)+1

 # traverse through the entire string

 for index in range(len(words)):

 if words[index] == w1:

 for search in range(len(words)):

 if words[search] == w2:

 # the distance between the words is

 # the index of the first word - the

 # current word index

 curr = abs(index - search) - 1;

 # comparing current distance with

 # the previously assumed distance

 if curr < min_dist:

 min_dist = curr

 # w1 and w2 are same and adjacent

 return min_dist

 

# Driver code

s = "geeks for geeks contribute practice"

w1 = "geeks"

w2 = "practice"

print(distance(s, w1, w2))  
  
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

// C# program to find Minimum Distance

// Between Words of a String

using System;

 class solution

 {

 

// Function to calculate the minimum

// distance between w1 and w2 in s

static int distance(string s,string w1,string w2)

{

 

 if (w1 .Equals( w2) )

 return 0 ;

 

 // get individual words in a list

 string[] words = s.Split(" ");

 

 // assume total length of the string

 // as minimum distance

 int min_dist = (words.Length) + 1;

 

 // traverse through the entire string

 for (int index = 0;

 index < words.Length ; index ++)

 {

 

 if (words[index] .Equals( w1))

 {

 for (int search = 0;

 search < words.Length; search ++)

 {

 if (words[search] .Equals(w2))

 {

 // the distance between the words is

 // the index of the first word - the

 // current word index

 int curr = Math.Abs(index - search) - 1;

 

 // comparing current distance with

 // the previously assumed distance

 if (curr < min_dist)

 {

 min_dist = curr ;

 }

 }

 }

 }

 }

 

 // w1 and w2 are same and adjacent

 return min_dist;

}

 

// Driver code

public static void Main()

{

 

string s = "geeks for geeks contribute practice";

string w1 = "geeks" ;

string w2 = "practice" ;

 

Console.Write( distance(s, w1, w2) );

 

}

}  
  
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

// PHP program to find Minimum Distance

// Between Words of a String

// Function to calculate the minimum

// distance between w1 and w2 in s

function distance($s, $w1, $w2)

{

 

 if ($w1 == $w2 )

 return 0 ;

 // get individual words in a list

 $words = explode(" ", $s);

 // assume total length of the string

 // as minimum distance

 $min_dist = sizeof($words) + 1;

 // traverse through the entire string

 for ($index = 0;

 $index < sizeof($words) ; $index ++)

 {

 if ($words[$index] == $w1)

 {

 for ($search = 0;

 $search < sizeof($words); $search ++)

 {

 if ($words[$search] == $w2)

 {

 // the distance between the words is

 // the index of the first word - the

 // current word index

 $curr = abs($index - $search) - 1;

 // comparing current distance with

 // the previously assumed distance

 if ($curr < $min_dist)

 {

 $min_dist = $curr ;

 }

 }

 }

 }

 }

 

 // w1 and w2 are same and adjacent

 return $min_dist;

}

// Driver code

$s = "geeks for geeks contribute practice";

$w1 = "geeks" ;

$w2 = "practice" ;

echo distance($s, $w1, $w2) ;

// This code is contributed by Ryuga

?>  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    1

