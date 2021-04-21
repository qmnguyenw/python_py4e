Python | Program that matches a word containing ‘g’ followed by one or more
e’s using regex



 **Prerequisites :** Regular Expressions | Set 1, Set 2

Given a string, the task is to check if that string contains any _g_ followed
by one or more _e’s_ in it, otherwise, print No match.

 **Examples :**

    
    
    **Input :** geeks for geeks
    **Output :** geeks 
             geeks
    
    **Input :** graphic era
    **Output :** No match 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach :** Firstly, make a regular expression (regex) object that matches
a word which contains ‘g’ followed by one or more e’s, then pass a string in
the findall method. This method returns the list of the matched strings.
Loop through the list and print each matched word.

>  **\w –** represent Any letter, numeric digit, or the underscore character.  
>  ***** means zero or more occurrence of the character.  
>  **+** means one or more occurrence of the character.
>
>  
>
>
>  
>

Below is the implementation :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program that matches a word

# containing ‘g’ followed by one or

# more e’s using regex

 

# import re packages

import re

 

# Function check if the any word of

# the string containing 'g' followed

# by one or more e's

def check(string) :

 

 

 # Regex \w * ge+\w * will match 

 # text that contains 'g', followed 

 # by one or more 'e'

 regex = re.compile("ge+\w*")

 

 # The findall() method returns all 

 # matching strings of the regex pattern

 match_object = regex.findall(string)

 

 # If length of match_object is not

 # equal to zero then it contains

 # matched string

 if len(match_object) != 0 :

 

 # looping through the list

 for word in match_object :

 print(word)

 

 else :

 print("No match")

 

 

# Driver Code 

if __name__ == '__main__' :

 

 # Enter the string

 string = "Welcome to geeks for geeks"

 

 # Calling check function

 check(string)  
  
---  
  
 __

 __

 **Output :**

    
    
    geeks
    geeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

