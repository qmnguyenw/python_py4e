Minimum number of subsequences required to convert one string to another using
Greedy Algorithm



Given two strings **A** and **B** consists of lowercase letters, the task to
find the minimum number of subsequence required to form **A** from **B**. If
it is impossible to form, print -1.

 **Examples:**

>  **Input:** A = “aacbe”, B = “aceab”  
>  **Output:** 3  
>  **Explanation:**  
>  The minimum number of subsequences required for creating A from B is “aa”,
> “cb” and “e”.
>
>  **Input:** A = “geeks”, B = “geekofthemonth”  
>  **Output:** -1  
>  **Explanation:**  
>  It is not possible to create A, as the character ‘s’ is missing in B.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

For **brute-force approach** refer here  
Minimum number of subsequences required to convert one string to another

  

  

 **Greedy Approach:**

  1. Create a 2D-Array of **26 * size_of_string_B** to store the occurrence of indices of the character and initialize the array with ‘infinite’ values.
  2. Maintain the 2D Array with indices of the character in the String **B**
  3. If the value of any element of the 2D Array is infinite, then update the value with the next value in the same row.
  4. Initialize the position of the pointer to 0
  5. Iterate the String **A** and for each character –
    * If the position of the pointer is 0 and if that position in the 2D Array is infinite, then the character is not present in the string **B**.
    * If the value in the 2D Array is not equal to infinite, then update the value of the position with the value present at the 2D Array for that position of the pointer, Because the characters before it cannot be considered in the subsequence.

Below is the implementation of the above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation for minimum

// number of subsequences required

// to convert one string to another

 

#include <iostream>

using namespace std;

 

// Function to find the minimum number

// of subsequences required to convert

// one string to another

// S2 == A and S1 == B

int findMinimumSubsequences(string A,

 string B){

 

 // At least 1 subsequence is required

 // Even in best case, when A is same as B

 int numberOfSubsequences = 1; 

 

 // size of B

 int sizeOfB = B.size();

 

 // size of A

 int sizeOfA = A.size();

 int inf = 1000000;

 

 // Create an 2D array next[][] 

 // of size 26 * sizeOfB to store 

 // the next occurrence of a character

 // ('a' to 'z') as an index [0, sizeOfA - 1]

 int next[26][sizeOfB];

 

 // Array Initialization with infinite

 for (int i = 0; i < 26; i++) {

 for (int j = 0; j < sizeOfB; j++) {

 next[i][j] = inf;

 }

 }

 

 // Loop to Store the values of index

 for (int i = 0; i < sizeOfB; i++) {

 next[B[i] - 'a'][i] = i;

 }

 

 // If the value of next[i][j]

 // is infinite then update it with 

 // next[i][j + 1]

 for (int i = 0; i < 26; i++) {

 for (int j = sizeOfB - 2; j >= 0; j--) {

 if (next[i][j] == inf) {

 next[i][j] = next[i][j + 1];

 }

 }

 }

 

 // Greedy algorithm to obtain the maximum

 // possible subsequence of B to cover the

 // remaining string of A using next subsequence

 int pos = 0;

 int i = 0;

 

 // Loop to iterate over the string A

 while (i < sizeOfA) {

 

 // Condition to check if the character is 

 // not present in the string B

 if (pos == 0 &&

 next[A[i] - 'a'][pos] == inf) {

 numberOfSubsequences = -1;

 break;

 }

 

 // Condition to check if there 

 // is an element in B matching with 

 // character A[i] on or next to B[pos]

 // given by next[A[i] - 'a'][pos]

 else if (pos < sizeOfB &&

 next[A[i] - 'a'][pos] < inf) {

 int nextIndex = next[A[i] - 'a'][pos] + 1;

 pos = nextIndex;

 i++;

 }

 

 // Condition to check if reached at the end

 // of B or no such element exists on

 // or next to A[pos], thus increment number

 // by one and reinitialise pos to zero

 else {

 numberOfSubsequences++;

 pos = 0;

 }

 }

 return numberOfSubsequences;

}

 

// Driver Code

int main()

