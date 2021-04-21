Python Program for KMP Algorithm for Pattern Searching



Given a text _txt[0..n-1]_ and a pattern _pat[0..m-1]_ , write a function
_search(char pat[], char txt[])_ that prints all occurrences of _pat[]_ in
_txt[]_. You may assume that _n > m_.

 **Examples:**

    
    
    Input:  txt[] = "THIS IS A TEST TEXT"
            pat[] = "TEST"
    Output: Pattern found at index 10
    
    Input:  txt[] =  "AABAACAADAABAABA"
            pat[] =  "AABA"
    Output: Pattern found at index 0
            Pattern found at index 9
            Pattern found at index 12
    ![pattern-searching](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Pattern-Searching-2-1.png)
    

## Recommended: Please solve it on “ ** _ _PRACTICE__** ” first, before moving
on to the solution.  

  

  

Pattern searching is an important problem in computer science. When we do
search for a string in notepad/word file or browser or database, pattern
searching algorithms are used to show the search results.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for KMP Algorithm

def KMPSearch(pat, txt):

 M = len(pat)

 N = len(txt)

 

 # create lps[] that will hold the longest prefix suffix 

 # values for pattern

 lps = [0]*M

 j = 0 # index for pat[]

 

 # Preprocess the pattern (calculate lps[] array)

 computeLPSArray(pat, M, lps)

 

 i = 0 # index for txt[]

 while i < N:

 if pat[j] == txt[i]:

 i += 1

 j += 1

 

 if j == M:

 print "Found pattern at index " + str(i-j)

 j = lps[j-1]

 

 # mismatch after j matches

 elif i < N and pat[j] != txt[i]:

 # Do not match lps[0..lps[j-1]] characters,

 # they will match anyway

 if j != 0:

 j = lps[j-1]

 else:

 i += 1

 

def computeLPSArray(pat, M, lps):

 len = 0 # length of the previous longest prefix suffix

 

 lps[0] # lps[0] is always 0

 i = 1

 

 # the loop calculates lps[i] for i = 1 to M-1

 while i < M:

 if pat[i]== pat[len]:

 len += 1

 lps[i] = len

 i += 1

 else:

 # This is tricky. Consider the example.

 # AAACAAAA and i = 7. The idea is similar 

 # to search step.

 if len != 0:

 len = lps[len-1]

 

 # Also, note that we do not increment i here

 else:

 lps[i] = 0

 i += 1

 

txt = "ABABDABACDABABCABAB"

pat = "ABABCABAB"

KMPSearch(pat, txt)

 

# This code is contributed by Bhavya Jain  
  
---  
  
 __

 __

 **Output:**

    
    
    Found pattern at index 10
    

Please refer complete article on KMP Algorithm for Pattern Searching for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

