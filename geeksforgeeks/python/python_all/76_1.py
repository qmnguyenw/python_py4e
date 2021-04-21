Python – Convert Dictionary to Concatenated String



Sometimes, while working with Dictionaries, we can have a task in which we
need to perform the conversion of converting dictionary to string, which is
concatenated key-value pair. This can have application in domains in which we
require to reduce storage space or require strings as target data. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Usingjoin() + items()**  
The combination of above functions can be used to solve this problem. In this,
we need to perform the task of concatenation using join() and extraction of
dictionary items is done using items().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Dictionary to Concatenated String

# Using join() + items()

 

# initializing dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert Dictionary to Concatenated String

# Using join() + items()

res = ''.join(key + str(val) for key, val in
test_dict.items())

 

# printing result 

print("The dictionary after concatenation is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {'gfg': 1, 'best': 3, 'is': 2}
    The dictionary after concatenation is : gfg1best3is2
    

**Method #2 : Usingreduce() \+ lambda**  
The combination of above functions can be used to perform this task. In this,
we perform the task of concatenation using combination of reduce() and lambda.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Dictionary to Concatenated String

# Using reduce() + lambda

from functools import reduce

 

# initializing dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert Dictionary to Concatenated String

# Using reduce() + lambda

res = reduce(lambda key, val : key + str(val[0]) +
str(val[1]), test_dict.items(), '')

 

# printing result 

print("The dictionary after concatenation is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {'gfg': 1, 'best': 3, 'is': 2}
    The dictionary after concatenation is : gfg1best3is2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

