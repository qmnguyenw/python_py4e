Python – Filter dictionary values in heterogenous dictionary



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to filter out certain values based on certain condition on a
particular type, e.g all values smaller than K. This task becomes complex when
dictionary values can be heterogenous. This kind of problem can have
applications across many domains. Let’s discuss certain ways in which this
task can be performed.

>  **Input** : test_dict = {‘Gfg’ : 10, ‘for’ : ‘geeks’}  
>  **Output** : {‘Gfg’: 10, ‘for’: ‘geeks’}
>
>  **Input** : test_dict = {‘Gfg’ : ‘geeks’}  
>  **Output** : {‘Gfg’: ‘geeks’}

 **Method #1 : Using type() \+ dictionary comprehension**  
The combination of above functions can be used to perform this task. In this,
we check for integral type using type() and filter the data in dictionary
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter dictionary values in heterogenous dictionary

# Using type() + dictionary comprehension

 

# initializing dictionary

test_dict = {'Gfg' : 4, 'is' : 2, 'best' : 3,
'for' : 'geeks'}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing K 

K = 3

 

# Filter dictionary values in heterogenous dictionary

# Using type() + dictionary comprehension

res = {key : val for key, val in test_dict.items()

 if type(val) != int or val > K}

 

# printing result 

print("Values greater than K : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary : {'Gfg': 4, 'for': 'geeks', 'is': 2, 'best': 3}
    Values greater than K : {'Gfg': 4, 'for': 'geeks'}
    

