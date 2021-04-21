Python | Grouping list values into dictionary



Sometimes, while working with data, we can be encountered with a situation in
which we have list of list and we need to group it’s 2nd index with the common
initial element in lists. Let’s discuss way in which this problem can be
solved.

 **Method : Usingdefaultdict() \+ loop + dict()**

The defaultdict can be used to initialize the group elements and loop can be
used to group the values together and conversion to dictionary can be done
using dict().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Grouping list values into dictionary

# Using defaultdict() + loop + dict()

from collections import defaultdict

 

# initializing list

test_list = [['Gfg', 1], ['Gfg', 2], ['is', 3],
['best', 4], ['is', 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Grouping list values into dictionary

# Using defaultdict() + loop + dict()

temp = defaultdict(list)

for key, val in test_list:

 temp[key].append(val)

res = dict((key, tuple(val)) for key, val in temp.items())

 

# printing result

print("The grouped dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [['Gfg', 1], ['Gfg', 2], ['is', 3], ['best', 4], ['is', 5]]
    The grouped dictionary is :  {'Gfg': (1, 2), 'best': (4, ), 'is': (3, 5)}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

