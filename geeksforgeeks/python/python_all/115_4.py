Python | Replace rear word in String



Sometimes, while working with String list, we can have a problem in which we
need to replace the most rear i.e last word of string. This problem has many
application in web development domain. Let’s discuss different ways in which
this problem can be solved.

 **Method #1 : Usingsplit() + join()**  
This is one way in which we can perform this task. In this, we break elements
into parts and then return the last value and perform the addition of new
element using join().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rear word replace in String

# using split() + join()

 

# initializing string 

test_str = "GFG is good"

 

# printing original string 

print("The original string is : " + test_str)

 

# initializing replace string 

rep_str = "best"

 

# Rear word replace in String

# using split() + join()

res = " ".join(test_str.split(' ')[:-1] + [rep_str])

 

# printing result

print("The String after performing replace : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GFG is good
    The String after performing replace : GFG is best
    

**Method #2 : Usingrfind() + join()**  
The combination of these functions can also be used to perform this task. In
this, we perform the task of extracting the last word of string using rfind()
and join() is used to perform replace.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rear word replace in String

# using rfind() + join()

 

# initializing string 

test_str = "GFG is good"

 

# printing original string 

print("The original string is : " + test_str)

 

# initializing replace string 

rep_str = "best"

 

# Rear word replace in String

# using rfind() + join()

res = test_str[: test_str.rfind(' ')] + ' ' + rep_str

 

# printing result

print("The String after performing replace : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GFG is good
    The String after performing replace : GFG is best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

