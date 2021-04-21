Python Dictionary items() method



 **Dictionary** in Python is an unordered collection of data values, used to
store data values like a map, which unlike other Data Types that hold only
single value as an element, Dictionary holds key : value pair.  
In Python Dictionary, **items()** method is used to return the list with all
dictionary keys with values.  

> **Syntax:** dictionary.items()  
>  **Parameters:** This method takes no parameters.  
>  **Returns:** A view object that displays a list of a given dictionary’s
> (key, value) tuple pair.

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

# of items() method in Dictionary

 

# Dictionary with three items 

Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks'
}

 

print("Dictionary items:")

 

# Printing all the items of the Dictionary

print(Dictionary1.items())  
  
---  
  
 __

 __

 **Output:**  

    
    
    Dictionary items:
    dict_items([('A', 'Geeks'), ('B', 4), ('C', 'Geeks')])
    
    

Order of these items in the list may not always be same.  
  
**Example #2:** To show working of items() after modification of Dictionary.  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to show working

# of items() method in Dictionary

 

# Dictionary with three items 

Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks'
}

 

print("Original Dictionary items:")

 

items = Dictionary1.items()

 

# Printing all the items of the Dictionary

print(items)

 

# Delete an item from dictionary

del[Dictionary1['C']]

print('Updated Dictionary:')

print(items)  
  
---  
  
 __

 __

 **Output:**  

    
    
    Original Dictionary items:
    dict_items([('A', 'Geeks'), ('C', 'Geeks'), ('B', 4)])
    Updated Dictionary:
    dict_items([('A', 'Geeks'), ('B', 4)])
    
    

If the Dictionary is updated anytime, the changes are reflected in the view
object automatically.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

