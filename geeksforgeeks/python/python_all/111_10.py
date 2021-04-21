Python – Remove rear element from list



Stack data structure is very well known data structure, lists in Python
usually appends the elements to the end of the list. For implementing a stack
data structure, it is essential to be able to remove the end element from a
list. Let’s discuss the ways to achieve this so that stack data structure can
be implemented easily using lists.

 **Method #1 : Usingpop(-1)**  
This method pops, i.e removes and prints the i’th element from the list. This
method is mostly used among the other available options to perform this task.
This changes the original list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Remove rear element

# using pop(-1)

 

# initializing list 

test_list = [1, 4, 3, 6, 7]

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# using pop(-1) to

# Remove rear element

test_list.pop(-1)

 

# Printing modified list 

print ("Modified list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list is : [1, 4, 3, 6, 7]
    Modified list is : [1, 4, 3, 6]
    

**Method #2 : Using del list[-1]**  
This is just the alternate method to perform the rear deletion, this method
also performs the removal of list element in place and decreases the size of
list by 1.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Remove rear element

# using del list[-1]

 

# initializing list 

test_list = [1, 4, 3, 6, 7]

 

# Printing original list

print ("Original list is : " + str(test_list))

 

# using del list[-1] to

# Remove rear element

del test_list[-1]

 

# Printing modified list 

print ("Modified list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list is : [1, 4, 3, 6, 7]
    Modified list is : [1, 4, 3, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

