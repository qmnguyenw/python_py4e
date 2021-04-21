Python | Split tuple into groups of n



Given a tuple, the task is to divide it into smaller groups of n. Let’s
discuss a few methods to accomplish a given task.

 **Method #1: Using enumerate and range function**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# how to split tuple

# into the group of k-tuples

 

# initialising tuple

ini_tuple = (1, 2, 3, 4, 8, 12, 3, 34,

 67, 45, 1, 1, 43, 65, 9, 10)

 

# printing initial tuple

print ("initial list", str(ini_tuple))

 

# code to group

# tuple into size 4 tuples

res = tuple(ini_tuple[x:x + 4] 

 for x in range(0, len(ini_tuple), 4))

 

# printing result

print ("resultant tuples", str(res))  
  
---  
  
 __

 __

 **Output:**

> initial list (1, 2, 3, 4, 8, 12, 3, 34, 67, 45, 1, 1, 43, 65, 9, 10)  
> resultant tuples ((1, 2, 3, 4), (8, 12, 3, 34), (67, 45, 1, 1), (43, 65, 9,
> 10))

  
**Method #2: Using enumerate and _mod_ operator**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# how to split tuple

# into the group of k-tuples

 

# initialising tuple

ini_tuple = (1, 2, 3, 4, 8, 12, 3, 34,

 67, 45, 1, 1, 43, 65, 9, 10)

 

# printing initial tuple

print ("initial list", str(ini_tuple))

 

# code to group

# tuple into size 4 tuples

res = tuple(ini_tuple[n:n + 4] for n, i in
enumerate(ini_tuple)

 if n % 4 == 0)

 

# printing result

print ("resultant tuples", str(res))  
  
---  
  
 __

 __

 **Output:**

> initial list (1, 2, 3, 4, 8, 12, 3, 34, 67, 45, 1, 1, 43, 65, 9, 10)  
> resultant tuples ((1, 2, 3, 4), (8, 12, 3, 34), (67, 45, 1, 1), (43, 65, 9,
> 10))

  
**Method #3: Using itertools receipes**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# how to split tuple

# into the group of k-tuples

 

# function to group tuple into groups of 4

def grouper(n, iterable):

 args = [iter(iterable)] * n

 return zip(*args)

 

 

# initialising tuple

ini_tuple = (1, 2, 3, 4, 8, 12, 3, 34,

 67, 45, 1, 1, 43, 65, 9, 10)

 

# printing initial tuple

print ("initial list", str(ini_tuple))

 

# code to group

# tuple into size 4 tuples

res = tuple(grouper(4, ini_tuple))

 

# printing result

print ("resultant tuples", str(res))  
  
---  
  
 __

 __

 **Output:**

> initial list (1, 2, 3, 4, 8, 12, 3, 34, 67, 45, 1, 1, 43, 65, 9, 10)  
> resultant tuples ((1, 2, 3, 4), (8, 12, 3, 34), (67, 45, 1, 1), (43, 65, 9,
> 10))

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

