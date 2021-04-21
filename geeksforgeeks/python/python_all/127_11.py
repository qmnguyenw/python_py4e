Python | Check if Non-None values are contiguous



Sometimes, while working with Python lists, we can have a problem in which we
need to find if all the values that are valid (Non None). This has a lot of
application in day-day programming. Let’s discuss a method in which this task
can be performed.

 **Method : Using iterator +all() + any()**  
Combination of above functions can be used to perform this particular task. In
this, we filter the leading None values using initial all(), then check for
singular valid value sublist using any() and then check for all the required
None values. If any of the above return false. The Non-None values are not
contiguous.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if Non-None values are contiguous

# Using iterator + all() + any()

 

# helper function 

def check_cont(test_list):

 test_list = iter(test_list)

 all(x is None for x in test_list) 

 any(x is None for x in test_list) 

 return all(x is None for x in test_list)

 

# initializing list 

test_list = [None, None, 'Gfg', 'is', 'Good',
None, None, None]

 

# printing list 

print("The original list : " + str(test_list))

 

# Check if Non-None values are contiguous

# Using iterator + all() + any()

res = check_cont(test_list)

 

# Printing result

print("Are non-none values contiguous ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [None, None, 'Gfg', 'is', 'Good', None, None, None]
    Are non-none values contiguous ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

