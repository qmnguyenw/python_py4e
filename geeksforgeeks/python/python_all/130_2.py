Python | Concatenate dictionary value lists



Sometimes, while working with dictionaries, we might have a problem in which
we have lists as it’s value and wish to have it cumulatively in single list by
concatenation. This problem can occur in web development domain. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usingsum() + values()**  
This is the most recommended method and one liner to perform this task. In
this, we access all list values using values() and concatenation utility is
performed using sum().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenating dictionary value lists

# Using sum() + values()

 

# initializing dictionary

test_dict = {"Gfg" : [4, 5], "is" : [6, 8],
"best" : [10]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Concatenating dictionary value lists

# Using sum() + values()

res = sum(test_dict.values(), [])

 

# printing result 

print("The Concatenated list values are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Gfg': [4, 5], 'best': [10], 'is': [6, 8]}
    The Concatenated list values are : [4, 5, 10, 6, 8]
    

**Method #2 : Using chain() + * operator**  
This task can also be performed using the combination of these methods. In
these, we just use inbuilt function of chain for concatenation to list and *
operator is used to access all the list values into one.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenating dictionary value lists

# Using chain() + * operator

from itertools import chain

 

# initializing dictionary

test_dict = {"Gfg" : [4, 5], "is" : [6, 8],
"best" : [10]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Concatenating dictionary value lists

# Using chain() + * operator

res = list(chain(*test_dict.values()))

 

# printing result 

print("The Concatenated list values are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Gfg': [4, 5], 'best': [10], 'is': [6, 8]}
    The Concatenated list values are : [4, 5, 10, 6, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

