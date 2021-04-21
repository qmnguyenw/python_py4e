Python | Initializing dictionary with list index values



While working with dictionaries, we might come across a problem in which we
require to attach each value in list with it’s index, to be used afterwards to
solve question. This technique is usually very useful in competitive
programming domain. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using dictionary comprehension andenumerate()**  
The combo of above methods can achieve this task. In this, enumerate()’s
inbuilt capability to iterate value with it’s index is used to construct a key
to corresponding value using dictionary comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initializing dictionary with index value

# Using dictionary comprehension and enumerate()

 

# Initialize list

test_list = ['gfg', 'is', 'best', 'for', 'CS']

 

# Printing original list 

print("The original list is : " + str(test_list))

 

# using dictionary comprehension and enumerate()

# Initializing dictionary with index value

res = {key: val for val, key in enumerate(test_list)}

 

# printing result 

print("Constructed dictionary with index value : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'CS']
    Constructed dictionary with index value : {'gfg': 0, 'is': 1, 'best': 2, 'CS': 4, 'for': 3}
    

**Method #2 : Usingzip() + dict() + range() + len()**  
This task can also be performed by nesting the above functions. The task
performed above by enumerate is handles by range and len functions and
zip and dict perform the task of binding key with value and dictionary
conversion respectively.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initializing dictionary with index value

# Using zip() + dict() + range() + len()

 

# Initialize list

test_list = ['gfg', 'is', 'best', 'for', 'CS']

 

# Printing original list 

print("The original list is : " + str(test_list))

 

# using zip() + dict() + range() + len()

# Initializing dictionary with index value

res = dict(zip(test_list, range(len(test_list))))

 

# printing result 

print("Constructed dictionary with index value : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'CS']
    Constructed dictionary with index value : {'gfg': 0, 'is': 1, 'best': 2, 'CS': 4, 'for': 3}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

