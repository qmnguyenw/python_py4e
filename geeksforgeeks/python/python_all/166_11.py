Python | Slicing list from Kth element to last element



Python list slicing slices the list from start index till _end – 1_ ,
specified as list elements. So its tricky when we require to also slice the
last element of list. Trying to slice till list _size + 1_ gives an error.
Let’s discuss ways in which last element can be included during a list slice.  

 **Method #1 : Using None**  
During list slicing, giving the desired first index K and specifying ‘None’ as
the second argument in slicing works internally as slicing all the elements
from K in list till end including it.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# list slicing from K to end

# using None

 

# initializing list

test_list = [5, 6, 2, 3, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# index to begin slicing

K = 2

 

# using None 

# to perform list slicing from K to end

res = test_list[K : None]

 

# printing result 

print ("The sliced list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [5, 6, 2, 3, 9]
    The sliced list is : [2, 3, 9]
    

**Method #2 : Leaving the last element empty**  
Usually, not specifying any element as end element of slicing instructs python
to include whole list after K in list. But the main drawback in using this is
code readability. Hence above method is preferred more than this.  

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# list slicing from K to end

# without specifying last element 

 

# initializing list

test_list = [5, 6, 2, 3, 9]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# index to begin slicing

K = 2

 

# without specifying last element 

# to perform list slicing from K to end

res = test_list[K :]

 

# printing result 

print ("The sliced list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [5, 6, 2, 3, 9]
    The sliced list is : [2, 3, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

