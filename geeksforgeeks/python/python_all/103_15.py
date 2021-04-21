Python – Cumulative product of dictionary value lists



Sometimes, while working with Python dictionaries, we can have it’s values as
lists. In this can we can have a problem that we just require the product of
elements in those list as a whole. This can be a problem in Data Science in
which we need to get total records in observations. Let’s discuss certain ways
in which this task can be performed

 **Method #1 : Using loop + list comprehension**  
This task can be performed using explicit product function which can be used
to get the product and internal list comprehension can provide a mechanism to
iterate this logic to all the keys of dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cummulative product of dictionary value lists

# using loop + list comprehension

 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res

 

# initialize dictionary

test_dict = {'gfg' : [5, 6, 7], 'is' : [10,
11], 'best' : [19, 31, 22]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Cummulative product of dictionary value lists

# using loop + list comprehension

res = sum(prod(sub) for sub in test_dict.values())

 

# printing result

print("Product of dictionary list values are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': [19, 31, 22], 'gfg': [5, 6, 7], 'is': [10, 11]}
    Product of dictionary list values are : 13278
    

**Method #2 : Using loop +map()**  
This task can also be performed using map function in place of list
comprehension to extend the logic of finding the product, rest all the
functionality remaining same as the above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cummulative product of dictionary value lists

# using loop + map()

 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res

 

# initialize dictionary

test_dict = {'gfg' : [5, 6, 7], 'is' : [10,
11], 'best' : [19, 31, 22]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Cummulative product of dictionary value lists

# using loop + map()

res = sum(map(prod, test_dict.values()))

 

# printing result

print("Product of dictionary list values are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': [19, 31, 22], 'gfg': [5, 6, 7], 'is': [10, 11]}
    Product of dictionary list values are : 13278
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

