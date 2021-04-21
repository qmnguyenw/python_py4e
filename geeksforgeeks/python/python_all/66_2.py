Python – Dictionary Tuple values update



Sometimes, while working with Tuple data, we can have problem when we perform
its editions, reason being it’s immutability. This discusses the editions in
tuple values in dictionary. This can have application in many domains as
dictionary is often popular data type in web development and Data Science
domains. Let’s discuss certain ways in which this problem can be solved.

>  **Input** :  
> test_dict = {‘Gfg’ : (5, 6, 7, 8)}  
> K = 2  
>  **Output** : {‘Gfg’: (10, 12, 14, 16)}
>
>  **Input** :  
> test_dict = {‘Gfg’ : (5, ), ‘is’ : (6, ), ‘best’ : (7, )}  
> K = 7  
>  **Output** : {‘Gfg’: (35, ), ‘is’: (42, ), ‘best’: (49, )}

 **Method #1 : Using generator expression + dictionary comprehension**  
The combination of above functionalities offer one liner brute force way to
solve this problem. In this, we perform the task of edition using generator
expression and dictionary comprehension to remake dictionary with edited
values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Tuple values update

# Using generator expression + dictionary comprehension

 

# initializing dictionary

test_dict = {'Gfg' : (5, 6), 'is' : (7, 8),
'best' : (10, 11)}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K

# performing mutiplication by K 

K = 3

 

# Dictionary Tuple values update

# Using generator expression + dictionary comprehension

res = {key: tuple(idx * K for idx in val) 

 for key, val in test_dict.items()}

 

# printing result 

print("The edited tuple values : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary is : {'Gfg': (5, 6), 'is': (7, 8), 'best': (10, 11)}
    The edited tuple values : {'Gfg': (15, 18), 'is': (21, 24), 'best': (30, 33)}
    

