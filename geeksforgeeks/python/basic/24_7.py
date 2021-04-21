Python code to move spaces to front of string in single traversal



Given a string that has set of words and spaces, write a program to move all
spaces to front of string, by traversing the string only once.

Examples:

    
    
    Input  : str = "geeks for geeks"
    Output : ste = "  geeksforgeeks"
    
    Input  : str = "move these spaces to beginning"
    Output : str = "    movethesespacestobeginning"
    There were four space characters in input,
    all of them should be shifted in front. 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution, please refer Move spaces to front of
string in single traversal link.  
We will solve this problem quickly in Python using List Comprehension.  
 **Approach** :

  1. Traverse input string and create a string without any space character using list comprehension.
  2. Now to know how many space characters were there in original string just take a difference of length of original string and new string.
  3. Now create another string and append space characters at the beginning.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to move spaces to front of string

# in single traversal in Python 

 

def moveSpaces(input): 

 

 # Traverse string to create string without spaces 

 noSpaces = [ch for ch in input if ch!=' '] 

 

 # calculate number of spaces 

 space= len(input) - len(noSpaces) 

 

 # create result string with spaces 

 result = ' '*space 

 

 # concatenate spaces with string having no spaces 

 result = '"'+result + ''.join(noSpaces)+'"'

 print (result) 

 

# Driver program 

if __name__ == "__main__": 

 input = 'geeks for geeks'

 moveSpaces(input)   
  
---  
  
__

__

Output:

    
    
    "  geeksforgeeks"
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

