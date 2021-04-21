Python | Get duplicate tuples from list



Sometimes, while working with records, we can have a problem of extracting
those records which occur more than once. This kind of application can occur
in web development domain. Let’s discuss certain ways in which this task can
be performed.

 **Method #1 : Using list comprehension +set() + count()**  
Initial approach that can be applied is that we can iterate on each tuple and
check it’s count in list using count(), if greater than one, we can add to
list. To remove multiple additions, we can convert the result to set using
set().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get duplicate tuples from list

# Using list comprehension + set() + count()

 

# initialize list

test_list = [(3, 4), (4, 5), (3, 4), 

 (3, 4), (4, 5), (6, 7)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Get duplicate tuples from list

# Using list comprehension + set() + count()

res = list(set([ele for ele in test_list

 if test_list.count(ele) > 1]))

 

# printing result

print("All the duplicates from list are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(3, 4), (4, 5), (3, 4), (3, 4), (4, 5), (6, 7)]
    All the duplicates from list are : [(4, 5), (3, 4)]
    

**Method #2 : UsingCounter() + items() \+ list comprehension**  
The combination of above functions can also be used to perform this particular
task. In this, we just get the count of each occurrence of element using
Counter() as dictionary and then extract all those whose value is above 1.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get duplicate tuples from list

# Using list comprehension + Counter() + items()

from collections import Counter

 

# initialize list

test_list = [(3, 4), (4, 5), (3, 4), 

 (3, 4), (4, 5), (6, 7)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Get duplicate tuples from list

# Using list comprehension + Counter() + items()

res = [ele for ele, count in Counter(test_list).items()

 if count > 1]

 

# printing result

print("All the duplicates from list are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(3, 4), (4, 5), (3, 4), (3, 4), (4, 5), (6, 7)]
    All the duplicates from list are : [(4, 5), (3, 4)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

