Python list | reverse()



reverse() is an inbuilt method in Python programming language that reverses
objects of list in place.

 **Syntax:**

    
    
    list_name.reverse()
    

**Parameters:**

    
    
    There are no parameters

 **Returns:**

    
    
    The reverse() method does not return any value but 
    reverse the given object from the list.

 **Code#1:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate the

# use of reverse method 

 

# a list of numbers

list1 = [1, 2, 3, 4, 1, 2, 6] 

list1.reverse() 

print(list1) 

 

# a list of characters

list2 = ['a', 'b', 'c', 'd', 'a', 'a'] 

list2.reverse() 

print(list2)   
  
---  
  
__

__

**Output:**

    
    
    [6, 2, 1, 4, 3, 2, 1]
    ['a', 'a', 'd', 'c', 'b', 'a']
    

**Error:**

    
    
    When anything other than list is used in place of list, 
    then it returns an AttributeError

