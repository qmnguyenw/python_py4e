Python | Prefix key match in dictionary



Sometimes, while working with dictionaries, we can have a problem in which we
need to find the dictionary items that have some constraints on keys. One such
constraint can be a prefix match on keys. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Using dictionary comprehension + startswith()**  
The combination of above two methods can be used to perform this particular
task. In this, dictionary comprehension does the basic task of dictionary
construction and startswith() performs the utility task of checking keys
starting with specific prefix.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Prefix key match in dictionary

# Using dictionary comprehension + startswith()

 

# Initialize dictionary

test_dict = {'tough' : 1, 'to' : 2, 'do' : 3,
'todays' : 4, 'work' : 5}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize prefix 

test_pref = 'to'

 

# Using dictionary comprehension + startswith()

# Prefix key match in dictionary

res = {key:val for key, val in test_dict.items() 

 if key.startswith(test_pref)}

 

# printing result 

print("Filtered dictionary keys are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘to’: 2, ‘tough’: 1, ‘work’: 5, ‘todays’: 4,
> ‘do’: 3}  
> Filtered dictionary keys are : {‘to’: 2, ‘tough’: 1, ‘todays’: 4}

  

  

**Method #2 : Usingmap() + filter() + items() + startswith()**  
This particular task can also be performed using the combination of above
functions. The map function ties the filter logic of startswith() to each
dictionary’s items extracted by items()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Prefix key match in dictionary

# Using map() + filter() + items() + startswith()

 

# Initialize dictionary

test_dict = {'tough' : 1, 'to' : 2, 'do' : 3,
'todays' : 4, 'work' : 5}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize prefix 

test_pref = 'to'

 

# Using map() + filter() + items() + startswith()

# Prefix key match in dictionary

res = dict(filter(lambda item:
item[0].startswith(test_pref),

 test_dict.items()))

 

# printing result 

print("Filtered dictionary keys are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘to’: 2, ‘tough’: 1, ‘work’: 5, ‘todays’: 4,
> ‘do’: 3}  
> Filtered dictionary keys are : {‘to’: 2, ‘tough’: 1, ‘todays’: 4}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

