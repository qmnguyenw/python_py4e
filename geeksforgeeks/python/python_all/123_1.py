Python | Aggregate values by tuple keys



Sometimes, while working with records, we can have a problem in which we need
to group the like keys and aggregate the values of like keys. This can have
application in any kind of scoring. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : UsingCounter() \+ generator expression**  
The combination of above functions can be used to perform this particular
task. In this, we need to first combine the like key elements and task of
aggregation is performed by Counter().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Aggregate values by tuple keys

# using Counter() + generator expression

from collections import Counter

 

# initialize list

test_list = [('gfg', 50), ('is', 30), ('best',
100), 

 ('gfg', 20), ('best', 50)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Aggregate values by tuple keys

# using Counter() + generator expression

res = list(Counter(key for key, num in test_list 

 for idx in range(num)).items())

 

# printing result

print("List after grouping : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('gfg', 50), ('is', 30), ('best', 100), ('gfg', 20), ('best', 50)]
    List after grouping : [('best', 150), ('gfg', 70), ('is', 30)]
    

**Method #2 : Usinggroupby() + map() + itemgetter() + sum()**  
The combination of above functions can also be used to perform this particular
task. In this, we group the elements using groupby(), decision of key’s index
is given by itemgetter. Task of addition(aggregation) is performed by sum()
and extension of logic to all tuples is handled by map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Aggregate values by tuple keys

# using groupby() + map() + itemgetter() + sum()

from itertools import groupby

from operator import itemgetter

 

# initialize list

test_list = [('gfg', 50), ('is', 30), ('best',
100),

 ('gfg', 20), ('best', 50)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Aggregate values by tuple keys

# using groupby() + map() + itemgetter() + sum()

res = [(key, sum(map(itemgetter(1), ele)))

 for key, ele in groupby(sorted(test_list, key =
itemgetter(0)), 

 key = itemgetter(0))]

 

# printing result

print("List after grouping : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('gfg', 50), ('is', 30), ('best', 100), ('gfg', 20), ('best', 50)]
    List after grouping : [('best', 150), ('gfg', 70), ('is', 30)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

