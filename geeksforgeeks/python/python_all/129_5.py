Python | Indices of N largest elements in list



Sometimes, while working with Python lists, we can have a problem in which we
wish to find N largest elements. This task can occur in many domains such as
web development and while working with Databases. We might sometimes, require
to just find the indices of them. Let’s discuss certain way to find indices of
N largest elements in list.

 **Method : Usingsorted() \+ lambda + list slicing**  
This task can be performed using the combination of above functions. In this
the sorted(), can be used to get the container in way which requires to get
N largest elements at rear end and then the indices can be computed using list
slicing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Indices of N largest elements in list

# using sorted() + lambda + list slicing

 

# initialize list

test_list = [5, 6, 10, 4, 7, 1, 19]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize N 

N = 4

 

# Indices of N largest elements in list

# using sorted() + lambda + list slicing

res = sorted(range(len(test_list)), key = lambda sub:
test_list[sub])[-N:]

 

# printing result

print("Indices list of max N elements is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 10, 4, 7, 1, 19]
    Indices list of max N elements is : [1, 4, 2, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

