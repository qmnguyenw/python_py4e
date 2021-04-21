Python | Check for None Tuple



Sometimes, while working with Python records, we can have a problem in which
we need to filter out all the tuples which contains just None values. This can
have possible application in Data Science domain. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Usingall() \+ generator expression**  
The combination of above functionalities can be used to perform this
particular task. In this we feed the logic of finding None using generator
expression and checking for each element is handled by all().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for None Tuple

# using all() + generator expression

 

# initialize tuple

test_tup = (None, None, None, None, None)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Check for None Tuple

# using all() + generator expression

res = all(ele is None for ele in test_tup)

 

# printing result

print("Does tuple contain all None elements ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (None, None, None, None, None)
    Does tuple contain all None elements ? : True
    

**Method #2 : Usinglen() + count()**  
The combination of above functions can be used to perform this task. In this,
we just count the occurrences of None and equate to list length to check if
all elements are None.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check for None Tuple

# using len() + count()

 

# initialize tuple

test_tup = (None, None, None, None, None)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Check for None Tuple

# using len() + count()

res = len(test_tup) == test_tup.count(None)

 

# printing result

print("Does tuple contain all None elements ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (None, None, None, None, None)
    Does tuple contain all None elements ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

