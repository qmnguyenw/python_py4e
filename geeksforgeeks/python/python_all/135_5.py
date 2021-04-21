Python | Get values of particular key in list of dictionaries



Sometimes, we may require a way in which we have to get all the values of
specific key from a list of dictionary. This kind of problem has a lot of
application in web development domain in which we sometimes have a json and
require just to get single column from records. Let’s discuss certain ways in
which this problem can be solved.

 **Method #1 : Using list comprehension**  
Using list comprehension is quite straight forward method to perform this
particular task. In this, we just iterate over the list of dictionary for
desired value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get values of particular key in list of dictionaries

# Using list comprehension

 

# initializing list

test_list = [{'gfg' : 1, 'is' : 2, 'good' : 3}, 

 {'gfg' : 2}, {'best' : 3, 'gfg' : 4}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Using list comprehension

# Get values of particular key in list of dictionaries

res = [ sub['gfg'] for sub in test_list ]

 

# printing result 

print("The values corresponding to key : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [{‘is’: 2, ‘gfg’: 1, ‘good’: 3}, {‘gfg’: 2}, {‘best’:
> 3, ‘gfg’: 4}]  
> The values corresponding to key : [1, 2, 4]

  

  

**Method #2 : Usingmap() \+ itemgetter()**  
This problem can also be solved using another technique using map() and
itemgetter(). In this, map is used to link the value to all the dictionary
keys and itemgetter gets the desired key.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get values of particular key in list of dictionaries

# Using map() + itemgetter()

from operator import itemgetter

 

# initializing list

test_list = [{'gfg' : 1, 'is' : 2, 'good' : 3},

 {'gfg' : 2}, {'best' : 3, 'gfg' : 4}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Using map() + itemgetter()

# Get values of particular key in list of dictionaries

res = list(map(itemgetter('gfg'), test_list))

 

# printing result 

print("The values corresponding to key : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [{‘is’: 2, ‘gfg’: 1, ‘good’: 3}, {‘gfg’: 2}, {‘best’:
> 3, ‘gfg’: 4}]  
> The values corresponding to key : [1, 2, 4]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

