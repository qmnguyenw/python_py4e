Python | Group and count similar records



Sometimes, while working with records, we can have a problem in which we need
to collect and maintain the counter value inside records. This kind of
application is important in web development domain. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Using loop +Counter() + set()**  
The combination of above functionalities can be employed to achieve this task.
In this, we run a loop to capture each tuple and add to set and check if it’s
already existing, then increase and add a counter value to it. The cumulative
count is achieved by using Counter().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group and count similar records

# using Counter() + loop + set()

from collections import Counter

 

# initialize list

test_list = [('gfg', ), ('is', ), ('best', ), ('gfg', ),

 ('is', ), ('for', ), ('geeks', )]

 

# printing original list

print("The original list : " + str(test_list))

 

# Group and count similar records

# using Counter() + loop + set()

res = []

temp = set()

counter = Counter(test_list)

for sub in test_list:

 if sub not in temp:

 res.append((counter[sub], ) + sub)

 temp.add(sub)

 

# printing result

print("Grouped and counted list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [(‘gfg’, ), (‘is’, ), (‘best’, ), (‘gfg’, ), (‘is’, ),
> (‘for’, ), (‘geeks’, )]  
> Grouped and counted list is : [(2, ‘gfg’), (2, ‘is’), (1, ‘best’), (1,
> ‘for’), (1, ‘geeks’)]

  

  

**Method #2 : UsingCounter() + list comprehension + items()**

This is one liner approach and recommended to use for programming. The task of
loops is handled by list comprehension and items() is used to access all the
elements of Counter converted dictionary to allow computations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group and count similar records

# using Counter() + list comprehension + items()

from collections import Counter

 

# initialize list

test_list = [('gfg', ), ('is', ), ('best', ), ('gfg', ),

 ('is', ), ('for', ), ('geeks', )]

 

# printing original list

print("The original list : " + str(test_list))

 

# Group and count similar records

# using Counter() + list comprehension + items()

res = [(counter, ) + ele for ele, counter in
Counter(test_list).items()]

 

# printing result

print("Grouped and counted list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [(‘gfg’, ), (‘is’, ), (‘best’, ), (‘gfg’, ), (‘is’, ),
> (‘for’, ), (‘geeks’, )]  
> Grouped and counted list is : [(2, ‘gfg’), (2, ‘is’), (1, ‘best’), (1,
> ‘for’), (1, ‘geeks’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

