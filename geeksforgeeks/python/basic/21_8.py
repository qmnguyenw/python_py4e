Python String | strip()



The _**strip() method**_ in-built function of Python is used to remove all the
leading and trailing spaces from a string.

>  **Syntax :** string.strip([chars])
>
>  **Parameter:**
>
>  **chars(optional):** Character or a set of characters, that needs to be
> removed from the string.
>
>  **Returns:** A copy of the string with both leading and trailing characters
> stripped.
>
>  
>
>
>  
>

#### Using strip() method:

  * In case the character of the string to the left doesn’t match with the characters in the _char_ parameter, the method stops removing the leading characters.
  * In case the character of the string to the right doesn’t match with the characters in the _char_ parameter, the method stops removing the trailing characters.

 **Example #1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate the working of strip()

string = ' Geeks for Geeks '

# Leading spaces are removed

print(string.strip())

# Geeks is removed

print(string.strip(' Geeks'))

# Not removed since the spaces do not match

print(string.strip('Geeks'))  
  
---  
  
 __

 __

 **Output :**

    
    
    Geeks for Geeks
    for
       Geeks for Geeks   

**Example #2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate the working of strip()

string = '@@@@Geeks for Geeks@@@@@'

# Strip all '@' from beginning and ending

print(string.strip('@'))

string = 'www.Geeksforgeeks.org'

# '.grow' removes 'www' and 'org' and '.'

print(string.strip('.grow'))  
  
---  
  
 __

 __

 **Output:**

    
    
    Geeks for Geeks
    Geeksforgeeks

 **Example #3:**  
The following code shows an application of strip() in python.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to check for identifiers

def Count(string):

 print("Length before strip()")

 print(len(string))

 # Using strip() to remove white spaces

 str = string.strip()

 print("Length after removing spaces")

 return str

# Driver Code

string = " Geeks for Geeks "

print(len(Count(string)))  
  
---  
  
 __

 __

 **Output:**

    
    
    Length before strip()
    17
    Length after removing spaces
    15

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

