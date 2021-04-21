Python program to change values in a Dictionary



Given a dictionary in Python, the task is to write a Python program to change
the value in one of the key-value pairs. This article discusses mechanisms to
do this effectively.

 **Examples:**

    
    
     **Input:** {'hari': 1, 'dita': 2}
    **Output:** {'hari': 1, 'dita': 4}
    
    **Input:** {'hari': 1, 'dita': 2}
    **Output:** {'hari': 3, 'dita': 5}

### Changing Values of a Dictionary

 **Method 1**

In this we refer to the key of the value to be changed and supply it with a
new value.

 **Example:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# declaring dictionary

dict = {'hari': 1, 'dita': 2}

 

# original dictionary

print("initial dictionary-", dict)

 

# changing the key value from 2 to 4

dict['dita'] = 4

 

# dictionary after update

print("dictionary after modification-", dict)  
  
---  
  
 __

 __

 **Output:**

> initial dictionary- {‘hari’: 1, ‘dita’: 2}  
>
>
> dictionary after modification- {‘hari’: 1, ‘dita’: 4}

 **Method 2:**

In this method we use zip() function, which aggregates the iterable and
combines them into a tuple form.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# declaring dictionary

dict1 = {'hari': 1, 'dita': 2}

 

# original dictionary

print("initial dictionary-", dict1)

 

# list of values which will replace the values of dict1

list1 = [3, 5]

 

# this preserves the keys and modifies the values

dict1 = dict(zip(list(dict1.keys()), list1))

 

# modified dictionary

print("dictionary after modification-", dict1)  
  
---  
  
 __

 __

 **Output:**

> initial dictionary- {‘hari’: 1, ‘dita’: 2}
>
> dictionary after modification- {‘hari’: 3, ‘dita’: 5}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

