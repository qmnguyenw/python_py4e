Python | Get the first key in dictionary



Many times, while working with Python, we can have a situation in which we
require to get the initial key of the dictionary. There can be many specific
uses of it, either for checking the indexing and many more of these kinds.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usinglist() + keys()**

The combination of the above methods can be used to perform this particular
task. In this, we just convert the entire dictionaries’ keys extracted by
keys() into a list and just access the first key. Just one thing you have to
keep in mind while using this i.e it’s complexity. It will first convert the
whole dictionary to list by iterating over each item and then extract its
first element. Using this method complexity would be O(n).

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Getting first key in dictionary

# Using keys() + list()

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using keys() + list()

# Getting first key in dictionary

res = list(test_dict.keys())[0]

 

# printing initial key

print("The first key of dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': 3, 'Gfg': 1, 'is': 2}
    The first key of dictionary is : best
    

  

  

**Method #2 : Usingnext() + iter()**  
This task can also be performed using these functions. In this, we just take
the first next key using next() and iter function is used to get the
iterable conversion of dictionary items. So if you want only the first key
then this method is more efficient. Its complexity would be O(1).

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Getting first key in dictionary

# Using next() + iter()

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using next() + iter()

# Getting first key in dictionary

res = next(iter(test_dict))

 

# printing initial key

print("The first key of dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': 3, 'Gfg': 1, 'is': 2}
    The first key of dictionary is : best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

