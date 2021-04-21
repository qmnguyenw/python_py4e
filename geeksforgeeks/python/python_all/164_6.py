Iterative Letter Combinations of a Phone Number



Given an integer array containing digits from **[0, 9]** , the task is to
print all possible letter combinations that the numbers could represent.  
A mapping of digit to letters (just like on the telephone buttons) is being
followed. **Note** that **0** and **1** do not map to any letters. All the
mapping are shown in the image below:  

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Mobile-
keypad-267x300.png)

**Example:**

> **Input:** arr[] = {2, 3}  
> **Output:** ad ae af bd be bf cd ce cf
>
>  **Input:** arr[] = {9}  
> **Output:** w x y z
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Now let us think how we would approach this problem without
doing it in an iterative way. A recursive solution is intuitive and common. We
keep adding each possible letter recursively and this will generate all the
possible strings.  
Let us think about how we can build an iterative solution using the recursive
one. Recursion is possible through the use of a stack. So if we use a stack
instead of a recursive function will that be an iterative solution? One could
say so speaking technically but we then aren’t really doing anything different
in terms of logic.  
A Stack is a LIFO DS. Can we use another Data structure? What will be the
difference if we use a FIFO DS? Let’s say a queue. Since BFS is done by queue
and DFS by stack is there any difference between the two?  
The difference between DFS and BFS is similar to this question. In DFS we will
find each path possible in the tree one by one. It will perform all steps for
a path first whereas BFS will build all paths together one step at a time.  
So, a queue would work perfectly for this question. The only difference
between the two algorithms using queue and stack will be the way in which they
are formed. Stack will form all strings completely one by one whereas the
queue will form all the strings together i.e. after x number of passes all the
strings will have a length of x.

 **For example:**

    
    
    If the given number is "23", 
    then using **queue** , the letter combinations 
    obtained will be:
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"] 
    and using **stack** , the letter combinations obtained will 
    be:
    ["cf","ce","cd","bf","be","bd","af","ae","ad"].
    

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

// Function to return a vector that contains

// all the generated letter combinations

vector<string> letterCombinationsUtil(const int number[],

 int n,

 const string table[])

{

 // To store the generated letter combinations

 vector<string> list;

 queue<string> q;

 q.push("");

 while (!q.empty()) {

 string s = q.front();

 q.pop();

 // If complete word is generated

 // push it in the list

 if (s.length() == n)

 list.push_back(s);

 else

 // Try all possible letters for current digit

 // in number[]

 for (auto letter : table[number[s.length()]])

 q.push(s + letter);

 }

 // Return the generated list

 return list;

}

// Function that creates the mapping and

// calls letterCombinationsUtil

void letterCombinations(const int number[], int n)

{

 // table[i] stores all characters that

 // corresponds to ith digit in phone

 string table[10]

 = { "0", "1", "abc", "def", "ghi",

 "jkl", "mno", "pqrs", "tuv", "wxyz" };

 vector<string> list

 = letterCombinationsUtil(number, n, table);

 // Print the contents of the vector

 for (auto word : list)

 cout << word << " ";

 return;

}

// Driver code

int main()

{

 int number[] = { 2, 3 };

 int n = sizeof(number) / sizeof(number[0]);

 // Function call

 letterCombinations(number, n);

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

import java.io.*;

import java.util.*;

class GFG {

 // Function to return a vector that contains

 // all the generated letter combinations

 static ArrayList<String>

 letterCombinationsUtil(int[] number, int n,

 String[] table)

 {

 // To store the generated letter combinations

 ArrayList<String> list = new ArrayList<>();

 Queue<String> q = new LinkedList<>();

 q.add("");

 while (!q.isEmpty()) {

 String s = q.remove();

 // If complete word is generated

 // push it in the list

 if (s.length() == n)

 list.add(s);

 else {

 String val = table[number[s.length()]];

 for (int i = 0; i < val.length(); i++)

 {

 q.add(s + val.charAt(i));

 }

 }

 }

 return list;

 }

 // Function that creates the mapping and

 // calls letterCombinationsUtil

 static void letterCombinations(int[] number, int n)

 {

 // table[i] stores all characters that

 // corresponds to ith digit in phone

 String[] table

 = { "0", "1", "abc", "def", "ghi",

 "jkl", "mno", "pqrs", "tuv", "wxyz" };

 ArrayList<String> list

 = letterCombinationsUtil(number, n, table);

 // Print the contents of the list

 for (int i = 0; i < list.size(); i++) {

 System.out.print(list.get(i) + " ");

 }

 }

 // Driver code

 public static void main(String args[])

 {

 int[] number = { 2, 3 };

 int n = number.length;

 

 // Funciton call

 letterCombinations(number, n);

 }

}

// This code is contributed by rachana soma  
  
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

# Python3 implementation of the approach

from collections import deque

# Function to return a list that contains

# all the generated letter combinations

def letterCombinationsUtil(number, n, table):

 list = []

 q = deque()

 q.append("")

 while len(q) != 0:

 s = q.pop()

 # If complete word is generated

 # push it in the list

 if len(s) == n:

 list.append(s)

 else:

 # Try all possible letters for current digit

 # in number[]

 for letter in table[number[len(s)]]:

 q.append(s + letter)

 # Return the generated list

 return list

# Function that creates the mapping and

# calls letterCombinationsUtil

def letterCombinations(number, n):

 # table[i] stores all characters that

 # corresponds to ith digit in phone

 table = ["0", "1", "abc", "def", "ghi",
"jkl",

 "mno", "pqrs", "tuv", "wxyz"]

 list = letterCombinationsUtil(number, n, table)

 s = ""

 for word in list:

 s += word + " "

 print(s)

 return

# Driver code

number = [2, 3]

n = len(number)

# Function call

letterCombinations(number, n)  
  
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

 // Function to return a vector that contains

 // all the generated letter combinations

 static List<String>

 letterCombinationsUtil(int[] number, int n,

 String[] table)

 {

 // To store the generated letter combinations

 List<String> list = new List<String>();

 Queue<String> q = new Queue<String>();

 q.Enqueue("");

 while (q.Count != 0) {

 String s = q.Dequeue();

 // If complete word is generated

 // push it in the list

 if (s.Length == n)

 list.Add(s);

 else {

 String val = table[number[s.Length]];

 for (int i = 0; i < val.Length; i++) {

 q.Enqueue(s + val[i]);

 }

 }

 }

 return list;

 }

 // Function that creates the mapping and

 // calls letterCombinationsUtil

 static void letterCombinations(int[] number, int n)

 {

 // table[i] stores all characters that

 // corresponds to ith digit in phone

 String[] table

 = { "0", "1", "abc", "def", "ghi",

 "jkl", "mno", "pqrs", "tuv", "wxyz" };

 List<String> list

 = letterCombinationsUtil(number, n, table);

 // Print the contents of the list

 for (int i = 0; i < list.Count; i++) {

 Console.Write(list[i] + " ");

 }

 }

 // Driver code

 public static void Main(String[] args)

 {

 int[] number = { 2, 3 };

 int n = number.Length;

 

 // Function call

 letterCombinations(number, n);

 }

}

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output**

    
    
    ad ae af bd be bf cd ce cf 
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

