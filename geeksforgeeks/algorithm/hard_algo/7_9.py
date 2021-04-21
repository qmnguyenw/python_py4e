Sum of similarities of string with all of its suffixes



Given a string **str** , the task is to find the sum of the similarities of
**str** with each of its suffixes.  
The similarity of strings **A** and **B** is the length of the longest prefix
common to both the strings i.e. the similarity of “aabc” and “aab” is **3**
and that of “qwer” and “abc” is **0**.

 **Examples:**

>  **Input:** str = “ababa”  
>  **Output:** 9  
> The suffixes of str are “ababa”, “baba”, “aba”, “ba” and “a”. The
> similarities of these strings with the original string “ababa” are 5, 0, 3,
> 0 & 1 respectively.  
> Thus, the answer is 5 + 0 + 3 + 0 + 1 = 9.
>
>  **Input:** str = “aaabaab”  
>  **Output:** 13

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Compute Z-array using Z-algorithm – For a string str[0..n-1], Z
array is of same length as string. An element Z[i] of Z array stores length of
the longest substring starting from str[i] which is also a prefix of
str[0..n-1]. The first entry of Z array is the length of the string.  
Now, sum all the elements of the Z-array to get the required sum of the
similarities.

  

  

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

#include <string>

#include <vector>

using namespace std;

 

// Function to calculate the Z-array for the given string

void getZarr(string str, int n, int Z[])

{

 int L, R, k;

 

 // [L, R] make a window which matches with prefix of s

 L = R = 0;

 for (int i = 1; i < n; ++i) {

 

 // if i>R nothing matches so we will calculate.

 // Z[i] using naive way.

 if (i > R) {

 L = R = i;

 

 // R-L = 0 in starting, so it will start

 // checking from 0'th index. For example,

 // for "ababab" and i = 1, the value of R

 // remains 0 and Z[i] becomes 0. For string

 // "aaaaaa" and i = 1, Z[i] and R become 5

 while (R < n && str[R - L] == str[R])

 R++;

 Z[i] = R - L;

 R--;

 }

 else {

 

 // k = i-L so k corresponds to number which

 // matches in [L, R] interval.

 k = i - L;

 

 // if Z[k] is less than remaining interval

 // then Z[i] will be equal to Z[k].

 // For example, str = "ababab", i = 3, R = 5

 // and L = 2

 if (Z[k] < R - i + 1)

 Z[i] = Z[k];

 

 // For example str = "aaaaaa" and i = 2, R is 5,

 // L is 0

 else {

 // else start from R and check manually

 L = i;

 while (R < n && str[R - L] == str[R])

 R++;

 Z[i] = R - L;

 R--;

 }

 }

 }

}

 

// Function to return the similarity sum

int sumSimilarities(string s, int n)

{

 int Z[n] = { 0 };

 

 // Compute the Z-array for the given string

 getZarr(s, n, Z);

 

 int total = n;

 

 // Summation of the Z-values

 for (int i = 1; i < n; i++)

 total += Z[i];

 

 return total;

}

 

// Driver code

int main()

