Find the first repeated word in a string in Python using Dictionary



 **Prerequisite :** Dictionary data structure

Given a string, Find the 1st repeated word in a string.  
Examples:

    
    
    Input : "Ravi had been saying that he had been there"
    Output : had
     
    Input : "Ravi had been saying that"
    Output : No Repetition
    
    Input : "he had had he"
    Output : he
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Find the first
repeated word in a string link. We can solve this problem quickly in python
using Dictionary data structure. Approach is simple,

  1. First split given string separated by space.
  2. Now convert list of words into dictionary using collections.Counter(iterator) method. Dictionary contains words as key and it’s frequency as value.
  3. Now traverse list of words again and check which first word has frequency greater than 1.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to Find the first repeated word in a string

from collections import Counter 

 

def firstRepeat(input): 

 

 # first split given string separated by space 

 # into words 

 words = input.split(' ') 

 

 # now convert list of words into dictionary 

 dict = Counter(words) 

 

 # traverse list of words and check which first word 

 # has frequency > 1 

 for key in words: 

 if dict[key]>1: 

 print (key) 

 return

 

# Driver program 

if __name__ == "__main__": 

 input = 'Ravi had been saying that he had been there'

 firstRepeat(input)   
  
---  
  
__

__

Output:

    
    
    had
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

