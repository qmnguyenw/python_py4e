Python | Ways to remove numeric digits from given string



Given a string (may contain both characters and digits), write a Python
program to remove the numeric digits from string.

Let’s discuss the different ways we can achieve this task.

 **Method #1: Usingjoin and isdigit()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# how to remove numeric digits from string

# using join and isdigit

 

# initialising string

ini_string = "Geeks123for127geeks"

 

# printing initial ini_string

print("initial string : ", ini_string)

 

# using join and isdigit 

# to remove numeric digits from string

res = ''.join([i for i in ini_string if not i.isdigit()])

 

# printing result

print("final string : ", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string :  Geeks123for127geeks
    final string :  Geeksforgeeks
    

  
**Method #2: Using translate and digits**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# how to remove numeric digits from string

# using translate

from string import digits

 

# initialising string

ini_string = "Geeks123for127geeks"

 

# printing initial ini_string

print("initial string : ", ini_string)

 

# using translate and digits

# to remove numeric digits from string

remove_digits = str.maketrans('', '', digits)

res = ini_string.translate(remove_digits)

 

# printing result

print("final string : ", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string :  Geeks123for127geeks
    final string :  Geeksforgeeks
    

  
**Method #3: Using filter and lambda**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# how to remove numeric digits from string

# using filter and lambda

 

# initialising string

ini_string = "akshat123garg"

 

# printing initial ini_string

print("initial string : ", ini_string)

 

# using filter and lambda

# to remove numeric digits from string

res = "".join(filter(lambda x: not x.isdigit(), ini_string))

 

# res = ini_string

# printing result

print("final string : ", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string :  akshat123garg
    final string :  akshatgarg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

