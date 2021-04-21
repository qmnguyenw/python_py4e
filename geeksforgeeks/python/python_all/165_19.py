Python | Split string into list of characters



Given a string, write a Python program to split the characters of the given
string into a list.  

**Examples:**

    
    
    **Input :** geeks
    **Output :** ['g', 'e', 'e', 'k', 's']
    
    **Input :** Word
    **Output :** ['W', 'o', 'r', 'd']

  
**Code #1 :** Using List Comprehension  
This approach uses list comprehension to convert each character into a list.
Using the following syntax you can split the characters of a string into a
list.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Split string into characters

def split(word):

 return [char for char in word]

 

# Driver code

word = 'geeks'

print(split(word))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['g', 'e', 'e', 'k', 's']

  
**Code #2 :** Typecasting to list  
Python provides direct typecasting of string into list using list().  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Split string into characters

def split(word):

 return list(word)

 

# Driver code

word = 'geeks'

print(split(word))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['g', 'e', 'e', 'k', 's']

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

