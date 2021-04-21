Generate all binary strings of length n with sub-string “01” appearing exactly
twice



Given an integer **N** , the task is to generate all possible binary strings
of length **N** which contain **“01”** as the sub-string exactly twice.

 **Examples:**

>  **Input:** N = 4  
>  **Output:**  
>  0101  
> “0101” is the only binary string of length 4  
> that contains “01” exactly twice as the sub-string.
>
>  **Input:** N = 5  
>  **Output:**  
>  00101  
> 01001  
> 01010  
> 01011  
> 01101  
> 10101

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem can solved using backtracking. To generate a
binary string, we implement a function that generate each bit at a time,
update the state of the binary string (current length, number of occurrences
of the pattern). Then call the function recursively, and according to the
current state of the binary string, the function will decide how to generate
the next bit or print out the binary string (if the problem’s requirement is
met).

  

  

For this problem, backtracking strategy looks like we generate a binary tree
with each node can have either value **0** or **1**.  
For example, with **N = 4** , the tree will look like:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190326214456/tree14-300x214.png)

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

#include <iostream>

#include <stdlib.h>

using namespace std;

 

// Utility function to print the given binary string

void printBinStr(int* str, int len)

{

 for (int i = 0; i < len; i++) {

 cout << str[i];

 }

 cout << endl;

}

 

// This function will be called recursively

// to generate the next bit for given

// binary string according to its current state

void generateBinStr(int* str, int len, int currlen,

 int occur, int nextbit)

{

 

 // Base-case: if the generated binary string

 // meets the required length and the pattern "01"

 // appears twice

 if (currlen == len) {

 

 // nextbit needs to be 0 because each time

 // we call the function recursively,

 // we call 2 times for 2 cases:

 // next bit is 0 or 1

 // The is to assure that the binary

 // string is printed one time only

 if (occur == 2 && nextbit == 0)

 printBinStr(str, len);

 return;

 }

 

 // Generate the next bit for str

 // and call recursive

 if (currlen == 0) {

 

 // Assign first bit

 str[0] = nextbit;

 

 // The next generated bit will wither be 0 or 1

 generateBinStr(str, len, currlen + 1, occur, 0);

 generateBinStr(str, len, currlen + 1, occur, 1);

 }

 else {

 

 // If pattern "01" occurrence is < 2

 if (occur < 2) {

 

 // Set next bit

 str[currlen] = nextbit;

 

 // If pattern "01" appears then

 // increase the occurrence of pattern

 if (str[currlen - 1] == 0 && nextbit == 1) {

 occur += 1;

 }

 generateBinStr(str, len, currlen + 1, occur, 0);

 generateBinStr(str, len, currlen + 1, occur, 1);

 

 // Else pattern "01" occurrence equals 2

 }

 else {

 

 // If previous bit is 0 then next bit cannot be 1

 if (str[currlen - 1] == 0 && nextbit == 1) {

 return;

 

 // Otherwise

 }

 else {

 str[currlen] = nextbit;

 generateBinStr(str, len, currlen + 1, occur, 0);

 generateBinStr(str, len, currlen + 1, occur, 1);

 }

 }

 }

}

 

// Driver code

int main()

