Python – Remove nested records from tuple



Sometimes, while working with records, we can have a problem in which an
element of a record is another tuple records and we might have to remove the
nested records. This is a problem which does not occur commonly, but having a
solution to it is useful. Let’s discuss certain way in which this task can be
performed.

 **Method : Using loop +isintance() + enumerate()**  
This problem can be solved using the above functionalities. In this, we just
loop through the elements using enumerate() to get the index count of it and
check the type using isinstance() and recreate the new tuple by checking
ignoring tuple records.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove nested records

# using isinstance() + enumerate() + loop

 

# initialize tuple

test_tup = (1, 5, 7, (4, 6), 10)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Remove nested records

# using isinstance() + enumerate() + loop

res = tuple()

for count, ele in enumerate(test_tup):

 if not isinstance(ele, tuple):

 res = res + (ele, )

 

# printing result

print("Elements after removal of nested records : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (1, 5, 7, (4, 6), 10)
    Elements after removal of nested records : (1, 5, 7, 10)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

