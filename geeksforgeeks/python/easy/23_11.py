Python list | insert()



 ** _insert()_** is an inbuilt function in Python that inserts a given element
at a given index in a list.

 **Syntax :**

    
    
    list_name.insert(index, element)

 **Parameters :**

    
    
     **index -** the index at which the element has to be inserted.
    **element -** the element to be inserted in the list.

 **Returns :**

    
    
    This method does not return any value but
    it inserts the given element at the given index.

 **Error :**

  

  

    
    
    If anything other then a list is used with 
    insert(), then it returns an AttributeError.

 **Note :** If given index >= length(list) is given, then it inserts at the
end of the list.

 **Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for use

# of insert() method 

 

list1 = [ 1, 2, 3, 4, 5, 6, 7 ] 

 

# insert 10 at 4th index 

list1.insert(4, 10) 

print(list1) 

 

list2 = ['a', 'b', 'c', 'd', 'e'] 

 

# insert z at the front of the list

list2.insert(0, 'z')

print(list2)   
  
---  
  
__

__

Output :

    
    
    [1, 2, 3, 4, 10, 5, 6, 7]
    ['z', 'a', 'b', 'c', 'd', 'e']
    

  
**Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for error

# of insert() method 

 

# attribute error 

string = "1234567"

 

string.insert(10, 1)

print(string)   
  
---  
  
__

__

**Output :**

    
    
    Traceback (most recent call last):
      File "/home/2fe54bd8723cd0ae89a17325da8b2eb5.py", line 7, in 
        string.insert(10, 1)
    AttributeError: 'str' object has no attribute 'insert'
    

**Practical Application :**  
Insertion in a list before any element :

 **Code #3 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for Insertion in a list

# before any element using insert() method 

 

list1 = [ 1, 2, 3, 4, 5, 6 ]

 

# Element to be inserted 

element = 13

 

# Element to be inserted before 3

beforeElement = 3

 

# Find index

index = list1.index(beforeElement) 

 

# Insert element at beforeElement 

list1.insert(index, element) 

print(list1)  
  
---  
  
 __

 __

 **Output :**

    
    
    [1, 2, 13, 3, 4, 5, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

