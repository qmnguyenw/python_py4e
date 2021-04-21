Python – Random uppercase in Strings



Given a String, the task is to write a Python program to convert its
characters to uppercase randomly.

 **Examples:**

    
    
     **Input :** test_str = 'geeksforgeeks'
    **Output :** GeeksfORgeeks
    
    **Explanation :** Random elements are converted to Upper case characters.
    
    **Input :** test_str = 'gfg'
    **Output :** GFg
    
    **Explanation :** Random elements are converted to Upper case characters.

 **Method #1 : Using** **join()** **+** **choice()** **+** **upper()** **+**
**lower()**

In this, we perform the task of choosing random characters to upper case using
choice() at each character. The upper() and lower() perform task of
uppercasing and lowercasing characters respectively.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Random uppercase in Strings

# Using join() + choice() + upper() + lower()

from random import choice

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# choosing from upper or lower for each character

res = ''.join(choice((str.upper, str.lower))(char) for char
in test_str)

 

# printing result

print("Random Uppercased Strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original string is : geeksforgeeks
    Random Uppercased Strings : gEEkSFoRgEeKS

 **Method #2 : Using** **map()** **+** **choice()** **+** **zip()**

In this, we imply choice() over all the characters of lowercase and uppercase
Strings joined (using zip()), using map().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Random uppercase in Strings

# Using map() + choice() + zip()

from random import choice

 

# initializing string

test_str = 'geeksforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# choosing from upper or lower for each character

# extending logic to each character using map()

res = ''.join(map(choice, zip(test_str.lower(),
test_str.upper())))

 

# printing result

print("Random Uppercased Strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : geeksforgeeks
    Random Uppercased Strings : geEkSFORgEEKS

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

