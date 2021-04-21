Python | Remove given element from the list



Given a list, write a Python program to remove the given element (list may
have duplicates) from given list. There are multiple ways we can do this task
in Python. Let’s see some of Pythonic ways to do this task.

 **Method #1:** Using pop() method [Remove given element found first.]

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove given element from the list

list1 = [1, 9, 8, 4, 9, 2, 9] 

 

# Printing initial list 

print ("original list : "+ str(list1)) 

 

remove = 9

 

# using pop() 

# to remove list element 9

if remove in list1: 

 list1.pop(list1.index(remove)) 

 

# Printing list after removal 

print ("List after element removal is : " + str(list1))   
  
---  
  
__

__

**Output:**

    
    
    original list : [1, 9, 8, 4, 9, 2, 9]
    List after element removal is : [1, 8, 4, 9, 2, 9]
    

  
**Method #2:** Using remove() method

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to remove given element from the list

list1 = [1, 9, 8, 4, 9, 2, 9] 

 

# Printing initial list 

print ("original list : "+ str(list1)) 

 

# using remove() to remove list element 9

list1.remove(9) 

 

 

# Printing list after removal 

print ("List after element removal is : " + str(list1))   
  
---  
  
__

__

**Output:**

  

  

    
    
    original list : [1, 9, 8, 4, 9, 2, 9]
    List after element removal is : [1, 8, 4, 9, 2, 9]
    

