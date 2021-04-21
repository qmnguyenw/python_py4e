Python Program for Longest Palindromic Subsequence | DP-12



Given a sequence, find the length of the longest palindromic subsequence in
it.

![longest-palindromic-subsequence](https://media.geeksforgeeks.org/wp-
content/cdn-uploads/longest-palindromic-subsequence.png)

As another example, if the given sequence is “BBABCBCAB”, then the output
should be 7 as “BABCBAB” is the longest palindromic subseuqnce in it. “BBBBB”
and “BBCBB” are also palindromic subsequences of the given sequence, but not
the longest ones.  
 **1) Optimal Substructure:**  
Let X[0..n-1] be the input sequence of length n and L(0, n-1) be the length of
the longest palindromic subsequence of X[0..n-1].

If last and first characters of X are same, then L(0, n-1) = L(1, n-2) + 2.  
Else L(0, n-1) = MAX (L(1, n-1), L(0, n-2)).  
Following is a general recursive solution with all cases handled.  
 **Dynamic Programming Solution**  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A Dynamic Programming based Python

# program for LPS problem Returns the length

# of the longest palindromic subsequence in seq

def lps(str):

 n = len(str)

 

 # Create a table to store results of subproblems

 L = [[0 for x in range(n)] for x in range(n)]

 

 # Strings of length 1 are palindrome of length 1

 for i in range(n):

 L[i][i] = 1

 

 # Build the table. Note that the lower 

 # diagonal values of table are

 # useless and not filled in the process. 

 # The values are filled in a

 # manner similar to Matrix Chain 

 # Multiplication DP solution (See

 # https://www.geeksforgeeks.org/

 # dynamic-programming-set-8-matrix-chain-multiplication/

 # cl is length of substring

 for cl in range(2, n + 1):

 for i in range(n-cl + 1):

 j = i + cl-1

 if str[i] == str[j] and cl == 2:

 L[i][j] = 2

 elif str[i] == str[j]:

 L[i][j] = L[i + 1][j-1] + 2

 else:

 L[i][j] = max(L[i][j-1], L[i + 1][j]);

 

 return L[0][n-1]

 

# Driver program to test above functions

seq = "GEEKS FOR GEEKS"

n = len(seq)

print("The length of the LPS is " + str(lps(seq)))

 

# This code is contributed by Bhavya Jain  
  
---  
  
 __

 __

 **Output:**

    
    
    The length of the LPS is 7
    

Please refer complete article on Longest Palindromic Subsequence | DP-12 for
more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

