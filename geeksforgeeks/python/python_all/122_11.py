Python | Top N pairs by Kth element from list



Sometimes, while working with data, we can have a problem in which we need to
get the maximum of elements filtered by the Kth element of record. This has a
very important utility in web development domain. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Usingfilter() + lambda + set() \+ list comprehension**

The combination of above functions can be used to perform this particular
function. In this, we first filter the top N elements from Kth index and then
apply these values to the list and return the result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Top N pairs by Kth element from list

# Using filter() + lambda + set() + list comprehension

 

# initialize list 

test_list = [('gfg', 4, 'good'), ('gfg', 2,
'better'), 

 ('gfg', 1, 'best'), ('gfg', 3, 'geeks')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize N 

N = 3

 

# initialize K 

K = 1

 

# Top N pairs by Kth element from list

# Using filter() + lambda + set() + list comprehension

temp = set(list({sub[K] for sub in test_list})[-N:])

res = list(filter(lambda sub: sub[K] in temp, test_list))

 

# printing result

print("Top N elements of Kth index are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [(‘gfg’, 4, ‘good’), (‘gfg’, 2, ‘better’), (‘gfg’, 1,
> ‘best’), (‘gfg’, 3, ‘geeks’)]  
> Top N elements of Kth index are : [(‘gfg’, 4, ‘good’), (‘gfg’, 2, ‘better’),
> (‘gfg’, 3, ‘geeks’)]
>
>  
>
>
>  
>

**Method #2 : Usinggroupby() + sorted() \+ loop**

This task can also be performed using above functionalities. In this, we first
group the top N elements together and then limit by N while constructing the
result list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Top N pairs by Kth element from list

# Using groupby() + sorted() + loop

import itertools

 

# initialize list 

test_list = [('gfg', 4, 'good'), ('gfg', 2,
'better'),

 ('gfg', 1, 'best'), ('gfg', 3, 'geeks')]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize N 

N = 3

 

# initialize K 

K = 1

 

# Top N pairs by Kth element from list

# Using groupby() + sorted() + loop

res = []

temp = itertools.groupby(sorted(test_list, key = lambda sub :
sub[K], 

 reverse = True), key = lambda sub : sub[K])

for i in range(N):

 res.extend(list(next(temp)[K]))

 

# printing result

print("Top N elements of Kth index are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [(‘gfg’, 4, ‘good’), (‘gfg’, 2, ‘better’), (‘gfg’, 1,
> ‘best’), (‘gfg’, 3, ‘geeks’)]  
> Top N elements of Kth index are : [(‘gfg’, 4, ‘good’), (‘gfg’, 2, ‘better’),
> (‘gfg’, 3, ‘geeks’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

