Python | Swap commas and dots in a String



The problem is quite simple. Given a string, we need to replace all commas
with dots and all dots with the commas. This can be achieved in two popular
ways.  
Examples:

    
    
    Input : 14, 625, 498.002
    Output : 14.625.498, 002 

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Using maketrans and translate()**

 **maketrans:** This static method returns a translation table usable for
_str.translate()_. This builds a translation table, which is a mapping of
integers or characters to integers, strings, or None.  
 **translate:** This returns a copy of the string where all characters
occurring in the optional argument are removed, and the remaining characters
have been mapped through the translation table, given by the maketrans table.  
For more reference visit Python String Methods.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to replace, with . and vice-versa

def Replace(str1):

 maketrans = str1.maketrans

 final = str1.translate(maketrans(',.', '.,', ' '))

 return final.replace(',', ", ")

# Driving Code

string = "14, 625, 498.002"

print(Replace(string))  
  
---  
  
 __

 __

 **Output:**

    
    
    14.625.498, 002

 **Using replace()**

  

  

This is more of a logical approach in which we swap the symbols considering
third variables. The replace method can also be used to replace the methods in
strings. We can convert “, ” to a symbol then convert “.” to “, ” and the
symbol to “.”. For more reference visit Python String Methods.  
Example:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def Replace(str1):

 str1 = str1.replace(', ', 'third')

 str1 = str1.replace('.', ', ')

 str1 = str1.replace('third', '.')

 return str1

 

string = "14, 625, 498.002"

print(Replace(string))  
  
---  
  
 __

 __

 **Output:**

    
    
    14.625.498, 002

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

