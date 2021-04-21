Python Dictionary | setdefault() method



 **Dictionary** in Python is an unordered collection of data values, used to
store data values like a map, which unlike other Data Types that hold only
single value as an element, Dictionary holds key : value pair.  
In Python Dictionary, **setdefault()** method returns the value of a key (if
the key is in dictionary). If not, it inserts key with a value to the
dictionary.  

> **Syntax:** dict.setdefault(key, default_value)  
>  **Parameters:** It takes two parameters:  
> **key –** Key to be searched in the dictionary.  
> **default_value (optional) –** Key with a value default_value is inserted to
> the dictionary if key is not in the dictionary. If not provided, the
> default_value will be None.  
>  **Returns:**  
> Value of the key if it is in the dictionary.  
> None if key is not in the dictionary and default_value is not specified.  
> default_value if key is not in the dictionary and default_value is
> specified.

  
**Example #1:**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to show working

# of setdefault() method in Dictionary

# Dictionary with single item

Dictionary1 = { 'A': 'Geeks', 'B': 'For', 'C':
'Geeks'}

# using setdefault() method

Third_value = Dictionary1.setdefault('C')

print("Dictionary:", Dictionary1)

print("Third_value:", Third_value)  
  
---  
  
 __

 __

 **Output:**  

    
    
    Dictionary: {'A': 'Geeks', 'C': 'Geeks', 'B': 'For'}
    Third_value: Geeks
    

  
**Example #2:** When key is not in the dictionary.  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to show working

# of setdefault() method in Dictionary

# Dictionary with single item

Dictionary1 = { 'A': 'Geeks', 'B': 'For'}

# using setdefault() method

# when key is not in the Dictionary

Third_value = Dictionary1.setdefault('C')

print("Dictionary:", Dictionary1)

print("Third_value:", Third_value)

# using setdefault() method

# when key is not in the Dictionary

# but default value is provided

Fourth_value = Dictionary1.setdefault('D', 'Geeks')

print("Dictionary:", Dictionary1)

print("Fourth_value:", Fourth_value)  
  
---  
  
 __

 __

 **Output:**  

    
    
    Dictionary: {'A': 'Geeks', 'B': 'For', 'C': None}
    Third_value: None
    Dictionary: {'A': 'Geeks', 'B': 'For', 'C': None, 'D': 'Geeks'}
    Fourth_value: Geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

