Python – Extract Unique values dictionary values



Sometimes, while working with data, we can have problem in which we need to
perform the extraction of only unique values from dictionary values list. This
can have application in many domains such as web development. Lets discuss
certain ways in which this task can be performed.

 **Method #1 : Usingsorted() + set comprehension + values()**  
The combination of above functionalities can be used to perform this task. In
this, we extract all the values using values() and set comprehension is used
to get unique values compiled in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Unique values dictionary values

# Using set comprehension + values() + sorted()

 

# initializing dictionary

test_dict = {'gfg' : [5, 6, 7, 8],

 'is' : [10, 11, 7, 5],

 'best' : [6, 12, 10, 8],

 'for' : [1, 2, 5]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Extract Unique values dictionary values

# Using set comprehension + values() + sorted()

res = list(sorted({ele for val in test_dict.values() for
ele in val}))

 

# printing result 

print("The unique values list is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: [5, 6, 7, 8], ‘best’: [6, 12, 10, 8],
> ‘is’: [10, 11, 7, 5], ‘for’: [1, 2, 5]}  
> The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]

  

  

**Method #2 : Usingchain() + sorted() + values()**  
This performs the task in similar way. The difference is that the task of set
comprehension is performed using chain().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Unique values dictionary values

# Using chain() + sorted() + values()

from itertools import chain

 

# initializing dictionary

test_dict = {'gfg' : [5, 6, 7, 8],

 'is' : [10, 11, 7, 5],

 'best' : [6, 12, 10, 8],

 'for' : [1, 2, 5]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Extract Unique values dictionary values

# Using chain() + sorted() + values()

res = list(sorted(set(chain(*test_dict.values()))))

 

# printing result 

print("The unique values list is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: [5, 6, 7, 8], ‘best’: [6, 12, 10, 8],
> ‘is’: [10, 11, 7, 5], ‘for’: [1, 2, 5]}  
> The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

