Python | Convert list to indexed tuple list



Sometimes, while working with Python lists, we can have a problem in which we
need to convert a list to tuple. This kind of problem have been dealt with
before. But sometimes, we have it’s variation in which we need to assign the
index of element along with element as a tuple. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Usinglist() + enumerate()**  
Combination of above functions can be used to perform this particular task. In
this, we just pass the enumerated list to list(), which returns the tuple with
first element as index and second as list element at that index.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert list to indexed tuple

# Using list() + enumerate()

 

# initializing list

test_list = [4, 5, 8, 9, 10]

 

# printing list

print("The original list : " + str(test_list))

 

# Convert list to indexed tuple

# Using list() + enumerate()

res = list(enumerate(test_list))

 

# Printing result

print("List after conversion to tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [4, 5, 8, 9, 10]
    List after conversion to tuple list : [(0, 4), (1, 5), (2, 8), (3, 9), (4, 10)]
    

**Method #2 : Usingzip() + range()**  
The combination of above functions can also be used to perform this particular
task. In this, we just use the ability of zip() to convert to tuple and
range() to get element index till length. This pairs index to value in form
of tuple list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert list to indexed tuple

# Using zip() + range()

 

# initializing list

test_list = [4, 5, 8, 9, 10]

 

# printing list

print("The original list : " + str(test_list))

 

# Convert list to indexed tuple

# Using zip() + range()

res = list(zip(range(len(test_list)), test_list))

 

# Printing result

print("List after conversion to tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [4, 5, 8, 9, 10]
    List after conversion to tuple list : [(0, 4), (1, 5), (2, 8), (3, 9), (4, 10)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

