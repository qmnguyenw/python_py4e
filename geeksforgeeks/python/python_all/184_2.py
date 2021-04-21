Python Program for Anagram Substring Search (Or Search for all permutations)



Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function
search(char pat[], char txt[]) that prints all occurrences of pat[] and its
permutations (or anagrams) in txt[]. You may assume that n > m.  
Expected time complexity is O(n)

 **Examples:**

    
    
    1) Input:  txt[] = "BACDGABCDA"  pat[] = "ABCD"
       Output:   Found at Index 0
                 Found at Index 5
                 Found at Index 6
    2) Input: txt[] =  "AAABABAA" pat[] = "AABA"
       Output:   Found at Index 0
                 Found at Index 1
                 Found at Index 4

## We strongly recommend that you click here and practice it, before moving on
to the solution.

  
A simple idea is to modify Rabin Karp Algorithm. For example we can keep the
hash value as sum of ASCII values of all characters under modulo of a big
prime number. For every character of text, we can add the current character to
hash value and subtract the first character of previous window. This solution
looks good, but like standard Rabin Karp, the worst case time complexity of
this solution is O(mn). The worst case occurs when all hash values match and
we one by one match all characters.  
We can achieve O(n) time complexity under the assumption that alphabet size is
fixed which is typically true as we have maximum 256 possible characters in
ASCII. The idea is to use two count arrays:

1) The first count array store frequencies of characters in pattern.  
2) The second count array stores frequencies of characters in current window
of text.

  

  

The important thing to note is, time complexity to compare two count arrays is
O(1) as the number of elements in them are fixed (independent of pattern and
text sizes). Following are steps of this algorithm.  
1) Store counts of frequencies of pattern in first count array _countP[]_.
Also store counts of frequencies of characters in first window of text in
array _countTW[]_.

2) Now run a loop from i = M to N-1. Do following in loop.  
…..a) If the two count arrays are identical, we found an occurrence.  
…..b) Increment count of current character of text in countTW[]  
…..c) Decrement count of first character in previous window in countWT[]

3) The last window is not checked by above loop, so explicitly check it.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to search all

# anagrams of a pattern in a text

 

MAX = 256

 

# This function returns true

# if contents of arr1[] and arr2[]

# are same, otherwise false.

def compare(arr1, arr2):

 for i in range(MAX):

 if arr1[i] != arr2[i]:

 return False

 return True

 

# This function search for all

# permutations of pat[] in txt[] 

def search(pat, txt):

 

 M = len(pat)

 N = len(txt)

 

 # countP[]: Store count of

 # all characters of pattern

 # countTW[]: Store count of

 # current window of text

 countP = [0]*MAX

 

 countTW = [0]*MAX

 

 for i in range(M):

 (countP[ord(pat[i]) ]) += 1

 (countTW[ord(txt[i]) ]) += 1

 

 # Traverse through remaining

 # characters of pattern

 for i in range(M, N):

 

 # Compare counts of current

 # window of text with

 # counts of pattern[]

 if compare(countP, countTW):

 print("Found at Index", (i-M))

 

 # Add current character to current window

 (countTW[ ord(txt[i]) ]) += 1

 

 # Remove the first character of previous window

 (countTW[ ord(txt[i-M]) ]) -= 1

 

 # Check for the last window in text 

 if compare(countP, countTW):

 print("Found at Index", N-M)

 

# Driver program to test above function 

txt = "BACDGABCDA"

pat = "ABCD"

search(pat, txt) 

 

# This code is contributed

# by Upendra Singh Bartwal  
  
---  
  
 __

 __

 **Output:**

    
    
    ('Found at Index', 0)
    ('Found at Index', 5)
    ('Found at Index', 6)
    

Please refer complete article on Anagram Substring Search (Or Search for all
permutations) for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

