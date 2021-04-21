Python program to swap two elements in a list



Given a list in Python and provided the positions of the elements, write a
program to swap the two elements in the list.

 **Examples:**

    
    
    **Input :** List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
    **Output :** [19, 65, 23, 90]
    
    **Input :** List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
    **Output :** [1, 5, 3, 4, 2]
    

**Approach #1:** Simple swap

Since the positions of the elements are known, we can simply swap the
positions of the elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to swap elements

# at given positions

 

# Swap function

def swapPositions(list, pos1, pos2):

 

 list[pos1], list[pos2] = list[pos2], list[pos1]

 return list

 

# Driver function

List = [23, 65, 19, 90]

pos1, pos2 = 1, 3

 

print(swapPositions(List, pos1-1, pos2-1))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [19, 65, 23, 90]

  
**Approach #2 :** Using Inbuilt list.pop() function

Pop the element at _pos1_ and store it in a variable. Similarly, pop the
element at _pos2_ and store it in another variable. Now insert the two popped
element at each other’s original position.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to swap elements

# at given positions

 

# Swap function

def swapPositions(list, pos1, pos2):

 

 # popping both the elements from list

 first_ele = list.pop(pos1) 

 second_ele = list.pop(pos2-1)

 

 # inserting in each others positions

 list.insert(pos1, second_ele) 

 list.insert(pos2, first_ele) 

 

 return list

 

# Driver function

List = [23, 65, 19, 90]

pos1, pos2 = 1, 3

 

print(swapPositions(List, pos1-1, pos2-1))  
  
---  
  
 __

 __

 **Output:**

    
    
    [19, 65, 23, 90]

  
**Approach #3 :** Using tuple variable

Store the element at _pos1_ and _pos2_ as a pair in a tuple variable, say
_get_. Unpack those elements with _pos2_ and _pos1_ positions in that list.
Now, both the positions in that list are swapped.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to swap elements at

# given positions

 

# Swap function

def swapPositions(list, pos1, pos2):

 

 # Storing the two elements

 # as a pair in a tuple variable get

 get = list[pos1], list[pos2]

 

 # unpacking those elements

 list[pos2], list[pos1] = get

 

 return list

 

# Driver Code

List = [23, 65, 19, 90]

 

pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))  
  
---  
  
 __

 __

 **Output:**

    
    
    [19, 65, 23, 90]

 **Approach #4 :** Using comma assignment

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to swap elements

# at given positions

 

def swapPositions(list, pos1, pos2):

 list[pos1],list[pos2] = list[pos2],list[pos1]

 return list

 

# Driver Code

List = [23, 65, 19, 90]

pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))  
  
---  
  
 __

 __

 **Output:**

    
    
    [19, 65, 23, 90]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

