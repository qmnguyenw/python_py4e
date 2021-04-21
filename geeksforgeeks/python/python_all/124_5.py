Python | Remove duplicate lists in tuples (Preserving Order)



Sometimes, while working with records, we can have a problem in which we need
to remove duplicate records. This kind of problem is common in web development
domain. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +set()**  
In this method, we test for each list as it appears and add it to set so that
it’s repeated occurrence can be avoided and then this is added to newly
maintained unique tuple, removing duplicates.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove duplicate lists in tuples(Preserving Order)

# Using list comprehension + set()

 

# Initializing tuple 

test_tup = ([4, 7, 8], [1, 2, 3], [4, 7,
8], [9, 10, 11], [1, 2, 3])

 

# printing original tuple 

print("The original tuple is : " + str(test_tup))

 

# Remove duplicate lists in tuples(Preserving Order)

# Using list comprehension + set()

temp = set()

res = [ele for ele in test_tup if not(tuple(ele) in
temp or temp.add(tuple(ele)))]

 

# printing result

print("The unique lists tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
    The unique lists tuple is : [[4, 7, 8], [1, 2, 3], [9, 10, 11]]
    

**Method #2 : UsingOrderedDict() + tuple()**  
The combination of above functions can also be used to perform this particular
task. In this, we convert the tuple to OrderedDict(), which autoatically
removes the duplicate elemets and then construct a new tuple list using
tuple().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove duplicate lists in tuples(Preserving Order)

# Using OrderedDict() + tuple()

from collections import OrderedDict

 

# Initializing tuple 

test_tup = ([4, 7, 8], [1, 2, 3], [4, 7,
8], [9, 10, 11], [1, 2, 3])

 

# printing original tuple 

print("The original tuple is : " + str(test_tup))

 

# Remove duplicate lists in tuples(Preserving Order)

# Using OrderedDict() + tuple()

res = list(OrderedDict((tuple(x), x) for x in
test_tup).values())

 

# printing result

print("The unique lists tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
    The unique lists tuple is : [[4, 7, 8], [1, 2, 3], [9, 10, 11]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

