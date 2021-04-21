Python | Extract K sized strings



Sometimes, while working with huge amount of data, we can have a problem in
which we need to extract just specific sized strings. This kind of problem can
occur during validation cases across many domains. Let’s discuss certain ways
to handle this in Python strings list.

 **Method #1 : Using list comprehension +len()**  
The combination of above functionalities can be used to perform this task. In
this, we iterate for all the strings and return only K sized strings checked
using len().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract K sized strings

# using list comprehension + len()

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize K 

K = 3

 

# Extract K sized strings

# using list comprehension + len()

res = [ele for ele in test_list if len(ele) == K]

 

# printing result

print("The K sized strings are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    The K sized strings are : ['gfg', 'for']
    

**Method #2 : Usingfilter() \+ lambda**  
The combination of above functionalities can be used to perform this task. In
this, we extract the elements using filter() and logic is compiled in a lambda
function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract K sized strings

# using filter() + lambd

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize K 

K = 3

 

# Extract K sized strings

# using filter() + lambda

res = list(filter(lambda ele: len(ele) == K,
test_list))

 

# printing result

print("The K sized strings are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    The K sized strings are : ['gfg', 'for']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

