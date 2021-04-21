Split a Numeric String into Fibonacci Sequence



Given a numeric string **S** representing a large number, the task is to form
a Fibonacci Sequence of at least length 3 from the given string. If such a
split is not possible, print **-1.**

 **Examples:**

> **Input:** S = “5712”  
> **Output:** 5 7 12  
> **Explanation:**  
>  Since 5 + 7 = 12, the splits {5}, {7}, {12} forms a Fibonacci sequence.
>
>  **Input:** S = “11235813″  
> **Output:** 1 1 2 3 5 8 13

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
To solve the problem, the idea is to use Backtracking to find a sequence that
follows the conditions of the **Fibonacci Sequence**.

  

  

Follow the steps below to solve the problem:

  1. Initialize a vector **seq[]** to store the **Fibonacci sequence**.
  2. Initialize a variable **pos** which points to the current index of the string **S** , initially _**0**_.
  3. Iterate over the indices **[pos, length – 1]** : 
    * Add the number **S[pos:** **i]** to the Fibonacci sequence **seq** if the length of **seq** is less than _2_ or the current number is equal to the sum of the last two numbers of **seq**. Recur for the index **i + 1** and proceed.
    * If the last added number **S[pos:** **i]** does not form a Fibonacci sequence and returns _false_ after recursion, then remove it from the **seq.**
    * Otherwise, end the loop and return true as the Fibonacci sequence is formed.
  4. If **pos** exceeds the length of **S** , then: 
    * If the length of the sequence **seq** is greater than or equal to _3_ , then a Fibonacci sequence is found, hence return _true_.
    * Otherwise, the Fibonacci sequence is not possible and hence returns _false_.
  5. Finally, if the length of **seq** is greater than or equal to _3,_ then print the numbers in **seq** as the required Fibonacci sequence or, otherwise print _-1_.

Below is the illustration of the recursive structure where only one branch is
extended to get the result:  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200717184738/recursive.png)

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program of the above approach

#include <bits/stdc++.h>

using namespace std;

#define LL long long

// Function that returns true if

// Fibonacci sequence is found

bool splitIntoFibonacciHelper(int pos,

 string S,

 vector<int>& seq)

{

 // Base condition:

 // If pos is equal to length of S

 // and seq length is greater than 3

 if (pos == S.length()

 and (seq.size() >= 3)) {

 // Return true

 return true;

 }

 // Stores current number

 LL num = 0;

 for (int i = pos; i < S.length(); i++) {

 // Add current digit to num

 num = num * 10 + (S[i] - '0');

 // Avoid integer overflow

 if (num > INT_MAX)

 break;

 // Avoid leading zeros

 if (S[pos] == '0' and i > pos)

 break;

 // If current number is greater

 // than last two number of seq

 if (seq.size() > 2

 and (num > ((LL)seq.back()

 + (LL)seq[seq.size()

 - 2])))

 break;

 // If seq length is less

 // 2 or current number is

 // is equal to the last

 // two of the seq

 if (seq.size() < 2

 or (num == ((LL)seq.back()

 + (LL)seq[seq.size()

 - 2]))) {

 // Add to the seq

 seq.push_back(num);

 // Recur for i+1

 if (splitIntoFibonacciHelper(i + 1,

 S, seq))

 return true;

 // Remove last added number

 seq.pop_back();

 }

 }

 // If no sequence is found

 return false;

}

// Function that prints the Fibonacci

// sequence from the split of string S

void splitIntoFibonacci(string S)

{

 // Initialize a vector to

 // store the sequence

 vector<int> seq;

 // Call helper function

 splitIntoFibonacciHelper(0, S,

 seq);

 // If sequence length is

 // greater than 3

 if (seq.size() >= 3) {

 // Print the sequence

 for (int i : seq)

 cout << i << " ";

 }

 // If no sequence is found

 else {

 // Print -1

 cout << -1;

 }

}

// Driver Code

int main()

