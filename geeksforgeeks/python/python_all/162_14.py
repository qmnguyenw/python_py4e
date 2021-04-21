Python | Type conversion in dictionary values



The problem of conventional type conversion is quite common and can be easily
done using the built-in converters of python libraries. But sometimes, we may
require the same functionality in a more complex scenario vis. for keys of
list of dictionaries. Let’s discuss certain ways in which this can be
achieved.  

 **Method #1 : Naive Method**  
In the naive method, we employ 2 loops, nested. One for all the dictionaries
in the list and the second one for the dictionary key-value pairs in a
specific dictionary.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Type conversion in list of dicts.

# using naive method

 

# initializing list of dictionary

test_list = [{'a' : '1', 'b' : '2'}, { 'c' : '3',
'd' : '4'}]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using naive method

# type converstion in list of dicts.

for dicts in test_list:

 for keys in dicts:

 dicts[keys] = int(dicts[keys])

 

# printing result 

print ("The modified converted list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [{'a': '1', 'b': '2'}, {'c': '3', 'd': '4'}]
    The modified converted list is : [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
    

**Method #2 : Usingitems() \+ list comprehension**  
This can easily performed using just a one line with the help of list
comprehension. The items function can be exploited to extract the list values
as when required and list comprehension part handles the iteration part.  

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Type conversion in list of dicts.

# using items() + list comprehension

 

# initializing list of dictionary

test_list = [{'a' : '1', 'b' : '2'}, { 'c' : '3',
'd' : '4'}]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using items() + list comprehension

# type converstion in list of dicts.

res = [dict([key, int(value)] 

 for key, value in dicts.items()) 

 for dicts in test_list]

 

# printing result 

print ("The modified converted list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [{'b': '2', 'a': '1'}, {'c': '3', 'd': '4'}]
    The modified converted list is : [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

