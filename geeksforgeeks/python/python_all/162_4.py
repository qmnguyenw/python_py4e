Python | Front and rear range deletion in a list



Sometimes, we require to shrink a list by deletion of its certain elements.
One of the methods that is employed to perform this particular task is front
and rear element deletion. It is a good utility whose solution can be useful
to have. Let’s discuss certain ways in which this can be performed.  

 **Method #1 : Using list slicing +del operator**  
The del operator can be clubbed with the slicing action to delete the front
and rear elements from a list to obtain a cropped version of list.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# front and rear deletion 

# using del operator + list slicing

 

# initializing list 

test_list = [2, 3, 5, 7, 9, 10, 8, 6]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using del operator + list slicing

# front and rear deletion 

del test_list[-2:], test_list[:2]

 

# printing result 

print ("The cropped list is : " + str(test_list))  
  
---  
  
 __

 __

Output :

    
    
    The original list is : [2, 3, 5, 7, 9, 10, 8, 6]
    The cropped list is : [5, 7, 9, 10]
    

**Method #2 : Using list slicing**  
Above method can be modified and the use of del operator can be omitted to
achieve this particular task. We can slice a list in a way that specific
number of elements are removed from the list.  

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# front and rear deletion 

# using list slicing

 

# initializing list 

test_list = [2, 3, 5, 7, 9, 10, 8, 6]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using list slicing

# front and rear deletion 

res = test_list[2 : -2]

 

# printing result 

print ("The cropped list is : " + str(res))  
  
---  
  
 __

 __

Output :

    
    
    The original list is : [2, 3, 5, 7, 9, 10, 8, 6]
    The cropped list is : [5, 7, 9, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

