Python | Cartesian product of string elements



Sometimes, while working with Python strings, we can have problem that we have
data in string which is comma or any delim separated. We might want to perform
cartesian product with other similar strings to get all possible pairs of
data. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension + split()**  
This task can be performed using list comprehension. In this, we perform the
task of extracting individual elements using split(). The task of list
comprehension is to form pairs.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cartesian product of string elements

# Using split() + list comprehension

 

# initializing strings

test_str1 = "gfg, is, best"

test_str2 = "for, all, geeks"

 

# printing original strings

print("The original string 1 is : " + test_str1)

print("The original string 2 is : " + test_str2)

 

# Cartesian product of string elements

# Using split() + list comprehension

res = [sub1 + sub2 for sub1 in test_str1.split(", ")
for sub2 in test_str2.split(", ")]

 

# printing result 

print("Cartesian product list : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string 1 is : gfg, is, best
    The original string 2 is : for, all, geeks
    Cartesian product list : ['gfgfor', 'gfgall', 'gfggeeks', 'isfor', 'isall', 'isgeeks', 'bestfor', 'bestall', 'bestgeeks']
    

**Method #2 : Using List comprehension +product()**  
The combination of above functions can be used to perform this task. In this,
we employ product() in place of nested comprehension to perform the task of
pairing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cartesian product of string elements

# Using product() + list comprehension

from itertools import product

 

# initializing strings

test_str1 = "gfg, is, best"

test_str2 = "for, all, geeks"

 

# printing original strings

print("The original string 1 is : " + test_str1)

print("The original string 2 is : " + test_str2)

 

# Cartesian product of string elements

# Using product() + list comprehension

res = [sub1 + sub2 for sub1, sub2 in
product(test_str1.split(", "), test_str2.split(", "))]

 

# printing result 

print("Cartesian product list : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string 1 is : gfg, is, best
    The original string 2 is : for, all, geeks
    Cartesian product list : ['gfgfor', 'gfgall', 'gfggeeks', 'isfor', 'isall', 'isgeeks', 'bestfor', 'bestall', 'bestgeeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

