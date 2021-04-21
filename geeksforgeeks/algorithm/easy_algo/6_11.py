Smallest Greater (than S) String of length K whose letters are subset of S



Given a string S of length N consisting of lowercase English letters and an
integer K. Find the lexicographically smallest string T of length K, such that
its set of letters is a subset of the set of letters of S and T is
lexicographically greater than S. _Note: The set of letters is a set, not a
multiset. For example, the set of letters of abadaba is {a, b, d}._

Examples:

> Input : S = “abc”, K = 3  
> Output : T = “aca”  
>  **Explanation** : The list of strings T of length 3, such that the set of
> letters of T is a subset of letters of S is as follows: “aaa”, “aab”, “aac”,
> “aba”, “abb”, “abc”, “aca”, “acb”, …. Among them, those which are
> lexicographically greater than “abc”:  
> “aca”, “acb”, …. Out of those the lexicographically smallest is “aca”.
>
> Input : S = “abc”, K = 2  
> Output : T = “ac”

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **simple solution** is to one by on try all strings of length k in
increasing order. For every string, check if it is greater than S, if yes,
then return it.

Below is an **efficient method** to solve this problem.

  

  

Let’s consider two cases:  
 **1\. If N < K**: For this case, we can simply copy the string S to string T
for upto N characters and for the remaining (K – N) characters we can append
the minimum character (least ASCII value) in string S to string T (K – N)
times since we have to find the lexicographically smallest string which is
just greater than string S.

 **2\. If N ≥ K** : For this case, we need to copy the string S to string T
for upto K characters and then for string T by iterating in reverse direction
we have to replace all those characters by some character until the string T
becomes the lexicographically smallest string greater than string S. For this
we can do the following:

  1. Store the characters of string S in a STL set (ofcourse, in sorted order)
  2. Copy the string S to string T upto K characters.
  3. Iterating in reverse direction, find a character (let it be found at position ‘p’) for which there exists some character having greater ASCII value in the set.
  4. Replace this character with that found in the set.
  5. Replace all characters with minimum character after (p + 1)th index upto Kth index.

 **Illustration:** Let S = “bcegikmyyy”, N = 10, K = 9. Set = { b, c, e, g, i,
k, m, y }. Copy string S to T upto K characters T = “bcegikmyy”. Then
iterating in reverse direction, we first have ‘y’ but there is no greater
character than ‘y’ in the set so move ahead. Again we have ‘y’, move ahead now
we have ‘m’ for which there is a greater character ‘y’ in the set. Replace ‘m’
with ‘y’ and then after ‘m’ in forward direction replace all characters with
minimum character i.e. ‘b’. Hence the string T becomes T = “bcegikybb”;

 __

 __  
 __

 __

 __  
 __  
 __

/* CPP Program to find the lexicographically

 smallest string T greater than S whose

 letters are subset of letters of S */

#include <bits/stdc++.h>

 

using namespace std;

 

// function to find the lexicographically

// smallest string greater than S

string findString(string S, int N, int K)

{

 // stores minimum character

 char minChar = 'z';

 

 // stores unique characters of

 // string in sorted order

 set<char> found;

 

 // Loop through to find the minimum character

 // and stores characters in the set

 for (int i = 0; i < N; i++) {

 found.insert(S[i]);

 if (S[i] < minChar)

 minChar = S[i];

 }

 

 string T;

 

 // Case 1: If N < K

 if (N < K) {

 

 // copy the string S upto N characters

 T = S;

 

 // append minChar to make the remaining 

 // characters

 for (int i = 0; i < (K - N); i++)

 T += minChar;

 }

 

 // Case 2 : If N >= K

 else {

 T = "";

 

 // copy the string S upto K characters

 for (int i = 0; i < K; i++)

 T += S[i];

 

 int i;

 

 // an iterator to the set

 set<char>::iterator it;

 

 // iterating in reverse direction

 for (i = K - 1; i >= 0; i--) {

 

 // find the current character in the set

 it = found.find(T[i]);

 

 // increment the iterator

 it++;

 

 // check if some bigger character exists in set

 if (it != found.end())

 break;

 }

 

 // Replace current character with that found in set

 T[i] = *it;

 

 // Replace all characters after with minChar

 for (int j = i + 1; j < K; j++)

 T[j] = minChar;

 }

 

 return T;

}

 

// Driver Code to test the above function

int main()

{

 string S = "abc";

 int N = S.length();

 

 // Length of required string

 int K = 3;

 

 string T = findString(S, N, K);

 cout << "Lexicographically Smallest String "

 "greater than " << S

 << " is " << T << endl;

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    Lexicographically Smallest String greater than abc is aca
    

Time Complexity: **O(N + K)** , where N is the length of given string and K is
the length of required string.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

