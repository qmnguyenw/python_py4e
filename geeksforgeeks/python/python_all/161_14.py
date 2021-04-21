Python | Set Difference in list of dictionaries



The difference of two lists have been discussed many a times, but sometimes we
have a large number of data and we need to find the difference i.e the
elements in dict2 not in 1 to reduce the redundancies. Let’s discuss certain
ways in which this can be done.

 **Method #1 : Using list comprehension**  
The naive method to iterate both the list and extract the difference can be
shortened to the method in which we shorten the code and increase the
readability using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# set difference in dictionary list 

# using list comprehension

 

# initializing list 

test_list1 = [{"HpY" : 22}, {"BirthdaY" : 2}, ]

test_list2 = [{"HpY" : 22}, {"BirthdaY" : 2},
{"Shambhavi" : 2019}]

 

# printing original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# using list comprehension

# set difference in dictionary list 

res = [i for i in test_list1 if i not in test_list2] \

 + [j for j in test_list2 if j not in test_list1]

 

# printing result 

print ("The set difference of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [{‘HpY’: 22}, {‘BirthdaY’: 2}]  
> The original list 2 is : [{‘HpY’: 22}, {‘BirthdaY’: 2}, {‘Shambhavi’: 2019}]  
> The set difference of list is : [{‘Shambhavi’: 2019}]

  
**Method #2 : Usingitertools.filterfalse()**  
This is a different way in which this particular task can be performed using
the in built python function. The filterfalse method filters the not present
element of one list with respect to other.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# set difference in dictionary list 

# using itertools.filterfalse()

import itertools

 

# initializing list 

test_list1 = [{"HpY" : 22}, {"BirthdaY" : 2}, ]

test_list2 = [{"HpY" : 22}, {"BirthdaY" : 2},
{"Shambhavi" : 2019}]

 

# printing original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# using itertools.filterfalse()

# set difference in dictionary list 

res = list(itertools.filterfalse(lambda i: i in test_list1,
test_list2)) \

 + list(itertools.filterfalse(lambda j: j in test_list2,
test_list1))

 

# printing result 

print ("The set difference of list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [{‘HpY’: 22}, {‘BirthdaY’: 2}]  
> The original list 2 is : [{‘HpY’: 22}, {‘BirthdaY’: 2}, {‘Shambhavi’: 2019}]  
> The set difference of list is : [{‘Shambhavi’: 2019}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

