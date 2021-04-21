Python – Find the indices for k Smallest elements



Sometimes, while working with Python lists, we can have a problem in which we
wish to find the indices for K smallest elements. This task can occur in many
domains such as web development and while working with Databases. We might
sometimes, require to just find the indices of them. Let’s discuss a certain
way to find indices of K smallest elements in list.

 **Usingsorted() \+ lambda + list slicing**

This task can be performed using the combination of above functions. In this
the sorted(), can be used to get the container in a way which requires to
get K smallest elements at front end and then the indices can be computed
using list slicing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Smallest K elements indices

# using sorted() + lambda + list slicing

 

# initialize list

test_list = [5, 6, 10, 4, 7, 1, 19]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize K

K = 3

 

# Smallest K elements indices

# using sorted() + lambda + list slicing

res = sorted(range(len(test_list)), key = lambda sub:
test_list[sub])[:K]

 

# printing result

print("Indices list of min K elements is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 10, 4, 7, 1, 19]
    Indices list of min K elements is : [5, 3, 0]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

