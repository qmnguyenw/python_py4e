Python | Find top K frequent elements from a list of tuples



Given a list of tuples with word as first element and its frequency as second
element, the task is to find top _k_ frequent element.

Below are some ways to above achieve the above task.

 **Method #1: Usingdefaultdict**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find top 'k' frequent element

 

# Importing

import collections

from operator import itemgetter

from itertools import chain

 

# Input list initialization

Input =[[('Name', 151)], [('ACe', 400)],

 [('TURN', 210)], [('RED', 1113)],

 [('YELLOW', 1)]]

 

# K initialization

K = 3

 

# Using defaultdict to find top 'k' frequent element

dict_ = collections.defaultdict(list)

new_list = list(chain.from_iterable(Input))

 

for elem in new_list:

 dict_[elem[0]].append(elem[1])

 

res = {k: sum(v) for k, v in dict_.items()}

 

# Using sorted

Output = sorted(res.items(), key = itemgetter(1),

 reverse = True)[0:K]

 

# printing output

print("Initial List of tuple is", Input)

print("\nTop 'K' elements are", Output)  
  
---  
  
 __

 __

 **Output:**

> Initial List of tuple is [[(‘Name’, 151)], [(‘ACe’, 400)], [(‘TURN’, 210)],
> [(‘RED’, 1113)], [(‘YELLOW’, 1)]]
>
>  
>
>
>  
>
>
> Top ‘K’ elements are [(‘RED’, 1113), (‘ACe’, 400), (‘TURN’, 210)]

  
**Method #2: Usingitertools and sorted**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find top 'k' frequent element

from operator import itemgetter

from itertools import chain

 

# Input list initialization

Input =[[('Name', 151)], [('ACe', 400)],

 [('TURN', 210)], [('RED', 1113)],

 [('YELLOW', 1)]]

 

# k initialization

K = 3

 

# Finding top 'k' frequent element 

# without using collection

Output = sorted(list(chain.from_iterable(Input)),

 key = itemgetter(1), reverse = True)[0:K]

 

# Printing Output

print("Initial List of tuple is", Input)

print("\nTop 'K' elements are", Output)  
  
---  
  
 __

 __

 **Output:**

> Initial List of tuple is [[(‘Name’, 151)], [(‘ACe’, 400)], [(‘TURN’, 210)],
> [(‘RED’, 1113)], [(‘YELLOW’, 1)]]
>
> Top ‘K’ elements are [(‘RED’, 1113), (‘ACe’, 400), (‘TURN’, 210)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

