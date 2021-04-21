Python – Adding Tuple to List and vice – versa



Sometimes, while working with Python containers, we can have a problem in
which we need to perform addition of one container with another. This kind of
problem can have occurrence in many data domains across Computer Science and
Programming. Let’s discuss certain ways in which this task can be performed.

 **Method 1 : Using += operator [list + tuple]**  
This operator can be used to join a list with a tuple. Internally its working
is similar to that of list.extend(), which can have any iterable as its
argument, tuple in this case.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Adding Tuple to List and vice - versa

# Using += operator (list + tuple)

 

# initializing list

test_list = [5, 6, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing tuple 

test_tup = (9, 10)

 

# Adding Tuple to List and vice - versa

# Using += operator (list + tuple)

test_list += test_tup

 

# printing result 

print("The container after addition : " + str(test_list))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [5, 6, 7]
    The container after addition : [5, 6, 7, 9, 10]
    

**Method #2 : Usingtuple(), data type conversion [tuple + list]**  
The following techinque is used to add list to a tuple. The tuple has to
converted to list and list has to be added, at last resultant is converted to
tuple.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Adding Tuple to List and vice - versa

# Using tuple(), data type conversion [tuple + list]

 

# initializing list

test_list = [5, 6, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing tuple 

test_tup = (9, 10)

 

# Adding Tuple to List and vice - versa

# Using tuple(), data type conversion [tuple + list]

res = tuple(list(test_tup) + test_list)

 

# printing result 

print("The container after addition : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [5, 6, 7]
    The container after addition : (9, 10, 5, 6, 7)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

