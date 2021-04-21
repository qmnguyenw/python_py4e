Python – Create acronyms from words



Given a string, the task is to write a Python program to extract the acronym
from that string.

 **Examples:**

>  **Input:** Computer Science Engineering
>
>  **Output:** CSE
>
>  **Input:** geeks for geeks
>
>  
>
>
>  
>
>
>  **Output:** GFG
>
>  **Input:** Uttar pradesh
>
>  **Output:** UP

 **Approach 1:**

The following steps are required:

  * Take input as a string.
  * Add the first letter of string to output.
  * Iterate over the full string and add every next letter to space to output.
  * Change the output to uppercase(required acronym).

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function to create acronym

def fxn(stng):

 

 # add first letter

 oupt = stng[0]

 

 # iterate over string

 for i in range(1, len(stng)):

 if stng[i-1] == ' ':

 

 # add letter next to space

 oupt += stng[i]

 

 # uppercase oupt

 oupt = oupt.upper()

 return oupt

 

 

# input string

inpt1 = "Computer Science Engineering"

 

# output acronym

print(fxn(inpt1))

 

# input string

inpt1 = "geeks for geeks"

 

# output acronym

print(fxn(inpt1))

 

# input string

inpt1 = "Uttar pradesh"

 

# output acronym

print(fxn(inpt1))  
  
---  
  
 __

 __

 **Output:**

    
    
    CSE
    GFG
    UP

 **Approach 2:**

The following steps are required:

  * Take input as a string.
  * Split the words.
  * Iterate over words and add the first letter to output.
  * Change the output to uppercase(required acronym).

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function to create acronym

def fxn(stng):

 

 # get all words

 lst = stng.split()

 oupt = ""

 

 # iterate over words

 for word in lst:

 

 # get first letter of each word

 oupt += word[0]

 

 # uppercase oupt

 oupt = oupt.upper()

 return oupt

 

 

# input string

inpt1 = "Computer Science Engineering"

 

# output acronym

print(fxn(inpt1))

 

# input string

inpt1 = "geeks for geeks"

 

# output acronym

print(fxn(inpt1))

 

# input string

inpt1 = "Uttar pradesh"

 

# output acronym

print(fxn(inpt1))  
  
---  
  
 __

 __

 **Output:**

    
    
    CSE
    GFG
    UP

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

