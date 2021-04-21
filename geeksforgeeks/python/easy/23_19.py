Python | a += b is not always a = a + b



In python a += b doesn’t always behave the same way as a = a + b, same
operands may give the different results under different conditions.  
  
 **Consider these examples for list manipulation:**  
 **Example 1**

 __

 __  
 __

 __

 __  
 __  
 __

list1= [5, 4, 3, 2, 1]

list2 = list1

list1 += [1, 2, 3, 4]

 

print(list1)

print(list2)  
  
---  
  
 __

 __

Output:

    
    
    [5, 4, 3, 2, 1, 1, 2, 3, 4]
    [5, 4, 3, 2, 1, 1, 2, 3, 4]
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190912115916/list12.png)

**Example 2**

 __

 __  
 __

 __

 __  
 __  
 __

list1= [5, 4, 3, 2, 1]

list2 = list1

list1 = list1 + [1, 2, 3, 4]

 

# Contents of list1 are same as above 

# program, but contents of list2 are

# different.

print(list1)

print(list2)  
  
---  
  
 __

 __

Output:

  

  

    
    
    [5, 4, 3, 2, 1, 1, 2, 3, 4]
    [5, 4, 3, 2, 1]
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190912120043/list22.png)

  * expression **list1 += [1, 2, 3, 4]** modifies the list in-place, means it extends the list such that “list1” and “list2” still have the reference to the same list.
  * expression **list1 = list1 + [1, 2, 3, 4]** creates a new list and changes “list1” reference to that new list and “list2” still refer to the old list.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

