Python – Group Similar Start and End character words



Sometimes, while working with Python data, we can have problem in which we
need to group all the words on basis of front and end characters. This kind of
application is common in domains in which we work with data like web
development. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingdefaultdict() \+ loop**  
The combination of above functions can be used to perform this task. In this,
we check for front and last element using string slice notations and store in
dict. with first and last character as key.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Similar Start and End character words

# Using defaultdict() + loop

from collections import defaultdict

 

def end_check(word):

 sub1 = word.strip()[0]

 sub2 = word.strip()[-1]

 temp = sub1 + sub2

 return temp

 

def front_check(word):

 sub = word.strip()[1:-1]

 return sub

 

# initializing string

test_str = 'geeksforgeeks is indias best and bright for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Group Similar Start and End character words

# Using defaultdict() + loop

test_list = test_str.split()

res = defaultdict(set)

for ele in test_list:

 res[end_check(ele)].add(front_check(ele))

 

# printing result 

print("The grouped dictionary is : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

> The original string is : geeksforgeeks is indias best and bright for geeks  
> The grouped dictionary is : {‘fr’: {‘o’}, ‘bt’: {‘righ’, ‘es’}, ‘ad’: {‘n’},
> ‘gs’: {‘eeksforgeek’, ‘eek’}, ‘is’: {”, ‘ndia’}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

