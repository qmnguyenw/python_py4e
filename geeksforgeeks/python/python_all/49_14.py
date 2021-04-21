Python – Add prefix to each key name in dictionary



Given a dictionary, update its each key by adding prefix to each key.

>  **Input** : test_dict = {‘Gfg’ : 6, ‘is’ : 7, ‘best’ : 9}, temp = “Pro”  
>  **Output** : {‘ProGfg’ : 6, ‘Prois’ : 7, ‘Probest’ : 9}  
>  **Explanation** : “Pro” prefix added to each key.
>
>  **Input** : test_dict = {‘Gfg’ : 6, ‘is’ : 7, ‘best’ : 9}, temp = “a”  
>  **Output** : {‘aGfg’ : 6, ‘ais’ : 7, ‘abest’ : 9}  
>  **Explanation** : “a” prefix added to each key.

 **Method #1 : Using dictionary comprehension**

This is one of the methods in which this task can be performed. In this we
construct new dictionary by performing concatenation of prefix with all keys.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add prefix to each key name in dictionary

# Using loop

 

# initializing dictionary

test_dict = {'Gfg' : 6, 'is' : 7, 'best' : 9,
'for' : 8, 'geeks' : 11} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing prefix 

temp = "Pro"

 

# + operator is used to perform task of concatenation

res = {temp + str(key): val for key, val in
test_dict.items()}

 

# printing result 

print("The extracted dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 6, 'is': 7, 'best': 9, 'for': 8, 'geeks': 11}
    The extracted dictionary : {'ProGfg': 6, 'Prois': 7, 'Probest': 9, 'Profor': 8, 'Progeeks': 11}
    

**Method #2 : Using f strings + dictionary comprehension**

The combination of above functionalities can be used to solve this problem. In
this, we perform the task of concatenation using f strings. Works only in
>=3.6 versions of Python.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add prefix to each key name in dictionary

# Using f strings + dictionary comprehension

 

# initializing dictionary

test_dict = {'Gfg' : 6, 'is' : 7, 'best' : 9,
'for' : 8, 'geeks' : 11} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing prefix 

temp = "Pro"

 

# dictionary comprehension is used to bind result 

# f strings are used to bind prefix with key

res = {f"Pro{key}": val for key, val in test_dict.items()}

 

# printing result 

print("The extracted dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 6, 'is': 7, 'best': 9, 'for': 8, 'geeks': 11}
    The extracted dictionary : {'ProGfg': 6, 'Prois': 7, 'Probest': 9, 'Profor': 8, 'Progeeks': 11}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

