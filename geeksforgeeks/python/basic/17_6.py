Python Dictionary pop() method



Python language specified **pop()** for almost all containers, be it list,
set etc. This particular article focuses on illustrating the **pop()**
method offered by Python dictionaries. This method is useful for the
programmers who deal with the dictionary too often.

>  **Syntax :** dict.pop(key, def)
>
>  **Parameters :**  
>  **key :** The key whose key-value pair has to be returned and removed.  
>  **def :** The default value to return if specified key is not present.
>
>  **Returns :**  
>  Value associated to deleted key-value pair, if key is present.  
> Default value if specified if key is not present.  
> KeyError, if key not present and default value not specified.

  

  

**Code #1 :** Demonstrating working of pop(), when key is present.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# working of pop()

 

# initializing dictionary 

test_dict = { "Nikhil" : 7, "Akshat" : 1, "Akash" :
2 }

 

# Printing initial dict

print ("The dictionary before deletion : " + str(test_dict))

 

# using pop to return and remove key-value pair.

pop_ele = test_dict.pop('Akash')

 

# Printing the value associated to popped key 

print ("Value associated to poppped key is : " + str(pop_ele))

 

# Printing dictionary after deletion

print ("Dictionary after deletion is : " + str(test_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    The dictionary before deletion : {'Nikhil': 7, 'Akshat': 1, 'Akash': 2}
    Value associated to poppped key is : 2
    Dictionary after deletion is : {'Nikhil': 7, 'Akshat': 1}
    

The behavior of pop() function is **different when the key is not present in
dictionary.** In this case, it returns the default provided value or KeyError
in case even default is not provided.

 **Code #2 :** Demonstrating the working of pop() without key

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# working of pop() without key

 

# initializing dictionary 

test_dict = { "Nikhil" : 7, "Akshat" : 1, "Akash" :
2 }

 

# Printing initial dict

print ("The dictionary before deletion : " + str(test_dict))

 

# using pop to return and remove key-value pair

# provided default

pop_ele = test_dict.pop('Manjeet', 4)

 

# Printing the value associated to popped key 

# Prints 4

print ("Value associated to poppped key is : " + str(pop_ele))

 

# using pop to return and remove key-value pair

# not provided default

pop_ele = test_dict.pop('Manjeet')

 

# Printing the value associated to popped key 

# KeyError

print ("Value associated to poppped key is : " + str(pop_ele))  
  
---  
  
 __

 __

 **Output :**

    
    
    The dictionary before deletion : {'Nikhil': 7, 'Akshat': 1, 'Akash': 2}
    Value associated to poppped key is : 4
    Traceback (most recent call last):
      File "main.py", line 20, in 
        pop_ele = test_dict.pop('Manjeet')
    KeyError: 'Manjeet'
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

