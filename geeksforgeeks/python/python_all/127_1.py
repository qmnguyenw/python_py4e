Python | Filter list by Boolean list



Sometimes, while working with Python list, we can have a problem in which we
have to filter a list. This can sometimes, come with variations. One such
variation can be filtering by the use of Boolean list. Let’s discuss a way in
which this task can be done.

 **Method : Usingitertools.compress()**  
The most elegant and straightforward method to perform this particular task is
to use inbuilt functionality of compress() to filter out all the elements from
list which exists at Truth positions with respect to index of other list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter list by Boolean list

# Using itertools.compress

from itertools import compress

 

# initializing list

test_list = [6, 4, 8, 9, 10]

 

# printing list

print("The original list : " + str(test_list))

 

# initializing Boolean list

bool_list = [True, False, False, True, True]

 

# printing boolean list 

print("The bool list is : " + str(bool_list))

 

# Filter list by Boolean list

# Using itertools.compress

res = list(compress(test_list, bool_list))

 

# Printing result

print("List after filtering is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [6, 4, 8, 9, 10]
    The bool list is : [True, False, False, True, True]
    List after filtering is : [6, 9, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

