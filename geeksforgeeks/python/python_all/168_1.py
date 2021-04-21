Check if the binary representation of a number has equal number of 0s and 1s
in blocks



Given an integer N, the task is to check if its equivalent binary number has
the equal frequency of consecutive blocks of 0 and 1. Note that 0 and a number
with all 1s are not considered to have number of blocks of 0s and 1s.

 **Examples:**

> **Input:** N = 5  
> **Output:** Yes  
> Equivalent binary number of 5 is 101.  
> The first block is of 1 with length 1, the second block is of 0 with length
> 1  
> and the third block is of 1 is also of length 1. So, all blocks of 0 and 1
> have an equal frequency which is 1.
>
>  **Input:** N = 51  
> **Output:** Yes  
> Equivalent binary number of 51 is 110011.
>
>  **Input:** 8  
> **Output:** No
>
>  
>
>
>  
>
>
>  **Input:** 7  
> **Output:** No

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Simple Approach:** First convert the integer to its equivalent binary
number. Traverse binary string from left to right, for each block of 1 or 0,
find its length and add it in a set. If length of set is 1, print “Yes” else
print “No”.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above

// approach 

#include <bits/stdc++.h>

using namespace std;

// Function to check

void hasEqualBlockFrequency(int N)

{

 // Converting integer to its equivalent 

 // binary number

 string S = bitset<3> (N).to_string();

 set<int> p;

 int c = 1;

 for(int i = 0; i < S.length(); i++)

 {

 // If adjacent character are same 

 // then increase counter

 if (S[i] == S[i + 1])

 c += 1;

 else

 {

 p.insert(c);

 c = 1;

 }

 p.insert(c);

 }

 if (p.size() == 1)

 cout << "Yes" << endl;

 else

 cout << "No" << endl;

}

// Driver code

int main()

{

 int N = 5;

 hasEqualBlockFrequency(N);

 return 0;

}

// This code is contributed by divyesh072019  
  
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

// Java implementation of the above

// approach 

import java.util.*;

 

class GFG{

 

// Function to check

static void hasEqualBlockFrequency(int N)

{

 

 // Converting integer to its equivalent 

 // binary number

 String S = Integer.toString(N,2);

 HashSet<Integer> p = new HashSet<Integer>();

 int c = 1;

 

 for(int i = 0; i < S.length() - 1; i++)

 {

 

 // If adjacent character are same 

 // then increase counter

 if (S.charAt(i) == S.charAt(i + 1))

 c += 1;

 

 else

 {

 p.add(c);

 c = 1;

 }

 p.add(c);

 }

 

 if (p.size() == 1)

 System.out.println("Yes");

 else

 System.out.println("No");

}

 

// Driver Code

public static void main(String []args)

{

 int N = 5;

 

 hasEqualBlockFrequency(N);

}

}

// This code is contributed by rutvik_56  
  
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

# Python3 implementation of the above

# approach

 

# Function to check

def hasEqualBlockFrequency(N):

 

 # Converting integer to its equivalent

 # binary number

 S = bin(N).replace("0b", "")

 p = set()

 c = 1

 for i in range(len(S)-1):

 # If adjacent character are same

 # then increase counter

 if (S[i] == S[i + 1]):

 c += 1

 else:

 p.add(c)

 c = 1

 p.add(c)

 if (len(p) == 1):

 print("Yes")

 else:

 print("No")

# Driver code

N = 5

hasEqualBlockFrequency(N)  
  
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

// C# implementation of the above

// approach 

using System;

using System.Collections.Generic;

class GFG{

 

// Function to check

static void hasEqualBlockFrequency(int N)

{

 

 // Converting integer to its equivalent 

 // binary number

 string S = Convert.ToString(N, 2);

 HashSet<int> p = new HashSet<int>();

 int c = 1;

 

 for(int i = 0; i < S.Length - 1; i++)

 {

 

 // If adjacent character are same 

 // then increase counter

 if (S[i] == S[i + 1])

 c += 1;

 

 else

 {

 p.Add(c);

 c = 1;

 }

 p.Add(c);

 }

 

 if (p.Count == 1)

 Console.WriteLine("Yes");

 else

 Console.WriteLine("No");

}

// Driver Code

static void Main()

{

 int N = 5;

 

 hasEqualBlockFrequency(N);

}

}

// This code is contributed by divyeshrabadiya07  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

**Optimized Solution :** We traverse from last bit. We first count number of
same bits in the last block. We then traverse through all bits, for every
block, we count number of same bits and if this count is not same as first
count, we return false. If all blocks have same count, we return true.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to check if a number has

// same counts of 0s and 1s in every

// block.

#include <iostream>

using namespace std;

// function to convert decimal to binary

bool isEqualBlock(int n)

{

 // Count same bits in last block

 int first_bit = n % 2;

 int first_count = 1;

 n = n / 2;

 while (n % 2 == first_bit && n > 0) {

 n = n / 2;

 first_count++;

 }

 // If n is 0 or it has all 1s,

 // then it is not considered to

 // have equal number of 0s and

 // 1s in blocks.

 if (n == 0)

 return false;

 // Count same bits in all remaining blocks.

 while (n > 0) {

 int first_bit = n % 2;

 int curr_count = 1;

 n = n / 2;

 while (n % 2 == first_bit) {

 n = n / 2;

 curr_count++;

 }

 if (curr_count != first_count)

 return false;

 }

 return true;

}

// Driver program to test above function

