Python | Ways to remove a key from dictionary



Dictionary is used in manifold practical applications such as day-day
programming, web development and AI/ML programming as well, making it a useful
container overall. Hence, knowing shorthands for achieving different tasks
related to dictionary usage always is a plus. This article deals with one such
task of deleting a dictionary key-value pair from a dictionary.  

 **Method 1 : Usingdel**

del keyword can be used to inplace delete the key that is present in the
dictionary. One drawback that can be thought of using this is that is raises
an exception if the key is not found and hence non-existence of key has to be
handled.  
  
 **Code #1 :** Demonstrating key-value pair deletion using del

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# removal of dict. pair 

# using del

 

# Initializing dictionary

test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" :
21, "Haritha" : 21}

 

# Printing dictionary before removal

print ("The dictionary before performing remove is : " +
str(test_dict))

 

# Using del to remove a dict

# removes Mani

del test_dict['Mani']

 

# Printing dictionary after removal

print ("The dictionary after remove is : " + str(test_dict))

 

# Using del to remove a dict

# raises exception

del test_dict['Manjeet']  
  
---  
  
 __

 __

 **Output :**

    
    
    The dictionary before performing remove is : {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
    The dictionary after remove is : {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22}
    

**Exception :**

  

  

    
    
    Traceback (most recent call last):
      File "/home/44db951e7011423359af4861d475458a.py", line 20, in 
        del test_dict['Manjeet']
    KeyError: 'Manjeet'
    

**Method 2 : Usingpop()**

 **pop()** can be used to delete a key and its value inplace. Advantage over
using del is that it provides the mechanism to print desired value if tried
to remove a non-existing dict. pair. Second, it also returns the value of key
that is being removed in addition to performing a simple delete operation.  
  
 **Code #2 :** Demonstrating key-value pair deletion using pop()  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# removal of dict. pair 

# using pop()

 

# Initializing dictionary

test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" :
21, "Haritha" : 21}

 

# Printing dictionary before removal

print ("The dictionary before performing remove is : " +
str(test_dict))

 

# Using pop() to remove a dict. pair

# removes Mani

removed_value = test_dict.pop('Mani')

 

# Printing dictionary after removal

print ("The dictionary after remove is : " + str(test_dict))

print ("The removed key's value is : " + str(removed_value))

 

print ('\r')

 

# Using pop() to remove a dict. pair

# doesn't raise exception

# assigns 'No Key found' to removed_value

removed_value = test_dict.pop('Manjeet', 'No Key found')

 

# Printing dictionary after removal

print ("The dictionary after remove is : " + str(test_dict))

print ("The removed key's value is : " + str(removed_value))  
  
---  
  
 __

 __

 **Output :**

    
    
    The dictionary before performing remove is : {'Arushi': 22, 'Anuradha': 21, 'Mani': 21, 'Haritha': 21}
    The dictionary after remove is : {'Arushi': 22, 'Anuradha': 21, 'Haritha': 21}
    The removed key's value is : 21
    
    The dictionary after remove is : {'Arushi': 22, 'Anuradha': 21, 'Haritha': 21}
    The removed key's value is : No Key found
    

**Method 3 : Using items() \+ dict comprehension**

items() coupled with dict comprehension can also help us achieve task of
key-value pair deletion but, it has drawback of not being an inplace dict.
technique. Actually a new dict if created except for the key we don’t wish to
include.  
  
 **Code #3 :** Demonstrating key-value pair deletion using items() \+ dict.
comprehension  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# removal of dict. pair 

# using items() + dict comprehension

 

# Initializing dictionary

test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" :
21, "Haritha" : 21}

 

# Printing dictionary before removal

print ("The dictionary before performing remove is : " +
str(test_dict))

 

# Using items() + dict comprehension to remove a dict. pair

# removes Mani

new_dict = {key:val for key, val in test_dict.items() if key
!= 'Mani'}

 

# Printing dictionary after removal

print ("The dictionary after remove is : " + str(new_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    The dictionary before performing remove is : {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
    The dictionary after remove is : {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

