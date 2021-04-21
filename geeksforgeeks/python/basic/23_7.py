Python | Print list after removing element at given index



Given an index, remove the element at that index from the list and print the
new list.  
![](https://media.geeksforgeeks.org/wp-content/uploads/WhatsApp-
Image-2017-12-24-at-12.09.55-AM.jpeg)  
Examples:

    
    
    Input : list = [10, 20, 30, 40, 50] 
            index = 2
    Output : [10, 20, 40, 50] 
    
    Input : list = [10, 20, 40, 50] 
            index = 0 
    Output : [20, 40, 50] 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method 1: Traversal of list**

Using traversal in the list, append all the index values except the given
index to a new list and then print the new list. For this we will require a
new list where we can append all the values except the given index value.

Below is the Python3 implementation of the above approach

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to remove the index

# element from the list 

# using traversal 

 

def remove(list1, pos):

 newlist = []

 

 # traverse in the list

 for x in range(len(list1)):

 

 # if index not equal to pos

 if x != pos:

 newlist.append(list1[x]) 

 print(*newlist) 

 

# driver code

list1 = [10, 20, 30, 40, 50]

pos = 2

remove(list1, pos)  
  
---  
  
 __

 __

 **Output:**

    
    
    10 20 40 50
    

**Method 2: pop()**

pop() function helps us to pop the value at any desired position that is
passed in the parameter, if nothing is passed in the parameter, then it
removes the last index value.

Below is the Python3 implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to remove the index

# element from the list 

# using pop()

 

def remove(list1, pos):

 

 # pop the element at index = pos

 list1.pop(pos) 

 print(*list1)

 

 

# driver code

list1 = [10, 20, 30, 40, 50]

pos = 2

remove(list1, pos)  
  
---  
  
 __

 __

 **Output:**

    
    
    10 20 40 50
    

**Method 3: del function**

del function can be used to remove any element at any given position. If -1 or
-2 is given in the [] brackets, then it deletes the last and second last
element respectively.

Below is the Python3 implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to remove the index element

# from the list using del

 

def remove(list1, pos):

 

 # delete the element at index = pos

 del list1[pos] 

 print(*list1)

 

 

# driver code

list1 = [10, 20, 30, 40, 50]

pos = 2

remove(list1, pos)  
  
---  
  
 __

 __

 **Output:**

    
    
    10 20 40 50
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

