Python – Append items at beginning of dictionary



Given a dictionary, append another dictionary at beginning of it.

>  **Input** : test_dict = {“Gfg” : 5, “is” : 3, “best” : 10}, updict =
> {“pre1” : 4}  
>  **Output** : {‘pre1’: 4, ‘Gfg’: 5, ‘is’: 3, ‘best’: 10}  
>  **Explanation** : New dictionary updated at front of dictionary.
>
>  **Input** : test_dict = {“Gfg” : 5}, updict = {“pre1” : 4}  
>  **Output** : {‘pre1’: 4, ‘Gfg’: 5}  
>  **Explanation** : New dictionary updated at front of dictionary, “pre1” :
> 4.

 **Method #1 : Using update()**

This is one of the ways in which this task can be performed. In this, we use
update function to update old dictionary after the new one so that new
dictionary is appended at beginning.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append items at beginning of dictionary 

# Using update()

 

# initializing dictionary

test_dict = {"Gfg" : 5, "is" : 3, "best" : 10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing update dictionary

updict = {"pre1" : 4, "pre2" : 8}

 

# update() on new dictionary to get desired order

updict.update(test_dict)

 

# printing result 

print("The required dictionary : " + str(updict))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 5, 'is': 3, 'best': 10}
    The required dictionary : {'pre1': 4, 'pre2': 8, 'Gfg': 5, 'is': 3, 'best': 10}
    

**Method #2 : Using ** operator**

This is yet another way in which this task can be performed. In this, we
perform packing and unpacking of items into custom made dictionary using **
operator.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Append items at beginning of dictionary 

# Using ** operator

 

# initializing dictionary

test_dict = {"Gfg" : 5, "is" : 3, "best" : 10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing update dictionary

updict = {"pre1" : 4, "pre2" : 8}

 

# ** operator for packing and unpacking items in order

res = {**updict, **test_dict}

 

# printing result 

print("The required dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 5, 'is': 3, 'best': 10}
    The required dictionary : {'pre1': 4, 'pre2': 8, 'Gfg': 5, 'is': 3, 'best': 10}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

