Python | Convert list of tuples to dictionary value lists



One among the problem of interconversion of data types in python is conversion
of list of tuples to dictionaries, in which the keys are 1st element of tuple,
which are uniquely identified as keys in dictionary and it’s corresponding
value as list of corresponding value of respective keys as tuple’s second
element. Let’s discuss how to solve this particular problem.

 **Method #1 : Using defaultdict() + loop**  
This problem can easily be solved using the defaultdict() and loop. The
defaultdict provides a default value dictionary container to assign
corresponding value list to keys, so that we don’t need to initialize keys
with empty list and loop is used to extract like values from tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert list of tuples to dictionary value lists

# Using defaultdict() + loop

from collections import defaultdict

 

# initializing list

test_list = [(1, 'gfg'), (1, 'is'), (2, 'best'),
(3, 'for'), (4, 'CS')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Using defaultdict() + loop

# Convert list of tuples to dictionary value lists

res = defaultdict(list)

for i, j in test_list:

 res[i].append(j)

 

# printing result 

print("The merged dictionary is : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [(1, ‘gfg’), (1, ‘is’), (2, ‘best’), (3, ‘for’), (4,
> ‘CS’)]  
> The merged dictionary is : {1: [‘gfg’, ‘is’], 2: [‘best’], 3: [‘for’], 4:
> [‘CS’]}

  

  

**Method #2 : Usingdefaultdict() + groupby()**  
This method performs the task similar to above method, just instead of using
loop to access each key value pair, here we use Python’s groupby library to
group keys with value and convert then into a list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert list of tuples to dictionary value lists

# Using defaultdict() + groupby()

from collections import defaultdict

from operator import itemgetter

from itertools import groupby

 

# initializing list

test_list = [(1, 'gfg'), (1, 'is'), (2, 'best'),
(3, 'for'), (4, 'CS')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Using defaultdict() + groupby()

# Convert list of tuples to dictionary value lists

res = dict((k, [v[1] for v in itr]) for k, itr in
groupby(

 test_list, itemgetter(0)))

 

# printing result 

print("The merged dictionary is : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [(1, ‘gfg’), (1, ‘is’), (2, ‘best’), (3, ‘for’), (4,
> ‘CS’)]  
> The merged dictionary is : {1: [‘gfg’, ‘is’], 2: [‘best’], 3: [‘for’], 4:
> [‘CS’]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

