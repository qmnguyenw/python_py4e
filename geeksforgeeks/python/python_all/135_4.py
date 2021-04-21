Python | Merge key value lists



Sometimes, while working with lists, we can come forward with a problem in
which we need to perform the merge function in which we have the key list and
need to create dictionary mapping keys with corresponding value in other list.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingzip() \+ loop + defaultdict()**  
The combination of above method can be used to perform this particular task.
In this, we use zip function to match the like elements of lists with each
other and loop is then used to assign the keys with value from zipped list to
add value to a defaultdict.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Merge key value list

# Using zip() + loop + defaultdict()

from collections import defaultdict

 

# initializing lists

test_list1 = [0, 0, 0, 1, 1, 1, 2, 2]

test_list2 = ['gfg', 'is', 'best', 'Akash', 'Akshat',
'Nikhil', 'apple', 'grapes']

 

# printing original lists

print("The original list1 is : " + str(test_list1))

print("The original list2 is : " + str(test_list2))

 

# Using zip() + loop + defaultdict()

# Merge key value list

res = defaultdict(list)

for i, j in zip(test_list1, test_list2):

 res[i].append(j)

 

# printing result 

print("The merged key value dictionary is : " +
str(dict(res)))  
  
---  
  
 __

 __

 **Output :**

> The original list1 is : [0, 0, 0, 1, 1, 1, 2, 2]  
> The original list2 is : [‘gfg’, ‘is’, ‘best’, ‘Akash’, ‘Akshat’, ‘Nikhil’,
> ‘apple’, ‘grapes’]  
> The merged key value dictionary is : {0: [‘gfg’, ‘is’, ‘best’], 1: [‘Akash’,
> ‘Akshat’, ‘Nikhil’], 2: [‘apple’, ‘grapes’]}

  

  

**Method #2 : Usingitemgetter() + groupby() + zip()**  
This is yet another way to perform this particular task. In this, we group the
keys fetched by itemgetter to the first list with the elements of other list
which is linked using the zip function using groupby method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Merge key value list

# Using itemgetter() + groupby() + zip()

from itertools import groupby

from operator import itemgetter

 

# initializing lists

test_list1 = [0, 0, 0, 1, 1, 1, 2, 2]

test_list2 = ['gfg', 'is', 'best', 'Akash', 'Akshat',
'Nikhil', 'apple', 'grapes']

 

# printing original lists

print("The original list1 is : " + str(test_list1))

print("The original list2 is : " + str(test_list2))

 

# Using itemgetter() + groupby() + zip()

# Merge key value list

res = {keys: [i for _, i in sub] for keys, sub in
groupby(

 zip(test_list1, test_list2), key = itemgetter(0))}

 

# printing result 

print("The merged key value dictionary is : " +
str(dict(res)))  
  
---  
  
 __

 __

 **Output :**

> The original list1 is : [0, 0, 0, 1, 1, 1, 2, 2]  
> The original list2 is : [‘gfg’, ‘is’, ‘best’, ‘Akash’, ‘Akshat’, ‘Nikhil’,
> ‘apple’, ‘grapes’]  
> The merged key value dictionary is : {0: [‘gfg’, ‘is’, ‘best’], 1: [‘Akash’,
> ‘Akshat’, ‘Nikhil’], 2: [‘apple’, ‘grapes’]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

