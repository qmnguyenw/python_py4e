Python | Move one list element to another list



Sometimes, while working with Python list, there can be a problem in which we
need to perform the inter list shifts of elements. Having solution to this
problem is always very useful. Let’s discuss certain way in which this task
can be performed.

 **Method : Usingpop() + insert() + index()**  
This particular task can be performed using combination of above functions. In
this we just use the property of pop function to return and remove element
and insert it to the specific position of other list using index function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Move one list element to another list

# Using pop() + index() + insert()

 

# initializing lists

test_list1 = [4, 5, 6, 7, 3, 8]

test_list2 = [7, 6, 3, 8, 10, 12]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Using pop() + index() + insert()

# Move one list element to another list

res = test_list1.insert(4, test_list2.pop(test_list2.index(10)))

 

# Printing result

print("The list 1 after insert is : " + str(test_list1))

print("The list 2 after remove is : " + str(test_list2))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [4, 5, 6, 7, 3, 8]
    The original list 2 is : [7, 6, 3, 8, 10, 12]
    The list 1 after insert is : [4, 5, 6, 7, 10, 3, 8]
    The list 2 after remove is : [7, 6, 3, 8, 12]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

