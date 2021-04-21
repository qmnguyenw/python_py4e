Python | Initializing dictionary with list index-values



While working with Python we might need to perform tasks in which we need to
assign a dictionary with list values as dictionary values and index as
dictionary keys. This type of problem is quite common in cases we need to
perform data-type conversion. Let’s discuss certain ways in which this task
can be performed.

 **Method #1 : Using dictionary comprehension +len()**

This task can be performed using the combination of above functions in which
we perform the construction of dictionary using the dictionary comprehension
and indexing the limited using the len function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initializing dictionary with list index-values

# Using dictionary comprehension + len()

 

# initializing list

test_list = ['Gfg', 'is', 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing dictionary with list index-values

# Using dictionary comprehension + len()

res = {x : test_list[x] for x in range(len(test_list))}

 

# printing result

print("The dictionary indexed as list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Gfg', 'is', 'best']
    The dictionary indexed as list is :  {0: 'Gfg', 1: 'is', 2: 'best'}
    

  

  

**Method #2 : Usingdict() + enumerate()**

The combination of these methods can also be used to perform this task. In
this we use the quality of enumerate function to get the indices and
dict() is used to convert the list to dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initializing dictionary with list index-values

# Using dict() + enumerate()

 

# initializing list

test_list = ['Gfg', 'is', 'best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing dictionary with list index-values

# Using dict() + enumerate()

res = dict(enumerate(test_list))

 

# printing result

print("The dictionary indexed as list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Gfg', 'is', 'best']
    The dictionary indexed as list is :  {0: 'Gfg', 1: 'is', 2: 'best'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

