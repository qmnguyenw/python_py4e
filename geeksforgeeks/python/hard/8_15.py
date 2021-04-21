Python | Convert a list of characters into a string



  
Given a list of characters, merge all of them into a string.

Examples:

    
    
    Input : ['g', 'e', 'e', 'k', 's', 'f', 'o', 
                 'r', 'g', 'e', 'e', 'k', 's']
    Output : geeksforgeeks 
    
    Input : ['p', 'r', 'o', 'g', 'r', 'a', 'm', 
                            'm', 'i', 'n', 'g']
    Output : programming 
    

## Recommended: Please solve it on **__PRACTICE__** first, before moving on to
the solution.

 **Method 1 : Traversal of list**

Initialize an empty string at the beginning. Traverse in the list of
characters, for every index add character to the initial string. After
complete traversal, print the string which has been added with every
character.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert a list

# of character

 

def convert(s):

 

 # initialization of string to ""

 new = ""

 

 # traverse in the string 

 for x in s:

 new += x 

 

 # return string 

 return new

 

 

# driver code 

s = ['g', 'e', 'e', 'k', 's', 'f', 'o',
'r', 'g', 'e', 'e', 'k', 's']

print(convert(s))  
  
---  
  
 __

 __

 **Output:**

    
    
    geeksforgeeks
    

**Method 2 : Using join() function**

By using join() function in python, all characters in the list can be joined.
The syntax is:

    
    
     **str = ""
    str1 = ( "geeks", "for", "geeks" )
    str.join(str1)**

The list of characters can be joined easily by initializing str=”” so that
there are no spaces in between.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert a list

# of character

 

def convert(s):

 

 # initialization of string to ""

 str1 = ""

 

 # using join function join the list s by 

 # separating words by str1

 return(str1.join(s))

 

# driver code 

s = ['g', 'e', 'e', 'k', 's', 'f', 'o',
'r', 'g', 'e', 'e', 'k', 's']

print(convert(s))  
  
---  
  
 __

 __

 **Output:**

    
    
    geeksforgeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

