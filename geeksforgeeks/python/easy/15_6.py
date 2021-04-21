Python program to check if a given string is Keyword or not



Given a string, write a Python program that checks if the given string is
keyword or not.

  * Keywords are reserved words which cannot be used as variable names.
  * There are 33 keywords in Python programming language.(in python 3.6.2 version)

 **Examples:**

    
    
    **Input:** str = "geeks"
    **Output:** geeks is not a keyword
    
    **Input:** str = "for"
    **Output:** for is a keyword
    

We can always get the list of keywords in the current Python version using
kwlist method in keyword module.

 __

 __  
 __

 __

 __  
 __  
 __

# import keyword library

import keyword

 

keyword_list = keyword.kwlist

print("No. of keywords present in current version :",

 len(keyword_list))

 

print(keyword_list)  
  
---  
  
 __

 __

 **Output:**

> No. of keywords present in current version : 33  
> [‘False’, ‘None’, ‘True’, ‘and’, ‘as’, ‘assert’, ‘break’, ‘class’,
> ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘finally’, ‘for’,
> ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘nonlocal’, ‘not’,
> ‘or’, ‘pass’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’]
>
>  
>
>
>  
>

Below is the Python code to check if a given string is Keyword or not:

 __

 __  
 __

 __

 __  
 __  
 __

# include keyword library in this program

import keyword

 

# Function to check whether the given 

# string is a keyword or not 

def isKeyword(word) :

 

 # kwlist attribute of keyword

 # library return list of keywords

 # present in current version of

 # python language.

 keyword_list = keyword.kwlist

 

 # check word in present in

 # keyword_list or not.

 if word in keyword_list :

 return "Yes"

 else :

 return "No"

 

 

# Driver Code

if __name__ == "__main__" :

 

 print(isKeyword("geeks"))

 print(isKeyword("for"))  
  
---  
  
 __

 __

 **Output:**

    
    
    No
    Yes
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

