Python sorted() to check if two strings are anagram or not



Given two strings s1 and s2, check if both the strings are anagrams of each
other.  
Examples:

    
    
    **Input :** s1 = "listen"
            s2 = "silent"
    **Output :** The strings are anagrams.
    
    
    **Input :** s1 = "dad"
            s2 = "bad"
    **Output :** The strings aren't anagrams.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

Python provides a inbuilt function sorted() which does not modify the original
string, but returns sorted string.  
Below is the Python implementation of the above approach:

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# function to check if two strings are

# anagram or not

def check(s1, s2):

 

 # the sorted strings are checked

 if(sorted(s1)== sorted(s2)):

 print("The strings are anagrams.")

 else:

 print("The strings aren't anagrams.") 

 

# driver code 

s1 ="listen"

s2 ="silent"

check(s1, s2)  
  
---  
  
 __

 __

 **Output**

    
    
    The strings are anagrams.
    

### Method #2:Using Counter() function

  * Count all the frequencies of 1st string and 2 and using counter()
  * If they are equal then print anagram

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for the above approach

from collections import Counter

# function to check if two strings are

# anagram or not

def check(s1, s2):

 

 # implementing counter function

 if(Counter(s1) == Counter(s2)):

 print("The strings are anagrams.")

 else:

 print("The strings aren't anagrams.")

# driver code

s1 = "listen"

s2 = "silent"

check(s1, s2)  
  
---  
  
 __

 __

 **Output**

    
    
    The strings are anagrams.
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