{

 

 int n = 5;

 

 // Length of the resulting strings

 // must be at least 4

 if (n < 4)

 cout << -1;

 else {

 int* str = new int[n];

 

 // Generate all binary strings of length n

 // with sub-string "01" appearing twice

 generateBinStr(str, n, 0, 0, 0);

 generateBinStr(str, n, 0, 0, 1);

 }

 

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

// Java implementation of the above approach

class GFG 

{

 

 // Utility function to print the given binary string

 static void printBinStr(int[] str, int len) 

 {

 for (int i = 0; i < len; i++)

 {

 System.out.print(str[i]);

 }

 System.out.println();

 }

 

 // This function will be called recursively

 // to generate the next bit for given

 // binary string according to its current state

 static void generateBinStr(int[] str, int len, int
currlen,

 int occur, int nextbit) 

 {

 

 // Base-case: if the generated binary string

 // meets the required length and the pattern "01"

 // appears twice

 if (currlen == len) 

 {

 

 // nextbit needs to be 0 because each time

 // we call the function recursively,

 // we call 2 times for 2 cases:

 // next bit is 0 or 1

 // The is to assure that the binary

 // string is printed one time only

 if (occur == 2 && nextbit == 0)

 {

 printBinStr(str, len);

 }

 return;

 }

 

 // Generate the next bit for str

 // and call recursive

 if (currlen == 0) 

 {

 

 // Assign first bit

 str[0] = nextbit;

 

 // The next generated bit will wither be 0 or 1

 generateBinStr(str, len, currlen + 1, occur, 0);

 generateBinStr(str, len, currlen + 1, occur, 1);

 } else // If pattern "01" occurrence is < 2

 if (occur < 2) 

 {

 

 // Set next bit

 str[currlen] = nextbit;

 

 // If pattern "01" appears then

 // increase the occurrence of pattern

 if (str[currlen - 1] == 0 && nextbit == 1) 

 {

 occur += 1;

 }

 generateBinStr(str, len, currlen + 1, occur, 0);

 generateBinStr(str, len, currlen + 1, occur, 1);

 

 // Else pattern "01" occurrence equals 2

 } else // If previous bit is 0 then next bit cannot be 1

 if (str[currlen - 1] == 0 && nextbit == 1) 

 {

 return;

 

 // Otherwise

 } 

 else

 {

 str[currlen] = nextbit;

 generateBinStr(str, len, currlen + 1, occur, 0);

 generateBinStr(str, len, currlen + 1, occur, 1);

 }

 }

 

 // Driver code

 public static void main(String[] args) 

 {

 int n = 5;

 

 // Length of the resulting strings

 // must be at least 4

 if (n < 4) 

 {

 System.out.print(-1);

 } 

 else

 {

 int[] str = new int[n];

 

 // Generate all binary strings of length n

 // with sub-string "01" appearing twice

 generateBinStr(str, n, 0, 0, 0);

 generateBinStr(str, n, 0, 0, 1);

 }

 }

}

 

// This code has been contributed by 29AjayKumar  
  
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

# Python3 implementation of the approach

 

# Utility function to print the 

# given binary string

def printBinStr(string, length):

 

 for i in range(0, length): 

 print(string[i], end = "")

 

 print()

 

# This function will be called recursively

# to generate the next bit for given

# binary string according to its current state

def generateBinStr(string, length, currlen,

 occur, nextbit):

 

 # Base-case: if the generated binary

 # string meets the required length and

 # the pattern "01" appears twice

 if currlen == length:

 

 # nextbit needs to be 0 because each

 # time we call the function recursively,

 # we call 2 times for 2 cases:

 # next bit is 0 or 1

 # The is to assure that the binary

 # string is printed one time only

 if occur == 2 and nextbit == 0:

 printBinStr(string, length)

 return

 

 # Generate the next bit for

 # str and call recursive

 if currlen == 0: 

 

 # Assign first bit

 string[0] = nextbit

 

 # The next generated bit will 

 # either be 0 or 1

 generateBinStr(string, length,

 currlen + 1, occur, 0)

 generateBinStr(string, length, 

 currlen + 1, occur, 1)

 

 else:

 

 # If pattern "01" occurrence is < 2

 if occur < 2: 

 

 # Set next bit

 string[currlen] = nextbit

 

 # If pattern "01" appears then

 # increase the occurrence of pattern

 if string[currlen - 1] == 0 and nextbit == 1:

 occur += 1

 

 generateBinStr(string, length, 

 currlen + 1, occur, 0)

 generateBinStr(string, length, 

 currlen + 1, occur, 1)

 

 # Else pattern "01" occurrence equals 2

 

 else:

 

 # If previous bit is 0 then next bit cannot be 1

 if string[currlen - 1] == 0 and nextbit == 1: 

 return

 

 # Otherwise

 

 else:

 string[currlen] = nextbit

 generateBinStr(string, length, 

 currlen + 1, occur, 0)

 generateBinStr(string, length,

 currlen + 1, occur, 1)

 

# Driver code

if __name__ == "__main__":

 

 n = 5

 

 # Length of the resulting strings

 # must be at least 4

 if n < 4:

 print(-1)

 else:

 string = [None] * n

 

 # Generate all binary strings of length n

 # with sub-string "01" appearing twice

 generateBinStr(string, n, 0, 0, 0)

 generateBinStr(string, n, 0, 0, 1)

 

# This code is contributed by Rituraj Jain  
  
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

// C# implementation of the above approach

using System;

 

class GFG 

{

 

// Utility function to print the given binary string

static void printBinStr(int[] str, int len) 

{

 for (int i = 0; i < len; i++)

 {

 Console.Write(str[i]);

 }

 Console.Write("\n");

}

 

// This function will be called recursively

// to generate the next bit for given

// binary string according to its current state

static void generateBinStr(int[] str, int len, int currlen,

 int occur, int nextbit) 

{

 

 // Base-case: if the generated binary string

 // meets the required length and the pattern "01"

 // appears twice

 if (currlen == len) 

 {

 

 // nextbit needs to be 0 because each time

 // we call the function recursively,

 // we call 2 times for 2 cases:

 // next bit is 0 or 1

 // The is to assure that the binary

 // string is printed one time only

 if (occur == 2 && nextbit == 0)

 {

 printBinStr(str, len);

 }

 return;

 }

 

 // Generate the next bit for str

 // and call recursive

 if (currlen == 0) 

 {

 

 // Assign first bit

 str[0] = nextbit;

 

 // The next generated bit will wither be 0 or 1

 generateBinStr(str, len, currlen + 1, occur, 0);

 generateBinStr(str, len, currlen + 1, occur, 1);

 } else // If pattern "01" occurrence is < 2

 if (occur < 2) 

 {

 

 // Set next bit

 str[currlen] = nextbit;

 

 // If pattern "01" appears then

 // increase the occurrence of pattern

 if (str[currlen - 1] == 0 && nextbit == 1) 

 {

 occur += 1;

 }

 generateBinStr(str, len, currlen + 1, occur, 0);

 generateBinStr(str, len, currlen + 1, occur, 1);

 

 // Else pattern "01" occurrence equals 2

 } else // If previous bit is 0 then next bit cannot be 1

 if (str[currlen - 1] == 0 && nextbit == 1) 

 {

 return;

 

 // Otherwise

 } 

 else

 {

 str[currlen] = nextbit;

 generateBinStr(str, len, currlen + 1, occur, 0);

 generateBinStr(str, len, currlen + 1, occur, 1);

 }

}

 

// Driver code

public static void Main(String[] args) 

{

 int n = 5;

 

 // Length of the resulting strings

 // must be at least 4

 if (n < 4) 

 {

 Console.Write(-1);

 } 

 else

 {

 int[] str = new int[n];

 

 // Generate all binary strings of length n

 // with sub-string "01" appearing twice

 generateBinStr(str, n, 0, 0, 0);

 generateBinStr(str, n, 0, 0, 1);

 }

}

}

 

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    00101
    01001
    01010
    01011
    01101
    10101
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

