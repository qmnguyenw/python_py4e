Python | Remove all digits from a list of strings



Given a list of strings, write a Python program to remove all digits from the
list of string.

 **Examples:**

    
    
    **Input :** ['alice1', 'bob2', 'cara3']
    **Output :** ['alice', 'bob', 'cara']
    
    **Input :** ['4geeks', '3for', '4geeks']
    **Output :** ['geeks', 'for', 'geeks']
    

**Method #1 :** Python Regex

Python regex pattern can also be used to find if each string contains a digit
or not and converting them to “”.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to Remove all

# digits from a list of string

import re

 

def remove(list):

 pattern = '[0-9]'

 list = [re.sub(pattern, '', i) for i in list]

 return list

 

# Driver code 

 

list = ['4geeks', '3for', '4geeks']

print(remove(list))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['geeks', 'for', 'geeks']
    

  
**Method #2 :** Using **str.maketrans()** method  
The maketrans() method returns a translation table that maps each character
in the intabstring into the character at the same position in the outtab
string. In this particular problem we translate each each digit to “” using
for loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to Remove all

# digits from a list of string

from string import digits

 

def remove(list):

 remove_digits = str.maketrans('', '', digits)

 list = [i.translate(remove_digits) for i in list]

 return list

 

# Driver code 

 

list = ['4geeks', '3for', '4geeks']

print(remove(list))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['geeks', 'for', 'geeks']
    

  
**Method #3 :** Using **str.isalpha()** method  
In ,this approach we use two for loops and check if the character of string is
an alphabet or not. If yes, join it within the list, otherwise leave it.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to Remove all

# digits from a list of string

from string import digits

 

def remove(list):

 list = [''.join(x for x in i if x.isalpha()) for i
in list]

 

 return list

 

# Driver code 

 

list = ['4geeks', '3for', '4geeks']

print(remove(list))  
  
---  
  
 __

 __

 **Output:**

    
    
    ['geeks', 'for', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

