Python | Get elements till particular element in list



Sometimes, while working with Python list, we can have a requirement in which
we need to remove all the elements after a particular element, or, get all
elements before a particular element. These both are similar problems and
having a solution to it is always helpful. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Usingindex() \+ list slicing**  
This problem can be solved using the combination of these functions. The
index() can be used to find the index of desired element and list slicing
can perform the remaining task of getting the elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get elements till particular element in list

# using index() + list slicing

 

# initialize list

test_list = [1, 4, 6, 8, 9, 10, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# declaring elements till which elements required

N = 8

 

# Get elements till particular element in list

# using index() + list slicing

temp = test_list.index(N)

res = test_list[:temp]

 

# printing result

print("Elements till N in list are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 6, 8, 9, 10, 7]
    Elements till N in list are : [1, 4, 6]
    

**Method #2 : Using generator**  
This task can also be performed using the generator function which uses
yield to get the elements just till the required element and breaks the
yields after that element.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get elements till particular element in list

# using generator

 

# helper function to perform task

def print_ele(test_list, val):

 for ele in test_list:

 if ele == val:

 return

 yield ele

 

# initialize list

test_list = [1, 4, 6, 8, 9, 10, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# declaring elements till which elements required

N = 8

 

# Get elements till particular element in list

# using generator

res = list(print_ele(test_list, N))

 

# printing result

print("Elements till N in list are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 6, 8, 9, 10, 7]
    Elements till N in list are : [1, 4, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

