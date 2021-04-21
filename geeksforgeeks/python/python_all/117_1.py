Python | Extract similar index elements



Sometimes, while working with Python data, we can have a problem in which we
require to extract the values across multiple lists which are having similar
index values. This kind of problem can come in many domains. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Using loop + zip()**  
The combination of above functions can be used to solve this problem. In this,
we extract combine the index elements using zip and then extract and check for
similarity using conditional statement in loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extracting similar index elements

# using loop + zip()

 

# initialize lists

test_list1 = ["a", "b", "c", "d"]

test_list2 = ["g", "b", "s", "d"]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Extracting similar index elements

# using loop + zip()

res = []

for i, j in zip(test_list1, test_list2):

 if i == j:

 res.append(i)

 

# printing result

print("Similar index elements in lists : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : ['a', 'b', 'c', 'd']
    The original list 2 : ['g', 'b', 's', 'd']
    Similar index elements in lists : ['b', 'd']
    

**Method #2 : Usingzip() \+ list comprehension**  
Combination of these functionalities can also be used to solve this problem.
In this, we use similar method as above, just a shorthand logic compressed
using list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extracting similar index elements

# using list comprehension + zip()

 

# initialize lists

test_list1 = ["a", "b", "c", "d"]

test_list2 = ["g", "b", "s", "d"]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Extracting similar index elements

# using list comprehension + zip()

res = [i for i, j in zip(test_list1, test_list2) if i
== j]

 

# printing result

print("Similar index elements in lists : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : ['a', 'b', 'c', 'd']
    The original list 2 : ['g', 'b', 's', 'd']
    Similar index elements in lists : ['b', 'd']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

