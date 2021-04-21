Python | Ways to rotate a list



The rotation of a list has been discussed earlier also, but this particular
article focuses on shorthands and various short techniques to achieve this in
one-liners or one word. This operation is quite essential in a programmers
life to achieve various tasks.

Let’s discuss different ways we can rotate a list.

 **Method #1 : Using Slicing**  
This particular method is the generic method and mostly employed to achieve
this task and also been discussed in many articles as well. It works by just
joining the later sliced part to the initial sliced part given the rotation
number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# rotation of list 

# using slice 

 

# initializing list

test_list = [1, 4, 6, 7, 2]

 

# printing original list 

print ("Original list : " + str(test_list))

 

# using slicing to left rotate by 3

test_list = test_list[3:] + test_list[:3]

 

# Printing list after left rotate

print ("List after left rotate by 3 : " + str(test_list))

 

# using slicing to right rotate by 3

# back to Original

test_list = test_list[-3:] + test_list[:-3]

 

# Printing after right rotate

print ("List after right rotate by 3(back to original) : "

 + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list : [1, 4, 6, 7, 2]
    List after left rotate by 3 : [7, 2, 1, 4, 6]
    List after right rotate by 3 ( back to original) : [1, 4, 6, 7, 2]
    

  
**Method #2 : Using list Comprehension**  
This problem can also be solved by naive method, but its shorter
implementation would be with the help of list comprehension. In this method,
we just reassign the index to each value to specific position after rotation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# rotation of list 

# using list comprehension

 

# initializing list

test_list = [1, 4, 6, 7, 2]

 

# printing original list 

print ("Original list : " + str(test_list))

 

# using list comprehension to left rotate by 3

test_list = [test_list[(i + 3) % len(test_list)]

 for i, x in enumerate(test_list)]

 

# Printing list after left rotate

print ("List after left rotate by 3 : " + str(test_list))

 

# using list comprehension to right rotate by 3

# back to Original

test_list = [test_list[(i - 3) % len(test_list)]

 for i, x in enumerate(test_list)]

 

# Printing after right rotate

print ("List after right rotate by 3(back to original) : "

 + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list : [1, 4, 6, 7, 2]
    List after left rotate by 3 : [7, 2, 1, 4, 6]
    List after right rotate by 3(back to original) : [1, 4, 6, 7, 2]
    

  
**Method #3 : Usingcollections.deque.rotate()**  
The collections module has deque class which provides the rotate(), which is
inbuilt function to allow rotation. This is lesser known function but has a
greater utility.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# rotation of list 

# using rotate()

from collections import deque

 

# initializing list

test_list = [1, 4, 6, 7, 2]

 

# printing original list 

print ("Original list : " + str(test_list))

 

# using rotate() to left rotate by 3

test_list = deque(test_list)

test_list.rotate(-3)

test_list = list(test_list)

 

# Printing list after left rotate

print ("List after left rotate by 3 : " + str(test_list))

 

# using rotate() to right rotate by 3

# back to Original

test_list = deque(test_list)

test_list.rotate(3)

test_list = list(test_list)

 

# Printing after right rotate

print ("List after right rotate by 3(back to original) : "

 + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list : [1, 4, 6, 7, 2]
    List after left rotate by 3 : [7, 2, 1, 4, 6]
    List after right rotate by 3(back to original) : [1, 4, 6, 7, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

