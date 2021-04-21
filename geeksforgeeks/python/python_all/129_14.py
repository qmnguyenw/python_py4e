Python | Iterating two lists at once



Sometimes, while working with Python list, we can have a problem in which we
have to iterate over two list elements. Iterating one after another is an
option, but it’s more cumbersome and a one-two liner is always recommended
over that. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop + “+” operator**  
The combination of above functionalities can make our task easier. But the
drawback here is that we might have to concatenate the list and hence would
consume more memory than desired.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Iterating two lists at once

# using loop + "+" operator

 

# initializing lists

test_list1 = [4, 5, 3, 6, 2]

test_list2 = [7, 9, 10, 0]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Iterating two lists at once

# using loop + "+" operator

# printing result 

print("The paired list contents are : ")

for ele in test_list1 + test_list2:

 print(ele, end =" ")  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [4, 5, 3, 6, 2]
    The original list 2 is : [7, 9, 10, 0]
    The paired list contents are : 
    4 5 3 6 2 7 9 10 0 
    

**Method #2 : Usingchain()**  
This is the method similar to above one, but it’s slightly more memory
efficient as the chain() is used to perform the task and creates an iterator
internally.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Iterating two lists at once

# using chain()

from itertools import chain

 

# initializing lists

test_list1 = [4, 5, 3, 6, 2]

test_list2 = [7, 9, 10, 0]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Iterating two lists at once

# using chain()

# printing result 

print("The paired list contents are : ")

for ele in chain(test_list1, test_list2):

 print(ele, end =" ")  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [4, 5, 3, 6, 2]
    The original list 2 is : [7, 9, 10, 0]
    The paired list contents are : 
    4 5 3 6 2 7 9 10 0 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

