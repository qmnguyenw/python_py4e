Python | Counting Nth tuple element



Sometimes, while working with Python, we can have a problem in which we need
to count the occurrence of a particular’s elements. This kind of problem is
quite common while working with records. Let’s discuss a way in which this
task can be performed.

 **Method #1 : UsingCounter() \+ generator expression**  
The combination of above functionalities can be used to achieve this
particular task. In this, we iterate through a specific index using generator
expression and compute the count using Counter().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Counting Nth tuple element

# using Counter() + generator expression

from collections import Counter

 

# initialize list

test_list = [('gfg', 0), ('is', 1), ('best', 2),

 ('gfg', 2), ('is', 0), ('for', 1),

 ('geeks', 2)]

 

# printing original list

print("The original list : " + str(test_list))

 

# initialize N

N = 1

 

# Counting Nth tuple element

# using Counter() + generator expression

res = dict(Counter(sub[N] for sub in test_list))

 

# printing result

print("The grouped Nth element frequency is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [(‘gfg’, 0), (‘is’, 1), (‘best’, 2), (‘gfg’, 2), (‘is’,
> 0), (‘for’, 1), (‘geeks’, 2)]  
> The grouped Nth element frequency is : {0: 2, 1: 2, 2: 3}

  

  

**Method #2 : UsingCounter() + map() + itemgetter()**  
The combination of above functions can be used to achieve this task. In this,
the task performed by generator expression is performed by map() and
itemgetter() is used to get the index of the container element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Counting Nth tuple element

# using Counter() + map() + itemgetter()

from collections import Counter

from operator import itemgetter

 

# initialize list

test_list = [('gfg', 0), ('is', 1), ('best', 2),


 ('gfg', 2), ('is', 0), ('for', 1),

 ('geeks', 2)]

 

# printing original list

print("The original list : " + str(test_list))

 

# initialize N

N = 1

 

# Counting Nth tuple element

# using Counter() + map() + itemgetter()

res = dict(Counter(map(itemgetter(N), test_list)))

 

# printing result

print("The grouped Nth element frequency is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [(‘gfg’, 0), (‘is’, 1), (‘best’, 2), (‘gfg’, 2), (‘is’,
> 0), (‘for’, 1), (‘geeks’, 2)]  
> The grouped Nth element frequency is : {0: 2, 1: 2, 2: 3}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

