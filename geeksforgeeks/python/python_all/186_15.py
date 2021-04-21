Python Program for Longest Common Subsequence



 _LCS Problem Statement:_ Given two sequences, find the length of longest
subsequence present in both of them. A subsequence is a sequence that appears
in the same relative order, but not necessarily contiguous. For example,
“abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So
a string of length n has 2^n different possible subsequences.

It is a classic computer science problem, the basis of diff (a file comparison
program that outputs the differences between two files), and has applications
in bioinformatics.

 **Examples:**  
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.  
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

Let the input sequences be X[0..m-1] and Y[0..n-1] of lengths m and n
respectively. And let L(X[0..m-1], Y[0..n-1]) be the length of LCS of the two
sequences X and Y. Following is the recursive definition of L(X[0..m-1],
Y[0..n-1]).

If last characters of both sequences match (or X[m-1] == Y[n-1]) then  
L(X[0..m-1], Y[0..n-1]) = 1 + L(X[0..m-2], Y[0..n-2])

  

  

If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then  
L(X[0..m-1], Y[0..n-1]) = MAX ( L(X[0..m-2], Y[0..n-1]), L(X[0..m-1],
Y[0..n-2])

 __

 __  
 __

 __

 __  
 __  
 __

# A Naive recursive Python implementation of LCS problem

 

def lcs(X, Y, m, n):

 

 if m == 0 or n == 0:

 return 0;

 elif X[m-1] == Y[n-1]:

 return 1 + lcs(X, Y, m-1, n-1);

 else:

 return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));

 

 

# Driver program to test the above function

X = "AGGTAB"

Y = "GXTXAYB"

print ("Length of LCS is ", lcs(X, Y, len(X), len(Y)))  
  
---  
  
 __

 __

 **Output:**

    
    
    Length of LCS is  4
    

Following is a tabulated implementation for the LCS problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Dynamic Programming implementation of LCS problem

 

def lcs(X, Y):

 # find the length of the strings

 m = len(X)

 n = len(Y)

 

 # declaring the array for storing the dp values

 L = [[None]*(n + 1) for i in range(m +
1)]

 

 """Following steps build L[m + 1][n + 1] in bottom up fashion

 Note: L[i][j] contains length of LCS of X[0..i-1]

 and Y[0..j-1]"""

 for i in range(m + 1):

 for j in range(n + 1):

 if i == 0 or j == 0 :

 L[i][j] = 0

 elif X[i-1] == Y[j-1]:

 L[i][j] = L[i-1][j-1]+1

 else:

 L[i][j] = max(L[i-1][j], L[i][j-1])

 

 # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]

 return L[m][n]

# end of function lcs

 

 

# Driver program to test the above function

X = "AGGTAB"

Y = "GXTXAYB"

print("Length of LCS is ", lcs(X, Y))

 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)  
  
---  
  
 __

 __

 **Output:**

    
    
    Length of LCS is  4
    

Please refer complete article on Dynamic Programming | Set 4 (Longest Common
Subsequence) for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

