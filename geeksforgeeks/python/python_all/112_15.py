Python – Extracting Kth Key in Dictionary



Many times, while working with Python, we can have a situation in which we
require to get the Kth key of dictionary. There can be many specific uses of
it, either for checking the indexing and many more of these kind. This is
useful for Python version 3.8 +, where key ordering are similar as insertion
ordering. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usinglist() + keys()**  
The combination of above methods can be used to perform this particular task.
In this, we just convert the entire dictionaries’ keys extracted by keys()
into a list and just access the Kth key.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extracting Kth Key in Dictionary

# Using keys() + list()

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 1

 

# Using keys() + list()

# Extracting Kth Key in Dictionary

res = list(test_dict.keys())[K]

 

# printing Kth key

print("The Kth key of dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': 3, 'Gfg': 1, 'is': 2}
    The Kth key of dictionary is : Gfg
    

**Method #2 : Usingnext() + iter()**  
This task can also be performed using these functions. In this, we just take
the Kth next key using next() and iter function is used to get the iterable
conversion of dictionary items.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extracting Kth Key in Dictionary

# Using next() + iter()

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 1

 

# Using next() + iter()

# Extracting Kth Key in Dictionary

test_dict = iter(test_dict)

for i in range(0, K + 1) :

 res = next(test_dict)

 

# printing Kth key

print("The Kth key of dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': 3, 'Gfg': 1, 'is': 2}
    The Kth key of dictionary is : Gfg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

