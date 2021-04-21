Python | Categorize tuple values into dictionary value list



Sometimes, while working with Python, we might face a problem in which we have
data in form of list of tuples, and what we intend is, to categorize them into
dictionary with a value list of tuples. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Usingsetdefault() \+ loop**  
This task can easily be performed using setdefault(). In this, we just take
key and value pair of tuple by iteration and setdafault() is used to assign
value to corresponding key of dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Categorize tuple values into dictionary value list

# Using setdefault() + loop

 

# Initialize list of tuples

test_list = [(1, 3), (1, 4), (2, 3), (3,
2), (5, 3), (6, 4)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using setdefault() + loop

# Categorize tuple values into dictionary value list

res = {}

for i, j in test_list:

 res.setdefault(j, []).append(i)

 

# printing result 

print("The dictionary converted from tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [(1, 3), (1, 4), (2, 3), (3, 2), (5, 3), (6, 4)]  
> The dictionary converted from tuple list : {2: [3], 3: [1, 2, 5], 4: [1, 6]}

  

  

**Method #2 : Usingdict() \+ list comprehension + frozenset()**  
The combination of above methods can be used to perform this particular task.
In this, the logical computations are done in comprehension with the help of
frozenset() and the container is converted to dictionary using dict().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Categorize tuple values into dictionary value list

# Using dict() + list comprehension + frozenset()

 

# Initialize list of tuples

test_list = [(1, 3), (1, 4), (2, 3), (3,
2), (5, 3), (6, 4)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using dict() + list comprehension + frozenset()

# Categorize tuple values into dictionary value list

res = dict((key, [i[0] for i in test_list if i[1]
== key])

 for key in frozenset(j[1] for j in test_list))

 

# printing result 

print("The dictionary converted from tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [(1, 3), (1, 4), (2, 3), (3, 2), (5, 3), (6, 4)]  
> The dictionary converted from tuple list : {2: [3], 3: [1, 2, 5], 4: [1, 6]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

