Python | Convert list to Python array



Sometimes while working in Python we can have a problem in which we need to
restrict the data elements to be just of one type. List, can be heterogeneous,
can have data of multiple data types and it is sometimes undesirable. There a
need to convert this to data structure which restricts the type of data. The
Python language comes with array data structure which can be used for this
purpose. Let’s discuss a way to convert list to array.

 **Method : Usingarray() \+ data type indicator**  
This task can be easily performed using array(). This is an inbuilt function
in Python to convert to array. The data type indicator “i” is used in case of
integers, which restricts data type.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert list to Python array

# Using array() + data type indicator

from array import array

 

# initializing list

test_list = [6, 4, 8, 9, 10]

 

# printing list

print("The original list : " + str(test_list))

 

# Convert list to Python array

# Using array() + data type indicator

res = array("i", test_list)

 

# Printing result

print("List after conversion to array : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [6, 4, 8, 9, 10]
    List after conversion to array : array('i', [6, 4, 8, 9, 10])
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

