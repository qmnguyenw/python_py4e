Python | Convert Tuples to Dictionary



Conversions among datatypes are quite popular utility and hence having
knowledge of it always proves out to be quite handy. The conversion of a list
of tuples into a dictionary had been discussed earlier, sometimes, we might
have a key and a value tuple to be converted to a dictionary. Let’s discuss
certain ways in which this can be performed.

 **Method #1 : Using Dictionary Comprehension**  
This task can be performed using the dictionary comprehension in which we can
iterate through the key and value tuple simultaneously using enumerate() and
construct the desired dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuples to Dictionary

# Using Dictionary Comprehension

# Note: For conversion of two tuples into a dictionary, we've to have the
same length of tuples. Otherwise, we can not match all the key-value pairs

 

# initializing tuples

test_tup1 = ('GFG', 'is', 'best')

test_tup2 = (1, 2, 3)

 

# printing original tuples

print("The original key tuple is : " + str(test_tup1))

print("The original value tuple is : " + str(test_tup2))

 

# Using Dictionary Comprehension

# Convert Tuples to Dictionary

if len(test_tup1) == len(test_tup2):

 res = {test_tup1[i] : test_tup2[i] for i, _ in
enumerate(test_tup2)}

 

# printing result 

print("Dictionary constructed from tuples : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original key tuple is : ('GFG', 'is', 'best')
    The original value tuple is : (1, 2, 3)
    Dictionary constructed from tuples : {'best': 3, 'is': 2, 'GFG': 1}
    

**Method #2 : Usingzip() + dict()**  
This is yet another method in which this task can be performed in which a
combination of zip function and dict function achieve this task. The zip
function is responsible for conversion of tuple to key-value pair with
corresponding indices. The dict function performs the task of conversion to
dictionary.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Tuples to Dictionary

# Using zip() + dict()

 

# initializing tuples

test_tup1 = ('GFG', 'is', 'best')

test_tup2 = (1, 2, 3)

 

# printing original tuples

print("The original key tuple is : " + str(test_tup1))

print("The original value tuple is : " + str(test_tup2))

 

# Using zip() + dict()

# Convert Tuples to Dictionary

if len(test_tup1) == len(test_tup2):

 res = dict(zip(test_tup1, test_tup2))

 

# printing result 

print("Dictionary constructed from tuples : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original key tuple is : ('GFG', 'is', 'best')
    The original value tuple is : (1, 2, 3)
    Dictionary constructed from tuples : {'GFG': 1, 'is': 2, 'best': 3}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

