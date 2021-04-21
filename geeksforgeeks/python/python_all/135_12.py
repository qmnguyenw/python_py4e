Python | Key index in Dictionary



The concept of dictionary is similar to that of map data structure in C++
language, but with the exception that keys in dictionary has nothing to do
with its ordering, i.e it is not sorted unlike C++ in which the keys are
sorted internally. This opens up the problem in which we might have to find
the exact position of key in the dictionary. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Using list comprehension +enumerate()**  
The combination of above functions together can perform this particular task.
In this, first the dictionary is converted to a pair tuple and then the first
element of tuple being the key is checked for index.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Key index in Dictionary

# Using list comprehension + enumerate()

 

# initializing dictionary

test_dict = {'all' : 1, 'food' : 2, 'good' : 3,
'have' : 4}

 

# initializing search key string

search_key = 'good'

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using list comprehension + enumerate()

# Key index in Dictionary

temp = list(test_dict.items()) 

res = [idx for idx, key in enumerate(temp) if key[0]
== search_key]

 

# printing result 

print("Index of search key is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'have': 4, 'all': 1, 'good': 3, 'food': 2}
    Index of search key is : [2]
    

**Method #2 : Usinglist() + keys() + index()**  
The combination of above functions can also be used to perform this particular
task. In this, the dictionary keys are first converted to list and then found
the desired one using the index method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Key index in Dictionary

# Using list() + keys() + index()

 

# initializing dictionary

test_dict = {'all' : 1, 'food' : 2, 'good' : 3,
'have' : 4}

 

# initializing search key string

search_key = 'good'

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using list() + keys() + index()

# Key index in Dictionary

res = list(test_dict.keys()).index(search_key)

 

# printing result 

print("Index of search key is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'food': 2, 'have': 4, 'good': 3, 'all': 1}
    Index of search key is : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

