Python | Boolean List AND and OR operations



Sometimes, while working with Python list, we can have a problem in which we
have a Boolean list and we need to find Boolean AND or OR of all elements in
it. This kind of problem has application in Data Science domain. Let’s discuss
an easy way to solve both these tasks.

 **Method #1 : AND operation – Usingall()**  
The solution to this problem is quite straight forward, but application
awareness is required. The all() performs the Boolean AND of the list and
returns the result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Boolean List AND and OR operations

# AND Operation - Using all()

 

# initialize list

test_list = [True, True, False, True, False]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Boolean List AND and OR operations

# AND Operation - Using all()

res = all(test_list)

 

# printing result

print("Result after performing AND among elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [True, True, False, True, False]
    Result after performing AND among elements : False
    

**Method #2 : OR operation – Usingany()**  
This task can be performed using any(). This checks for any True element in
list and returns True in that case else returns a False.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Boolean List AND and OR operations

# OR operation - Using any()

 

# initialize list

test_list = [True, True, False, True, False]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Boolean List AND and OR operations

# OR operation - Using any()

res = any(test_list)

 

# printing result

print("Result after performing OR among elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [True, True, False, True, False]
    Result after performing OR among elements : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

