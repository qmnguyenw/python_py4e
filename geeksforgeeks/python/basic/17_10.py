Python Dictionary keys() method



 **Dictionary** in Python is an unordered collection of data values, used to
store data values like a map, which unlike other Data Types that hold only
single value as an element, Dictionary holds key : value pair.

 **keys()** method in Python Dictionary, returns a view object that displays
a list of all the keys in the dictionary.

>  **Syntax:** dict.keys()
>
>  **Parameters:** There are no parameters.
>
>  **Returns:** A view object is returned that displays all the keys. This
> view object changes according to the changes in the dictionary.
>
>  
>
>
>  
>

 **Example #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to show working

# of keys in Dictionary

 

# Dictionary with three keys

Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C':
'Geeks'}

 

# Printing keys of dictionary

print(Dictionary1.keys())

 

# Creating empty Dictionary

empty_Dict1 = {}

 

# Printing keys of Empty Dictionary

print(empty_Dict1.keys())  
  
---  
  
 __

 __

 **Output:**

    
    
    dict_keys(['A', 'B', 'C'])
    dict_keys([])

Order of these key values in the list may not always be same.  
  
**Example #2:** To show how updation of dictionary works

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to show updation

# of keys in Dictionary

 

# Dictionary with two keys

Dictionary1 = {'A': 'Geeks', 'B': 'For'}

 

# Printing keys of dictionary

print("Keys before Dictionary Updation:")

keys = Dictionary1.keys()

print(keys)

 

# adding an element to the dictionary

Dictionary1.update({'C':'Geeks'})

 

print('\nAfter dictionary is updated:')

print(keys)  
  
---  
  
 __

 __

 **Output:**

    
    
    Keys before Dictionary Updation:
    dict_keys(['B', 'A'])
    
    After dictionary is updated:
    dict_keys(['B', 'A', 'C'])

Here, when the dictionary is updated, keys is also automatically updated to
show the changes.

 **Practical Application :** The keys() can be used to access the elements of
dictionary as we can do for list, without use of keys(), no other mechanism
provides means to access dictionary keys as list by index. This is
demonstrated in the example below.

 **Example #3 :** Demonstrating practical application of keys()

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# working of keys()

 

# initializing dictionary 

test_dict = { "geeks" : 7, "for" : 1, "geeks" : 2
}

 

# accessing 2nd element using naive method

# using loop

j = 0

for i in test_dict:

 if (j == 1):

 print ('2nd key using loop : ' + i)

 j = j + 1

 

# accessing 2nd element using keys()

print ('2nd key using keys() : ' + test_dict.keys()[1])  
  
---  
  
 __

 __

Note: - > the second approach would not work because dict_keys in Python 3
does not support indexing.  
 **Output :**

    
    
    2nd key using loop : for
    TypeError: 'dict_keys' object does not support indexing 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

