Python | Shift last element to first position in list



The cyclic rotations have been discussed in the earlier articles. But
sometimes, we just require a specific task, a part of rotation i.e shift last
element to first element in list. This has the application in day-day
programming in certain utilities. Let’s discuss certain ways in which this can
be achieved.

 **Method #1 : Using list slicing and “+” operator**  
The combination of these functions can be used to perform the task of a single
shift in list. The last element is added to the rest of the list to achieve
this task using slicing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# shift last element to first 

# using list slicing and "+" operator

 

# initializing list 

test_list = [1, 4, 5, 6, 7, 8, 9, 12]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using list slicing and "+" operator

# shift last element to first

test_list = test_list[-1:] + test_list[:-1] 

 

# printing result

print ("The list after shift is : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 4, 5, 6, 7, 8, 9, 12]
    The list after shift is : [12, 1, 4, 5, 6, 7, 8, 9]
    

**Method #2 : Usinginsert() + pop()**  
This functionality can also be achieved using the inbuilt functions of python
viz. insert() and pop(). The pop function returns the last element and that
is inserted at front using the insert function.  

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# shift last element to first 

# using insert() + pop()

 

# initializing list 

test_list = [1, 4, 5, 6, 7, 8, 9, 12]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using insert() + pop()

# shift last element to first

test_list.insert(0, test_list.pop())

 

# printing result

print ("The list after shift is : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 4, 5, 6, 7, 8, 9, 12]
    The list after shift is : [12, 1, 4, 5, 6, 7, 8, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

