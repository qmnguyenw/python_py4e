Python | Check if tuple and list are identical



Sometimes while working with different data in Python, we can have a problem
of having data in different containers. In this situations, there can be need
to test if data is identical cross containers. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Using loop**  
This is the brute force method to perform this particular task. In this, we
just iterate for list and tuple to test if at each index the elements are
similar.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if tuple and list are identical

# Using loop

 

# Initializing list and tuple

test_list = ['gfg', 'is', 'best']

test_tup = ('gfg', 'is', 'best')

 

# printing original list and tuple 

print("The original list is : " + str(test_list))

print("The original tuple is : " + str(test_tup))

 

# Check if tuple and list are identical

# Using loop

res = True

for i in range(0, len(test_list)):

 if(test_list[i] != test_tup[i]):

 res = False

 break

 

# printing result

print("Are tuple and list identical ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best']
    The original tuple is : ('gfg', 'is', 'best')
    Are tuple and list identical ? : True
    

**Method #2 : Usingall() + zip()**  
This task can also be performed in a single line using combination of above
functions. In this, we just combine the container elements using zip(), and
use all() to test for equality of elements at corresponding index.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if tuple and list are identical

# Using all() + zip()

 

# Initializing list and tuple

test_list = ['gfg', 'is', 'best']

test_tup = ('gfg', 'is', 'best')

 

# printing original list and tuple 

print("The original list is : " + str(test_list))

print("The original tuple is : " + str(test_tup))

 

# Check if tuple and list are identical

# Using all() + zip()

res = all( [i == j for i, j in zip(test_list,
test_tup)] )

 

# printing result

print("Are tuple and list identical ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['gfg', 'is', 'best']
    The original tuple is : ('gfg', 'is', 'best')
    Are tuple and list identical ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

