Check if both halves of the string have same set of characters in Python



Given a string of lowercase characters only, the task is to check if it is
possible to split a string from middle which will gives two halves having the
same characters and same frequency of each character. If the length of the
given string is ODD then ignore the middle element and check for the rest.

Examples:

    
    
    Input : abbaab
    Output : NO
    The two halves contain the same characters
    but their frequencies do not match so they
    are NOT CORRECT
    
    Input : abccab
    Output : YES
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution, please refer Check if both halves of the
string have same set of characters link. We will solve this problem in Python
quickly using **Dictionary** comparison.

Approach is very simple :

  

  

  1. Break string in two parts and convert both parts into dictionary using Counter(iterator) method, each dictionary contains it’s character as key and frequency as value.
  2. Now compare these two dictionaries. In python we can compare two using **==** operator, it first checks keys of both dictionaries are same or not, then it checks for values of each key. If everything is equal that means two dictionaries are identical.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to Check if both halves of

# the string have same set of characters 

from collections import Counter 

 

def checkTwoHalves(input): 

 

 length = len(input) 

 

 # Break input string in two parts 

 if (length % 2 != 0): 

 first = input[0:length // 2] 

 second = input[(length // 2) + 1:] 

 else: 

 first = input[0:length // 2] 

 second = input[length // 2:] 

 

 # Convert both halves into dictionary and compare 

 if Counter(first) == Counter(second): 

 print ('YES')

 else: 

 print ('NO')

 

# Driver program 

if __name__ == "__main__": 

 input = 'abbaab'

 checkTwoHalves(input)   
  
---  
  
__

__

**Output:**

    
    
    NO
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

