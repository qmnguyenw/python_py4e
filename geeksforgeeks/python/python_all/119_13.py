Python | Add dictionary to tuple



Sometimes, while working with data, we can have a problem in which we need to
append to a tuple a new record which is of form of Python dictionary. This
kind of application can come in web development domain in case of composite
attributes. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usinglist() + append + tuple()**  
This method can be used to solve this problem. In this, we just convert the
tuple into a list and then perform list append and then reconvert the list to
tuple using tuple().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add dictionary to tuple

# using append() + tuple() + list comprehension

 

# initialize tuple 

test_tup = (4, 5, 6)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# initialize dictionary 

test_dict = {"gfg" : 1, "is" : 2, "best" : 3}

 

# Add dictionary to tuple

# using append() + tuple() + list comprehension

test_tup = list(test_tup)

test_tup.append(test_dict)

test_tup = tuple(test_tup)

 

# printing result

print("Tuple after addition of dictionary : " + str(test_tup))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (4, 5, 6)
    Tuple after addition of dictionary : (4, 5, 6, {'best': 3, 'is': 2, 'gfg': 1})
    

**Method #2 : Using+ operator**  
This is another way to perform this task. In this, we add dictionary to
different tuple and then add the old tuple to this tuple and form new tuple.
Key difference is that this is not inplace addtion as upper method, but
creates new tuple out of old one.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add dictionary to tuple

# using + operator

 

# initialize tuple 

test_tup = (4, 5, 6)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# initialize dictionary 

test_dict = {"gfg" : 1, "is" : 2, "best" : 3}

 

# Add dictionary to tuple

# using + operator

res = test_tup + (test_dict, )

 

# printing result

print("Tuple after addition of dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (4, 5, 6)
    Tuple after addition of dictionary : (4, 5, 6, {'best': 3, 'is': 2, 'gfg': 1})
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

