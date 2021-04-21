Python | Initialize list with empty dictionaries



While working with Python, we can have a problem in which we need to
initialize a list of a particular size with empty dictionaries. This task has
it’s utility in web development to store records. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Using{} + "*" operator**  
This task can be performed using the “*” operator. We can create a list
containing single empty dictionary and then multiply it by Number that is size
of list. The drawback is that similar reference dictionaries will be made
which will point to similar memory location.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize list with empty dictionaries

# using {} + "*" operator

 

# Initialize list with empty dictionaries

# using {} + "*" operator

res = [{}] * 6

 

print("The list of empty dictionaries is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The list of empty dictionaries is : [{}, {}, {}, {}, {}, {}]
    

**Method #2 : Using{} \+ list comprehension**  
This is perhaps the better and correct way to perform this task. We initialize
the each index of list with dictionary, this way, we have independently
referring dictionaries and don’t point to single reference.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize list with empty dictionaries

# using {} + list comprehension

 

# Initialize list with empty dictionaries

# using {} + "*" operator

res = [{} for sub in range(6)]

 

print("The list of empty dictionaries is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The list of empty dictionaries is : [{}, {}, {}, {}, {}, {}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