{

 // Given String

 string S = "11235813";

 // Function Call

 splitIntoFibonacci(S);

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

// Java program of the above approach

import java.util.*;

class GFG{

// Function that returns true if

// Fibonacci sequence is found

static boolean splitIntoFibonacciHelper(int pos,

 String S,

 ArrayList<Long> seq)

{

 

 // Base condition:

 // If pos is equal to length of S

 // and seq length is greater than 3

 if (pos == S.length() && (seq.size() >= 3))

 {

 // Return true

 return true;

 }

 // Stores current number

 long num = 0;

 for(int i = pos; i < S.length(); i++)

 {

 

 // Add current digit to num

 num = num * 10 + (S.charAt(i) - '0');

 // Avoid integer overflow

 if (num > Integer.MAX_VALUE)

 break;

 // Avoid leading zeros

 if (S.charAt(pos) == '0' && i > pos)

 break;

 // If current number is greater

 // than last two number of seq

 if (seq.size() > 2 &&

 (num > ((long)seq.get(seq.size() - 1) +

 (long)seq.get(seq.size() - 2))))

 break;

 // If seq length is less

 // 2 or current number is

 // is equal to the last

 // two of the seq

 if (seq.size() < 2 ||

 (num == ((long)seq.get(seq.size() - 1) +

 (long)seq.get(seq.size() - 2))))

 {

 

 // Add to the seq

 seq.add(num);

 // Recur for i+1

 if (splitIntoFibonacciHelper(i + 1,

 S, seq))

 return true;

 // Remove last added number

 seq.remove(seq.size() - 1);

 }

 }

 

 // If no sequence is found

 return false;

}

// Function that prints the Fibonacci

// sequence from the split of string S

static void splitIntoFibonacci(String S)

{

 

 // Initialize a vector to

 // store the sequence

 ArrayList<Long> seq = new ArrayList<>();

 // Call helper function

 splitIntoFibonacciHelper(0, S, seq);

 // If sequence length is

 // greater than 3

 if (seq.size() >= 3)

 {

 

 // Print the sequence

 for (int i = 0; i < seq.size(); i++)

 System.out.print(seq.get(i) + " ");

 }

 // If no sequence is found

 else

 {

 // Print -1

 System.out.print("-1");

 }

}

// Driver code

public static void main(String[] args)

{

 

 // Given String

 String S = "11235813";

 

 // Function Call

 splitIntoFibonacci(S);

}

}

// This code is contributed by offbeat  
  
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

# Python3 program of the above approach

import sys

# Function that returns true if

# Fibonacci sequence is found

def splitIntoFibonacciHelper(pos, S, seq):

 # Base condition:

 # If pos is equal to length of S

 # and seq length is greater than 3

 if (pos == len(S) and (len(seq) >= 3)):

 

 # Return true

 return True

 

 # Stores current number

 num = 0

 

 for i in range(pos, len(S)):

 

 # Add current digit to num

 num = num * 10 + (ord(S[i]) - ord('0'))

 

 # Avoid integer overflow

 if (num > sys.maxsize):

 break

 

 # Avoid leading zeros

 if (ord(S[pos]) == ord('0') and i > pos):

 break

 

 # If current number is greater

 # than last two number of seq

 if (len(seq) > 2 and

 (num > (seq[-1] +

 seq[len(seq) - 2]))):

 break

 

 # If seq length is less

 # 2 or current number is

 # is equal to the last

 # two of the seq

 if (len(seq) < 2 or

 (num == (seq[-1] +

 seq[len(seq) - 2]))):

 

 # Add to the seq

 seq.append(num)

 

 # Recur for i+1

 if (splitIntoFibonacciHelper(

 i + 1, S, seq)):

 return True

 

 # Remove last added number

 seq.pop()

 

 # If no sequence is found

 return False

# Function that prints the Fibonacci

# sequence from the split of string S

def splitIntoFibonacci(S):

 

 # Initialize a vector to

 # store the sequence

 seq = []

 

 # Call helper function

 splitIntoFibonacciHelper(0, S, seq)

 

 # If sequence length is

 # greater than 3

 if (len(seq) >= 3):

 

 # Print the sequence

 for i in seq:

 print(i, end = ' ')

 

 # If no sequence is found

 else:

 

 # Print -1

 print(-1, end = '')

 

# Driver Code

if __name__=='__main__':

 

 # Given String

 S = "11235813"

 

 # Function Call

 splitIntoFibonacci(S)

# This code is contributed by pratham76  
  
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

// C# program of the above approach

using System;

using System.Collections;

using System.Collections.Generic;

class GFG{

 

// Function that returns true if

// Fibonacci sequence is found

static bool splitIntoFibonacciHelper(int pos,

 string S,

 ArrayList seq)

{

 

 // Base condition:

 // If pos is equal to length of S

 // and seq length is greater than 3

 if (pos == S.Length && (seq.Count >= 3))

 {

 // Return true

 return true;

 }

 // Stores current number

 long num = 0;

 for(int i = pos; i < S.Length; i++)

 {

 

 // Add current digit to num

 num = num * 10 + (S[i] - '0');

 // Avoid integer overflow

 if (num > Int64.MaxValue)

 break;

 

 // Avoid leading zeros

 if (S[pos] == '0' && i > pos)

 break;

 // If current number is greater

 // than last two number of seq

 if (seq.Count> 2 &&

 (num > ((long)seq[seq.Count - 1] +

 (long)seq[seq.Count - 2])))

 break;

 // If seq length is less

 // 2 or current number is

 // is equal to the last

 // two of the seq

 if (seq.Count < 2 ||

 (num == ((long)seq[seq.Count - 1] +

 (long)seq[seq.Count - 2])))

 {

 

 // Add to the seq

 seq.Add(num);

 // Recur for i+1

 if (splitIntoFibonacciHelper(i + 1,

 S, seq))

 return true;

 // Remove last added number

 seq.Remove(seq.Count - 1);

 }

 }

 

 // If no sequence is found

 return false;

}

// Function that prints the Fibonacci

// sequence from the split of string S

static void splitIntoFibonacci(string S)

{

 

 // Initialize a vector to

 // store the sequence

 ArrayList seq = new ArrayList();

 // Call helper function

 splitIntoFibonacciHelper(0, S, seq);

 // If sequence length is

 // greater than 3

 if (seq.Count >= 3)

 {

 

 // Print the sequence

 for(int i = 0; i < seq.Count; i++)

 Console.Write(seq[i] + " ");

 }

 // If no sequence is found

 else

 {

 

 // Print -1

 Console.Write("-1");

 }

}

// Driver Code

public static void Main(string[] args)

{

 

 // Given String

 string S = "11235813";

 

 // Function call

 splitIntoFibonacci(S);

}

}

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    1 1 2 3 5 8 13

_**Time Complexity:** O(N2) _  
_**Space Complexity:** O(N)_  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

