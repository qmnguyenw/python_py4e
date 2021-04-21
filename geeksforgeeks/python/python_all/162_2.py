Python | Find longest consecutive letter and digit substring



Given a String (may contain both letters and digits), write a Python program
to find the longest consecutive letter and digit substring.

 **Examples:**

    
    
    **Input :** geeks123available
    **Output :** ('available', 123)
    
    **Input :** 98apple658pine
    **Output :** ('apple', 658)
    

  
**Approach #1 :** Brute force  
This is the Naive or brute force approach to find the longest consecutive
letter and digit substring. We take two string type variable _longest_letter_
and _longest_digit_. We start a loop and check for consecutive substrings of
letter and digit. In each iteration, we check if the current letter substring
is longer than the longest letter or digit substring respectively. If yes, we
assign the current substring of letter and digit to the longest letter and
digit substring respectively. Otherwise, do nothing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find the longest

# consecutive substring of a certain type

import re

 

def longestSubstring(s):

 

 longest_letterSeq = ''

 longest_digitSeq = ''

 i = 0

 while(i<len(s)):

 

 curr_letterSeq = ''

 curr_digitSeq = ''

 

 # For letter substring 

 while(i<len(s) and s[i].isalpha()):

 curr_letterSeq += s[i]

 i+= 1

 

 # For digit substring

 while(i<len(s) and s[i].isdigit()):

 curr_digitSeq += s[i]

 i+= 1

 

 # Case handling if the character 

 # is neither letter nor digit 

 if(i< len(s) and not(s[i].isdigit()) 

 and not(s[i].isalpha())) :

 i+= 1

 

 if(len(curr_letterSeq) > len(longest_letterSeq) ):

 longest_letterSeq = curr_letterSeq

 

 if(len(curr_digitSeq) > len(longest_digitSeq) ):

 longest_digitSeq = curr_digitSeq

 

 return longest_letterSeq, longest_digitSeq

 

# Driver Code

str = '3Geeksfor123geeks3'

print(longestSubstring(str))  
  
---  
  
 __

 __

 **Output:**

    
    
    ('Geeksfor', '123')
    

  
**Approach #2 :** Using Python regex  
Python Regex is another method to solve the given problem. Find the substring
sequence of digits and letters using Python regex and then find the longest
substring length respectively.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find the longest

# consecutive substring of a certain type

import re

 

def longestSubstring(str):

 letter = max(re.findall(r'\D+', str), key = len)

 digit = max(re.findall(r'\d+', str), key = len)

 

 return letter, digit

 

# Driver Code

str = 'geeks123geeksforgeeks1'

print(longestSubstring(str))  
  
---  
  
 __

 __

 **Output:**

    
    
    ('geeksforgeeks', '123')
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

