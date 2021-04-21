Python | Shift from Front to Rear in List



The cyclic rotations have been discussed in the earlier articles. But
sometimes, we just require a specific task, a part of rotation i.e shift first
element to last element in list. This has the application in day-day
programming in certain utilities. Let’s discuss certain ways in which this can
be achieved.

 **Method #1 : Using list slicing and“+” operator**  
The combination of the these functions can be used to perform the task of
single shift in list. The first element is added to the rest of the list to
achieve this task using slicing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Shift from Front to Rear in List

# using list slicing and "+" operator

 

# initializing list 

test_list = [1, 4, 5, 6, 7, 8, 9, 12]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using list slicing and "+" operator

# Shift from Front to Rear in List

test_list = test_list[1 :] + test_list[: 1] 

 

# printing result

print ("The list after shift is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 6, 7, 8, 9, 12]
    The list after shift is : [4, 5, 6, 7, 8, 9, 12, 1]
    

**Method #2 : Usinginsert() + pop()**  
This functionality can also be achieved using the inbuilt functions of python
viz. insert() and pop(). The pop function removes the first element and that
is inserted at last using the insert function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Shift from Front to Rear in List

# using insert() + pop()

 

# initializing list 

test_list = [1, 4, 5, 6, 7, 8, 9, 12]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using insert() + pop()

# Shift from Front to Rear in List

test_list.insert(len(test_list) - 1, test_list.pop(0))

 

# printing result

print ("The list after shift is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 6, 7, 8, 9, 12]
    The list after shift is : [4, 5, 6, 7, 8, 9, 12, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

