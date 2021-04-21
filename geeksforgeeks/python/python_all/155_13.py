Python | Check if a given object is list or not



Given an object, the task is to check whether the object is list or not.

 **Method #1: Using _isinstance_**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# check whether the object 

# is a list or not

 

# initialisation list

ini_list1 = [1, 2, 3, 4, 5]

ini_list2 = '12345'

 

# code to check whether

# object is a list or not

if isinstance(ini_list1, list):

 print("your object is a list !")

else:

 print("your object is not a list")

 

if isinstance(ini_list2, list):

 print("your object is a list")

else:

 print("your object is not a list")  
  
---  
  
 __

 __

 **Output:**

    
    
    your object is a list !
    your object is not a list
    

  
**Method #2: Usingtype(x)**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# check whether object 

# is a list or not

 

# initialisation list

ini_list1 = [1, 2, 3, 4, 5]

ini_list2 = (12, 22, 33)

 

# code to check whether

# object is a list or not

if type(ini_list1) is list:

 print("your object is a list")

else:

 print("your object is not a list")

 

if type(ini_list2) is list:

 print("your object is a list")

else:

 print("your object is not a list")  
  
---  
  
 __

 __

 **Output:**

    
    
    your object is a list
    your object is not a list
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

