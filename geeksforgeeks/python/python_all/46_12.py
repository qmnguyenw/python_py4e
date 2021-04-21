Python – Key Columns Dictionary from Matrix



Given a Matrix and list of keys, map each column values with custom list key.

>  **Input** : test_list1 = [[4, 6], [8, 6]], test_list2 = [“Gfg”, “Best”]  
>  **Output** : {‘Gfg’: [4, 8], ‘Best’: [6, 6]}  
>  **Explanation** : Column wise, Key values assigment.
>
>  **Input** : test_list1 = [[4], [6]], test_list2 = [“Gfg”]  
>  **Output** : {‘Gfg’: [4, 6]}  
>  **Explanation** : Column wise, Key values assigment, just single element
> list.

 **Method #1 : Using list comprehension + dictionary comprehension**

The combination of above functionality can be used to solve this problem. In
this, we perform the task of extracting column values using list comprehension
and then dictionary comprehension is used to form dictionary with list keys.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Key Columns Dictionary from Matrix

# Using list comprehension + dictionary comprehension

 

# initializing lists

test_list1 = [[4, 6, 8], [8, 4, 2], [8,
6, 3]]

test_list2 = ["Gfg", "is", "Best"]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using enumerate to get column numbers 

# dictionary comprehension to compile result 

res = {key: [sub[idx] for sub in test_list1] for idx, key
in enumerate(test_list2)}

 

# printing result 

print("The paired dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [[4, 6, 8], [8, 4, 2], [8, 6, 3]]
    The original list 2 : ['Gfg', 'is', 'Best']
    The paired dictionary : {'Gfg': [4, 8, 8], 'is': [6, 4, 6], 'Best': [8, 2, 3]}
    

**Method #2 : Using zip() + dict()**

This is yet another way in which this task can be peformed. In this, we join
key-value pair using zip() and dict() is used to convert result in dictionary.
The difference is that it generates tuples rather than lists as mapped values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Key Columns Dictionary from Matrix

# Using zip() + dict()

 

# initializing lists

test_list1 = [[4, 6, 8], [8, 4, 2], [8,
6, 3]]

test_list2 = ["Gfg", "is", "Best"]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# zip() used to map keys with values and return tuples 

# as result 

# * operator used to perform unpacking

res = dict(zip(test_list2, zip(*test_list1)))

 

# printing result 

print("The paired dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [[4, 6, 8], [8, 4, 2], [8, 6, 3]]
    The original list 2 : ['Gfg', 'is', 'Best']
    The paired dictionary : {'Gfg': (4, 8, 8), 'is': (6, 4, 6), 'Best': (8, 2, 3)}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

