Python – Assigning Key values to list elements from Value list Dictionary



Given List of elements, map them with keys of matching value from value list.

>  **Input** : test_list = [4, 6, 3, 5, 3], test_dict = {“Gfg” : [5, 3, 6],
> “is” : [8, 4]}  
>  **Output** : [‘is’, ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘Gfg’]  
>  **Explanation** : 4 is present in “is” key, hence mapped in new list.
>
>  **Input** : test_list = [6, 3, 5, 3], test_dict = {“Gfg” : [5, 3, 6], “is”
> : [18, 14]}  
>  **Output** : [‘Gfg’, ‘Gfg’, ‘Gfg’, ‘Gfg’]  
>  **Explanation** : All elements present in “Gfg” key.

 **Method #1 : Using list comprehension**

This is one of the ways in which this task can be performed. In this, we
extract each element of dictionary value list to check list value occurrence,
if matched, we assign that key’s value to that index.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assigning Key values to list elements from Value list Dictionary

# Using list comprehension

 

# initializing list

test_list = [4, 6, 3, 10, 5, 3]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing dictionary 

test_dict = {"Gfg" : [5, 3, 6], "is" : [8,
4], "Best" : [10, 11]}

 

# nested loop inside list comprehension to check each key 

res = [key for ele in test_list

 for key, val in test_dict.items() if ele in val]

 

# printing result 

print("The filtered list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [4, 6, 3, 10, 5, 3]
    The filtered list : ['is', 'Gfg', 'Gfg', 'Best', 'Gfg', 'Gfg']
    

**Method #2 : Using dictionary comprehension + list comprehension**

This is yet another way in which this task can be performed. In this we create
inverse dictionary, and map each list value with its key, post that each key
is mapped with argument key list elements for matching key value.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assigning Key values to list elements from Value list Dictionary

# Using dictionary comprehension + list comprehension

 

# initializing list

test_list = [4, 6, 3, 10, 5, 3]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing dictionary 

test_dict = {"Gfg" : [5, 3, 6], "is" : [8,
4], "Best" : [10, 11]}

 

# creating inverse dictionary of elements 

temp = {j : i for i, k in test_dict.items() for j in k}

 

# creating end result by mapping elements

res = [temp.get(key) for key in test_list]

 

# printing result 

print("The filtered list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [4, 6, 3, 10, 5, 3]
    The filtered list : ['is', 'Gfg', 'Gfg', 'Best', 'Gfg', 'Gfg']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