{

 string A = "aacbe"; 

 string B = "aceab";

 

cout << findMinimumSubsequences(A, B);

 

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

// Java implementation for minimum

// number of subsequences required

// to convert one String to another

class GFG

{

 

// Function to find the minimum number

// of subsequences required to connvert

// one String to another

// S2 == A and S1 == B

static int findMinimumSubsequences(String A,

 String B)

{

 

 // At least 1 subsequence is required

 // Even in best case, when A is same as B

 int numberOfSubsequences = 1; 

 

 // size of B

 int sizeOfB = B.length();

 

 // size of A

 int sizeOfA = A.length();

 int inf = 1000000;

 

 // Create an 2D array next[][] 

 // of size 26 * sizeOfB to store 

 // the next occurrence of a character

 // ('a' to 'z') as an index [0, sizeOfA - 1]

 int [][]next = new int[26][sizeOfB];

 

 // Array Initialization with infinite

 for (int i = 0; i < 26; i++) {

 for (int j = 0; j < sizeOfB; j++) {

 next[i][j] = inf;

 }

 }

 

 // Loop to Store the values of index

 for (int i = 0; i < sizeOfB; i++) {

 next[B.charAt(i) - 'a'][i] = i;

 }

 

 // If the value of next[i][j]

 // is infinite then update it with 

 // next[i][j + 1]

 for (int i = 0; i < 26; i++) {

 for (int j = sizeOfB - 2; j >= 0; j--) {

 if (next[i][j] == inf) {

 next[i][j] = next[i][j + 1];

 }

 }

 }

 

 // Greedy algorithm to obtain the maximum

 // possible subsequence of B to cover the

 // remaining String of A using next subsequence

 int pos = 0;

 int i = 0;

 

 // Loop to iterate over the String A

 while (i < sizeOfA) {

 

 // Condition to check if the character is 

 // not present in the String B

 if (pos == 0 &&

 next[A.charAt(i)- 'a'][pos] == inf) {

 numberOfSubsequences = -1;

 break;

 }

 

 // Condition to check if there 

 // is an element in B matching with 

 // character A[i] on or next to B[pos]

 // given by next[A[i] - 'a'][pos]

 else if (pos < sizeOfB &&

 next[A.charAt(i) - 'a'][pos] < inf) {

 int nextIndex = next[A.charAt(i) - 'a'][pos] + 1;

 pos = nextIndex;

 i++;

 }

 

 // Condition to check if reached at the end

 // of B or no such element exists on

 // or next to A[pos], thus increment number

 // by one and reinitialise pos to zero

 else {

 numberOfSubsequences++;

 pos = 0;

 }

 }

 return numberOfSubsequences;

}

 

// Driver Code

public static void main(String[] args)

{

 String A = "aacbe"; 

 String B = "aceab";

 

 System.out.print(findMinimumSubsequences(A, B));

}

}

 

// This code is contributed by Rajput-Ji  
  
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

# Python3 implementation for minimum

# number of subsequences required

# to convert one to another

 

# Function to find the minimum number

# of subsequences required to convert

# one to another

# S2 == A and S1 == B

def findMinimumSubsequences(A, B):

 

 # At least 1 subsequence is required

 # Even in best case, when A is same as B

 numberOfSubsequences = 1

 

 # size of B

 sizeOfB = len(B)

 

 # size of A

 sizeOfA = len(A)

 inf = 1000000

 

 # Create an 2D array next[][]

 # of size 26 * sizeOfB to store

 # the next occurrence of a character

 # ('a' to 'z') as an index [0, sizeOfA - 1]

 next = [[ inf for i in range(sizeOfB)] for i in
range(26)]

 

 # Loop to Store the values of index

 for i in range(sizeOfB):

 next[ord(B[i]) - ord('a')][i] = i

 

 # If the value of next[i][j]

 # is infinite then update it with

 # next[i][j + 1]

 for i in range(26):

 for j in range(sizeOfB-2, -1, -1):

 if (next[i][j] == inf):

 next[i][j] = next[i][j + 1]

 

 # Greedy algorithm to obtain the maximum

 # possible subsequence of B to cover the

 # remaining of A using next subsequence

 pos = 0

 i = 0

 

 # Loop to iterate over the A

 while (i < sizeOfA):

 

 # Condition to check if the character is

 # not present in the B

 if (pos == 0 and

 next[ord(A[i]) - ord('a')][pos] == inf):

 numberOfSubsequences = -1

 break

 

 # Condition to check if there

 # is an element in B matching with

 # character A[i] on or next to B[pos]

 # given by next[A[i] - 'a'][pos]

 elif (pos < sizeOfB and

 next[ord(A[i]) - ord('a')][pos] < inf) :

 nextIndex = next[ord(A[i]) - ord('a')][pos] + 1

 pos = nextIndex

 i += 1

 

 # Condition to check if reached at the end

 # of B or no such element exists on

 # or next to A[pos], thus increment number

 # by one and reinitialise pos to zero

 else :

 numberOfSubsequences += 1

 pos = 0

 

 return numberOfSubsequences

 

# Driver Code

if __name__ == '__main__':

 A = "aacbe"

 B = "aceab"

 print(findMinimumSubsequences(A, B))

 

# This code is contributed by mohit kumar 29  
  
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

// C# implementation for minimum

// number of subsequences required

// to convert one String to another

using System;

 

class GFG

{

 

// Function to find the minimum number

// of subsequences required to convert

// one String to another

// S2 == A and S1 == B

static int findMinimumSubsequences(String A,

 String B)

{

 

 // At least 1 subsequence is required

 // Even in best case, when A is same as B

 int numberOfSubsequences = 1; 

 

 // size of B

 int sizeOfB = B.Length;

 

 // size of A

 int sizeOfA = A.Length;

 int inf = 1000000;

 

 // Create an 2D array next[,] 

 // of size 26 * sizeOfB to store 

 // the next occurrence of a character

 // ('a' to 'z') as an index [0, sizeOfA - 1]

 int [,]next = new int[26,sizeOfB];

 

 // Array Initialization with infinite

 for (int i = 0; i < 26; i++)

 {

 for (int j = 0; j < sizeOfB; j++) 

 {

 next[i, j] = inf;

 }

 }

 

 // Loop to Store the values of index

 for (int i = 0; i < sizeOfB; i++)

 {

 next[B[i] - 'a', i] = i;

 }

 

 // If the value of next[i,j]

 // is infinite then update it with 

 // next[i,j + 1]

 for (int i = 0; i < 26; i++) 

 {

 for (int j = sizeOfB - 2; j >= 0; j--)

 {

 if (next[i, j] == inf) 

 {

 next[i, j] = next[i, j + 1];

 }

 }

 }

 

 // Greedy algorithm to obtain the maximum

 // possible subsequence of B to cover the

 // remaining String of A using next subsequence

 int pos = 0;

 int I = 0;

 

 // Loop to iterate over the String A

 while (I < sizeOfA) 

 {

 

 // Condition to check if the character is 

 // not present in the String B

 if (pos == 0 &&

 next[A[I]- 'a', pos] == inf) 

 {

 numberOfSubsequences = -1;

 break;

 }

 

 // Condition to check if there 

 // is an element in B matching with 

 // character A[i] on or next to B[pos]

 // given by next[A[i] - 'a',pos]

 else if (pos < sizeOfB &&

 next[A[I] - 'a',pos] < inf)

 {

 int nextIndex = next[A[I] - 'a',pos] + 1;

 pos = nextIndex;

 I++;

 }

 

 // Condition to check if reached at the end

 // of B or no such element exists on

 // or next to A[pos], thus increment number

 // by one and reinitialise pos to zero

 else

 {

 numberOfSubsequences++;

 pos = 0;

 }

 }

 return numberOfSubsequences;

}

 

// Driver Code

public static void Main(String[] args)

{

 String A = "aacbe"; 

 String B = "aceab";

 

 Console.Write(findMinimumSubsequences(A, B));

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Time Complexity:** O(N), where N is the length of string to be formed (here
A)  
 **Auxiliary Space Complexity:** O(N), where N is the length of string to be
formed (here A)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