{

 string s = "ababa";

 int n = s.length();

 

 cout << sumSimilarities(s, n);

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

 

public class GFG{

 

// Function to calculate the Z-array for the given string

static void getZarr(String str, int n, int Z[])

{

 int L, R, k;

 

 // [L, R] make a window which matches with prefix of s

 L = R = 0;

 for (int i = 1; i < n; ++i) {

 

 // if i>R nothing matches so we will calculate.

 // Z[i] using naive way.

 if (i > R) {

 L = R = i;

 

 // R-L = 0 in starting, so it will start

 // checking from 0'th index. For example,

 // for "ababab" and i = 1, the value of R

 // remains 0 and Z[i] becomes 0. For string

 // "aaaaaa" and i = 1, Z[i] and R become 5

 while (R < n && str.charAt(R - L) == str.charAt(R))

 R++;

 Z[i] = R - L;

 R--;

 }

 else {

 

 // k = i-L so k corresponds to number which

 // matches in [L, R] interval.

 k = i - L;

 

 // if Z[k] is less than remaining interval

 // then Z[i] will be equal to Z[k].

 // For example, str = "ababab", i = 3, R = 5

 // and L = 2

 if (Z[k] < R - i + 1)

 Z[i] = Z[k];

 

 // For example str = "aaaaaa" and i = 2, R is 5,

 // L is 0

 else {

 // else start from R and check manually

 L = i;

 while (R < n && str.charAt(R - L) == str.charAt(R))

 R++;

 Z[i] = R - L;

 R--;

 }

 }

 }

}

 

// Function to return the similarity sum

static int sumSimilarities(String s, int n)

{

 int Z[] = new int[n] ;

 

 // Compute the Z-array for the given string

 getZarr(s, n, Z);

 

 int total = n;

 

 // Summation of the Z-values

 for (int i = 1; i < n; i++)

 total += Z[i];

 

 return total;

}

 

// Driver code

public static void main(String []args)

{

 String s = "ababa";

 int n = s.length();

 

 System.out.println(sumSimilarities(s, n));

}

// This code is contributed by Ryuga

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

# Python3 implementation of the approach

def getZarr(s, n, Z):

 L, R, k = 0, 0, 0

 

 # [L, R] make a window which matches

 # with prefix of s

 for i in range(n):

 # if i>R nothing matches so we will 

 # calculate Z[i] using naive way.

 if i > R:

 L, R = i, i

 

 '''

 R-L = 0 in starting, so it will start 

 checking from 0'th index. For example, 

 for "ababab" and i = 1, the value of R 

 remains 0 and Z[i] becomes 0. For string 

 "aaaaaa" and i = 1, Z[i] and R become 5

 '''

 while R < n and s[R - L] == s[R]:

 R += 1

 Z[i] = R - L

 R -= 1

 else:

 

 # k = i-L so k corresponds to number 

 # which matches in [L, R] interval.

 k = i - L

 

 # if Z[k] is less than remaining interval 

 # then Z[i] will be equal to Z[k]. 

 # For example, str = "ababab", i = 3, R = 5 

 # and L = 2 

 if Z[k] < R - i + 1:

 Z[i] = Z[k]

 else:

 L = i

 while R < n and s[R - L] == s[R]:

 R += 1

 Z[i] = R - L

 R -= 1

 

def sumSimilarities(s, n):

 Z = [0 for i in range(n)]

 

 # Compute the Z-array for the 

 # given string

 getZarr(s, n, Z)

 

 total = n

 

 # summation of the Z-values

 for i in range(n):

 total += Z[i]

 return total

 

# Driver Code

s = "ababa"

 

n = len(s)

 

print(sumSimilarities(s, n))

 

# This code is contributed 

# by Mohit kumar 29  
  
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

//C# implementation of the above approach

using System;

 

public class GFG{

 // Function to calculate the Z-array for the given string

static void getZarr(string str, int n, int []Z)

{

 int L, R, k;

 

 // [L, R] make a window which matches with prefix of s

 L = R = 0;

 for (int i = 1; i < n; ++i) {

 

 // if i>R nothing matches so we will calculate.

 // Z[i] using naive way.

 if (i > R) {

 L = R = i;

 

 // R-L = 0 in starting, so it will start

 // checking from 0'th index. For example,

 // for "ababab" and i = 1, the value of R

 // remains 0 and Z[i] becomes 0. For string

 // "aaaaaa" and i = 1, Z[i] and R become 5

 while (R < n && str[R - L] == str[R])

 R++;

 Z[i] = R - L;

 R--;

 }

 else {

 

 // k = i-L so k corresponds to number which

 // matches in [L, R] interval.

 k = i - L;

 

 // if Z[k] is less than remaining interval

 // then Z[i] will be equal to Z[k].

 // For example, str = "ababab", i = 3, R = 5

 // and L = 2

 if (Z[k] < R - i + 1)

 Z[i] = Z[k];

 

 // For example str = "aaaaaa" and i = 2, R is 5,

 // L is 0

 else {

 // else start from R and check manually

 L = i;

 while (R < n && str[R - L] == str[R])

 R++;

 Z[i] = R - L;

 R--;

 }

 }

 }

}

 

// Function to return the similarity sum

static int sumSimilarities(string s, int n)

{

 int []Z = new int[n] ;

 

 // Compute the Z-array for the given string

 getZarr(s, n, Z);

 

 int total = n;

 

 // Summation of the Z-values

 for (int i = 1; i < n; i++)

 total += Z[i];

 

 return total;

}

 

// Driver code

 static public void Main (){

 

 string s = "ababa";

 int n = s.Length;

 

 Console.WriteLine(sumSimilarities(s, n));

}

// This code is contributed by ajit.

}  
  
---  
  
 __

 __

 **Output:**

    
    
    9
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

