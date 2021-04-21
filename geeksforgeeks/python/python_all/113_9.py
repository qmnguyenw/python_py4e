Python | Minimum K records of Nth index in tuple list



Sometimes, while working with data, we can have a problem in which we need to
get the minimum of elements filtered by the Nth element of record. This has a
very important utility in web development domain. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Usingfilter() + lambda + set() \+ list comprehension**  
The combination of above functions can be used to perform this particular
function. In this, we first filter the min K elements from Nth index and then
apply this values to the list and return the result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum K records of Nth index in tuple list

# Using filter() + lambda + set() + list comprehension

 

# initialize list 

test_list = [('gfg', 4, 'good'), ('gfg', 2,
'better'), 

 ('gfg', 1, 'best'), ('gfg', 3, 'geeks')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize N 

N = 1

 

# initialize K 

K = 2

 

# Minimum K records of Nth index in tuple list

# Using filter() + lambda + set() + list comprehension

temp = set(list({sub[N] for sub in test_list})[ :K])

res = list(filter(lambda sub: sub[N] in temp, test_list))

 

# printing result

print("Min K elements of Nth index are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [(‘gfg’, 4, ‘good’), (‘gfg’, 2, ‘better’), (‘gfg’, 1,
> ‘best’), (‘gfg’, 3, ‘geeks’)]  
> Min K elements of Nth index are : [(‘gfg’, 2, ‘better’), (‘gfg’, 1, ‘best’)]

  

  

**Method #2 : Using groupby() + sorted() \+ loop**  
This task can also be performed using above functionalities. In this, we first
group the min K elements together and then limit by K while constructing the
result list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum K records of Nth index in tuple list

# Using groupby() + sorted() + loop

import itertools

 

# initialize list 

test_list = [('gfg', 4, 'good'), ('gfg', 2,
'better'),

 ('gfg', 1, 'best'), ('gfg', 3, 'geeks')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize N 

N = 1

 

# initialize K 

K = 2

 

# Minimum K records of Nth index in tuple list

# Using groupby() + sorted() + loop

res = []

temp = itertools.groupby(sorted(test_list, key = lambda sub :
sub[N]), 

 key = lambda sub : sub[N])

 

for i in range(K):

 res.extend(list(next(temp)[N]))

 

# printing result

print("Min K elements of Nth index are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [(‘gfg’, 4, ‘good’), (‘gfg’, 2, ‘better’), (‘gfg’, 1,
> ‘best’), (‘gfg’, 3, ‘geeks’)]  
> Min K elements of Nth index are : [(‘gfg’, 2, ‘better’), (‘gfg’, 1, ‘best’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

