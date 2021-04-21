Python – Get next key in Dictionary



Sometimes, while working with Python dictionaries, we can have problem in
which we need to extract the next key in order of dictionary. This can have
application as from Python 3.6 onwards the dictionaries are ordered. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using index() \+ loop**  
The combination of above functions can be used to perform this task. In this,
we perform the conversion of dictionary elements to list. And then index() is
used to check for index and append the index count to get the next item.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get next key in Dictionary

# Using index() + loop

 

# initializing dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing key

test_key = 'is'

 

# Get next key in Dictionary

# Using index() + loop

temp = list(test_dict)

try:

 res = temp[temp.index(test_key) + 1]

except (ValueError, IndexError):

 res = None

 

# printing result 

print("The next key is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {'gfg': 1, 'best': 3, 'is': 2}
    The next key is : best
    

**Method #2 : Usingiter() + next()**  
This is yet another way in which this task can be performed. In this, we
convert the dictionary to iterator using iter() and then extract the next key
using next().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get next key in Dictionary

# Using iter() + next()

 

# initializing dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing key

test_key = 'is'

 

# Get next key in Dictionary

# Using iter() + next()

res = None

temp = iter(test_dict)

for key in temp:

 if key == test_key:

 res = next(temp, None)

 

# printing result 

print("The next key is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {'gfg': 1, 'best': 3, 'is': 2}
    The next key is : best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

