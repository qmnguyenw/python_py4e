Python set to check if string is panagram



Given a string, check if the given string is pangram or not.

Examples:

    
    
    Input : The quick brown fox jumps over the lazy dog
    Output : The string is a pangram
    
    Input : geeks for geeks
    Output : The string is not pangram
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A normal way would have been to use frequency table and check if all elements
were present or not. But using **import ascii_lowercase as asc_lower** we
import all the lower characters in set and all characters of string in another
set. In the function, two sets are formed- one for all lower case letters and
one for the letters in the string. The two sets are subtracted and if it is an
empty set, the string is a pangram.

Below is Python implementation of the above approach:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import from string all ascii_lowercase and asc_lower

from string import ascii_lowercase as asc_lower

 

# function to check if all elements are present or not

def check(s):

 return set(asc_lower) - set(s.lower()) == set([])

 

# driver code

strng ="The quick brown fox jumps over the lazy dog"

if(check(strng)== True):

 print("The string is a pangram")

else:

 print("The string isn't a pangram")  
  
---  
  
 __

 __

Output:

    
    
    
    The string is a pangram
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

