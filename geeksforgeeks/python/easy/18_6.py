Python | Add new keys to a dictionary



Dictionary in Python is an unordered collection of data values, used to store
data values like a map, which unlike other Data Types that hold only single
value as an element, Dictionary holds key:value pair.

Key value is provided in the dictionary to make it more optimized. Each key-
value pair in a Dictionary is separated by a colon **:** , whereas each key
is separated by a ‘comma’. Keys of a Dictionary must be unique and of
immutable data type such as Strings, Integers and tuples, but the key-values
can be repeated and be of any type.

Let’s see all different ways of adding new keys to a dictionary.

Create a dictionary first.

 __

 __  
 __

 __

 __  
 __  
 __

# Let's create a dictionary, the functional way

 

# Create your dictionary class

class my_dictionary(dict):

 

 # __init__ function

 def __init__(self):

 self = dict()

 

 # Function to add key:value

 def add(self, key, value):

 self[key] = value

 

# Main Function

dict_obj = my_dictionary()

 

dict_obj.add(1, 'Geeks')

dict_obj.add(2, 'forGeeks')

 

print(dict_obj)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    {1: 'Geeks', 2: 'forGeeks'}

 **Method #1:** Using Subscript notation

This method will create a new key\value pair on a dictionary by assigning a
value to that key. If the key doesn’t exist, it will be added and will point
to that value. If the key exists, the current value it points to will be
overwritten.

 __

 __  
 __

 __

 __  
 __  
 __

dict = {'key1':'geeks', 'key2':'fill_me'}

print("Current Dict is: ", dict)

 

# using the subscript notation

# Dictionary_Name[New_Key_Name] = New_Key_Value

dict['key2'] = 'for'

dict['key3'] = 'geeks'

print("Updated Dict is: ", dict)  
  
---  
  
 __

 __

 **Output:**

    
    
    Current Dict is:  {'key1': 'geeks', 'key2': 'fill_me'}
    Updated Dict is:  {'key3': 'geeks', 'key1': 'geeks', 'key2': 'for'}

  
**Method #2:** Using update() method

When we have to update/add a lots of key/value to dictionary, update()
method is suitable.

 __

 __  
 __

 __

 __  
 __  
 __

dict = {'key1':'geeks', 'key2':'for'}

print("Current Dict is: ", dict)

 

# adding key3

dict.update({'key3':'geeks'})

print("Updated Dict is: ", dict)

 

# adding dict1 (key4 and key5) to dict

dict1 = {'key4':'is', 'key5':'fabulous'}

dict.update(dict1)

print(dict)

 

# by assigning 

dict.update(newkey1 ='portal')

print(dict)  
  
---  
  
 __

 __

 **Output:**

    
    
    Current Dict is:  {'key2': 'for', 'key1': 'geeks'}
    Updated Dict is:  {'key2': 'for', 'key3': 'geeks', 'key1': 'geeks'}
    
    {'key4': 'is', 'key2': 'for', 'key5': 'fabulous', 'key3': 'geeks', 'key1': 'geeks'}
    
    {'key3': 'geeks', 'newkey1': 'portal', 'key1': 'geeks',
            'key4': 'is', 'key2': 'for', 'key5': 'fabulous'}

  
**Method #3:** __setitem__ method to add a key-value pair to a dict

Using __setitem__ method should be avoided because of its poor
performance(computationally inefficient).

 __

 __  
 __

 __

 __  
 __  
 __

dict = {'key1':'geeks', 'key2':'for'}

 

# using __setitem__ method

dict.__setitem__('newkey2', 'GEEK')

print(dict)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'key2': 'for', 'newkey2': 'GEEK', 'key1': 'geeks'}

  
**Method #4:** Using * operator

Using this method we can merge old dictionary and new key/value pair in
another dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

dict = {'a': 1, 'b': 2}

 

# will create a new dictionary

new_dict = {**dict, **{'c': 3}}

 

print(dict)

print(new_dict)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'b': 2, 'a': 1}
    {'b': 2, 'c': 3, 'a': 1}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

