Python | Substring Key match in dictionary



Sometimes, while working with dictionaries, we might have a use case in which
we are not known the exact keys we require but just a specific part of keys
that we require to fetch. This kind of problem can arise in many applications.
Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Usingitems() \+ list comprehension**  
The combination of above method can be used to perform this particular task in
which we just access the key value pairs using the items function and list
comprehension helps in the iteration and access logic.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substring Key match in dictionary

# Using items() + list comprehension

 

# initializing dictionary

test_dict = {'All' : 1, 'have' : 2, 'good' : 3,
'food' : 4}

 

# initializing search key string

search_key = 'ood'

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using items() + list comprehension

# Substring Key match in dictionary

res = [val for key, val in test_dict.items() if search_key
in key]

 

# printing result 

print("Values for substring keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'All': 1, 'food': 4, 'have': 2, 'good': 3}
    Values for substring keys : [4, 3]
    

**Method #2 : Usingdict() + filter() \+ lambda**  
The combination of above functions can be used to perform this particular
task. In this, the dict and filter function is used to convert the result
to dictionary and query for the substring in list respectively. The lambda
performs the task of accessing all key-value pairs.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substring Key match in dictionary

# Using dict() + filter() + lambda

 

# initializing dictionary

test_dict = {'All' : 1, 'have' : 2, 'good' : 3,
'food' : 4}

 

# initializing search key string

search_key = 'ood'

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using dict() + filter() + lambda

# Substring Key match in dictionary

res = dict(filter(lambda item: search_key in item[0],
test_dict.items()))

 

# printing result 

print("Key-Value pair for substring keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'have': 2, 'good': 3, 'food': 4, 'All': 1}
    Key-Value pair for substring keys : {'good': 3, 'food': 4}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