int main()

{

 int n = 51;

 if (isEqualBlock(n))

 cout << "Yes";

 else

 cout << "No";

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

// Java program to check if a number has

// same counts of 0s and 1s in every

// block.

import java.io.*;

class GFG

{

// function to convert decimal to binary

static boolean isEqualBlock(int n)

{

 // Count same bits in last block

 int first_bit = n % 2;

 int first_count = 1;

 n = n / 2;

 while (n % 2 == first_bit && n > 0)

 {

 n = n / 2;

 first_count++;

 }

 // If n is 0 or it has all 1s,

 // then it is not considered to

 // have equal number of 0s and

 // 1s in blocks.

 if (n == 0)

 return false;

 // Count same bits in all remaining blocks.

 while (n > 0)

 {

 first_bit = n % 2;

 int curr_count = 1;

 n = n / 2;

 while (n % 2 == first_bit)

 {

 n = n / 2;

 curr_count++;

 }

 if (curr_count != first_count)

 return false;

 }

 return true;

}

// Driver code

public static void main (String[] args)

{

 int n = 51;

 if (isEqualBlock(n))

 System.out.println( "Yes");

 else

 System.out.println("No");

}

}

// This code is contributed by inder_mca  
  
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

# Python3 program to check if a number has

# same counts of 0s and 1s in every block.

# Function to convert decimal to binary

def isEqualBlock(n):

 # Count same bits in last block

 first_bit = n % 2

 first_count = 1

 n = n // 2

 while n % 2 == first_bit and n > 0:

 n = n // 2

 first_count += 1

 # If n is 0 or it has all 1s,

 # then it is not considered to

 # have equal number of 0s and

 # 1s in blocks.

 if n == 0:

 return False

 # Count same bits in all remaining blocks.

 while n > 0:

 first_bit = n % 2

 curr_count = 1

 n = n // 2

 while n % 2 == first_bit:

 n = n // 2

 curr_count += 1

 

 if curr_count != first_count:

 return False

 

 return True

# Driver Code

if __name__ == "__main__":

 n = 51

 if isEqualBlock(n):

 print("Yes")

 else:

 print("No")

 

# This code is contributed by

# Rituraj Jain  
  
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

// C# program to check if a number has

// same counts of 0s and 1s in every

// block.

using System;

class GFG

{

 // function to convert decimal to binary

 static bool isEqualBlock(int n)

 {

 // Count same bits in last block

 int first_bit = n % 2;

 int first_count = 1;

 n = n / 2;

 while (n % 2 == first_bit && n > 0)

 {

 n = n / 2;

 first_count++;

 }

 

 // If n is 0 or it has all 1s,

 // then it is not considered to

 // have equal number of 0s and

 // 1s in blocks.

 if (n == 0)

 return false;

 

 // Count same bits in all remaining blocks.

 while (n > 0)

 {

 

 first_bit = n % 2;

 int curr_count = 1;

 n = n / 2;

 

 while (n % 2 == first_bit)

 {

 n = n / 2;

 curr_count++;

 }

 

 if (curr_count != first_count)

 return false;

 }

 return true;

 }

 

 // Driver code

 public static void Main ()

 {

 int n = 51;

 

 if (isEqualBlock(n))

 Console.WriteLine( "Yes");

 else

 Console.WriteLine("No");

 }

}

// This code is contributed by Ryuga  
  
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

// PHP program to check if a number has

// same counts of 0s and 1s in every

// block.

// function to convert decimal to binary

function isEqualBlock($n)

{

 // Count same bits in last block

 $first_bit = $n % 2;

 $first_count = 1;

 $n = (int)($n / 2);

 while ($n % 2 == $first_bit && $n > 0)

 {

 $n = (int)($n / 2);

 $first_count++;

 }

 // If n is 0 or it has all 1s, then

 // it is not considered to have equal

 // number of 0s and 1s in blocks.

 if ($n == 0)

 return false;

 // Count same bits in all remaining blocks.

 while ($n > 0)

 {

 $first_bit = $n % 2;

 $curr_count = 1;

 $n = (int)($n / 2);

 while ($n % 2 == $first_bit)

 {

 $n = (int)($n / 2);

 $curr_count++;

 }

 if ($curr_count != $first_count)

 return false;

 }

 return true;

}

// Driver Code

$n = 51;

if (isEqualBlock($n))

 echo "Yes";

else

 echo "No";

// This code is contributed by

// Shivi_Aggarwal

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

// javascript program to check if a number has

// same counts of 0s and 1s in every

// block.

// function to convert decimal to binary

function isEqualBlock(n)

{

 // Count same bits in last block

 var first_bit = n % 2;

 var first_count = 1;

 n = n / 2;

 while (n % 2 == first_bit && n > 0)

 {

 n = n / 2;

 first_count++;

 }

 // If n is 0 or it has all 1s,

 // then it is not considered to

 // have equal number of 0s and

 // 1s in blocks.

 if (n == 0)

 return false;

 // Count same bits in all remaining blocks.

 while (n > 0)

 {

 first_bit = n % 2;

 var curr_count = 1;

 n = n / 2;

 while (n % 2 == first_bit)

 {

 n = n / 2;

 curr_count++;

 }

 if (curr_count != first_count)

 return false;

 }

 return true;

}

// Driver code

var n = 51;

if (isEqualBlock(n))

 document.write( "Yes");

else

 document.write("No");

// This code contributed by shikhasingrajput

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

