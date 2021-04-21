Add a key:value pair to dictionary in Python



Dictionary in Python is an unordered collection of data values, used to store
data values like a map, which unlike other Data Types that hold only single
value as an element, Dictionary holds key:value pair.

While using Dictionary, sometimes, we need to add or modify the key/value
inside the dictionary. Let’s see how to add a key:value pair to dictionary
in Python.

 **Code #1:** Using Subscript notation

This method will create a new key:value pair on a dictionary by assigning a
value to that key.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to add a key:value pair to dictionary

 

dict = {'key1':'geeks', 'key2':'for'} 

print("Current Dict is: ", dict) 

 

# using the subscript notation 

# Dictionary_Name[New_Key_Name] = New_Key_Value 

 

dict['key3'] = 'Geeks'

dict['key4'] = 'is'

dict['key5'] = 'portal'

dict['key6'] = 'Computer'

print("Updated Dict is: ", dict)  
  
---  
  
 __

 __

 **Output:**

  

  

> Current Dict is: {‘key2’: ‘for’, ‘key1’: ‘geeks’}  
> Updated Dict is: {‘key3’: ‘Geeks’, ‘key5’: ‘portal’, ‘key6’: ‘Computer’,
> ‘key4’: ‘is’, ‘key1’: ‘geeks’, ‘key2’: ‘for’}

