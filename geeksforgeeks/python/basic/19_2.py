Python program to print even length words in a string



Given a string. The task is to print all words with even length in the given
string.

 **Examples:**

    
    
    **Input:** s = "This is a python language"
    **Output:** This
            is
            python
            language 
    
    **Input:** s = "i am muskan"
    **Output:** am
            muskan
            
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Split the string using split() function. Iterate in the words
of a string using for loop. Calculate the length of the word using len()
function. If the length is even, then print the word.

Below is the Python implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to print

# even length words in a string 

 

def printWords(s):

 

 # split the string 

 s = s.split(' ') 

 

 # iterate in words of string 

 for word in s: 

 

 # if length is even 

 if len(word)%2==0:

 print(word) 

 

 

# Driver Code 

s = "i am muskan"

printWords(s)   
  
---  
  
__

__

**Output:**

    
    
    am
    muskan
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

