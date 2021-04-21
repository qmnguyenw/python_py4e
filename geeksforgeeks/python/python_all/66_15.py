Python – Retain list elements value items



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to retain only those keys, whose values are part of target list.
This kind of problem can have potential problem in many domains including web
development. Let’s discuss certain ways in which this task can be performed.

>  **Input** :  
> test_dict = {‘gfg’: 3}  
> tar_list = [3, 4, 10] (Values to retain)  
>  **Output** : {‘gfg’: 3}
>
>  **Input** :  
> test_dict = {‘gfg’: 5, ‘best’: 12}  
> tar_list = [3, 4, 10] (Values to retain)  
>  **Output** : {}

 **Method #1: Using dictionary comprehension**  
This is one of the ways in which this problem can be solved. In this, we
perform the task of filtering using conditional expression inside
comprehension, retaining only those items present list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Retain list elements value items

# Using dictionary comprehension

 

# initializing dictionary

test_dict = {'gfg': 3, 'is': 2, 'best': 4,
'for': 7, 'geeks': 10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing target list 

tar_list = [3, 4, 10]

 

# Retain list elements value items

# Using dictionary comprehension

res = {key : val for key, val in test_dict.items() if val
in tar_list}

 

# printing result 

print("The filtered dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary is : {'gfg': 3, 'is': 2, 'best': 4, 'for': 7, 'geeks': 10}
    The filtered dictionary : {'gfg': 3, 'best': 4, 'geeks': 10}
    

