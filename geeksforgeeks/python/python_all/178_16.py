Find words which are greater than given length k



A string is given and you have to find all the words (substrings separated by
a space) which are greater than given length k.

Examples:

    
    
    Input : str = "hello geeks for geeks 
              is computer science portal" 
            k = 4
    Output : hello geeks geeks computer 
             science portal
    Explanation : The output is list of all 
    words that are of length more than k.
    
    Input : str = "string is fun in python"
            k = 3
    Output : string python
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The idea is to first split given string around space. Then traverse through
all words. For every word, check

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find all string

// which are greater than given length k

 

#include <bits/stdc++.h>

using namespace std;

 

// function find sttring greater than

// length k

void string_k(string s, int k)

{

 // create the empty string

 string w = "";

 // iterate the loop till every space

 for(int i = 0; i < s.size(); i++)

 {

 if(s[i] != ' ')

 

 // append this sub string in

 // string w

 w = w + s[i];

 else {

 

 // if length of current sub

 // string w is greater than

 // k then print

 if(w.size() > k)

 cout << w << " ";

 w = "";

 }

 }

}

 

// Driver code

int main()

{

 string s = "geek for geeks";

 int k = 3;

 s = s + " ";

 string_k(s, k);

 return 0;

}

 

// This code is contributed by 

// Manish Shaw (manishshaw1)  
  
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

// Java program to find all string

// which are greater than given length k

import java.io.*;

import java.util.*;

 

public class GFG {

 

 // function find sttring greater than

 // length k

 static void string_k(String s, int k)

 {

 // create the empty string

 String w = "";

 

 // iterate the loop till every space

 for(int i = 0; i < s.length(); i++)

 {

 if(s.charAt(i) != ' ')

 

 // append this sub string in

 // string w

 w = w + s.charAt(i);

 else {

 

 // if length of current sub

 // string w is greater than

 // k then print

 if(w.length() > k)

 System.out.print(w + " ");

 w = "";

 }

 }

 }

 

 // Driver code

 public static void main(String args[])

 {

 String s = "geek for geeks";

 int k = 3;

 s = s + " ";

 string_k(s, k);

 }

}

 

// This code is contributed by 

// Manish Shaw (manishshaw1)  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find all string

# which are greater than given length k

 

# function find sttring greater than length k

def string_k(k, str):

 

 # create the empty string

 string = []

 

 # split the string where space is comes

 text = str.split(" ")

 

 # iterate the loop till every substring

 for x in text:

 

 # if length of current sub string

 # is greater than k then

 if len(x) > k:

 

 # append this sub string in

 # string list

 string.append(x)

 

 # return string list

 return string

 

 

# Driver Program 

k = 3

str ="geek for geeks"

print(string_k(k, str))   
  
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

// C# program to find all string

// which are greater than given length k

using System;

 

class GFG {

 

 // function find sttring greater than

 // length k

 static void string_k(string s, int k)

 {

 // create the empty string

 string w = "";

 

 // iterate the loop till every space

 for(int i = 0; i < s.Length; i++)

 {

 if(s[i] != ' ')

 

 // append this sub string in

 // string w

 w = w + s[i];

 else {

 

 // if length of current sub

 // string w is greater than

 // k then print

 if(w.Length > k)

 Console.Write(w + " ");

 w = "";

 }

 }

 }

 

 // Driver code

 static void Main()

 {

 string s = "geek for geeks";

 int k = 3;

 s = s + " ";

 string_k(s, k);

 }

}

 

// This code is contributed by 

// Manish Shaw (manishshaw1)  
  
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

// PHP program to find all $

// which are greater than given length k

 

// function find sttring greater than

// length k

function string_k($s, $k)

{

 

 // create the empty string

 $w = "";

 

 // iterate the loop till every space

 for($i = 0; $i < strlen($s); $i++)

 {

 if($s[$i] != ' ')

 

 // append this sub $in $w

 $w = $w.$s[$i];

 else {

 

 // if length of current sub

 // $w is greater than

 // k then print

 if(strlen($w) > $k)

 echo ($w." ");

 $w = "";

 }

 }

}

 

// Driver code

$s = "geek for geeks";

$k = 3;

$s = $s . " ";

string_k($s, $k);

 

// This code is contributed by 

// Manish Shaw (manishshaw1)

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    ['geek', 'geeks']
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

