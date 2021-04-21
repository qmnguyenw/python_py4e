Python – Consecutive K elements join in List



Sometimes, while working with Python lists, we can have a problem in which we
need to join every K characters into one collection. This type of application
can have use case in many domains like day-day and competitive programming.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using List comprehension**  
This is one of the ways by which this task can be performed. In this, we
iterate through the list and join elements using list slicing and return the
aggregated list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive K elements join in List

# using List comprehension

 

# Initializing list

test_list = ['g', 'f', 'g', 'i', 's', 'b',
'e', 's', 't']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 3

 

# Consecutive K elements join in List

# using List comprehension

res = [ "".join(test_list[idx : idx + K]) for idx in
range(len(test_list) - K + 1) ]

 

# printing result 

print ("List after consecutive joining : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [‘g’, ‘f’, ‘g’, ‘i’, ‘s’, ‘b’, ‘e’, ‘s’, ‘t’]  
> List after consecutive joining : [‘gfg’, ‘fgi’, ‘gis’, ‘isb’, ‘sbe’, ‘bes’,
> ‘est’]

  

  

**Method #2 : Using loop**  
This is brute way to perform this task. This is similar to above method, just
the string is iterated using a loop and making task more longer and tedious.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Consecutive K elements join in List

# using loop

 

# Initializing list

test_list = ['g', 'f', 'g', 'i', 's', 'b',
'e', 's', 't']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing K 

K = 3

 

# Consecutive K elements join in List

# using loop

res = []

for idx in range(0, len(test_list) - K + 1):

 res.append("".join(test_list[idx : idx + K]))

 

# printing result 

print ("List after consecutive joining : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [‘g’, ‘f’, ‘g’, ‘i’, ‘s’, ‘b’, ‘e’, ‘s’, ‘t’]  
> List after consecutive joining : [‘gfg’, ‘fgi’, ‘gis’, ‘isb’, ‘sbe’, ‘bes’,
> ‘est’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

