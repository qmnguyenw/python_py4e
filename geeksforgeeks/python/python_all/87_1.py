Python – Difference of List keeping duplicates



The problem of finding difference between list, i.e removing elements that
occur in one list and not in other is discussed before. But the usage of sets
ignores duplicates and we sometimes, require to remove the exact elements that
occur in lists. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute way in which this task can be performed. In this, we extract the
elements in a form in which we remove elements each time and break the loop to
remove one element at a time.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Difference of List keeping duplicates

# using loop

 

# Initializing lists

test_list1 = [4, 5, 7, 4, 3]

test_list2 = [7, 3, 4]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Difference of List keeping duplicates

# using loop

for ele in test_list2:

 for sub in test_list1:

 if ele == sub:

 test_list1.remove(sub)

 break

 

# printing result 

print ("List after performing difference : " + str(test_list1))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [4, 5, 7, 4, 3]
    The original list 2 is : [7, 3, 4]
    List after performing difference : [5, 4]
    

**Method #2 : Usingpop() + list comprehension + index()**  
This task can also be performed using combination of above functionalities. In
this, we just iterate the list using list comprehension and remove element
using index() and pop().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Difference of List keeping duplicates

# using pop() + list comprehension + index()

 

# Initializing lists

test_list1 = [4, 5, 7, 4, 3]

test_list2 = [7, 3, 4]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Difference of List keeping duplicates

# using pop() + list comprehension + index()

[test_list1.pop(test_list1.index(idx)) for idx in test_list2]

 

# printing result 

print ("List after performing difference : " + str(test_list1))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [4, 5, 7, 4, 3]
    The original list 2 is : [7, 3, 4]
    List after performing difference : [5, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

