Python list copy() method



Sometimes, there is a need to reuse any object, hence copy methods are always
of a great utility. Python in its language offers a number of ways to achieve
this. This particular article aims at demonstrating the copy method present in
the list. Since the list is widely used hence, its copy is also necessary.  

> Syntax : **list.copy()**  
>  **Parameters :**  
>  None  
>  **Returns :**  
>  Returns a shallow copy of a list.  
> Shallow copy means the any modification in new list won’t be reflected to
> original list  
>

**Code #1 :** Demonstrating the working of list.copy()  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# working of list.copy()

 

# Initializing list 

lis1 = [ 1, 2, 3, 4 ]

 

# Using copy() to create a shallow copy

lis2 = lis1.copy()

 

# Printing new list 

print ("The new list created is : " + str(lis2))

 

# Adding new element to new list

lis2.append(5)

 

# Printing lists after adding new element

# No change in old list

print ("The new list after adding new element : " + str(lis2))

print ("The old list after adding new element to new list : " +
str(lis1))  
  
---  
  
 __

 __

 **Output:**  

    
    
    The new list created is : [1, 2, 3, 4]
    The new list after adding new element : [1, 2, 3, 4, 5]
    The old list after adding new element to new list  : [1, 2, 3, 4]
    

**Deep Copy vs Shallow copy** **: An Analysis**  
A shallow copy means if we modify any of the nested list elements, changes are
reflected in both the list as they point to the same reference. Whereas in
deep copy, when we add an element in any of the lists, only that list is
modified. When we use “=” operator the new list refers to the same object,
hence any change (append, remove, change of value) in one list is reflected on
both. But when we use list.copy() method, changes made to one list or not
reflected on other except for in nested elements (like list within list), Here
we should use copy.deepcopy() from the copy module to avoid this problem.  
 **Techniques to deep copy :**  

  

  

  * Using copy.deepcopy()

 **Techniques to shallow copy :**  

  * Using copy.copy()
  * Using list.copy()
  * Using slicing

 **Code #2:** Demonstrating techniques of shallow and deep copy  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# techniques of deep and shallow copy

import copy

 

# Initializing list 

list1 = [ 1, [2, 3] , 4 ]

 

# all changes are reflected

list2 = list1 

 

# shallow copy - changes to nested list is reflected,

# same as copy.copy(), slicing

 

list3 = list1.copy() 

 

# deep copy - no change is reflected

list4 = copy.deepcopy(list1) 

 

list1.append(5)

list1[1][1] = 999

 

print("list 1 after modification:\n", list1)

print("list 2 after modification:\n", list2)

print("list 3 after modification:\n", list3)

print("list 4 after modification:\n", list4)  
  
---  
  
 __

 __

Output:  

    
    
    list 1 after modification:
     [1, [2, 999], 4, 5]
    list 2 after modification:
     [1, [2, 999], 4, 5]
    list 3 after modification:
     [1, [2, 999], 4]
    list 4 after modification:
     [1, [2, 3], 4]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

