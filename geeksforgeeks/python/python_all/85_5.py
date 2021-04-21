Python – Group records by Kth column in List



Sometimes, while working with Python lists, we can have a problem in which we
need to perform grouping of records on basis of certain parameters. One such
parameters can be on the Kth element of Tuple. Lets discuss certain ways in
which this task can be performed.

 **Method #1 : Using loop +defaultdict()**  
The combination of above methods can be used to perform this task. In this we
store the tuples in different list on basis of Kth Column using defaultdict
and iteration using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Group records by Kth column in List

# using loop + defaultdict()

from collections import defaultdict

 

# Initializing list

test_list = [('Gfg', 1), ('is', 2), ('Gfg', 3),
('is', 4), ('best', 5)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 0

 

# Group records by Kth column in List

# using loop + defaultdict()

temp = defaultdict(list)

for ele in test_list:

 temp[ele[K]].append(ele)

res = list(temp.values())

 

# printing result 

print ("The list after grouping : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('Gfg', 1), ('is', 2), ('Gfg', 3), ('is', 4), ('best', 5)]
    The list after grouping : [[('Gfg', 1), ('Gfg', 3)], [('is', 2), ('is', 4)], [('best', 5)]]
    

**Method #2 : Usingitemgetter() + groupby() \+ list comprehension**  
The combination of above function can also be performed using above functions.
In this, itemgetter is used to select Kth Column, groupby() is used to group
and list comprehension is used to compile the result.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Group records by Kth column in List

# using itemgetter() + list comprehension + groupby()

from operator import itemgetter

from itertools import groupby

 

# Initializing list

test_list = [('Gfg', 1), ('is', 2), ('Gfg', 3),
('is', 4), ('best', 5)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 0

 

# Group records by Kth column in List

# using loop + defaultdict()

temp = itemgetter(K)

res = [list(val) for key, val in
groupby(sorted(test_list, key = temp), temp)]

 

# printing result 

print ("The list after grouping : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('Gfg', 1), ('is', 2), ('Gfg', 3), ('is', 4), ('best', 5)]
    The list after grouping : [[('Gfg', 1), ('Gfg', 3)], [('is', 2), ('is', 4)], [('best', 5)]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

