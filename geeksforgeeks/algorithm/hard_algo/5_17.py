Find the count of M character words which have at least one character repeated



Given two integers **N** and **M** , the task is count the total words of
**M** character length formed by the given **N** distinct characters such that
the words have at least one character repeated more than once.

 **Examples:**

>  **Input:** N = 3, M = 2  
>  **Output:** 3  
> Suppose the characters are {‘a’, ‘b’, ‘c’}  
> All 2 length words that can be formed with these characters  
> are “aa”, “ab”, “ac”, “ba”, “bb”, “bc”, “ca”, “cb” and “cc”.  
> Out of these words only “aa”, “bb” and “cc” have  
> at least one character repeated more than once.
>
>  **Input:** N = 10, M = 5  
>  **Output:** 69760

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
Total number of M character words possible from N characters, **total = N M**.  
Total number of M character words possible from N characters where no
character repeats itself, **noRepeat = NPM**.  
So, total words where at least a single character appear more than once is
**total – noRepeat** i.e. **N M – NPM**.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation for the above approach

#include <math.h> 

#include <iostream>

using namespace std;

 

// Function to return the

// factorial of a number

int fact(int n)

{

 if (n <= 1)

 return 1;

 return n * fact(n - 1);

}

 

// Function to return the value of nPr

int nPr(int n, int r)

{

 return fact(n) / fact(n - r);

}

 

// Function to return the total number of

// M length words which have at least a

// single character repeated more than once

int countWords(int N, int M)

{

 return pow(N, M) - nPr(N, M);

}

 

// Driver code

int main()

{

 int N = 10, M = 5;

 cout << (countWords(N, M));

 return 0;

}

 

// This code is contributed by jit_t  
  
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

class GFG {

 

 // Function to return the

 // factorial of a number

 static int fact(int n)

 {

 if (n <= 1)

 return 1;

 return n * fact(n - 1);

 }

 

 // Function to return the value of nPr

 static int nPr(int n, int r)

 {

 return fact(n) / fact(n - r);

 }

 

 // Function to return the total number of

 // M length words which have at least a

 // single character repeated more than once

 static int countWords(int N, int M)

 {

 return (int)Math.pow(N, M) - nPr(N, M);

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int N = 10, M = 5;

 System.out.print(countWords(N, M));

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

# Python3 implementation for the above approach

 

# Function to return the

# factorial of a number

def fact(n):

 

 if (n <= 1):

 return 1;

 return n * fact(n - 1);

 

# Function to return the value of nPr

def nPr(n, r):

 

 return fact(n) // fact(n - r);

 

# Function to return the total number of

# M length words which have at least a

# single character repeated more than once

def countWords(N, M):

 

 return pow(N, M) - nPr(N, M);

 

# Driver code

N = 10; M = 5;

print(countWords(N, M));

 

# This code is contributed by Code_Mech  
  
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

 // factorial of a number

 static int fact(int n)

 {

 if (n <= 1)

 return 1;

 return n * fact(n - 1);

 }

 

 // Function to return the value of nPr

 static int nPr(int n, int r)

 {

 return fact(n) / fact(n - r);

 }

 

 // Function to return the total number of

 // M length words which have at least a

 // single character repeated more than once

 static int countWords(int N, int M)

 {

 return (int)Math.Pow(N, M) - nPr(N, M);

 }

 

 // Driver code

 static public void Main ()

 {

 int N = 10, M = 5;

 Console.Write(countWords(N, M));

 }

}

 

// This code is contributed by ajit.  
  
---  
  
 __

 __

 **Output:**

    
    
    69760
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

