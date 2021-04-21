Python | Creating Multidimensional dictionary



Sometimes, while working with Python dictionaries we need to have nested
dictionaries. But the issue is that, we have to declare before initializing a
value in nested dictionary. Let’s resolve this particular problem via methods
discussed in this article.

 **Method #1 : Usingsetdefault()**  
This function is used to define an empty dictionary on 1st nested level of
dictionary to make it 2D. In this case there is no need to define explicit
dictionaries at that level of dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Creating Multidimensional dictionary

# Using setdefault()

 

# Initialize dictionary

test_dict = {}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using setdefault()

# Creating Multidimensional dictionary

test_dict.setdefault(1, {})[4] = 7

 

# printing result 

print("Dictionary after nesting : " + str(test_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {}
    Dictionary after nesting : {1: {4: 7}}
    

**Method #2 : Usingdefaultdict()**  
One can achieve the creation of multi nesting using defaultdict(). Not only at
one level, but till N level the nesting can be achieved using this. Drawback
is that it creates the defaultdict objects.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Creating Multidimensional dictionary

# Using defaultdict()

from collections import defaultdict

 

# Utiliy function to create dictionary

def multi_dict(K, type):

 if K == 1:

 return defaultdict(type)

 else:

 return defaultdict(lambda: multi_dict(K-1, type))

 

# Initialize dictionary

test_dict = {}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Using defaultdict()

# Creating Multidimensional dictionary

# calling function

test_dict = multi_dict(3, int)

test_dict[2][3][4] = 1

 

# printing result 

print("Dictionary after nesting : " + str(dict(test_dict)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {}
    Dictionary after nesting : {2: defaultdict(<function multi_dict.<locals>.<lambda> at 0x7f8707a54158>, {3: defaultdict(<class 'int'>, {4: 1})})}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

