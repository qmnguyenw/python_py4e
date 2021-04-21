Python | Convert list of strings to space separated string



Given a list of strings, write a Python program to convert the given list of
strings into a space-separated string.

 **Examples:**

    
    
    **Input :** ['geeks', 'for', 'geeks']
    **Output :** geeks for geeks
    
    **Input :** ['Python', 'Language']
    **Output :** Python Language
    

**Approach #1 :** Python string _translate()_

The string translate() method returns a string where each character is mapped
to its corresponding character in the translation table. The limitation of
this method is that it does not work for Python 3 and above versions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Convert a list of

# strings to space-separated string

 

def convert(lst):

 

 return str(lst).translate(None, '[],\'')

 

# Driver code

lst = ['geeks', 'for', 'geeks']

print(convert(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    geeks for geeks
    

