Python – Value nested grouping on List



Sometimes, while working with data, we can have a problem in which we have
flat data in the form of list of dictionaries, and we need to perform the
categorization from that bare dictionaries according to ids. This can have
application in domains which involve data, such as web development and Data
Science. Let’s discuss certain way in which this task can be performed.

 **Method : Usingdefaultdict() + setdefault() \+ loop**  
The combination of above functionalities can be used to perform this task.
This is brute way in which this can be performed. In this, we initialize the
defaultdict() with dictionary values for nested records formation and
according populate the data using setdefault() and conditions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Value nested grouping on List

# Using loop + setdefault() + defaultdict()

from collections import defaultdict

 

# initializing list

test_list = [{ 'value' : 'Fruit'},

 { 'tag' : 'Fruit', 'value' : 'mango'},

 { 'value' : 'Car'},

 { 'tag' : 'Car', 'value' : 'maruti'},

 { 'tag' : 'Fruit', 'value' : 'orange'},

 { 'tag' : 'Car', 'value' : 'city'}]

 

 

# printing original list

print("The original list is : " + str(test_list))

 

# Value nested grouping on List

# Using loop + setdefault() + defaultdict()

temp = defaultdict(dict)

res = {}

for sub in test_list:

 type = sub['value']

 if 'tag' in sub:

 tag = sub['tag']

 temp[tag].setdefault(type, temp[type])

 else:

 res[type] = temp[type]

 

# printing result 

print("The dictionary after grouping : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘value’: ‘Fruit’}, {‘tag’: ‘Fruit’, ‘value’:
> ‘mango’}, {‘value’: ‘Car’}, {‘tag’: ‘Car’, ‘value’: ‘maruti’}, {‘tag’:
> ‘Fruit’, ‘value’: ‘orange’}, {‘tag’: ‘Car’, ‘value’: ‘city’}]  
> The dictionary after grouping : {‘Fruit’: {‘mango’: {}, ‘orange’: {}},
> ‘Car’: {‘city’: {}, ‘maruti’: {}}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

